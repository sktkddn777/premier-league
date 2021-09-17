from typing import Optional

from pydantic import BaseModel, EmailStr, Field

	# overall_gp: str = Field(...)
	# overall_w: str = Field(...)
	# overall_d: str = Field(...)
	# overall_l: str = Field(...)
	# overall_gs: str = Field(...)
	# overall_ga: str = Field(...)
	# home_gp: str = Field(...)
	# home_w: str = Field(...)
	# home_d: str = Field(...)
	# home_l: str = Field(...)
	# home_gs: str = Field(...)
	# home_ga: str = Field(...)
	# away_gp: str = Field(...)
	# away_w: str = Field(...)
	# away_d: str = Field(...)
	# away_l: str = Field(...)
	# away_gs: str = Field(...)
	# away_ga: str = Field(...)
	# gd: str = Field(...)
class TeamSchema(BaseModel):
  _id: str = Field(...)
  name: str = Field(...)
  overall_ga: str = Field(...)
  overall_gs: str = Field(...)
  points:str = Field(...)
  round: str = Field(...)
  season: str = Field(...)
  squad: list = Field(...)

  class Config:
        schema_extra = {
            "example": {
                "_id": "1111",
                "name": "4",
                "overall_ga": "3",
                "overall_gs": "1",
                "points": "6",
                "round": "6",
                "season": "2020/2021",
                "squad": ["player1","player2", "player3"],
            }
        }


# class UpdateStudentModel(BaseModel):
#     comp_id: Optional[str]
#     round: Optional[str]
#     country: Optional[str]
#     team_id: Optional[str]
#     team_name:Optional[str]
#     recent_form: Optional[str]
#     position: Optional[str]
#     points: Optional[str]
#     description: Optional[str]

#     class Config:
#         schema_extra = {
#             "example": {
#                 "comp_id": "1204",
#                 "round": "4",
#                 "country": "England",
#                 "team_id": "9260",
#                 "team_name": "Manchester Utd",
#                 "recent_form": "WWDW",
#                 "position": "1",
#                 "points": "10",
#                 "description": "Promotion - Champions League (Group Stage)",
#             }
#         }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}