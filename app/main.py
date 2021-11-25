from fastapi import FastAPI
import uvicorn

from routes.team import router as EplRouter

app = FastAPI()

# app.include_router(EplRouter, tags=["EPL"], prefix="/epl")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to fantastic fast api world!!!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



