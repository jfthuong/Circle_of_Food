import streamlit as st

from species import SpeciesType, SpeciesDiet, SpeciesSpecimen

st.set_page_config(page_title="Circle of Food", page_icon="🥩", layout="wide")

st.title("🥩Circle of Food🌿")

player_1, player_2 = st.columns(2)

PLAYER_1 = "P1"
PLAYER_2 = "P2"

if PLAYER_1 not in st.session_state:
    st.session_state[PLAYER_1] = []
if PLAYER_2 not in st.session_state:
    st.session_state[PLAYER_2] = []

with player_1:
    st.header("Player 1")
    player_1_name = st.text_input("Enter your name", "Player 1")

    cerf = SpeciesSpecimen(
        name="Cerf",
        species="deer",
        type_=SpeciesType.ANIMAL,
        diet=SpeciesDiet.HERBIVORE,
    )

    plante_carnivore = SpeciesSpecimen(
        name="Plante Carnivore",
        species="carnivorous_plant",
        type_=SpeciesType.PLANT,
        diet=SpeciesDiet.CARNIVORE,
    )

    renard = SpeciesSpecimen(
        name="Renard",
        species="fox",
        type_=SpeciesType.ANIMAL,
        diet=SpeciesDiet.CARNIVORE,
    )

    herb_snake = SpeciesSpecimen(
        name="Serpent Herbivore",
        species="snake",
        type_=SpeciesType.ANIMAL,
        diet=SpeciesDiet.HERBIVORE,
    )

    if not st.session_state[PLAYER_1]:
        st.session_state[PLAYER_1] = [cerf, plante_carnivore, renard, herb_snake]

    for species in st.session_state[PLAYER_1]:
        species.show_in_streamlit()


with player_2:
    st.header("Player 2")
    player_2_name = st.text_input("Enter your name", "Player 2")

    brocoli = SpeciesSpecimen(
        name="petit Brocoli",
        species="broccoli",
        type_=SpeciesType.PLANT,
        diet=SpeciesDiet.HERBIVORE,
    )

    loup = SpeciesSpecimen(
        name="Loup",
        species="wolf",
        type_=SpeciesType.ANIMAL,
        diet=SpeciesDiet.CARNIVORE,
    )

    chouette = SpeciesSpecimen(
        name="Chouette",
        species="owl",
        type_=SpeciesType.ANIMAL,
        diet=SpeciesDiet.CARNIVORE,
    )

    licorne = SpeciesSpecimen(
        name="Licorne",
        species="unicorn",
        type_=SpeciesType.ANIMAL,
        diet=SpeciesDiet.HERBIVORE,
    )

    if not st.session_state[PLAYER_2]:
        st.session_state[PLAYER_2] = [brocoli, loup, chouette, licorne]

    for species in st.session_state[PLAYER_2]:
        species.show_in_streamlit()
