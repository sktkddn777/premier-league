import requests
import json
from os import path
from insert_data import Database

BASE_DIR = path.dirname(path.abspath(__file__))


class Premier:
  def __init__(self, id, name, base_url, authorization):
      self.id = id
      self.name = name
      self.base_url = base_url
      self.authorization = authorization
      self.filepath = f"../football_json/{self.name}"
      self.data = {}
      self.team_data = {}

  def competition_standing(self):
    '''
      현재 리그 정보를 받아온다.
    '''
    
    league_team = f"{self.base_url}/standings/{self.id}?Authorization={self.authorization}"

    response = requests.get(league_team)
    if response.status_code == 200:
      self.data[self.name] = response.json()

      with open(f"{self.filepath}.json", 'w') as outfile:
        json.dump(self.data, outfile, indent="\t")

    elif response.status_code == 401:
      print("Invalid competition ID supplied")
    elif response.status_code == 404:
      print("Competition not found")
  
  
  def squad(self):
    '''
      team과 squad를 가져온다.
    '''
    team = []
    for t in self.data[self.name]:
      team.append([t['team_id'], t['team_name']])
    
    for data in team:
      id, name = data[0], data[1]
      team_squad = f"{self.base_url}/teams/{id}?Authorization={self.authorization}"
      response = requests.get(team_squad)
      if response.status_code == 200:
        self.team_data[name] = response.json()

        with open(f"{self.filepath}_squad.json", 'w') as outfile:
          json.dump(self.team_data, outfile, indent="\t")

      elif response.status_code == 401:
        print("Invalid team ID")
      elif response.status_code == 404:
        print("We did not find the requested team")


def make_data():
  '''
  프리미어리그 정보 + 스쿼드 정보를 받아 json형태로 저장한다.
  '''
  SECRET_PATH = path.join(BASE_DIR, ".config_secret/secrets.json")
  secrets = json.loads(open(SECRET_PATH).read())
  authorization = secrets['AUTHORIZATION_KEY']

  base_url = "https://data.football-api.com/v3"
  competition_url = f"{base_url}/competitions?Authorization={authorization}"
  response = requests.get(competition_url)

  if response.status_code == 200:    
    premier_league = response.json()[4] # 받아오는 json 데이터의 4번째가 프리미어리그 관련 정보.
    p = Premier(premier_league['id'], premier_league['name'], base_url, authorization) # ['id'] : 1204 , ['name'] : Premier League
    p.competition_standing()
    p.squad()

  elif response.status_code == 429:
    print("too many requests")


if __name__ == "__main__":
  make_data()
  db = Database()
  db.open_premier_data()
  db.connect_mongo()
  


  