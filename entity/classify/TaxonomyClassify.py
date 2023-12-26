from dataclasses import dataclass

@dataclass
class TaxonomyClassify:
    taxonomy_id: int = 0
    parent_taxonomy_id: int = None
    name: str = ""
    level: str = ""


