from fastapi import APIRouter


from database import (
    retrieve_teams_ranking,
)
from models.teams import (
    ResponseModel,
)

router = APIRouter()

@router.get("/", response_description="Teams ranking data retrieved")
async def retrieve_teams_data():
    teams = await retrieve_teams_ranking()
    if teams:
        return ResponseModel(teams, "Teams data retrieved successfully")
    return ResponseModel(teams, "Empty")