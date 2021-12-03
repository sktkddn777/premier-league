from fastapi import FastAPI, Request
import uvicorn

from routes.team import router as EPL_Router
from routes.rank import rank_helper, player_helper
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import retrieve_teams, retrieve_squads

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(EPL_Router, tags=["EPL"], prefix="/epl")


@app.get("/", tags=["Root"])
async def root():
  return {"message": "Welcome to fantastic fast api world!!!"}


@app.get("/rank", tags=["rank_info"])
async def read_item(request: Request):
  data = []
  teams_data = await retrieve_teams()
  for i, team in enumerate(teams_data):
     data.append([i, rank_helper(team)])

  return templates.TemplateResponse("index.html", {"request": request, "data":data})


@app.get("/squad/{team_name}", tags=["team_info"])
async def read_item(request: Request, team_name: str):
  data = []
  teams_data = await retrieve_squads()
  for team in teams_data:
    if team['name'] == team_name:
      squad_data = team['squad']
      break
  for player in squad_data:
    data.append(player_helper(player))

  return templates.TemplateResponse("squad.html", {"request": request, "data":data, "team_name":team_name})


if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)