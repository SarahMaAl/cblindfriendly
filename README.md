# cblindfriendly

Une librairie de palettes de couleurs contrastées et accessibles pour les utilisateurs daltoniens.

## Description

`cblindfriendly` est une librairie Python qui fournit des palettes de couleurs optimisées pour les personnes atteintes de daltonisme. Ces palettes sont conçues pour être facilement visibles et compréhensibles, même pour ceux qui ont des difficultés à distinguer certaines couleurs. Cette librairie est utile pour les graphiques, les visualisations de données et toutes les applications nécessitant des couleurs accessibles.

## Installation

Vous pouvez installer la librairie directement depuis GitHub en utilisant `pip` :

```bash
pip install git+https://github.com/SarahMaAl/cblindfriendly.git
```

### Dépendances

Cette librairie nécessite les dépendances suivantes :

- `matplotlib` : pour la création de graphiques et de visualisations.
- `numpy` : pour les calculs numériques et la gestion des données.

Vous pouvez également installer les dépendances via `pip` en utilisant un fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

## Utilisation

Voici un exemple simple de comment utiliser `cblindfriendly` pour générer une palette de couleurs accessibles :

```python
import cblindfriendly

# Exemple d'utilisation d'une palette
palette = cblindfriendly.get_palette()
print(palette)
```

## Contribuer

Les contributions sont les bienvenues ! Si vous avez des suggestions ou des améliorations, n'hésitez pas à ouvrir une *issue* ou à soumettre une *pull request*.

### Étapes pour contribuer

1. Forkez ce dépôt
2. Créez une nouvelle branche (`git checkout -b feature-nouvelle-fonctionnalite`)
3. Faites vos changements et commitez (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`)
4. Pushez votre branche (`git push origin feature-nouvelle-fonctionnalite`)
5. Ouvrez une pull request

## License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteur

Sarah MARTIN-ALONSO  
Email: [sarah.martin.alonso@gmail.com](mailto:sarah.martin.alonso@gmail.com)  
GitHub: [https://github.com/SarahMaAl](https://github.com/SarahMaAl)
