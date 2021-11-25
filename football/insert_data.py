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
    database = client.teams
    self.team_collection = database.get_collection("teams_collection")
    self.premier_insert()


  def open_premier_data(self):
    with open('../football_json/Premier League.json') as f:
        self.premier_league_data = json.load(f)

    with open('../football_json/Premier League_squad.json') as f:
        self.squad_data = json.load(f)


  def premier_insert(self):
    premierLeague = self.premier_league_data['Premier League']
    season = premierLeague[0]["season"]
    round = premierLeague[0]["round"]

    for data in premierLeague:
        team_name = data["team_name"]
        points = data["points"]
        team_squad = self.squad_data[team_name][0]["squad"]
              
        self.team_collection.update_one(
            {"name": team_name}, { "$set" : {
                "season": season, 
                "round":round,
                "points":points,
                "squad":team_squad
            }},
            upsert=True,
        )









