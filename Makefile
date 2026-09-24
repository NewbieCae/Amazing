# ============================================================
#  A-Maze-ing - Makefile
# ============================================================

PYTHON     := python3
PIP        := $(PYTHON) -m pip
MAIN       := a_maze_ing.py
CONFIG     ?= config.txt

MYPY_FLAGS := --warn-return-any --warn-unused-ignores --ignore-missing-imports \
              --disallow-untyped-defs --check-untyped-defs

.PHONY: all install run debug lint lint-strict test build clean fclean re help

all: run

## install : installe les dependances du projet
install:
	$(PIP) install --upgrade pip
	@if [ -f requirements.txt ]; then \
		$(PIP) install -r requirements.txt; \
	else \
		echo "requirements.txt absent -> installation des outils de base"; \
		$(PIP) install flake8 mypy build pytest; \
	fi

## run : lance le programme principal (make run CONFIG=autre.txt)
run:
	$(PYTHON) $(MAIN) $(CONFIG)

## debug : lance le programme sous le debugger pdb
debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

## lint : flake8 + mypy avec les flags imposes par le sujet
lint:
	flake8 .
	mypy . $(MYPY_FLAGS)

## lint-strict : version renforcee (optionnelle)
lint-strict:
	flake8 .
	mypy . --strict

## test : lance les tests unitaires (non notes)
test:
	$(PYTHON) -m pytest -v

## build : construit le package mazegen-* (.whl)
build:
	$(PYTHON) -m build --wheel --outdir .

## clean : supprime les caches et fichiers temporaires
clean:
	@find . -type d -name '__pycache__' -prune -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name '*.py[co]' -delete 2>/dev/null || true
	@rm -rf .mypy_cache .pytest_cache .ruff_cache
	@echo "Nettoyage termine."

## fclean : clean + artefacts de build et fichier de sortie
fclean: clean
	@rm -rf build/ dist/ *.egg-info
	@echo "Nettoyage complet termine."

re: fclean all

## help : affiche les regles disponibles
help:
	@grep -E '^## ' $(MAKEFILE_LIST) | sed 's/## //'
