display/
├── terminal.py          ← TA grosse tâche 6
└── mlx_display.py       ← seulement si vous faites l'option graphique

=====================================================
ÉTAPE 1 — COMPRENDRE LA REPRESENTATION DU LABYRINTHE
=====================================================

maze.width
maze.height
maze.entry
maze.exit

maze.has_wall(x, y, "N")
maze.has_wall(x, y, "E")
maze.has_wall(x, y, "S")
maze.has_wall(x, y, "W")

+---+
|   |
+---+

+---+
|
+---+

x = horizontal → gauche / droite
y = vertical   → haut / bas

visuellement :
           x →
        0     1     2     3
     +-----+-----+-----+-----+
y=0  | 0,0 | 1,0 | 2,0 | 3,0 |
     +-----+-----+-----+-----+
y=1  | 0,1 | 1,1 | 2,1 | 3,1 |
     +-----+-----+-----+-----+
y=2  | 0,2 | 1,2 | 2,2 | 3,2 |
     +-----+-----+-----+-----+
       ↓
       y

+    = intersection
---  = mur horizontal
|    = mur vertical
"   "= intérieur de la cellule


==================================================
ÉTAPE 2 — DESSINER SEULEMENT LA LIGNE DU HAUT
==================================================
def display_maze(maze) -> None:
    for x in range(maze.width):
        if maze.has_wall(x, 0, "N"):
            print("+---", end="")
        else:
            print("+   ", end="")

    print("+")


==================================================
ÉTAPE 3 — PARCOURIR LES LIGNES Y
==================================================
for y in range(maze.height):
    boucle des lignes x

Tu auras donc :
y = 0 → première ligne
y = 1 → deuxième ligne
y = 2 → troisième ligne
...

et a l'interieur:
for x in range(maze.width):
Donc mentalement :
for y
    └── for x

==================================================
ÉTAPE 4 — CONSTRUIRE LES 3 MORCEAUX D'UNE RANGEE
==================================================

Chaque ligne de cellules peut être affichée avec :
+---+---+---+
|   |       |
+---+   +---+

Donc on a  essentiellement :
    ligne des murs N
    ligne du contenu + murs E/W
    ligne des murs S (y = maze.height - 1)

==================================================
ÉTAPE 5 — AFFICHER L'ENTREE ET LA SORTIE DU LABYRINTHE
==================================================
    print("   ", end="")
    je le remplaces par cell_entry_exit(maze, x, y)

def cell_entry_exit(maze, x: int, y:int) -> str:
    if (x, y) == maze.entry:
        return " E "
    elif (x,y) == maze.exit:
        return " S "
    else:
        return "   "

==================================================
ÉTAPE 6 — AFFICHER LE CHEMIN AVEC maze.find_path()
==================================================

Pourquoi path and ? Parce que notre API de find_path() peut renvoyer None

donc on verifie s'il y a un path, si c'est le cas est ce que (x, y) est dedans ?
    show_path = True ou False
    permet de montrer le chemin en fonction
    on l'ajoute dans les fonctions display_maze et cell_entry_exit
    et on change le path, on ajoute show_path dans le elif qui contient path
    show_path = False -> on ignore le chemin
    sa donne :
    +---+---+---+---+
    | E |   |       |
    +---+   +---+   +
    |           |   |
    +   +---+   +---+
    |       |     S |
    +---+---+---+---+
    show_path = True -> on vérifie si (x, y) appartient au path
    sa donne:
    +---+---+---+---+
    | E | . |       |
    +---+   +---+   +
    |     .   . |   |
    +   +---+   +---+
    |       | .   S |
    +---+---+---+---+
 de ce fait on fait circuler un paramètre entre plusieurs fonctions.

=======================================================
ÉTAPE 7 — CREER LE MENU INTERACTIF AVEC maze.generate()
=======================================================

on va generer le menu interatif pour que le true et false se fasse de maniere
pour cela on va partir sur une nouvelle fonction :
    des qu'on lance le menu, le chemin est cache
    par la suite j'ai ajouter une boucle qui va tourner l'interface en continue
    avec while True
    voici la fonction creer :
    def terminal_menu(maze) -> None:
    show_path = False
    while True:
        display_maze(maze, show_path)
        print()
        print("[P] Afficher / masquer le chemin")
        print("[R] Regenerer le labyrinthe")
        print("[Q] Quitter")

    puis je suis passer de la creation de l'algo du menu
    choice = input("choix: ").strip().lower()

        if choice == "p":
            show_path = not show_path -> afficher/pas afficher (inverse show_path)
        elif choice == "r":
            maze.generate() -> generer maze
        elif choice == "q":
            break -> arrete le labirinthe (sprt du while)
        else :
            choix invalide

=====================================================
ÉTAPE 8 — VERIFIER QUE PYGAME PEUT OUVRIR UNE FENETRE
=====================================================

    je creer un environnement ou j'installe pygame

    code :
    j'importe pygame -> car je veux utiliser la bibliotheque Pygame
    sa me donne acces a : 
        -   pygame.init() -> Initialise les differents modules dont j'ai besoin (le bouton on)
        -   pygame.display...
        -   pygame.event...
        -   pygame.quit()

    j'ai cree la ft run_pygame() -> None:
    qui va gerer l'interface Pygame

    on veut un ecran -> screen = pygame.display.set_mode((800, 600))
    set_mode() cree la fenetre (lageur pixel sur hauteur pixel)

    pygame.display.set_caption("A-Maze-ing") -> sa donne un titre a la fenetre
    
    je creer un booleen
    running = True
    - la fenetre continue a tourner
    running False
    - on doit fermer la fenetre

    La boucle While
    While Running est comme le while true dans le fichier terminal, juste que la 
    c'est running.

    Les events -> for event in pygame.event.get():
    Pygame surveille ce que fait l'utilisateur
        déplacer souris
        cliquer
        appuyer sur P
        appuyer sur ESC
        fermer la fenêtre
        etc.
    pygame.event.get() ->  recupere les events qui viennent de se produire
    for event in pygame.event.get() -> Pour chaque événement reçu, regarde ce que c’est.

    if event.type == pygame.QUIT:
        detecter la fermeture -> quand l'utilisateur demande a fermer la  fenetre

    pygame.quit()
    dit a Pygame -> Tu peux arreter tes modules et fermer proprement 

    screen.fill((30, 30, 30)) -> correspond au couleur (R,G,B) et chaque valeur va de 0 a 255

    pygame.display.flip() -> dit a pygame:
        - maintenant, affiche dans la fenetre ce que j'ai dessine sur screen

    pygame.draw.line(
    screen,            ← OÙ dessiner
    (255,255,255),     ← COULEUR : blanc
    (100,100),         ← DÉPART : x=100, y=100
    (400,100),         ← ARRIVÉE : x=400, y=100
    3                  ← ÉPAISSEUR : 3 pixels
)

===============================================================
ÉTAPE 9 — COMPRENDRE LA TAILLE DES CELLULES ET LE REPERE PYGAME
===============================================================

    (0,0) ─────────────────────→ x
    │
    │       (100,100) ─────────── (400,100)
    │
    │
    ↓
    y

    Contrairement à un repère de maths classique, y augmente vers le bas.


    Dans le fichier terminal, on etait partie sur sur les charactere + --- |
    la cellule ressemblait a :
    +---+
    |   |
    +---+

    dans Pygame, on donne des mesure a la celule
    par exemple size_cell = 50
    pour une grille de 5 x 5 par exemple -> 5 x 50 de largeur et hauteur

