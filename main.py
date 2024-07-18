import os


def game_title(func:any):
    """
    Décorateur qui efface la console et imprime un titre de jeu avant d'exécuter la fonction décorée.
    Args:
        func (any):
    """
    def wrapper(*args, **kwargs):
        os.system('clear')

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
def get_player_names() -> tuple[str]:
    """
    Demande à l'utilisateur d'entrer les noms des deux joueurs de la partie.
    """
    return (input("Nom du Joueur 1: "), input("Nom du Joueur 2: "))


@game_title
def determine_the_starting_player(players: tuple) -> str:
    """    
    Demande à l'utilisateur de choisir le joueur qui commence le jeu entre deux joueurs spécifiés.
    """
    return input(f"Qui Commence ? {players[0]} (1) ou {players[1]} (2)? : ")


def main():

    player_names = get_player_names()
    determine_the_starting_player(player_names)


if __name__ == "__main__":
    main()

    """
    feat: Ajout d'un décorateur pour afficher le titre du jeu avant l'exécution de certaines fonctions, et implémentation des fonctions pour obtenir les noms des joueurs et déterminer le joueur qui commence.
    """