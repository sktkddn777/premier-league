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
  points:str = Field(...)
  round: str = Field(...)
  season: str = Field(...)
  squad: list = Field(...)

  class Config:
      schema_extra = {
          "example": {
              "name": "Chelsea",
              "gd": "+27",
              "overall_d": "3",
              "overall_gp": "14",
              "overall_l": "1",
              "overall_w": "10",
              "points": "33",
          }
      }

# How to store in Mongo DB
class SquadSchema(BaseModel):
  id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
  name: str = Field(...)
  squad: list = Field(...)

  class Config:
      schema_extra = {
          "example": {
              "name": "Chelsea",
              "squad": ["player1", "player2", "player3"]
          }
      }

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}