=====================================================
ÉTAPE 10 — CONVERTIR LES COORDONNEES (x, y) EN PIXELS
=====================================================
    -> donc on va convertir les coordonnees du maze en pixels:
    exemple :
    cellule (0,0) → pixel (0,0)
    cellule (1,0) → pixel (50,0)
    cellule (2,0) → pixel (100,0)

    la formule : 
    pixel_x = x * SIZE_CELL
    pixel_y = y * SIZE_CELL

on part de ce qu'on a fait dans terminal 
    for x in range(maze.width):
        if maze.has_wall(x, y, "N"):
            print("+---", end="")  |  pygame.draw.line(...)
        else:                      |  
            print("+   ", end="")  |  
        print("+")                 |  


comprendre les deplacements :
                N

    (pixel_x, pixel_y) ───────── (pixel_x + SIZE_CELL, pixel_y)
            +--------------------------------+
            |                                |
        W |                                | E
            |                                |
            +--------------------------------+
    (pixel_x, pixel_y + SIZE_CELL)    (pixel_x + SIZE_CELL,
                                    pixel_y + SIZE_CELL)

                S

    -> L'OFFSET / MARGE
        pixel_x = x * SIZE_CELL
        pixel_y = y * SIZE_CELL

        pixel_x = OFFSET_X + x * SIZE_CELL
        pixel_y = OFFSET_Y + y * SIZE_CELL

        EXEMPLE:offset_x = 50
        0 + 0x50 = 0    | avant
        50 + 0x50 = 50  | apres  on a 50 pixels de marge

    Prenons la cellule (0, 0) :
    pixel_x = OFFSET_X + x * SIZE_CELL
    pixel_y = OFFSET_Y + y * SIZE_CELL

    pixel_x = 50 + (0 × 50) = 50
    pixel_y = 50 + (0 × 50) = 50

    Donc au lieu de commencer ici :
    (0,0)
    ┌────────────
    │ MAZE

    elle commence la :
    (0,0)

        50 px
        ↓
        ┌────────────
        │ MAZE
        │
    Et la cellule (2, 1) :
    pixel_x = 50 + (2 × 50) = 150
    pixel_y = 50 + (1 × 50) = 100

    l'offset deplace donc tout le lab mais ne change ni la taille des cells et ni leur
    position les unes par rapport aux autres

    Maintenant on va centrer automatiquement le lab dans le screen

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    SIZE_CELL = 50

    le maze connait maze.width et maze.height
    on a besoin d'une formule pour calculer la largeur et prendre en compte les marges

    maze_pixel_width = maze.width * SIZE_CELL
    maze_pixel_height = maze.height * SIZE_CELL

    offset_x = (WINDOW_WIDTH - maze_pixel_width) // 2
    offset_y = (WINDOW_HEIGHT - maze_pixel_height) // 2

    se qui se passe : avec un offset_x de 800 et un offset_y de 600
    offset_x = (800 - 200) // 2
            = 600 // 2
            = 300

    offset_y = (600 - 150) // 2
            = 450 // 2
            = 225

    Fenêtre 800 px
    ┌───────────────────────────────────────┐
    │                                       │
    │        300px    MAZE    300px         │
    │              ┌──────────┐             │
    │              │          │             │
    │              │ 200×150  │             │
    │              │          │             │
    │              └──────────┘             │
    │                                       │
    └───────────────────────────────────────┘

dans la ft draw cell :
on utilise les constantes OFFSET_X et OFFSET_Y.
    mais maintenant ils sont calcules dans la ft run_pygame().

    la signature : 
    def draw_entry_exit(maze, screen, offset_x: int, offset_y: int) -> None:
    -> pas besoin de x et y, car le maze.entry(0,0) et maze.exit(3,2) les ont deja

    ... tuple unpacking
        maze.entry
    ↓
    (0, 0)
    ↓  ↓
    x  y

    maze_entry_x = 0
    maze_entry_y = 0

    entry_pixel_x = offset_x + maze_entry_x * SIZE_CELL
    offset_x                    → où commence le maze dans la fenêtre
    +
    maze_entry_x * SIZE_CELL    → où se trouve l'entrée dans le maze
    =
    entry_pixel_x               → où commence la cellule d'entrée à l'écran

    entry_pixel_x = 300
    SIZE_CELL = 50

    SIZE_CELL // 2 = 25

    entry_center_x = 300 + 25
                = 325 ✅

    300           325           350
    ↓             ↓             ↓
    +-------------X-------------+
    |                           |
    |          cellule          |
    |                           |
    +---------------------------+

afficher du texte dans pygame :
-> choisisr / creer une police
    Pygame permet d'utiliser sa police par defaut :
    font = pygame.font.Font(None, 30)
    pygame.font.Font(None, 30)
                 │     │
                 │     └── taille du texte
                 │
                 └── None = police par défaut de Pygame

-> Transformer "E" en image
   la var font represente la police, mais pygame ne peut pas daire directement: dessine "E"

   il faut d'abord rendre le texte avec .render().
   la structure est : 
   font.render(texte, antialiasing, couleur)
                |        |           |
                |        |           └── RGB
                |        └─True = contourss du texte plus lisses
                |
                └─Ce qu'on veut ecrire
    font -> .render("E", True, (255, 255, 255))
    -> une surface content l'image du E

on va aller pour nom : font_entry = font.render(texte, antialiasing, couleur)

font.render() ne retourne pas du texte. Il retiurne un objet Pygame de type Surface.
                  ------------------
font.render() -> |Surface Pygame "E"| -> entry_text
                  ------------------
or, les objets Surface de Pygame possedes deja plusieurs methodes.

Parmi elles, il y a : .get_rect()

get_rect()
    quand on ecrit entry_text.get_rect()
    -> "entry_text, toi qui est une Surface Pygame, donne-moi ton rectangle"

donc entry_text = l'image du E
entry_rect = ou cette image doit etre positionnee

blit()
    permet de dire a screen :
    "prends cette image(entry_text) et dessine-la a cette position (entry_rect)"
    screen.blit(surface, position)

-> Placer cette image sur screen
le chemin complet qu'on a fait :
"E"
 │
 │ font.render()
 ▼
entry_text              ← Surface : l'image du E
 │
 │ .get_rect(center=...)
 ▼
entry_rect              ← position de cette image
 │
 │ screen.blit()
 ▼
SCREEN
┌───────────────────┐
│                   │
│        E          │
│                   │
└───────────────────┘

on a fait la meme chose pour la sortie.
on a cree un exit

==================================================
ÉTAPE 11 — AFFICHER LE CHEMIN DANS PYGAME
==================================================

Dans le terminal, pour afficher le chemin on faisait :

    path = maze.find_path()

puis pour chaque cellule :

    if (x, y) in path:
        afficher "."

Dans Pygame on va aussi utiliser :

    maze.find_path()

mais cette fois on ne veut pas afficher des "." dans les cellules.
On veut tracer une ligne qui passe par le centre des cellules du chemin.


On cree donc une nouvelle fonction :

    def draw_path(maze, screen, offset_x: int, offset_y: int) -> None:
        path = maze.find_path()

Pourquoi une fonction separee ?

    draw_cell()          -> dessine les murs
    draw_entry_exit()    -> dessine E et S
    draw_path()          -> dessine le chemin

chaque fonction a donc son role.


--------------------------------------------------
1. RECUPERER LE PATH
--------------------------------------------------

    path = maze.find_path()

