from fastapi import FastAPI
from typing import Optional
import uvicorn
from common.config import conf
from models.teams import TeamSchema

from routes.team import router as EplRouter
from routes.player import router as PlayerRouter
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
app.include_router(PlayerRouter, tags=["EPL_Player"], prefix="/epl_player")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to fantastic fast api world!!!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



