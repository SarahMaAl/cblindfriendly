# color_palette/cblindfriendly.py

import matplotlib.pyplot as plt
import numpy as np

# Fonction pour récupérer un colormap
def get_colormap(name, n_colors=256):
    """Retourne un colormap avec n couleurs."""
    if name not in plt.colormaps():
        raise ValueError(f"Colormap {name} non trouvé. Liste des colormaps disponibles : {list_colormaps()}")
    
    cmap = plt.get_cmap(name, n_colors)
    return [cmap(i) for i in range(cmap.N)]  # Retourne les couleurs sous forme de liste

# Liste des colormaps populaires de matplotlib
def list_colormaps():
    """Retourne la liste des colormaps disponibles dans matplotlib."""
    return plt.colormaps()

# Palettes avec moins de couleurs et plus contrastées
def high_contrast_duo():
    """Retourne une palette avec deux couleurs contrastées."""
    return ['#0000FF', '#FF0000']  # Bleu et Rouge

# Nouvelle palette à 5 couleurs
def palette_5_MIB():
    """Retourne une palette de 5 couleurs personnalisée."""
    return ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000']

# Nouvelle palette à 8 couleurs (Version 1)
def palette_8_Wong():
    """Retourne une palette de 8 couleurs personnalisée."""
    return ['#000000', '#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7']

# Nouvelle palette à 8 couleurs (Version 2)
def palette_8_Tol():
    """Retourne une autre palette de 8 couleurs personnalisée."""
    return ['#332288', '#117733', '#44AA99', '#88CCEE', '#DDCC77', '#CC6677', '#AA4499', '#882255']

# Liste des duos de couleurs accessibles (choisies pour leur contraste élevé)
def accessible_duos():
    """Retourne une liste de duos de couleurs contrastées accessibles pour les daltoniens."""
    duos = [
        ['#FFC20A', '#0C7BDC'],  # Jaune et Bleu
        ['#994F00', '#006CD1'],  # Orange et Bleu
        ['#E1BE6A', '#40B0A6'],  # Jaune pâle et Vert menthe
        ['#E66100', '#5D3A9B'],  # Orange et Violet
        ['#1AFF1A', '#4B0092'],  # Vert vif et Violet
        ['#FEFE62', '#D35FB7'],  # Jaune et Rose
        ['#005AB5', '#DC3220'],  # Bleu et Rouge
        ['#1A85FF', '#D41159']   # Bleu clair et Rose vif
    ]
    
    # Créer les duos avec des noms comme 'duo 1', 'duo 2', etc.
    accessible_duos = []
    for i, duo in enumerate(duos, 1):  # Commencer l'indexation à 1
        duo_name = f"duo {i}"  # Utiliser la numérotation simple
        accessible_duos.append({
            'name': duo_name,
            'colors': duo
        })
    
    return accessible_duos

