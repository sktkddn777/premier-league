from pymongo import MongoClient
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))

mongo_details = "mongodb://root:example@mongo:27017"
client = MongoClient(mongo_details)
database = client.teams
team_collection = database.get_collection("teams_collection")
squad_collection = database.get_collection("squads_collection")

# team_helper
def team_helper(team) -> dict:
  return {
      "id": str(team["_id"]),
      "name": team["name"],
      "overall_gp": team["overall_gp"],
      "overall_w": team["overall_w"],
      "overall_d": team["overall_d"],
      "overall_l": team["overall_l"],
      "gd": team["gd"],
      "points": team["points"],
  }

# squad_helper
def squad_helper(team) -> dict:
  return {
      "id": str(team["_id"]),
      "name": team["name"],
      "squad": team["squad"],
  }


# retrieve all teams in database
async def retrieve_teams():
    teams = []
    for data in team_collection.find():
        teams.append(team_helper(data))
    return teams

async def retrieve_squads():
    teams = []
    for data in squad_collection.find():
        teams.append(squad_helper(data))
    return teams