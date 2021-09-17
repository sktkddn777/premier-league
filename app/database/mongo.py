from bson.objectid import ObjectId
import motor.motor_asyncio
import pymongo
import json
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))


class Mongo:
    def connect(self, username, password):
        MONGO_DETAILS = f"mongodb://{username}:{password}@localhost:27017"
        try:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
            print("Connect Successful")
        except:
            print("Connect failed")

    def teams(self):
        self.database = self.client.teams
        self.team_collection = self.database.get_collection("teams_collection")
    
    def premier_insert(self, team_data, squad_data):
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
            
            self.team_collection.update_one(
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
    

if __name__ == "__main__":
    # get team data
    with open('../../football/football_json/Premier League.json') as f:
        premier_league_data = json.load(f)

    # get squad data
    with open('../../football/football_json/Premier League_squad.json') as f:
        squad_data = json.load(f)

    SECRET_PATH = path.join(BASE_DIR, ".config_secret/secrets.json")
    secrets = json.loads(open(SECRET_PATH).read())

    mongo = Mongo()
    mongo.connect(secrets['SECRET_ID'], secrets['SECRET_PW'])

    mongo.teams()

    mongo.premier_insert(premier_league_data, squad_data)


def team_helper(team) -> dict:
    return {
        "comp_id": team["comp_id"],
        "round": team["round"],
        "country": team["country"],
        "team_id": team["team_id"],
        "team_name": team["team_name"],
        "recent_form": team["recent_form"],
        "position": team["position"],
        "points": team["points"],
        "description": team["description"],
    }


# retrieve all teams in database
async def retrieve_teams():
    teams = []
    async for team in team_collection.find():
        teams.append(team_helper(team))
    return teams

# Add a new student into to the database
async def add_team(team_data: dict) -> dict:
    team = await team_collection.insert_one(team_data)
    new_team = await team_collection.find_one({"comp_id": team.inserted_id})
    return team_helper(new_team)

# Retrieve a team with a matching ID
async def retrieve_team(id: str) -> dict:
    team = await team_collection.find_one({"team_id": ObjectId(id)})
    if team:
        return team_helper(team)

# Delete a team from the database
async def delete_team(id: str):
    team = await team_collection.find_one({"team_id": ObjectId(id)})
    if team:
        await team_collection.delete_one({"team_id": ObjectId(id)})
        return True