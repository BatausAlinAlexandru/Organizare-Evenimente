from abc import ABC
from dataclasses import dataclass


@dataclass
class Entity(ABC):
    """ Entity class for is used for id. """
    id_entity: str