find_path() nous retourne par exemple :

    [
        (0, 0),
        (1, 0),
        (1, 1),
        (2, 1),
        (2, 2),
        (3, 2)
    ]

Chaque tuple correspond a une cellule du chemin.

visuellement :

    (0,0) -> (1,0)
               |
               v
            (1,1) -> (2,1)
                        |
                        v
                     (2,2) -> (3,2)


On verifie ensuite qu'un chemin existe :

    if path:

Pourquoi ?

find_path() peut renvoyer un chemin mais peut aussi renvoyer None
s'il ne trouve pas de chemin.

Donc :

    if path:
        ...

veut dire :

    "s'il existe bien un chemin, alors je peux le dessiner"


--------------------------------------------------
2. PARCOURIR LES CELLULES DU PATH
--------------------------------------------------

On utilise :

    for path_x, path_y in path:

Ici on utilise encore le tuple unpacking.

Si le premier element du path est :

    (0, 0)

alors :

    path_x = 0
    path_y = 0

Au prochain tour si on a :

    (1, 0)

alors :

    path_x = 1
    path_y = 0


Donc :

    for path_x, path_y in path:

veut dire :

    "pour chaque cellule (x, y) du chemin,
     recupere son x et son y"


--------------------------------------------------
3. CONVERTIR LES COORDONNEES DU PATH EN PIXELS
--------------------------------------------------

Comme pour entry et exit, les coordonnees du maze ne sont
pas directement des coordonnees Pygame.

Par exemple :

    path_x = 1
    path_y = 0

ne veut pas dire :

    pixel (1, 0)

Cela veut dire :

    cellule (1, 0)


Il faut donc refaire notre conversion :

    path_pixel_x = offset_x + path_x * SIZE_CELL
    path_pixel_y = offset_y + path_y * SIZE_CELL


Exemple :

    offset_x = 300
    SIZE_CELL = 50
    path_x = 1

    path_pixel_x = 300 + 1 * 50
                 = 350


Donc :

    coordonnee maze
          |
          v
        (1,0)
          |
          | conversion
          v
    coin de la cellule en pixels
        (350,225)


--------------------------------------------------
4. TROUVER LE CENTRE DE CHAQUE CELLULE DU PATH
--------------------------------------------------

On ne veut pas que notre chemin passe sur le coin des cellules.

On veut qu'il passe au centre.

Donc comme pour E et S :

    path_center_pixel_x = path_pixel_x + SIZE_CELL // 2
    path_center_pixel_y = path_pixel_y + SIZE_CELL // 2


Exemple avec SIZE_CELL = 50 :

    SIZE_CELL // 2 = 25

donc :

    path_pixel_x = 350

    path_center_pixel_x = 350 + 25
                        = 375


visuellement :

    coin de la cellule
    ↓
    +-------------------+
    |                   |
    |         X         |  <- centre
    |                   |
    +-------------------+

              X
              |
              └── point par lequel notre chemin va passer


--------------------------------------------------
5. CREER UN POINT PYGAME
--------------------------------------------------

Maintenant on possede :

    path_center_pixel_x
    path_center_pixel_y

Mais pygame.draw.line() attend des points sous forme de tuple :

    (x, y)

Donc on cree :

    current_point = (
        path_center_pixel_x,
        path_center_pixel_y
    )


Par exemple :

    path_center_pixel_x = 375
    path_center_pixel_y = 250

donne :

    current_point = (375, 250)


ATTENTION au tuple :

    (375, 250)       -> un point avec x et y

et pas :

    (375), (250)

Le premier est un seul tuple contenant les deux coordonnees.


--------------------------------------------------
6. RELIER LES POINTS ENTRE EUX
--------------------------------------------------

Maintenant imaginons que find_path() nous donne :

    A -> B -> C -> D

Pour dessiner le chemin on doit faire :

    A -------- B
               |
               C -------- D


Mais pour dessiner A -> B,
quand on arrive sur B, il faut encore se souvenir de A.

On cree donc AVANT la boucle :

    previous_point = None


Pourquoi avant le for ?

Parce que previous_point doit survivre entre les tours de boucle.

Au depart :

    previous_point = None


Premier tour :

    current_point = A

mais :

    previous_point = None

On ne peut donc pas encore dessiner de ligne.


Ensuite :

    previous_point = current_point

donc :

    previous_point = A


Deuxieme tour :

    previous_point = A
    current_point = B

maintenant on possede les deux points :

    A -------- B


On peut donc faire :

    pygame.draw.line(
        screen,
        (255, 255, 255),
        previous_point,
        current_point,
        3
    )


--------------------------------------------------
7. POURQUOI ON VERIFIE previous_point ?
--------------------------------------------------

On utilise :

    if previous_point is not None:

car au premier tour :

    previous_point = None

et il n'existe encore aucun point precedent.


Le fonctionnement complet devient :

    depart :
        previous_point = None

    cellule A :
        current_point = A
        previous = None
        -> pas de ligne

        previous_point = A


    cellule B :
        current_point = B
        previous_point = A

        -> dessine A -------- B

        previous_point = B


    cellule C :
        current_point = C
        previous_point = B

        -> dessine B -------- C

        previous_point = C


    cellule D :
        current_point = D
        previous_point = C

        -> dessine C -------- D


Donc petit a petit :

    A
    ↓
    A ----- B
            ↓
    A ----- B ----- C
                    ↓
    A ----- B ----- C ----- D


--------------------------------------------------
8. previous_point = current_point
--------------------------------------------------

A la fin de chaque tour de boucle on fait :

    previous_point = current_point


ATTENTION au sens du =

    previous_point = current_point

veut dire :

    "previous_point prend maintenant la valeur de current_point"


Par exemple :

    previous_point = A
    current_point = B

puis :

    previous_point = current_point

donne :

    previous_point = B


On ne veut PAS faire :

    current_point = previous_point

car dans ce cas on remplacerait notre nouveau point par l'ancien.


Rappel :

    variable qui recoit = valeur qu'on lui donne

donc :

    previous_point = current_point
          ↑                 ↑
      recoit          valeur donnee


--------------------------------------------------
9. LA FONCTION draw_path() OBTENUE
--------------------------------------------------

On a donc construit :

    def draw_path(maze, screen, offset_x: int, offset_y: int) -> None:
        path = maze.find_path()

        if path:
            previous_point = None

            for path_x, path_y in path:
                path_pixel_x = offset_x + path_x * SIZE_CELL
                path_pixel_y = offset_y + path_y * SIZE_CELL

                path_center_pixel_x = path_pixel_x + SIZE_CELL // 2
                path_center_pixel_y = path_pixel_y + SIZE_CELL // 2

                current_point = (
                    path_center_pixel_x,
                    path_center_pixel_y
                )

                if previous_point is not None:
                    pygame.draw.line(
                        screen,
                        (255, 255, 255),
                        previous_point,
                        current_point,
                        3
                    )

                previous_point = current_point


--------------------------------------------------
10. APPELER draw_path()
--------------------------------------------------

Comme pour draw_entry_exit(), creer la fonction ne suffit pas.

Si on fait seulement :

    def draw_path(...):

Python connait la fonction,
mais personne ne lui demande encore de l'executer.


Il faut donc l'appeler dans run_pygame() :

    draw_path(maze, screen, offset_x, offset_y)


On la dessine dans cet ordre :

    1. screen.fill()
                ↓
    2. draw_cell()
                ↓
    3. draw_path()
                ↓
    4. draw_entry_exit()
                ↓
    5. pygame.display.flip()


