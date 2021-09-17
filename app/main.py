from fastapi import FastAPI
from typing import Optional
import uvicorn
from common.config import conf
from models.teams import TeamSchema

from routes.team import router as EplRouter

# def create_app():
#     """
#     앱 함수 실행.
#     """
#     c = conf()
#     app = FastAPI()
#     return app

# app = create_app()
app = FastAPI()
app.include_router(EplRouter, tags=["EPL"], prefix="/epl")
@app.get("/", tags=["Root"])
async def root():
    return {"message": "HelloWOrld"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



