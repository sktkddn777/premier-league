from fastapi import APIRouter

from database import (
    retrieve_teams,
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