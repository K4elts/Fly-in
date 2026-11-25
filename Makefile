.PHONY: install run debug clean lint lint-strict

PYTHON := python3
VENV := .venv
BIN := $(VENV)/bin
PIP := $(BIN)/pip
APP := fly-in.py
SRC := .

install:
	$(PYTHON) -m venv $(venv)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	$(BIN)/python $(APP)

debug:
	$(BIN)/python -m pdb $(APP) $(CONFIG)

lint:
	$(BIN)/flake8 $(SRC) --exclude $(VENV)
	$(BIN)/mypy $(SRC) --exclude '\$(VENV)' --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(BIN)/flake8 $(SRC) --exclude $(VENV)
	$(BIN)/mypy $(SRC) --exclude '\$(VENV)' --strict
