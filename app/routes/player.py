from bson.objectid import ObjectId
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from database import (
    retrieve_squads,
    # add_team,
    retrieve_squad,
    # delete_team,
)
from models.teams import (
    ErrorResponseModel,
    ResponseModel,
    SquadSchema,
)



router = APIRouter()


@router.get("/", response_description="Teams player data retrieved")
async def retrieve_squads_data():
    squads = await retrieve_squads()
    if squads:
        return ResponseModel(squads, "all players data retrieved")
    return ResponseModel(squads, "Empty")


@router.get("/{id}", response_description="team_player data retrieved")
async def retrieve_squad_data(id):
    squad = await retrieve_squad(id)
    if squad:
        return ResponseModel(squad, "team_players retrieved successfully")
    return ErrorResponseModel("Error occured", 404, "Team doesn't exist")