from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

from utils import Pokemon, convert_csv_to_dict

DATA = 'pokemon.csv'
all_pokemon = convert_csv_to_dict(DATA)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/", status_code=201)
async def create_pokemon(pokemon: Pokemon):
    all_pokemon[pokemon.pokedex_number] = pokemon
    return pokemon
