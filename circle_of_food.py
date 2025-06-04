import streamlit as st

from players import Player
from species import SpeciesType, SpeciesDiet, SpeciesSpecimen

st.set_page_config(page_title="Circle of Food", page_icon="🥩", layout="wide")

st.title("🥩Circle of Food🌿")

NB_PLAYERS = 2
KEY_PLAYERS = "players"

players = st.columns(NB_PLAYERS)


if KEY_PLAYERS not in st.session_state:
    st.session_state[KEY_PLAYERS] = [Player(id_=i + 1) for i in range(NB_PLAYERS)]

with players[0]:
    player = st.session_state[KEY_PLAYERS][0]
    st.header("Player 1")
    player_name = st.text_input("Enter your name", "Player 1", on_change=player.update_name)

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

    if player.has_no_species:
        player.add_species([cerf, plante_carnivore, renard, herb_snake])

    player.show_in_streamlit()


with players[1]:
    player = st.session_state[KEY_PLAYERS][1]
    st.header("Player ")
    player_name = st.text_input("Enter your name", "Player 2", on_change=player.update_name, args=(player.name))

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

    if player.has_no_species:
        player.add_species([brocoli, loup, chouette, licorne])

    player.show_in_streamlit()

    st.write(Player.from_json(player.to_json()).to_json())
