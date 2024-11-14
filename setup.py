from setuptools import setup, find_packages

setup(
    name="cblindfriendly",  # Nom de ta librairie
    version="0.1.0",       # Version de ta librairie
    packages=find_packages(),  # Trouve automatiquement tous les packages dans le dossier color_palette
    install_requires=[       # Liste des dépendances nécessaires (ici, matplotlib)
        "matplotlib",
    ],
    classifiers=[  # Pour décrire ta librairie
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="Une librairie de palettes de couleurs contrastées et accessibles",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Sarah MARTIN-ALONSO",
    author_email="sarah.martin.alonso@gmail.com",
    url="https://github.com/SarahMaAl/cblindfriendly", 
    license="MIT",
)
