# "species_id": row[0],
# "species_name": row[1],
# "species_alias": row[2],
# "genus_name": row[3],
# "family_name": row[4],
# "growth_env": row[5],
# "province": row[6],
# "city": row[7],
# "country": row[8]
from dataclasses import dataclass


@dataclass
class SpecieVO:
    species_id: int
    species_name: str
    species_alias: str
    genus_name: str
    family_name: str
    growth_env: str
    province: str
    city: str
    country: str
