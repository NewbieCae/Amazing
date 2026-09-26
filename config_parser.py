from dataclasses import dataclass


@dataclass
class MazeConfig:
    """Parametres de generation d'un labyrinthe."""
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int


class ConfigError(Exception):
    """Erreur detectee dans le fichier de configuration."""


def parse_config(config: str) -> dict[str, str]:
    """Parse le fichier de configuration et renvoie un dictionnaire."""
    config_dico = {}
    try:
        with open(config) as f:
            for numb_ligne, ligne in enumerate(f, 1):
                ligne = ligne.strip()
                if not ligne or ligne.startswith("#"):
                    continue
                if "=" not in ligne:
                    raise ConfigError(
                        f"ligne {numb_ligne} mal formee : '{ligne}'"
                        f" (format attendu : CLE=VALEUR)"
                    )
                nom, valeur = ligne.split("=", 1)
                config_dico[nom] = valeur
    except FileNotFoundError as e:
        raise ConfigError(f"fichier {config} inexistant") from e
    return config_dico


def check_coord(
    coord: tuple[int, int],
    width: int,
    height: int,
    key_name: str,
) -> None:
    """Verifie que la coordonnee est dans les limites du labyrinthe."""
    if coord[0] < 0 or coord[0] >= width:
        raise ConfigError(
            f"{key_name} hors limites (x={coord[0]}) :"
            f" doit etre entre 0 et {width - 1}"
        )
    if coord[1] < 0 or coord[1] >= height:
        raise ConfigError(
            f"{key_name} hors limites (y={coord[1]}) :"
            f" doit etre entre 0 et {height - 1}"
        )


def parse_int(data: dict[str, str], key: str) -> int:
    """Convertit la valeur d'une cle en entier."""
    try:
        return int(data[key])
    except ValueError as e:
        raise ConfigError(
            f"{key} invalide ('{data[key]}') : doit etre un entier"
        ) from e


def convert_config(data: dict[str, str]) -> MazeConfig:
    """Convertit les valeurs texte en un MazeConfig."""
    list_config = [
        "WIDTH", "HEIGHT",
        "ENTRY", "EXIT",
        "OUTPUT_FILE",
        "PERFECT", "SEED",
    ]
    for element in list_config:
        if element not in data:
            raise ConfigError(f"config incomplète, cle manquante : {element}")

    width = parse_int(data, "WIDTH")
    if width <= 1:
        raise ConfigError(f"WIDTH invalide ({width}) : doit etre au moins 2")

    height = parse_int(data, "HEIGHT")
    if height <= 1:
        raise ConfigError(f"HEIGHT invalide ({height}) : doit etre au moins 2")

    try:
        entry_tuple = data["ENTRY"]
        entry_x, entry_y = entry_tuple.split(",")
        entry = (int(entry_x), int(entry_y))
    except ValueError as e:
        raise ConfigError(
            f"ENTRY invalide ('{data['ENTRY']}') :"
            f" format attendu x,y avec deux entiers"
        ) from e
    check_coord(entry, width, height, "ENTRY")

    try:
        exit_tuple = data["EXIT"]
        exit_x, exit_y = exit_tuple.split(",")
        exit_ = (int(exit_x), int(exit_y))
    except ValueError as e:
        raise ConfigError(
            f"EXIT invalide ('{data['EXIT']}') :"
            f" format attendu x,y avec deux entiers"
        ) from e
    check_coord(exit_, width, height, "EXIT")

    if entry == exit_:
        raise ConfigError(
            f"ENTRY et EXIT identiques {entry} : ils doivent etre differents"
        )

    output_file = data["OUTPUT_FILE"]
    perfect_value = data["PERFECT"].strip().lower()

    if perfect_value == "true":
        perfect = True
    elif perfect_value == "false":
        perfect = False
    else:
        raise ValueError(
            "PERFECT must be either True or False"
        )
    seed = parse_int(data, "SEED")

    return MazeConfig(
        width=width,
        height=height,
        entry=entry,
        exit=exit_,
        output_file=output_file,
        perfect=perfect,
        seed=seed,
    )
