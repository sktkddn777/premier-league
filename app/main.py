from fastapi import FastAPI, Request
import uvicorn

from routes.team import router as EPL_Router
from routes.rank import rank_helper, get_data, get_team_data, player_helper
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(EPL_Router, tags=["EPL"], prefix="/epl")

@app.get("/", tags=["Root"])
async def root():
  return {"message": "Welcome to fantastic fast api world!!!"}


@app.get("/rank", tags=["rank"])
async def read_item(request: Request):
  data = []
  teams_data = get_data()
  for i, team in enumerate(teams_data['Premier League']):
    data.append([i, rank_helper(team)])
  return templates.TemplateResponse("index.html", {"request": request, "data":data})


@app.get("/squad/{team_name}", tags=["team_info"])
async def read_item(request: Request, team_name: str):
  data = []
  teams_data = get_team_data()
  squad_data = teams_data[team_name][0]['squad']
  for player in squad_data:
    data.append(player_helper(player))
  print(data)
  return templates.TemplateResponse("squad.html", {"request": request, "data":data, "team_name":team_name})


if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)