Pourquoi draw_entry_exit() apres draw_path() ?

Parce que le chemin commence sur E et finit sur S.

Si on dessine le chemin apres les lettres,
la ligne pourrait passer par-dessus les lettres.

Donc :

    chemin d'abord
    lettres ensuite

permet d'avoir :

    ───── E ───────────── S

avec E et S visibles au-dessus du chemin.


--------------------------------------------------
RESULTAT ACTUEL
--------------------------------------------------

On a maintenant une interface graphique capable de :

    - ouvrir une fenetre Pygame
    - parcourir toutes les cellules du maze
    - convertir les coordonnees (x,y) en pixels
    - centrer automatiquement le maze
    - dessiner les murs N / E / S / W
    - afficher l'entree E
    - afficher la sortie S
    - recuperer le chemin avec find_path()
    - convertir chaque cellule du chemin en point pixel
    - relier les points avec pygame.draw.line()


Visuellement on est passe de :

    MazeGenerator
         |
         | width / height
         | has_wall()
         | entry / exit
         | find_path()
         v
    -------------------------
        PYGAME DISPLAY
    -------------------------
         |
         +--> murs
         |
         +--> E / S
         |
         +--> chemin


PROCHAINE ETAPE :

    rendre le chemin interactif avec la touche P

Comme dans terminal.py :

    show_path = False

    P -> show_path = not show_path

Mais cette fois l'input ne viendra pas de :

    input()

Il viendra des events Pygame :

    pygame.event.get()

On va donc apprendre a detecter :
    - une touche du clavier
    - laquelle a ete appuyee
    - puis modifier show_path

==================================================
ÉTAPE 12 — RENDRE L'INTERFACE PYGAME INTERACTIVE
==================================================

OBJECTIF :
Permettre à l'utilisateur d'interagir avec le labyrinthe
directement depuis le clavier.

Touches :
P → afficher / masquer le chemin
R → régénérer le labyrinthe
Q → quitter


--------------------------------------------------
1. CREER L'ETAT show_path
--------------------------------------------------

Dans run_pygame(), on crée :

show_path = False

C'est un booléen qui mémorise si le chemin doit être affiché.

False → chemin caché
True  → chemin affiché


--------------------------------------------------
2. AFFICHER LE CHEMIN SEULEMENT SI show_path EST TRUE
--------------------------------------------------

Dans la boucle principale :

if show_path:
    draw_path(maze, screen, offset_x, offset_y, cell_size)

Donc :

show_path = False
        ↓
draw_path() n'est pas appelée
        ↓
pas de chemin

show_path = True
        ↓
draw_path() est appelée
        ↓
chemin affiché


--------------------------------------------------
3. DETECTER UNE TOUCHE AVEC pygame.KEYDOWN
--------------------------------------------------

Pygame récupère les événements avec :

for event in pygame.event.get():

Ensuite :

if event.type == pygame.KEYDOWN:

permet de savoir qu'une touche du clavier vient
d'être pressée.


--------------------------------------------------
4. IDENTIFIER LA TOUCHE AVEC event.key
--------------------------------------------------

Une fois qu'on sait qu'une touche a été pressée,
on regarde laquelle avec :

event.key

Exemples :

pygame.K_p → touche P
pygame.K_r → touche R
pygame.K_q → touche Q


--------------------------------------------------
5. AFFICHER / MASQUER LE CHEMIN AVEC P
--------------------------------------------------

if event.key == pygame.K_p:
    show_path = not show_path

"not" inverse le booléen.

False → not False → True
True  → not True  → False

Donc à chaque pression sur P :

P
↓
show_path change d'état
↓
le chemin apparaît ou disparaît


IMPORTANT :

=   → affecter une valeur
==  → comparer deux valeurs
is  → vérifier l'identité d'un objet

Ici :

show_path = not show_path

signifie qu'on remplace l'ancienne valeur
par son contraire.


--------------------------------------------------
6. REGENERER LE LABYRINTHE AVEC R
--------------------------------------------------

elif event.key == pygame.K_r:
    maze.generate()

On demande directement à l'objet maze
de générer un nouveau labyrinthe.

Avec MockMaze :

generate() contient pass

donc rien ne change visuellement.

Avec le vrai MazeGenerator du projet,
maze.generate() pourra réellement régénérer le maze.


--------------------------------------------------
7. QUITTER L'INTERFACE AVEC Q
--------------------------------------------------

elif event.key == pygame.K_q:
    running = False

La boucle principale fonctionne avec :

while running:

Donc :

running = True
      ↓
la fenêtre continue

Q
↓
running = False
↓
la condition du while devient fausse
↓
la boucle principale s'arrête


IMPORTANT :

On n'utilise pas simplement "break" ici.

Pourquoi ?

Parce que le traitement des événements est dans :

while running:
    for event in pygame.event.get():

Un break dans le "for event" quitterait seulement
la boucle for.

Le while pourrait continuer.

Avec :

running = False

on demande réellement à la boucle principale
de s'arrêter.


--------------------------------------------------
8. GERER LA CROIX DE LA FENETRE
--------------------------------------------------

if event.type == pygame.QUIT:
    running = False

pygame.QUIT correspond à la fermeture de la fenêtre
avec la croix.

Donc Q et la croix ont finalement le même effet :

running = False


--------------------------------------------------
9. ATTENTION AUX APPELS EN DOUBLE
--------------------------------------------------

Le chemin doit uniquement être dessiné ici :

if show_path:
    draw_path(...)

Si on écrit ensuite :

draw_path(...)

sans condition, le chemin sera toujours dessiné,
même lorsque show_path vaut False.

Donc une condition peut être correcte,
mais un autre appel plus loin dans le programme
peut annuler son effet.


=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================

OBJECTIF :

Ne plus imposer une taille fixe aux cellules.

La taille des cellules doit maintenant s'adapter
à la taille du labyrinthe et à la taille de la fenêtre.


--------------------------------------------------
1. LE PROBLEME DE SIZE_CELL
--------------------------------------------------

Avant :

SIZE_CELL = 50

Chaque cellule faisait toujours :

50 × 50 pixels

Exemple :

maze.width = 20

20 × 50 = 1000 pixels

Mais notre fenêtre fait seulement :

SCREEN_WIDTH = 800

Donc :

1000 > 800

Le labyrinthe dépasse de la fenêtre.


--------------------------------------------------
2. CALCULER LA TAILLE POSSIBLE EN LARGEUR
--------------------------------------------------

cell_width = SCREEN_WIDTH // maze.width

On demande :

"Combien de pixels maximum puis-je donner
à chaque cellule pour que toutes les colonnes
rentrent dans la largeur ?"

Exemple :

SCREEN_WIDTH = 800
maze.width = 20

800 // 20 = 40

Donc chaque cellule peut faire au maximum
40 pixels de large.


--------------------------------------------------
3. CALCULER LA TAILLE POSSIBLE EN HAUTEUR
--------------------------------------------------

cell_height = SCREEN_HEIGHT // maze.height

Même principe pour la hauteur.

Exemple :

SCREEN_HEIGHT = 600
maze.height = 15

600 // 15 = 40


--------------------------------------------------
4. CHOISIR LA PLUS PETITE VALEUR
--------------------------------------------------

Une cellule doit rester carrée.

On ne peut donc pas avoir :

largeur = 40
hauteur = 60

On choisit la contrainte la plus petite :

