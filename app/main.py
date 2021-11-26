from fastapi import FastAPI
import uvicorn
from routes.team import router as EPL_Router
from routes.rank import router as EPL_Ranking_Router

app = FastAPI()

app.include_router(EPL_Router, tags=["EPL"], prefix="/epl")
app.include_router(EPL_Ranking_Router, tags=["EPL_rank"], prefix="/epl_ranks")

@app.get("/", tags=["Root"])
async def root():
  return {"message": "Welcome to fantastic fast api world!!!"}

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)