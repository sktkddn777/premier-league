from pymongo import MongoClient
import json
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))


class Database:
  def __init__(self):
    self.SECRET_PATH = path.join(BASE_DIR, ".config_secret/secrets.json")

  def connect_mongo(self):
    secrets = json.loads(open(self.SECRET_PATH).read())
    MONGO_DETAILS = f"mongodb://{secrets['SECRET_ID']}:{secrets['SECRET_PW']}@mongo:27017"
    try:
        client = MongoClient(MONGO_DETAILS)
        print("Connect Successful")
    except:
        print("Connect failed")

    database_teams = client.teams
    self.team_collection = database_teams.get_collection("teams_collection")
    self.squad_collection = database_teams.get_collection("squads_collection")
    self.premier_insert()
    self.squad_insert()


  def open_premier_data(self):
    with open('../football_json/Premier League.json') as f:
        self.premier_league_data = json.load(f)

    with open('../football_json/Premier League_squad.json') as f:
        self.squad_data = json.load(f)


  def premier_insert(self):
    premierLeague = self.premier_league_data['Premier League'] 
    for data in premierLeague:
        team_name = data["team_name"]
        overall_gp = data["overall_gp"]
        overall_w = data["overall_w"]
        overall_d = data["overall_d"]
        overall_l = data["overall_l"]
        gd = data["gd"]
        points = data["points"]
        
              
        self.team_collection.update_one(
            {"name": team_name}, { "$set" : {
                "overall_gp":overall_gp,
                "overall_w":overall_w,
                "overall_d":overall_d,
                "overall_l":overall_l,
                "gd":gd,
                "points":points,
            }},
            upsert=True,
        )

  def squad_insert(self):
    squad_data = self.squad_data
    for name, value in squad_data.items():
      squad = value[0]["squad"]

      self.squad_collection.update_one(
        {"name": name}, { "$set" : {
          "squad": squad,
        }},
        upsert=True,
      )