cell_size = min(cell_width, cell_height)

Exemple :

cell_width = 80
cell_height = 30

min(80, 30)
     ↓
30

Donc :

cell_size = 30

La cellule fera :

30 × 30 pixels

Cela garantit que le labyrinthe rentre
à la fois en largeur ET en hauteur.


--------------------------------------------------
5. LIMITER LA TAILLE MAXIMALE
--------------------------------------------------

Problème :

Avec un petit labyrinthe 4 × 3 :

800 // 4 = 200
600 // 3 = 200

Donc :

cell_size = 200

Les cellules deviennent énormes.

On ajoute donc une taille maximale :

max_cell_size = 50

Puis :

cell_size = min(
    cell_width,
    cell_height,
    max_cell_size
)

Exemple petit maze :

min(200, 200, 50)
        ↓
50

Exemple grand maze :

min(40, 40, 50)
       ↓
40


Cela signifie :

"Réduis les cellules si nécessaire,
mais ne dépasse jamais 50 pixels."


--------------------------------------------------
6. CALCULER LA TAILLE REELLE DU LABYRINTHE
--------------------------------------------------

Maintenant on utilise cell_size :

maze_pixel_width = maze.width * cell_size
maze_pixel_height = maze.height * cell_size

Exemple :

maze.width = 20
cell_size = 40

20 × 40 = 800 pixels


--------------------------------------------------
7. CALCULER LES OFFSETS
--------------------------------------------------

Une fois la taille réelle du maze connue,
on peut calculer sa position dans la fenêtre :

offset_x = (SCREEN_WIDTH - maze_pixel_width) // 2
offset_y = (SCREEN_HEIGHT - maze_pixel_height) // 2

Les offsets servent à centrer le labyrinthe.


--------------------------------------------------
8. TRANSMETTRE cell_size AUX FONCTIONS
--------------------------------------------------

cell_size est calculée dans run_pygame().

Les autres fonctions ne connaissent pas
automatiquement cette variable.

Il faut donc la leur transmettre.

Exemple :

draw_cell(
    maze,
    screen,
    x,
    y,
    offset_x,
    offset_y,
    cell_size
)

Et la fonction doit accepter cet argument :

def draw_cell(
    maze,
    screen,
    x: int,
    y: int,
    offset_x: int,
    offset_y: int,
    cell_size: int
) -> None:


PRINCIPE IMPORTANT :

run_pygame()
      ↓
calcule cell_size
      ↓
transmet la valeur
      ↓
draw_cell(..., cell_size)
draw_path(..., cell_size)
draw_entry_exit(..., cell_size)


--------------------------------------------------
9. UTILISER cell_size DANS draw_cell()
--------------------------------------------------

Avant :

pixel_x = offset_x + x * SIZE_CELL
pixel_y = offset_y + y * SIZE_CELL

Maintenant :

pixel_x = offset_x + x * cell_size
pixel_y = offset_y + y * cell_size

Tous les calculs des murs utilisent également
cell_size.

Exemple pour le mur Nord :

(pixel_x, pixel_y)
        ↓
(pixel_x + cell_size, pixel_y)


--------------------------------------------------
10. UTILISER cell_size DANS draw_entry_exit()
--------------------------------------------------

La position de E et S dépend aussi
de la taille des cellules.

Exemple :

entry_pixel_x = offset_x + maze_entry_x * cell_size
entry_pixel_y = offset_y + maze_entry_y * cell_size

Pour trouver le centre :

entry_center_pixel_x = entry_pixel_x + cell_size // 2
entry_center_pixel_y = entry_pixel_y + cell_size // 2

Même principe pour la sortie.


--------------------------------------------------
11. UTILISER cell_size DANS draw_path()
--------------------------------------------------

Chaque cellule du path doit être convertie
en coordonnées pixels :

path_pixel_x = offset_x + path_x * cell_size
path_pixel_y = offset_y + path_y * cell_size

Puis on récupère son centre :

path_center_pixel_x = path_pixel_x + cell_size // 2
path_center_pixel_y = path_pixel_y + cell_size // 2

Le chemin reste donc centré dans les cellules,
quelle que soit leur taille.


--------------------------------------------------
12. SIZE_CELL N'EST PLUS NECESSAIRE
--------------------------------------------------

Avant :

SIZE_CELL = 50

était une constante globale.

Maintenant :

cell_size

est calculée dynamiquement dans run_pygame().

SIZE_CELL peut donc être supprimée.


--------------------------------------------------
13. RESUME DU FLUX
--------------------------------------------------

SCREEN_WIDTH / SCREEN_HEIGHT
           +
maze.width / maze.height
           ↓
cell_width / cell_height
           ↓
min(cell_width, cell_height, max_cell_size)
           ↓
       cell_size
           ↓
maze_pixel_width / maze_pixel_height
           ↓
       offsets
           ↓
 ┌─────────┼──────────────┐
 ↓         ↓              ↓
draw_cell  draw_path  draw_entry_exit

==================================================
ÉTAPE 14 — BRANCHER PYGAME AU VRAI MAZEGENERATOR
==================================================

OBJECTIF :

Jusqu'ici, Pygame utilisait MockMaze.

MockMaze était un faux labyrinthe utilisé uniquement pour développer
et tester l'affichage sans dépendre du vrai générateur.

On avait donc :

MockMaze
   ↓
run_pygame()
   ↓
affichage Pygame


Maintenant que l'affichage fonctionne, on veut utiliser le vrai
MazeGenerator.

On veut obtenir :

MazeGenerator
      ↓
maze.generate()
      ↓
run_pygame(maze)
      ↓
affichage du vrai labyrinthe


==================================================
1. COMPRENDRE MODULE / CLASSE / PACKAGE
==================================================

Il faut distinguer trois choses :

mazegen/                  → package Python
│
├── __init__.py
│
└── generator.py          → module Python
        │
        └── MazeGenerator → classe


Donc :

generator.py

est le FICHIER.


Alors que :

MazeGenerator

est la CLASSE contenue dans ce fichier.


Notre architecture est donc :

mazegen/
├── __init__.py
├── generator.py
├── grid.py
├── walls.py
├── solver.py
└── pattern42.py


==================================================
2. EXPOSER MAZEGENERATOR DEPUIS LE PACKAGE
==================================================

Dans :

mazegen/__init__.py

on met :

from .generator import MazeGenerator


Le "." signifie :

"cherche generator dans le package actuel"


Donc :

mazegen/
│
├── __init__.py
│       ↓
│   from .generator import MazeGenerator
│
└── generator.py
        ↓
    class MazeGenerator


Cela permet ensuite d'écrire ailleurs :

from mazegen import MazeGenerator


ATTENTION :

Dans __init__.py, il ne fallait PAS écrire :

from mazegen import MazeGenerator

car __init__.py aurait essayé d'importer MazeGenerator depuis
le package mazegen alors que ce même package était encore en train
d'être initialisé.

Cela provoque un import circulaire.


==================================================
3. VERIFIER QUE L'IMPORT FONCTIONNE
==================================================

On a testé :

python -c "from mazegen import MazeGenerator; print(MazeGenerator)"


Le terminal a retourné :

<class 'mazegen.generator.MazeGenerator'>


Cela signifie :

mazegen
   ↓
__init__.py
   ↓
generator.py
   ↓
MazeGenerator

fonctionne correctement.


==================================================
4. REMPLACER MOCKMAZE PAR MAZEGENERATOR
==================================================

Avant, pygame_display.py utilisait :

