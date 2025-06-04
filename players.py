from dataclasses import dataclass, field
from typing import Union

import streamlit as st

from species import SpeciesSpecimen


@dataclass
class Player:
    """A player in the game."""

    id_: int
    name: str = ""
    species: list[SpeciesSpecimen] = field(default_factory=list, init=False)

    def __post_init__(self):
        """Initialize the player."""
        if not self.name:
            self.name = f"Player {self.id_}"

    def update_name(self, new_name: str):
        """Update the player's name."""
        self.name = new_name

    @property
    def has_no_species(self) -> bool:
        """Check if the player has no species."""
        return len(self.species) == 0

    def add_species(self, species: Union[SpeciesSpecimen, list[SpeciesSpecimen]]):
        """Add a species to the player's collection."""
        if isinstance(species, list):
            self.species.extend(species)
        else:
            self.species.append(species)

    def show_in_streamlit(self):
        """Display the player's species in Streamlit."""
        for spec in self.species:
            spec.show_in_streamlit()
        st.write(self.to_json())

    def to_json(self) -> dict:
        """Convert the player to a JSON serializable dictionary."""
        return {
            "id": self.id_,
            "name": self.name,
            "species": [spec.to_json() for spec in self.species],
        }

    @classmethod
    def from_json(cls, data: dict) -> "Player":
        """Create a Player instance from a JSON dictionary."""
        player = cls(id_=data["id"], name=data["name"])
        player.species = [SpeciesSpecimen.from_json(spec) for spec in data["species"]]
        return player
