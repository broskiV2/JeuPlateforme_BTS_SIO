# Jeu de Plateforme 🎮

Un jeu de plateforme 2D créé avec Pygame, offrant une expérience de jeu captivante avec plusieurs niveaux et différents thèmes visuels.

## ✨ Caractéristiques

- Multiple niveaux avec difficulté progressive
- Différents thèmes visuels personnalisables
- Système de score
- Effets visuels et sonores
- Mode plein écran
- Interface utilisateur intuitive

## 🛠 Installation

1. Assurez-vous d'avoir Python 3.7+ installé sur votre système
2. Clonez ce dépôt ou téléchargez les fichiers
3. Ouvrez un terminal dans le dossier du jeu
4. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## 🚀 Lancement du jeu

Pour lancer le jeu, exécutez la commande suivante dans le terminal :
```bash
python game.py
```

## 🎯️ Contrôles

- **Flèches GAUCHE/DROITE** : Se déplacer
- **ESPACE** : Sauter
- **ÉCHAP** : Menu/Retour
- Collectez les pièces pour augmenter votre score
- Évitez les ennemis
- Atteignez le drapeau pour terminer le niveau

## ⚙️ Paramètres

Dans le menu OPTIONS, vous pouvez :
- Activer/désactiver le son
- Activer/désactiver le mode plein écran
- Changer le thème visuel

## 🎨 Thèmes disponibles

### 1. CLASSIQUE
- Fond noir
- Plateformes vertes
- Pièces dorées
- Ennemis rouges
- Joueur bleu

### 2. SOMBRE
- Fond sombre
- Plateformes grises
- Pièces or foncé
- Ennemis rouge foncé
- Joueur bleu foncé

### 3. COLORÉ
- Fond violet
- Plateformes violettes
- Pièces orange
- Ennemis rose
- Joueur cyan

### 4. RÉTRO
- Fond vert foncé
- Plateformes vert pixel
- Pièces jaune pixel
- Ennemis rouge pixel
- Joueur cyan pixel

### 5. FANTAISIE
- Fond violet profond
- Plateformes violet magique
- Pièces or brillant
- Ennemis turquoise
- Joueur rose vif

## 🔧 Configuration requise

- Python 3.7 ou supérieur
- Pygame 2.0.0 ou supérieur
- Système d'exploitation : Windows, macOS ou Linux

## 📁 Structure du projet

```
JeuPlateforme/
├── game.py                 # Point d'entrée du jeu
├── requirements.txt        # Dépendances Python
├── README.md              # Documentation
├── src/                   # Code source
│   ├── game/             # Logique du jeu
│   │   ├── __init__.py
│   │   ├── main.py       # Boucle principale
│   │   ├── menu.py       # Menus du jeu
│   │   ├── player.py     # Classe du joueur
│   │   ├── settings.py   # Configuration
│   │   └── ui.py         # Interface utilisateur
│   └── levels/           # Niveaux du jeu
│       ├── __init__.py
│       └── level*.py     # Fichiers de niveaux
└── assets/               # Ressources
    └── sounds/           # Sons et musique
```
