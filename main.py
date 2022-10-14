from typing import List

from fastapi import FastAPI, HTTPException
import uvicorn

from utils import Pokemon, convert_csv_to_dict

DATA = 'pokemon.csv'
all_pokemon = dict(convert_csv_to_dict(DATA))

app = FastAPI()


@app.post("/", status_code=201, response_model=Pokemon)
async def create_pokemon(pokemon: Pokemon):
    all_pokemon[pokemon.pokedex_number] = pokemon
    return pokemon


@app.get("/", response_model=List[Pokemon])
async def read_all_pokemon():
    return list(all_pokemon.values())


@app.get("/{pokedex_number}", response_model=Pokemon)
async def read_pokemon(pokedex_number: int):
    return all_pokemon[pokedex_number]


@app.put("/{pokedex_number}", response_model=Pokemon)
async def update_pokemon(pokedex_number: int, pokemon: Pokemon):
    if pokedex_number not in all_pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    all_pokemon[pokedex_number] = pokemon
    return pokemon


@app.delete("/{pokedex_number}")
async def delete_pokemon(pokedex_number: int):
    if pokedex_number not in all_pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    all_pokemon.pop(pokedex_number)
    return {"ok": True}


if __name__ == "__main__":
    uvicorn.run(app)
