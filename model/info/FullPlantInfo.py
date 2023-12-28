from dataclasses import dataclass
from typing import List

from model.info.Plant import Plant
from model.info.PlantImage import PlantImage
from model.info.Taxonomy import Taxonomy


@dataclass
class FullPlantInfo:
    plant: Plant
    taxonomy: Taxonomy
    image_list: List[PlantImage]
