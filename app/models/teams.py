from typing import Optional
from bson.objectid import ObjectId

from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

        
# How to store in Mongo DB
class TeamSchema(BaseModel):
  id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
  name: str = Field(...)
  overall_ga: str = Field(...)
  overall_gs: str = Field(...)
  points:str = Field(...)
  round: str = Field(...)
  season: str = Field(...)
  squad: list = Field(...)

  class Config:
    #   allow_population_by_field_name = True
    #   json_encoders = {ObjectId: str}
    #   arbitrary_types_allowed = True
      schema_extra = {
          "example": {
              "name": "4",
              "overall_ga": "3",
              "overall_gs": "1",
              "points": "6",
              "round": "6",
              "season": "2020/2021",
              "squad": ["player1","player2", "player3"],
          }
      }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}