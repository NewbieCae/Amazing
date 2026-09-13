display/
├── terminal.py          ← TA grosse tâche 6
└── mlx_display.py       ← seulement si vous faites l'option graphique

Etape 1 comprehension visuelle:

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

Étape 2 — dessiner seulement la ligne du haut
def display_maze(maze) -> None:
    for x in range(maze.width):
        if maze.has_wall(x, 0, "N"):
            print("+---", end="")
        else:
            print("+   ", end="")

    print("+")


Étape 3 — parcourir les lignes y
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

    Étape 4 — construire les 3 morceaux d’une rangée

Chaque ligne de cellules peut être affichée avec :
+---+---+---+
|   |       |
+---+   +---+

Donc on a  essentiellement :
    ligne des murs N
    ligne du contenu + murs E/W
    ligne des murs S (y = maze.height - 1)

Etape 5: l'entree et la sortie du labirinthe:
    print("   ", end="")
    je le remplaces par cell_entry_exit(maze, x, y)

def cell_entry_exit(maze, x: int, y:int) -> str:
    if (x, y) == maze.entry:
        return " E "
    elif (x,y) == maze.exit:
        return " S "
    else:
        return "   "

Etape 6: maze.find_path()
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

Etape 7: maze.generate()
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

Etape 8 : Verifier que Pygame peut ouvrir une fenetre
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

Etape 9 : Calculer les tailles des cellules
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

    Etape 10 : Convertir (x, y)
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
    ├── dessiner les murs (on est ici)
    ├── afficher entrée/sortie
    ├── afficher le chemin
    ├── afficher le motif 42
    ├── gérer touches/clavier
    └── régénérer le maze



mazegen/
└── pattern42.py         ← TA tâche 7

mazegen/generator.py     ← tâche 8 éventuellement
mazegen/grid.py          ← tâche 9 éventuellement

pyproject.toml           ← tâche 10
README.md                ← tâche 12
LICENSE.md               ← tâche 11

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