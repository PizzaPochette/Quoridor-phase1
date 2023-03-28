def formater_légende(joueurs):
  
    symboles = {1: '1', 2:'2'}
    légende = 'Légende:'
    
    for joueur, symbole in symboles.items():
        nom = joueurs[joueur]['nom']
        murs = joueurs[joueur]['murs']
        légende += f'{symbole}={nom}, murs={'|' * murs}'
        
    return légende
  
def formater_damier(joueurs, murs):

    cases = '  ' + '   '.join(str(i) for i in range(1, 10)) + '  \n'
    for j in range(9, 0, -1):
        ligne = f"{j}|"
        for i in range(1, 10):
            if joueur_id = None:
              for joueur, pos in joueurs.items():
                if pos == (i, j):
                  ligne += '.'
            if joueur_id is not None:
                ligne += f'{joueur_id}'
            else:
                ligne += '   '
            if (i, j) in murs["horizontaux"]:
                ligne += '-'
            else:
                ligne += ' '
            if (i, j) in murs["verticaux"]:
                ligne += '|'
            else:
                ligne += ' '
        ligne += '|\n'
        cases += ligne
        
    return cases
  
def formater_jeu(état):
  

def formater_les_parties(parties):
    result = ''
    for i, partie in enumerate(parties, 1):
        result += f''{i} : {partie['date']}, {partie['joueurs'][0]} contre {partie['joueurs'][1]}''
        if partie['gagnant']:
            result += f'', gagnant: {partie['gagnant']}''
        result +='\n'
        
    return result[:-1]
  
def récupérer le coup():
      while True:
        type_coup = input(''Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'): '')
        position_str = input('Donnez la position où appliquer ce coup (x,y): ')
        position = position_str.split(',')
        
        if len(position) != 2:
            print("Position invalide. Veuillez entrer deux nombres séparés par une virgule.")
            continue
        try:
            position = [int(x) for x in position]
            if not (0 <= position[0] <= 8 and 0 <= position[1] <= 8):
                raise ValueError
            break
        except ValueError:
            print('Position invalide. Veuillez entrer deux entiers entre 0 et 8 inclus.')
    
    return type_coup, position
