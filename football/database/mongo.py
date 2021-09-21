
import motor.motor_asyncio
import pymongo
import json
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))


class Mongo:
    def connect(self, username, password):
        MONGO_DETAILS = f"mongodb://{username}:{password}@mongo:27017"
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
        print("DONE")

if __name__ == "__main__":
    # get team data
    with open('../football_json/Premier League.json') as f:
        premier_league_data = json.load(f)
    print(premier_league_data)
    # get squad data
    with open('../football_json/Premier League_squad.json') as f:
        squad_data = json.load(f)

    SECRET_PATH = path.join(BASE_DIR, ".config_secret/secrets.json")
    secrets = json.loads(open(SECRET_PATH).read())

    mongo = Mongo()
    mongo.connect(secrets['SECRET_ID'], secrets['SECRET_PW'])

    mongo.teams()

    mongo.premier_insert(premier_league_data, squad_data)

