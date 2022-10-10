from fastapi import FastAPI
from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
