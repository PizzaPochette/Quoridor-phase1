import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase d\'initialisation')

    parser.add_argument('idul', metavar='idul', type=str, help='IDUL du joueur')
    parser.add_argument('-p', '--parties', action='store_true', help='Lister les parties existantes')

    return parser.parse_args()
