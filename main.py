from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List


class Pokemon(BaseModel):
    name: str
    japanese_name: str
    pokedex_number: int
    percentage_male: Optional[float]
    type1: str
    type2: str
    classification: str
    height_m: float
    weight_kg: float
    capture_rate: float
    baseeggsteps: int
    abilities: List
    experience_growth: str
    base_happiness: int
    against_type: List[float]
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    generation: str
    is_legendary: bool


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
