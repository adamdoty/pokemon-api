from typing import List

from fastapi import FastAPI
import uvicorn

from utils import Pokemon, convert_csv_to_dict

DATA = 'pokemon.csv'
all_pokemon = convert_csv_to_dict(DATA)

app = FastAPI()


@app.get("/", status_code=200, response_model=List[Pokemon])
async def read_all_pokemon():
    return list(all_pokemon.values())


@app.get("/{pokedex_number}", status_code=200, response_model=Pokemon)
async def read_pokemon(pokedex_number):
    return all_pokemon[pokedex_number]


@app.post("/", status_code=201)
async def create_pokemon(pokemon: Pokemon):
    all_pokemon[pokemon.pokedex_number] = pokemon
    return pokemon


if __name__ == "__main__":
    uvicorn.run(app)
