from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import json


router = APIRouter()
templates = Jinja2Templates(directory="templates")


def get_icon(name):
    with open('../football_json/test.json', 'r') as f:
        data = json.load(f)
    return data[name]

# # helper
def rank_helper(team) -> dict:
  return {
      "icon": get_icon(team["team_name"]),
      "name": team["team_name"],
      "points": team["points"],
  }

@router.get("/", response_description="Teams ranking data retrieved")
async def read_item(request: Request):
  team = []
  
  with open('../football_json/Premier League.json', 'r') as f:
    data = json.load(f)

  for t in data['Premier League']:
    team.append(rank_helper(t))
  return templates.TemplateResponse("index.html", {"request": request, "data":team})
