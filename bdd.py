import sqlite3

couleurs = { ## défini différentes couleurs pour les textes.
    "rouge": "\033[31m",
    "vert": "\033[0;32m",
    "jaune": "\033[33m",
    "bleu": "\033[0;36m",
    "violet": "\033[35m",
    "reset": "\033[0m"
}

style = { ##défini un style pour les textes.
    "gras":"\033[1m",
}


## Table Artiste

def sel_a():
    '''affiche l'intégralité des artistes'''
    conn = sqlite3.connect("musique.db") ##connecte sql à la bdd musique.db
    c = conn.cursor()
    val = "SELECT * FROM Artiste"  ##définit une instruction sql
    res = c.execute(val)     ##éxecute l'instructon et enregistre son résultat dans une variable
    return res.fetchall()  ##retourne le resultat
    conn.close() ##ferme la connection

def get_prenom_par_id_artiste(id):
    '''retourne le prénom d'un artiste en fonction de son id sql'''
    conn = sqlite3.connect("musique.db")
    c = conn.cursor()
    val = "SELECT prenom FROM Artiste WHERE id_titre =" + str(id)
    res = c.execute(val)
    return res.fetchall()
    conn.close()
    
def get_groupe_par_id_artiste(id):
    '''retourne le groupe d'un artiste s'il en a un, sinon indépendant'''
    conn = sqlite3.connect("musique.db")
    c = conn.cursor()
    val = "SELECT groupe FROM Artiste WHERE id_titre =" + str(id)
    res = c.execute(val)
    return res.fetchall()
    conn.close()


##Table Album
    
def get_annee_par_id_album(id):
    '''retourne l'année de sortie d'un album'''
    conn = sqlite3.connect("musique.db")
    c = conn.cursor()
    val = "SELECT annee FROM Album WHERE id_titre =" + str(id)
    res = c.execute(val)
    return res.fetchall()
    conn.close()

def sel_a_album():
    '''selectionne tout les albums de la base de donnée'''
    conn = sqlite3.connect("musique.db")
    c = conn.cursor()
    val = "SELECT * FROM Album"
    res = c.execute(val)
    return res.fetchall()
    conn.close()
##Table Titre
    
def get_lien_par_id_titre(id):
    '''retourne le raccourci de la musique depuis la base de donnée'''
    conn = sqlite3.connect("musique.db")
    c = conn.cursor()
    val = "SELECT lien FROM Titre WHERE id_titre =" + str(id)
    res = c.execute(val)
    return res.fetchall()
    conn.close()
    

def get_nom_par_id_titre(id):
    '''retourne le nom d'une musique grâce à son id'''
    conn = sqlite3.connect("musique.db")
    c = conn.cursor()
    val = "SELECT titre FROM Titre WHERE id_titre =" + str(id)
    res = c.execute(val)
    return res.fetchall()
    conn.close()

##autre


def make_dico():
    conn = sqlite3.connect("musique.db")
    c = conn.cursor()
    for album in sel_a_album():  ## pour chaque album dans tout ceux définis
        # retourne ligne par ligne l'id et le nom d'un album
        print(couleurs['vert'] + str(album[0]) + couleurs['reset'] + "  " + style['gras'] + album[1] + couleurs['reset'])
        # lie albums et artistes afin de retourner en dessous de chaque album l'artiste qui l'a créé
        artistes = c.execute(
            "SELECT Artiste.nom_artiste, Artiste.groupe FROM Album_Artiste JOIN Artiste ON Artiste.id = Album_Artiste.id_artiste WHERE Album_Artiste.id_album = " + str(album[0])
        ).fetchall()
        if len(artistes) > 1:
            print("   " + artistes[0][1])  ## si l'artiste est indépendant retourne le nom de scène
        else:
            print("   " + artistes[0][0])  ## sinon retourne le nom du groupe
        print("   (" + str(album[2]) + ")")  ## écrit l'année de sortie de l'album en dessous de celui-ci
        print()
    conn.close()

def get_titres_par_id_album(id):
    '''Retrouver les titres contenus dans un album donné avec son id'''
    conn = sqlite3.connect("musique.db")
    c = conn.cursor()
    res = c.execute("SELECT Titre.id_titre, Titre.titre FROM Album_Titre JOIN Titre ON Titre.id_titre = Album_Titre.id_titre WHERE Album_Titre.id_album = " + str(id))
    return res.fetchall()
    conn.close()
 
def make_dico_titres(id_album):
    '''Générer et afficher une liste des titres contenus dans un album avec son id'''
    conn = sqlite3.connect("musique.db")
    c = conn.cursor()
    album = c.execute("SELECT * FROM Album WHERE id = " + str(id_album)).fetchone()
    artistes = c.execute("SELECT Artiste.nom_artiste, Artiste.groupe FROM Album_Artiste JOIN Artiste ON Artiste.id = Album_Artiste.id_artiste WHERE Album_Artiste.id_album = " + str(id_album)).fetchall()
    conn.close()
 
    if len(artistes) > 1:
        print("\n" + style['gras'] + album[1] + couleurs['reset'] + " — " + artistes[0][1] + " " + str(album[2]) + "\n")
    else:
        print("\n" + style['gras'] + album[1] + couleurs['reset'] + " — " + artistes[0][0] + " (" + str(album[2]) + ")\n")
    for titre in get_titres_par_id_album(id_album):
        print("  " + couleurs['vert'] + str(titre[0]) + couleurs['reset'] + "  " + titre[1])
    print()
    return True



