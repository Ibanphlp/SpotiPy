# 🎵 Spotipy

**Spotipy** est un lecteur de musique en ligne de commande développé en Python. Il permet de parcourir une bibliothèque musicale organisée par albums, de consulter les titres disponibles et de lancer ou d'arrêter la lecture des morceaux.

Le projet utilise **Python**, **SQLite** et **Pygame** pour gérer les données musicales et la lecture audio.

## ✨ Fonctionnalités

- 📀 Affichage des albums disponibles, avec leur artiste et leur année de sortie.
- 🎶 Consultation des titres contenus dans chaque album.
- ▶️ Lecture des morceaux au format MP3.
- ⏹️ Arrêt de la lecture en cours.
- 🎨 Interface en terminal avec des couleurs ANSI.
- 🗄️ Stockage des informations musicales dans une base de données SQLite.
- ℹ️ Affichage des crédits du projet.

## 🛠️ Technologies utilisées

- **Python 3** — logique du programme.
- **SQLite** — stockage et récupération des informations musicales.
- **Pygame** — lecture audio.
- **Terminal** — interface utilisateur en ligne de commande.

## 📋 Prérequis

Avant de lancer le projet, assurez-vous de disposer de :

- Python 3 installé.
- Pygame installé.
- La base de données `musique.db`.
- Les fichiers audio MP3 référencés dans la base de données.

## 📥 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Ibanphlp/SpotiPy.git
cd Spotipy
```

### 2. Installer les dépendances

Avec `pip` :

```bash
python3 -m pip install pygame
```

Sur certaines distributions Linux, il est également possible d'utiliser :

```bash
sudo apt install python3-pygame
```

### 3. Vérifier la structure du projet

Les fichiers doivent être organisés de la manière suivante :

```text
Spotipy/
├── main.py
├── bdd.py
├── musique.db
└── archive/
    ├── morceau1.mp3
    ├── morceau2.mp3
    └── ...
```

Le dossier `archive/` doit contenir les fichiers audio correspondant aux chemins enregistrés dans la base de données.
⚠️ Aucun fichier mp3 n'est inclus dans le projet pour respecter les droits d'auteur.

**Important :** les fichiers `main.py`, `bdd.py` et `musique.db` doivent être accessibles depuis le répertoire de lancement du programme.

## 🚀 Lancement

Depuis le répertoire du projet, exécutez :

```bash
python3 main.py
```

Le menu principal affiche la liste des albums disponibles. Vous pouvez ensuite saisir l'identifiant d'un album pour consulter les titres qu'il contient.

## 🗄️ Base de données

La base de données `musique.db` est gérée avec SQLite. Elle contient les informations nécessaires à l'organisation de la bibliothèque musicale.

Les principales tables utilisées par le programme sont :

- `Artiste` : informations sur les artistes et leurs groupes.
- `Album` : noms et années de sortie des albums.
- `Titre` : noms et références des morceaux.
- `Album_Artiste` : association entre les albums et les artistes.
- `Album_Titre` : association entre les albums et leurs titres.

Le module `bdd.py` regroupe les fonctions permettant de récupérer et d'afficher ces informations.

## ⚠️ Limitations connues

- La lecture audio dépend de la disponibilité des fichiers MP3 référencés dans la base de données.
- La lecture audio peut ne pas fonctionner dans certains environnements virtuels ou certaines machines configurées sans prise en charge audio.
- La navigation repose sur la saisie des identifiants affichés dans le terminal.

## 👥 Crédits

Projet développé par :

- **Iban PHILIPPE**
- **Lalie PLAGELET**
- **Vigil VUILLIOMENET**

---
