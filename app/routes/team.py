from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database.mongo import (
    retrieve_teams,
    add_team,
    retrieve_team,
    delete_team,
)
from models.teams import (
    ErrorResponseModel,
    ResponseModel,
    TeamSchema,
)

router = APIRouter()


@router.post("/", response_description="team data added into the database")
async def add_team_data(team: TeamSchema = Body(...)):
    student = jsonable_encoder(team)
    new_team = await add_team(team)
    return ResponseModel(new_team, "Team added successfully.")