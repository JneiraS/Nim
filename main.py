#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


def game_title(func: any):
    """
    Décorateur qui efface la console et imprime un titre de jeu avant d'exécuter la fonction décorée.
    Args:
        func (any):
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
    return input("Nom du Joueur 1: "), input("Nom du Joueur 2: ")


@game_title
def determine_the_starting_player(players: tuple) -> str:
    """    
    Demande à l'utilisateur de choisir le joueur qui commence le jeu entre deux joueurs spécifiés.
    """
    return input(f"Qui Commence ? {players[0]} (1) ou {players[1]} (2)? : ")


def game_initialization() -> list:
    """
    La fonction game_initialization crée une liste de 21 éléments, chacun  à la lettre 'l'.
    """
    return ['l' for _ in range(21)]


def removing_elements(elements: list, number_of_elements_to_remove: int) -> None:
    for _ in range(number_of_elements_to_remove):
        elements.remove('l')


def main():
    player_names = get_player_names()
    determine_the_starting_player(player_names)


if __name__ == "__main__":
    # main()
    print(game_initialization())
