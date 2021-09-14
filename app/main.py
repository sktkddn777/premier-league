from fastapi import FastAPI
from typing import Optional
import uvicorn
from common.config import conf


def create_app():
    """
    앱 함수 실행.
    """
    c = conf()
    app = FastAPI()

    return app

app = create_app()

@app.get("/")
async def root():
    return {"message": "HelloWOrld"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



