from dataclasses import dataclass
from typing import List

from entity.info.Plant import Plant
from entity.info.PlantImage import PlantImage
from entity.info.Taxonomy import Taxonomy


@dataclass
class FullPlantInfo:
    plant: Plant
    taxonomy: Taxonomy
    image_list: List[PlantImage]
