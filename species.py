from enum import Enum
from dataclasses import dataclass, field, InitVar
from pathlib import Path

import streamlit as st

ASSETS_DIR = Path(__file__).parent / "assets"
DEAD_SVG = ASSETS_DIR / "dead.svg"


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
    life: int = field(init=False, repr=True)
    # show: InitVar[bool] = field(default=True)

    def __post_init__(self):
        """Set the life of the species based on its type."""
        if not self.name:
            self.name = self.species.capitalize()
        if self.diet == SpeciesDiet.CARNIVORE:
            self.life = 2
        elif self.diet == SpeciesDiet.HERBIVORE:
            self.life = 3
        else:
            raise ValueError("Invalid species type")

        # if show:
        #     self.show_in_streamlit()

    @property
    def is_dead(self) -> bool:
        """Check if the species is dead."""
        return self.life < 1

    @property
    def life_heart(self) -> str:
        """Return the life of the species."""
        if self.is_dead:
            return "💔 **DEAD**"
        return "♥️" * self.life

    def _add_life(self):
        """Add a life to the species."""
        self.life += 1

    def _remove_life(self):
        """Remove a life from the species."""
        if self.life > 0:
            self.life -= 1
        else:
            st.warning(f"{self.name} has no more lives left!")

    @property
    def svg(self) -> Path:
        """Return the path to the SVG file of the species."""
        return ASSETS_DIR / f"{self.species}.svg"

    def show_in_streamlit(self):
        """Display the species information in streamlit."""
        st.subheader(f"{self.name}", divider=True)
        # st.write(species)
        pic, change_lives, info, _ = st.columns([3, 2, 6, 12])
        with pic:
            if self.is_dead:
                st.image(DEAD_SVG, width=150)
            elif self.svg.exists():
                st.image(self.svg, width=150)
            else:
                pass
                # TODO: add a default image
        with change_lives:
            st.button(
                "",
                icon="💖",
                help="Add a life",
                key=f"{self.name}_plus",
                on_click=self._add_life,
                disabled=self.is_dead,
            )
            st.button(
                "",
                icon="💔",
                help="Remove a life",
                key=f"{self.name}_minus",
                on_click=self._remove_life,
                disabled=self.is_dead,
            )
        with info:
            st.write(f"**Species**: {self.species}")
            st.write(f"**Type**: {self.type_.value} {self.diet.value}")
            st.write(f"**Life**: {self.life_heart}")

        # st.write("---")
