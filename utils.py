from typing import Optional, List
import csv
import re

from pydantic import BaseModel

DATA = 'pokemon.csv'


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
    # against_type: List[float]
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    generation: str
    is_legendary: bool


def convert_csv_to_dict(data=DATA):
    '''write a function to parse marvel-wikia-data.csv, see
       https://docs.python.org/3.7/library/csv.html#csv.DictReader
       should return a list of OrderedDicts or a list of Character
       namedtuples (see Character namedtuple above')'''
    with open(data, encoding="utf-8") as csvfile:
        counter = 0
        for row in csv.DictReader(csvfile):
            if counter > 0:
                break

            print(row)
            print(row['name'])

            yield Pokemon(
                name=row['name'],
                japanese_name=row['japanese_name'],
                pokedex_number=row['pokedex_number'],
                percentage_male=row['percentage_male'],
                type1=row['type1'],
                type2=row['type2'],
                classification=row['classfication'],
                height_m=row['height_m'],
                weight_kg=row['weight_kg'],
                capture_rate=row['capture_rate'],
                baseeggsteps=row['base_egg_steps'],
                abilities=row['abilities'],
                experience_growth=row['experience_growth'],
                base_happiness=row['base_happiness'],
                # against_type=row['against_type'],
                against_type=[0.5, 0.1],
                hp=row['hp'],
                attack=row['attack'],
                defense=row['defense'],
                sp_attack=row['sp_attack'],
                sp_defense=row['sp_defense'],
                speed=row['speed'],
                generation=row['generation'],
                is_legendary=row['is_legendary'],
            )

            counter += 1


data = list(convert_csv_to_dict())
print(data[:3])