if __name__ == "__main__":
    from mock_maze import MockMaze

    maze = MockMaze()
    run_pygame(maze)


MockMaze servait uniquement à simuler l'interface du vrai labyrinthe.


Maintenant, on utilise :

from mazegen import MazeGenerator


Puis on crée un vrai objet :

maze = MazeGenerator(
    width=20,
    height=15,
    entry=(0, 0),
    exit=(19, 14),
    perfect=True,
    seed=42
)


IMPORTANT :

MazeGenerator(...)

crée l'OBJET.

Mais cela ne génère pas encore le labyrinthe.


On a donc trois étapes différentes :

MazeGenerator(...)
      ↓
création de l'objet

maze.generate()
      ↓
génération du labyrinthe

run_pygame(maze)
      ↓
affichage du labyrinthe


Le code de test devient donc :

maze = MazeGenerator(
    width=20,
    height=15,
    entry=(0, 0),
    exit=(19, 14),
    perfect=True,
    seed=42
)

maze.generate()

run_pygame(maze)


==================================================
5. TESTER LE VRAI LABYRINTHE DANS PYGAME
==================================================

On lance :

python -m display.pygame_display


Le vrai labyrinthe 20 x 15 apparaît correctement.


Cela permet de vérifier que :

maze.width
maze.height

fonctionnent.


Mais également que :

maze.has_wall()

est compatible avec notre fonction :

draw_cell()


On a donc :

MazeGenerator
      ↓
has_wall(x, y, direction)
      ↓
draw_cell()
      ↓
murs affichés dans Pygame


==================================================
6. TESTER LE CHEMIN AVEC P
==================================================

Quand on appuie sur P :

show_path change de valeur.


Puis :

if show_path:
    draw_path(...)


draw_path() appelle :

maze.find_path()


Cette fois, ce n'est plus le chemin artificiel de MockMaze.

C'est le vrai BFS du MazeGenerator.


Le flux devient :

P
↓
show_path = True
↓
draw_path()
↓
maze.find_path()
↓
BFS
↓
liste des cellules du chemin
↓
conversion cellules → pixels
↓
affichage du chemin entre E et S


Le test fonctionne :

P affiche correctement le chemin du vrai labyrinthe.


==================================================
7. TESTER LA REGENERATION AVEC R
==================================================

Avec MockMaze :

maze.generate()

ne faisait rien car sa méthode generate() contenait seulement :

pass


Avec le vrai MazeGenerator :

maze.generate()

génère réellement un nouveau labyrinthe.


Donc :

R
↓
pygame.K_r
↓
maze.generate()
↓
nouveaux passages
↓
nouveau labyrinthe affiché


Le test fonctionne.

Le labyrinthe change lorsque l'on appuie sur R.


Si on appuie ensuite sur P :

maze.find_path()

calcule le chemin correspondant au NOUVEAU labyrinthe.


Donc :

R → nouveau labyrinthe
P → nouveau chemin


==================================================
8. TESTER LE PROGRAMME PRINCIPAL
==================================================

Il ne suffisait pas de tester Pygame.

Il fallait également vérifier que :

a_maze_ing.py

fonctionnait toujours avec la nouvelle organisation du package.


a_maze_ing.py utilise :

from mazegen import MazeGenerator


On a donc lancé :

python a_maze_ing.py config.txt


Au premier test, une erreur est apparue :

Erreur : ligne 1 mal formee :
'from dataclasses import dataclass'


Cette erreur ne venait PAS de MazeGenerator.


Le problème venait de config.txt.


==================================================
9. CORRIGER CONFIG.TXT
==================================================

config.txt contenait accidentellement du code Python provenant
de config_parser.py.


Or parse_config() attend le format :

CLE=VALEUR


On a donc remis :

WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42


Le programme peut maintenant faire :

config.txt
    ↓
parse_config()
    ↓
dictionnaire
    ↓
convert_config()
    ↓
MazeConfig
    ↓
MazeGenerator(...)


==================================================
10. TESTER A_MAZE_ING.PY
==================================================

On relance :

python a_maze_ing.py config.txt


Aucune erreur n'est affichée.


Cela signifie que :

config.txt
    ↓
parse_config()
    ↓
convert_config()
    ↓
MazeGenerator(...)
    ↓
maze.generate()
    ↓
write_output()

fonctionne.


Le programme n'affiche pas forcément quelque chose dans le terminal.

Son résultat principal est écrit dans :

maze.txt


==================================================
11. VERIFIER MAZE.TXT
==================================================

On utilise :

head maze.txt


Exemple obtenu :

D539553955553D517913
97C693C69553C53C56AA
8153AC55695693A9556A
AAD2C3979693AAC6957A
...


Chaque caractère représente une cellule du labyrinthe
sous forme hexadécimale.


Le flux complet fonctionne donc :

MazeGenerator
      ↓
to_grid()
      ↓
valeur des murs
      ↓
conversion hexadécimale
      ↓
maze.txt


==================================================
12. VERIFIER LE DOUBLON MAZEGEN.PY
==================================================

Pendant la migration, on avait conservé :

mazegen.py

à la racine comme sauvegarde.


Et nous avions maintenant :

mazegen/
└── generator.py


Avant de supprimer l'ancien fichier, on a vérifié qu'ils étaient
strictement identiques avec :

diff mazegen.py mazegen/generator.py


La commande n'a rien retourné.


Cela signifie :

mazegen.py
     │
     │ diff
     ▼
mazegen/generator.py

AUCUNE DIFFERENCE


Donc generator.py contient bien l'intégralité de l'ancien code.


==================================================
13. SUPPRIMER L'ANCIEN DOUBLON
==================================================

Une fois les tests terminés et le diff vérifié, l'ancien :

mazegen.py

a été supprimé.


On conserve :

mazegen/
├── __init__.py
├── generator.py
├── grid.py
├── walls.py
├── solver.py
└── pattern42.py


Cela permet d'avoir un package organisé et réutilisable.


==================================================
14. ARCHITECTURE FINALE DE L'IMPORT
==================================================

Quand on écrit :

from mazegen import MazeGenerator


Python suit maintenant :

mazegen/
   ↓
__init__.py
   ↓
from .generator import MazeGenerator
   ↓
generator.py
   ↓
class MazeGenerator


Puis :

maze = MazeGenerator(...)
        ↓
création de l'objet

maze.generate()
        ↓
génération

maze.has_wall(...)
        ↓
lecture des murs

maze.find_path()
        ↓
recherche du chemin

maze.to_grid()
        ↓
représentation du labyrinthe


==================================================
15. RESULTAT DE L'ETAPE 14
==================================================

Le vrai MazeGenerator est maintenant correctement connecté
au reste du projet.


PYGAME :

Génération réelle              OK
Affichage des murs             OK
Entrée / sortie                OK
P → afficher/masquer chemin    OK
R → régénérer                  OK
P après R → nouveau chemin     OK
Q → quitter                    OK
Taille adaptative              OK


PROGRAMME PRINCIPAL :

config.txt                     OK
parse_config()                 OK
convert_config()               OK
MazeGenerator                  OK
generate()                     OK
write_output()                 OK
maze.txt                       OK


ARCHITECTURE :

mazegen/
   ↓
generator.py
   ↓
MazeGenerator

                              OK


==================================================
RÉSUMÉ MENTAL
==================================================

Il faut surtout retenir la différence entre :

PACKAGE
mazegen/

MODULE
generator.py

CLASSE
MazeGenerator


