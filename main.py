#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


def print_light_matches(light_matches:int) -> None:
    """
     Affiche visuellement les allumettes restantes.
    :param light_matches: (int) nombre d'allumettes

    """
    print('\n\n')
    print('  o ' * light_matches)  # Imprimer les sommets des allumettes
    print('  | ' * light_matches)  # Imprimer les bases des allumettes
    print('  | ' * light_matches)  # Imprimer les bases des allumettes
    print('\n\n')


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
                                                                                           
       _|                                _|                _|      _|  _|                  
       _|    _|_|    _|    _|        _|_|_|    _|_|        _|_|    _|      _|_|_|  _|_|    
       _|  _|_|_|_|  _|    _|      _|    _|  _|_|_|_|      _|  _|  _|  _|  _|    _|    _|  
 _|    _|  _|        _|    _|      _|    _|  _|            _|    _|_|  _|  _|    _|    _|  
   _|_|      _|_|_|    _|_|_|        _|_|_|    _|_|_|      _|      _|  _|  _|    _|    _|  
                                                                                           
                                                                                           \n"""
        )
        return func(*args, **kwargs)

    return wrapper


@game_title
def get_player_names():
    """
    Demande à l'utilisateur d'entrer les noms des deux joueurs de la partie.
    """
    return input("\tNom du Joueur 1: "), input("\tNom du Joueur 2: ")


@game_title
def determine_the_starting_player(players: tuple) -> int:
    """
    Détermine le joueur qui commence en demandant à l'utilisateur.

    :param players: (tuple): Noms des joueurs.
    :return: (int): Indice du joueur débutant.
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

    return int(input(f"\t{player}, combien d'allumettes souhaitez-vous enlever? :"))


def get_and_switch_player_response(player_index, player_names):
    """
    Retourne la réponse du joueur actuel.
    :param player_index: (int): Indice du joueur actuel.
    :param player_names: (list): Liste des noms des joueurs.
    :return: (int): La réponse du joueur actuel.
    """
    player_response: int = ask_players(player_names[player_index])

    return player_response


def main():
    player_names: tuple[str, str] = get_player_names()
    starting_player: int = determine_the_starting_player(player_names)
    list_of_elements: list = game_initialization()

    player_index = player_names.index(player_names[starting_player])

    while len(list_of_elements) != 0:
        player_response: int = ask_players(player_names[player_index], list_of_elements)
        removing_elements(list_of_elements, player_response)
        player_index ^= 1


if __name__ == "__main__":
    main()
