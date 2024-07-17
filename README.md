![](https://geps.dev/progress/0)
# Jeu de Nim - Arbitre
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Ce projet contient un script qui arbitre une partie du jeu de Nim. Le jeu de Nim est un jeu de stratégie où deux joueurs s'affrontent en retirant des allumettes d'un tas. Le joueur qui enlève la dernière allumette a perdu.

## Règles du jeu de Nim

1. Le jeu commence avec un tas de 21 allumettes.
2. Deux joueurs se relaient pour jouer.
3. À chaque tour, un joueur doit retirer entre 1 et 4 allumettes du tas.
4. Le joueur qui prend la dernière allumette perd la partie.

## Fonctionnalités du script

- Initialisation du jeu avec 21 allumettes.
- Saisie des noms des deux joueurs et détermination de qui commence.
- Gestion des tours des joueurs.
- Validation des mouvements pour s'assurer qu'ils sont légaux.
- Détection du perdant lorsqu'il ne reste plus d'allumettes.

## Prérequis

- Python 3.x installé sur votre machine.

## Installation

Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/votre-utilisateur/nim-game-arbitre.git
cd nim-game-arbitre
