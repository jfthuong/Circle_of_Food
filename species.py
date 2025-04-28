from enum import Enum
from dataclasses import dataclass, field, InitVar
from pathlib import Path

import streamlit as st


class SpeciesType(Enum):
    """Plant or animal"""
    PLANT = "🌳"
    ANIMAL = "🐴"


class SpeciesDiet(Enum):
    """Herbivore or carnivore"""
    HERBIVORE = "🌿"
    CARNIVORE = "🥩"


@dataclass
class SpeciesSpecimen:
    """A specimen of a species"""
    species: str
    type_: SpeciesType
    diet: SpeciesDiet
    name: str = field(default="")
    _life: int = field(init=False)
    show: InitVar[bool] = field(default=True)


    def __post_init__(self, show: bool):
        """Set the life of the species based on its type."""
        if not self.name:
            self.name = self.species.capitalize()
        if self.diet == SpeciesDiet.CARNIVORE:
            self._life = 2
        elif self.diet == SpeciesDiet.HERBIVORE:
            self._life = 3
        else:
            raise ValueError("Invalid species type")

        if show:
            self.show_in_streamlit()

    @property
    def life(self) -> int:
        """Return the life of the species."""
        return "♥️" * self._life

    @property
    def svg(self) -> Path:
        """Return the path to the SVG file of the species."""
        return Path(__file__).parent / "assets" / f"{self.species}.svg"


    def show_in_streamlit(self):
        """Display the species information in streamlit."""
        st.subheader(f"{self.name}", divider=True)
        # if self.svg.exists():
        #     st.image(self.svg, width=150)
        # st.write(f"Life: {self.life}")
        # st.write(f"Type: {self.type_.value}{self.diet.value}")
        pic, change_lives, info, _ = st.columns([3, 2, 6, 12])
        with pic:
            if self.svg.exists():
                st.image(self.svg, width=150)
        with info:
            st.write(f"**Species**: {self.species}")
            st.write(f"**Type**: {self.type_.value} {self.diet.value}")
            st.write(f"**Life**: {self.life}")
        with change_lives:
            if st.button("💖", help="Add a life", key=f"{self.name}_plus"):
                self._life += 1
            if st.button("💔", help="Remove a life", key=f"{self.name}_minus"):
                self._life -= 1

        # st.write("---")
