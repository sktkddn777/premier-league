from pymongo import MongoClient
from bson.objectid import ObjectId
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))

mongo_details = "mongodb://root:example@mongo:27017"
client = MongoClient(mongo_details)
database = client.teams
team_collection = database.get_collection("teams_collection")

# helper
def team_helper(team) -> dict:
  return {
      "id": str(team["_id"]),
      "name": team["name"],
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
    return teams

async def retrieve_team(id: str) -> dict:
    team = team_collection.find_one({"_id": ObjectId(id)})
    if team:
        return team_helper(team)


async def retrieve_teams_ranking():
    teams = []
    for idx, data in enumerate(team_collection.find()):
        name = team_helper(data)['name']
        point = team_helper(data)['points']
        teams.append((idx+1, name, point))
    return teams