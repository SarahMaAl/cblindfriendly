"""
cblindfriendly.py

Author: Sarah MARTIN-ALONSO
Date: 2024-11-14
License: MIT

This module provides utilities for working with color palettes and colormaps, 
specifically designed to be accessible for color-blind users.
"""

import matplotlib.pyplot as plt
import numpy as np


def get_colormap(name, n_colors=256):
    """
    Retrieve a colormap with a specified number of colors.

    Parameters:
        name (str): The name of the colormap to retrieve.
        n_colors (int): Number of colors in the colormap.

    Returns:
        list: A list of RGBA tuples representing the colormap.

    Raises:
        ValueError: If the specified colormap name is not found.
    """
    if name not in plt.colormaps():
        raise ValueError(f"Colormap '{name}' not found. Available colormaps: {list_colormaps()}")
    
    cmap = plt.get_cmap(name, n_colors)
    return [cmap(i) for i in range(cmap.N)]


def list_colormaps():
    """
    List available colormaps in matplotlib.

    Returns:
        list: A list of available colormap names.
    """
    return plt.colormaps()


def high_contrast_duo():
    """
    Return a high-contrast color duo (blue and red).

    Returns:
        list: A list containing two high-contrast color hex values.
    """
    return ['#0000FF', '#FF0000']  # Blue and Red


def palette_5_MIB():
    """
    Return a custom palette of 5 colors.

    Returns:
        list: A list of 5 color hex values.
    """
    return ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000']


def palette_8_Wong():
    """
    Return a custom palette of 8 colors (version 1).

    Returns:
        list: A list of 8 color hex values.
    """
    return ['#000000', '#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7']


def palette_8_Tol():
    """
    Return another custom palette of 8 colors (version 2).

    Returns:
        list: A list of 8 color hex values.
    """
    return ['#332288', '#117733', '#44AA99', '#88CCEE', '#DDCC77', '#CC6677', '#AA4499', '#882255']


def accessible_duos():
    """
    Return a list of accessible color duos with high contrast, suitable for color-blind users.

    Returns:
        list: A list of dictionaries containing duo names and color hex values.
    """
    duos = [
        ['#FFC20A', '#0C7BDC'],  # Yellow and Blue
        ['#994F00', '#006CD1'],  # Orange and Blue
        ['#E1BE6A', '#40B0A6'],  # Pale Yellow and Mint Green
        ['#E66100', '#5D3A9B'],  # Orange and Purple
        ['#1AFF1A', '#4B0092'],  # Bright Green and Purple
        ['#FEFE62', '#D35FB7'],  # Yellow and Pink
        ['#005AB5', '#DC3220'],  # Blue and Red
        ['#1A85FF', '#D41159']   # Light Blue and Bright Pink
    ]
    
    # Create the duos with names like 'duo 1', 'duo 2', etc.
    accessible_duos_list = []
    for i, duo in enumerate(duos, 1):
        duo_name = f"duo {i}"
        accessible_duos_list.append({
            'name': duo_name,
            'colors': duo
        })
    
    return accessible_duos_list
