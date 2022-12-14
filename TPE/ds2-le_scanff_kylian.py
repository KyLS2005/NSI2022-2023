# Première implémentation pour les piles
def creer_pile():
    '''Renvoie une pile vide'''
    return []

def est_vide(pile):
    '''Renvoie un booléen, True si la pile est vide et False sinon'''
    return p == []

def empiler(pile, element):
    '''Empile element au sommet de pile'''
    pile.append(element)
    
def depiler(pile):
    '''Renvoie et enlève la valeur du sommet de pile'''
    assert not est_vide(pile), "Pile vide"
    return pile.pop()

def sommet(pile):
    sommet = creer_pile()
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    if est_vide(pile) == True :
        raise IndexError('pile vide')
    else:
        sommet = depiler(pile)
        empiler(pile,sommet)
        return sommet

def mettre_disques(pile, n):
    '''met des disques de taille n à 1 sur la pile'''
    for i in list(range(n,0,-1)):
        empiler(pile,i)

def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    tours = creer_pile()
    tour = creer_pile()
    mettre_disques(tour, n)
    empiler(tours,tour)
    tour = creer_pile()
    for k in range (2):
        empiler(tours,tour)
    return tours

    