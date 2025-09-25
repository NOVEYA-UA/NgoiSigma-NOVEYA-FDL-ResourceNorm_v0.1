from enum import Enum

class ResourceType(str, Enum):
    ENERGY = "energy"
    FUEL = "fuel"
    RAW_MATERIAL = "raw_material"
    LABOR = "labor"
    CAPEX = "capex"
