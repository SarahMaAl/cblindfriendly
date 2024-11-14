from setuptools import setup, find_packages

# Lire le contenu de README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cblindfriendly",  # Nom de la librairie
    version="0.1.0",       # Version de la librairie
    packages=find_packages(),  # Trouve automatiquement tous les packages dans le dossier color_palette
    install_requires=[       # Liste des dépendances nécessaires
        "matplotlib",
        "numpy"
    ],
    classifiers=[  # Pour décrire la librairie
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="Une librairie de palettes de couleurs contrastées et accessibles pour les utilisateurs daltoniens.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sarah MARTIN-ALONSO",
    author_email="sarah.martin.alonso@gmail.com",
    url="https://github.com/SarahMaAl/cblindfriendly", 
    license="MIT",
    python_requires=">=3.6",
)
