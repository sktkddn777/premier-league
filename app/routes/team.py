from bson.objectid import ObjectId
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import database
from database import (
    retrieve_teams,
    retrieve_team,
)
from models.teams import (
    ErrorResponseModel,
    ResponseModel,
    TeamSchema,
)

router = APIRouter()


@router.get("/", response_description="Teams data retrieved")
async def retrieve_teams_data():
    teams = await retrieve_teams()
    if teams:
        return ResponseModel(teams, "Teams data retrieved")
    return ResponseModel(teams, "Empty")


@router.get("/{id}", response_description="team data retrieved")
async def retrieve_team_data(id):
    team = await retrieve_team(id)
    if team:
        return ResponseModel(team, "team data retrieved successfully")
    return ErrorResponseModel("Error occured", 404, "Team doesn't exist")