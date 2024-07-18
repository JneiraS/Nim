#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


def game_title(func: any):
    """
    Décorateur qui efface la console et imprime un titre de jeu avant d'exécuter la fonction décorée.
    Args :
        func (any) :
    """

    def wrapper(*args, **kwargs):
        # TODO gestion des system Linux
        os.system('cls')

        print(
            """
\t       _                  _        _   _ _           
\t      | |                | |      | \ | (_)          
\t      | | ___ _   _    __| | ___  |  \| |_ _ __ ___  
\t  _   | |/ _ | | | |  / _` |/ _ \ | . ` | | '_ ` _ \ 
\t | |__| |  __| |_| | | (_| |  __/ | |\  | | | | | | |
\t  \____/ \___|\__,_|  \__,_|\___| |_| \_|_|_| |_| |_|
                                                     
                                                     \n"""
        )
        return func(*args, **kwargs)

    return wrapper


def print_light_matches(light_matches: int) -> None:
    """
     Affiche visuellement les allumettes restantes.
    :param light_matches: (int) nombre d'allumettes
    """
    print('\n')
    print('  o ' * light_matches)
    print('  | ' * light_matches)
    print('  | ' * light_matches)
    print('\n\n')


def get_player_names():
    """
    Demande à l'utilisateur d'entrer les noms des deux joueurs de la partie.
    """
    return input("\tNom du Joueur 1: "), input("\tNom du Joueur 2: ")


def determine_the_starting_player(players: tuple) -> int:
    """
    Détermine le joueur qui commence en demandant à l'utilisateur.

    :param players: (tuple) : Noms des joueurs.
    :return: (int) : Indice du joueur débutant.
    """
    return int(input(f"\tQui Commence ? {players[0]} (1) ou {players[1]} (2)? : ")) - 1


def game_initialization() -> list:
    """
    La fonction game_initialization crée une liste de 21 éléments, chacun à la lettre 'l'.
    """
    return ['l' for _ in range(21)]


def removing_elements(elements: list, number_of_elements_to_remove: int) -> None:
    """
    Supprime un nombre spécifié d'éléments 'l' d'une liste donnée.
    """
    for _ in range(number_of_elements_to_remove):
        elements.remove('l')


@game_title
def ask_players(player: str, list_elements: list) -> int:
    """
    Demande à un joueur combien d'allumettes il souhaite enlever.
    """

    print_light_matches(len(list_elements))

    while True:

        light_matches_to_remove = int(input(
            f"\t{player}, il rest {len(list_elements)} allumettes, combien d'allumettes souhaitez-vous "
            f"enlever?: "))
        if 0 < light_matches_to_remove < 5:
            return light_matches_to_remove
        else:
            print(f"\t{light_matches_to_remove} n'est pas un nombre compris entre 1 et 4 !")


def get_and_switch_player_response(player_index, player_names):
    """
    Retourne la réponse du joueur actuel.
    :param player_index: (int) : Indice du joueur actuel.
    :param player_names: (list) : Liste des noms des joueurs.
    :return: (int) : La réponse du joueur actuel.
    """
    player_response: int = ask_players(player_names[player_index], player_names)
    return player_response


@game_title
def human_vs_human():
    """

    :return:
    """
    player_names: tuple[str, str] = get_player_names()

    list_of_elements, player_index = initialize_game_and_set_first_player(player_names)

    while len(list_of_elements) != 0:
        player_response: int = ask_players(player_names[player_index], list_of_elements)
        removing_elements(list_of_elements, player_response)
        player_index ^= 1

    input(f"\n\tvictoire écrasante de {player_names[player_index]}\n")


def human_vs_bot():
    """

    :return:
    """
    player_names: tuple[str, str] = (input('Votre nom ? :'), 'alpha-Nim')
    list_of_elements, player_index = initialize_game_and_set_first_player(player_names)
    player_response = 0

    while len(list_of_elements) != 0:

        if player_index == 1 and len(list_of_elements) % 5 > 1 and len(list_of_elements) != 21:
            bot_response: int = (len(list_of_elements) % 5) - 1
            removing_elements(list_of_elements, bot_response)
            player_index ^= 1

        elif player_index == 1:
            bot_response: int = 5 - player_response if player_response != 0 else 4
            removing_elements(list_of_elements, bot_response)
            player_index ^= 1

        else:
            player_response: int = ask_players(player_names[player_index], list_of_elements)
            removing_elements(list_of_elements, player_response)
            player_index ^= 1

    input(f"\n\tvictoire écrasante de {player_names[player_index]}\n")


def initialize_game_and_set_first_player(player_names: tuple):
    """
     Initialise le jeu et détermine l'indice du joueur qui commence.

    Après avoir identifié le premier joueur à jouer, initialise le jeu et récupère la liste des éléments
    nécessaires pour le démarrage. Ensuite, calcule l'indice du joueur qui commencera en fonction des noms
    de joueur fournis.
    :param player_names:
    :return: list_of_elements, player_index
    """
    starting_player: int = determine_the_starting_player(player_names)
    list_of_elements: list = game_initialization()
    player_index: int = player_names.index(player_names[starting_player])
    return list_of_elements, player_index


@game_title
def main():
    game_type = input('\tJouer contre un amis ou un BOT ? (a/B): ').lower()
    if game_type == 'a':
        human_vs_human()
    else:
        human_vs_bot()


if __name__ == "__main__":
    main()