Et la différence entre :

MazeGenerator(...)
→ crée un objet

maze.generate()
→ génère le labyrinthe

run_pygame(maze)
→ affiche le labyrinthe


FLUX GLOBAL :

config.txt
    ↓
config_parser
    ↓
MazeConfig
    ↓
MazeGenerator
    ↓
generate()
    ↓
    ├──────────────→ Pygame
    │                 ├─ has_wall()
    │                 └─ find_path()
    │
    └──────────────→ maze.txt
                      └─ to_grid()


ÉTAPE 14 VALIDÉE ✅

=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================
ÉTAPE 15 — CRÉER LE MOTIF "42" DANS LE LABYRINTHE

Objectif :
Créer un motif "42" composé de cellules complètement fermées.

Fichier :
mazegen/pattern42.py

On représente le motif avec des coordonnées locales.

PATTERN_WIDTH = 7
PATTERN_HEIGHT = 5

Le motif ressemble à :

#.#.###
#.#...#
###.###
..#.#..
..#.###

Chaque # représente une cellule bloquée.

Les coordonnées sont d'abord locales au motif :

(0,0), (2,0), etc.

Puis on transforme ces coordonnées locales en coordonnées du labyrinthe :

global_x = local_x + offset_x
global_y = local_y + offset_y

Le résultat est stocké dans un set :

pattern = set()

Pourquoi un set ?

- une cellule ne doit apparaître qu'une fois
- la recherche "est-ce que cette cellule est bloquée ?" est rapide

La fonction :

create_pattern42(width, height)

renvoie donc :

set[tuple[int, int]]

Exemple :

blocked = create_pattern42(20, 15)

Si le labyrinthe est trop petit pour contenir le motif :

return set()

et un message est affiché dans le terminal.

=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================
🟦 ÉTAPE 16 — INTÉGRER LE MOTIF 42 DANS MAZEGENERATOR

Objectif :
Faire comprendre au générateur que certaines cellules sont interdites.

MazeGenerator possède maintenant :

blocked: set[Cell] | None = None

Puis :

self.blocked = blocked if blocked is not None else set()

Donc :

blocked
   ↓
ensemble des cellules du 42
   ↓
MazeGenerator
   ↓
ne crée pas de passages vers ces cellules

Dans _neighbors(), on ignore une cellule si :

(vx, vy) in self.blocked

Le principe est :

cellule normale
    ↓
peut être visitée

cellule du 42
    ↓
ignorée par la génération
    ↓
aucun passage créé
    ↓
4 murs fermés

Dans a_maze_ing.py :

blocked = create_pattern42(
    maze_config.width,
    maze_config.height
)

Puis on transmet ce résultat au constructeur :

MazeGenerator(
    ...
    blocked=blocked
)

Ainsi le motif 42 fait maintenant partie de la vraie génération.

=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================
🟦 ÉTAPE 17 — CORRIGER LE POSITIONNEMENT DU 42

Problème rencontré :

En mode PERFECT=False, MazeGenerator ouvre spécialement :

- les quatre coins
- le centre du labyrinthe

Au départ, le chiffre 2 passait sur la cellule centrale.

Conséquence :

le générateur pouvait ouvrir une cellule appartenant au "2"
et casser le motif.

Solution :

décaler horizontalement le motif pour que le centre du labyrinthe
tombe dans l'espace entre le 4 et le 2.

On utilise :

offset_x = width // 2 - 3
offset_y = (height - PATTERN_HEIGHT) // 2

Exemple pour 20 × 15 :

offset_x = 20 // 2 - 3
         = 10 - 3
         = 7

offset_y = (15 - 5) // 2
         = 5

Une cellule locale :

(2, 0)

devient :

(2 + 7, 0 + 5)
= (9, 5)

Important :

x utilise offset_x
y utilise offset_y

=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================
🟦 ÉTAPE 18 — TESTER LE MOTIF 42

Fichier :

tests/test_pattern42.py

Objectif :
Vérifier que les cellules constituant le 42 restent complètement fermées.

On teste plusieurs générations :

for seed in range(100):

Cela donne :

seed = 0
seed = 1
...
seed = 99

Pour chaque génération :

1. création du motif
2. création du MazeGenerator
3. génération du labyrinthe
4. vérification des murs des cellules bloquées

Pour chaque cellule du motif :

for x, y in blocked:

On teste les quatre directions :

for direction in MOVES:

Puis :

assert maze.has_wall(x, y, direction) is True

Rappel :

assert condition

signifie :

condition vraie
    ↓
le programme continue

condition fausse
    ↓
AssertionError

"assert" est un mot-clé Python.
Ce n'est pas une fonction et il n'y a rien à importer.

On teste aussi un labyrinthe trop petit :

small_pattern = create_pattern42(5, 4)
assert small_pattern == set()

Commande correcte depuis la racine :

python3 -m tests.test_pattern42

Attention :

python -m attend un NOM DE MODULE.

Donc :

python3 -m tests.test_pattern42     ✅

et pas :

python3 -m tests.test_pattern42.py  ❌

=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================
🟦 ÉTAPE 19 — TESTER LE MODE PAC-MAN / PERFECT=FALSE

Fichier :

tests/test_pacman.py

Objectif :
Tester automatiquement plusieurs propriétés du labyrinthe imparfait.

On génère 100 labyrinthes avec :

for seed in range(100):

et :

perfect=False

On vérifie notamment :

- peu de dead ends
- aucune zone complètement ouverte de 3 × 3
- toutes les cellules accessibles sont connectées

IMPORTANT :

La limite :

dead_ends <= 3

est notre critère de test pour l'implémentation actuelle.

Ce n'est pas une valeur imposée explicitement par le sujet.

===================================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
===================================================================
🟦 ÉTAPE 20 — COMPRENDRE ET UTILISER BFS POUR TESTER LA CONNECTIVITÉ

Objectif :
Vérifier qu'on peut atteindre toutes les cellules navigables du labyrinthe.

On commence à l'entrée :

visited = {maze.entry}

visited contient les cellules déjà découvertes.

Puis :

queue = deque([maze.entry])

queue contient les cellules qu'il reste à explorer.

Fonctionnement :

queue
 ↓
prendre la première cellule
 ↓
regarder ses voisins accessibles
 ↓
ajouter les nouveaux voisins
 ↓
continuer jusqu'à ce que queue soit vide

On retire la première cellule avec :

current = queue.popleft()

Puis :

x, y = current

C'est du tuple unpacking.

Si :

current = (4, 7)

alors :

x = 4
y = 7

Pour chaque direction :

for direction in MOVES:

direction vaut par exemple :

"N"
"E"
"S"
"W"

MOVES est un dictionnaire.

Donc pour récupérer le déplacement :

dx, dy = MOVES[direction]

Exemple :

direction = "E"

MOVES["E"]
    ↓
(1, 0)

Puis :

neighbor = (x + dx, y + dy)

Si ce voisin n'a jamais été découvert :

if neighbor not in visited:
    visited.add(neighbor)
    queue.append(neighbor)

Différence importante :

set     → .add()
list    → .append()
deque   → .append()

On ne fait pas :

visited += neighbor

car un set n'utilise pas + pour ajouter un élément.

À la fin :

expected = maze.width * maze.height - len(blocked)

Puis :

assert len(visited) == expected

Cela vérifie que toutes les cellules qui ne font pas partie du 42
sont accessibles.

=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================
🟦 ÉTAPE 21 — TESTER LA CONTRAINTE 3 × 3

