from bson.objectid import ObjectId
from pymongo import MongoClient
import json
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))


def premier_insert(team_data, squad_data, team_collection):
        premierLeague = team_data['Premier League']
        squad = squad_data
        season = premierLeague[0]["season"]
        round = premierLeague[0]["round"]

        for data in premierLeague:
            team_name = data["team_name"]
            overall_gs = data["overall_gs"]
            overall_ga = data["overall_ga"]
            points = data["points"]
            team_squad = squad[team_name][0]["squad"]
            
            team_collection.update_one(
                {"name": team_name}, { "$set" : {
                    "season": season, 
                    "round":round,
                    "overall_gs":overall_gs,
                    "overall_ga":overall_ga,
                    "points":points,
                    "squad":team_squad
                }},
                upsert=True,
            )



with open('../football_json/Premier League.json') as f:
    premier_league_data = json.load(f)

# get squad data
with open('../football_json/Premier League_squad.json') as f:
    squad_data = json.load(f)

SECRET_PATH = path.join(BASE_DIR, ".config_secret/secrets.json")
secrets = json.loads(open(SECRET_PATH).read())
MONGO_DETAILS = f"mongodb://{secrets['SECRET_ID']}:{secrets['SECRET_PW']}@mongo:27017"
try:
    client = MongoClient(MONGO_DETAILS)
    print("Connect Successful")
except:
    print("Connect failed")

database = client.teams
team_collection = database.get_collection("teams_collection")
# for data in team_collection.find():
#     print(data)
# insert team and squad data to mongodb
premier_insert(premier_league_data, squad_data, team_collection)


# # helper
def team_helper(team) -> dict:
    return {
        "id": str(team["_id"]),
        "name": team["name"],
        "overall_ga": team["overall_ga"],
        "overall_gs": team["overall_gs"],
        "points": team["points"],
        "round": team["round"],
        "season": team["season"],
        "squad": team["squad"],
    }


# retrieve all teams in database
async def retrieve_teams():
    teams = []
    for data in team_collection.find():
        teams.append(team_helper(data))
    print(teams)
    return teams

# Add a new student into to the database
async def add_team(team_data: dict) -> dict:
    team = await team_collection.insert_one(team_data)
    new_team = await team_collection.find_one({"_id": team.inserted_id})
    return team_helper(new_team)

# Retrieve a team with a matching ID
async def retrieve_team(id: str) -> dict:
    team = team_collection.find_one({"_id": ObjectId(id)})
    if team:
        return team_helper(team)

# Delete a team from the database
async def delete_team(name: str):
    team = await team_collection.find_one({"name": ObjectId(name)})
    if team:
        await team_collection.delete_one({"name": ObjectId(name)})
        return True