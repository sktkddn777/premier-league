from fastapi import APIRouter

from database import (
    retrieve_teams,
    retrieve_team,
)
from models.teams import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

@router.get("/", response_description="Teams data retrieved")
async def retrieve_teams_data():
    teams = await retrieve_teams()
    if teams:
        return ResponseModel(teams, "Teams data retrieved successfully")
    return ResponseModel(teams, "Empty")


@router.get("/{id}", response_description="Team data retrieved")
async def retrieve_team_data(id):
    team = await retrieve_team(id)
    if team:
        return ResponseModel(team, "Team data retrieved successfully")
    return ErrorResponseModel("Error occured", 404, "Team doesn't exist")