Le mode imparfait peut créer des boucles.

Mais on ne veut pas créer une grande zone complètement ouverte
de 3 cellules × 3 cellules.

MazeGenerator possède :

_has_open_3x3()

Le test utilise :

assert maze._has_open_3x3() is False

Attention à la différence :

maze._has_open_3x3

= référence vers la méthode

maze._has_open_3x3()

= exécute réellement la méthode

Les parenthèses () sont donc importantes.

Le test Pac-Man complet est lancé avec :

python3 -m tests.test_pacman

Aucune sortie + aucune AssertionError
= tous les tests sont passés.

=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================
🟦 ÉTAPE 22 — TRANSFORMER MAZEGEN EN PACKAGE PYTHON

Objectif :
Rendre MazeGenerator réutilisable depuis un autre projet.

Architecture :

mazegen/
├── __init__.py
├── generator.py
├── pattern42.py
├── grid.py
├── solver.py
└── walls.py

generator.py contient notamment :

MazeGenerator

Le fichier :

mazegen/__init__.py

permet d'exposer la classe avec :

from .generator import MazeGenerator

Le point signifie :

depuis le package actuel "mazegen"
    ↓
va dans generator.py
    ↓
importe MazeGenerator

Cela permet ensuite à l'utilisateur d'écrire simplement :

from mazegen import MazeGenerator

au lieu de :

from mazegen.generator import MazeGenerator

=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================
🟦 ÉTAPE 23 — CRÉER LE PYPROJECT.TOML

Objectif :
Expliquer aux outils Python comment construire le package mazegen.

Contenu :

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "mazegen"
version = "0.1.0"
requires-python = ">=3.10"

[tool.setuptools.packages.find]
include = ["mazegen*"]

[build-system]

décrit le système utilisé pour construire le package.

requires = ["setuptools"]

indique que setuptools est nécessaire.

build-backend = "setuptools.build_meta"

indique à Python que setuptools effectue réellement la construction.

[project]

contient les informations du package.

name = "mazegen"

nom du package.

version = "0.1.0"

version actuelle.

requires-python = ">=3.10"

le package nécessite Python 3.10 minimum.

Pourquoi ?

Le code utilise notamment :

int | None

Cette syntaxe nécessite Python 3.10+.

Enfin :

[tool.setuptools.packages.find]
include = ["mazegen*"]

signifie :

cherche les packages Python
        ↓
mais conserve uniquement
        ↓
mazegen
et ses éventuels sous-packages

Lors du test automatique avec find_packages(),
setuptools trouvait :

['mazegen', 'display']

On ne voulait pas embarquer display dans le package réutilisable.

include = ["mazegen*"]

permet donc d'exclure display.

=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================
🟦 ÉTAPE 24 — CONSTRUIRE LE FICHIER .WHL

Objectif :
Créer la version distribuable du package.

On utilise :

python3 -m build --wheel --outdir .

Décomposition :

python3 -m build
    ↓
exécute l'outil Python "build"

--wheel
    ↓
construit un package .whl

--outdir .
    ↓
place le résultat dans le dossier actuel

Résultat :

mazegen-0.1.0-py3-none-any.whl

Le fichier .whl est le package distribuable.

On a ensuite inspecté son contenu avec :

python3 -m zipfile -l mazegen-0.1.0-py3-none-any.whl

Le package contient bien notamment :

mazegen/__init__.py
mazegen/generator.py
mazegen/pattern42.py

Et il ne contient pas :

display/
tests/

Donc notre configuration setuptools fonctionne correctement.

===========================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
===========================================================
🟦 ÉTAPE 25 — TESTER LE PACKAGE DANS UN ENVIRONNEMENT PROPRE

Objectif :
Ne pas seulement vérifier que le .whl se construit.

On veut vérifier qu'une autre personne peut réellement :

1. récupérer le .whl
2. l'installer
3. importer MazeGenerator

On crée un environnement temporaire :

python3 -m venv /tmp/test_mazegen

Puis on installe notre package dedans :

/tmp/test_mazegen/bin/python -m pip install ./mazegen-0.1.0-py3-none-any.whl

Résultat :

Successfully installed mazegen-0.1.0

Ensuite on teste l'import depuis /tmp pour éviter que Python
utilise accidentellement notre dossier source local :

cd /tmp && /tmp/test_mazegen/bin/python -c "from mazegen import MazeGenerator; print(MazeGenerator)"

Résultat :

<class 'mazegen.generator.MazeGenerator'>

Donc le package installé fonctionne réellement.

Rappel sur -c :

python -c "..."

signifie :

exécute directement le code Python écrit entre guillemets.

Cela évite de créer un fichier .py juste pour faire un petit test.

Chaîne complète validée :

code source
    ↓
pyproject.toml
    ↓
build
    ↓
mazegen-0.1.0-py3-none-any.whl
    ↓
installation dans un environnement propre
    ↓
from mazegen import MazeGenerator
    ↓
fonctionne ✅

=======================================================
ÉTAPE 13 — ADAPTER LA TAILLE DES CELLULES AU LABYRINTHE
=======================================================
🟦 ÉTAPE 26 — AJOUTER UNE LICENCE AU PROJET

Le sujet demande que le générateur puisse être réutilisé et distribué
dans de futurs projets.

Nous avons choisi :

MIT License

Pourquoi ?

Elle permet notamment :

- utiliser le code
- copier le code
- modifier le code
- intégrer le code dans un autre projet
- publier le code
- distribuer le code

Les auteurs indiqués sont :

celfofan
mcheddad

Début du fichier LICENSE.md :

MIT License

Copyright (c) 2026 celfofan and mcheddad

La licence impose principalement de conserver :

- la notice de copyright
- la notice de permission

Elle précise également que le logiciel est fourni "AS IS",
c'est-à-dire sans garantie.

Cela répond à l'objectif du sujet :

mazegen
    ↓
peut être réutilisé
    ↓
peut être modifié
    ↓
peut être distribué
    ↓
dans les projets suivants



-----------------------------------------------------
TÂCHE 6 — DISPLAY
│
├── 6A — Terminal obligatoire
│   ├── rendu des cellules (fini)
│   ├── murs N/E/S/W (fini)
│   ├── entrée (fini)
│   ├── sortie (fini)
│   ├── chemin (fini)
│   └── menu (fini)
│
└── 6B — Pygame
    ├── créer la fenêtre (fini)
    ├── calculer taille des cellules (fini)
    ├── convertir (x,y) → pixels (fini)
    ├── dessiner les murs (fini)
    ├── afficher entrée/sortie (fini)
    ├── afficher le chemin (fini)
    ├── afficher le motif 42 (fini)
    ├── gérer touches/clavier (fini)
    └── régénérer le maze (fini)



mazegen/
└── pattern42.py         ← TA tâche 7 (fini)
tests/test_pacaman.py    ← (fini)
tests/test_pattern42.py  ← (fini)

mazegen/generator.py     ← (fini fait par le binome)
mazegen/grid.py          ← tâche 9 éventuellement (a faire)

pyproject.toml           ← tâche 10 (fini)
README.md                ← tâche 12 (a faire)
LICENSE.md               ← tâche 11 (fini)

terminal.py
    │
    │ utilise
    ▼
MazeGenerator
    │
    ├── has_wall()
    ├── find_path()
    ├── width / height
    ├── entry / exit
    └── generate()

        X
        │
        └── terminal.py ne va pas fouiller
            dans grid.py / walls.py / generator.py