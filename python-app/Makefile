.PHONY: install lint format test type-check update-deps lock-deps clean

PYTHON := python3.11
VENV := .venv
BIN := $(VENV)/bin

install:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Virtual environment not found, creating one..."; \
		$(PYTHON) -m venv $(VENV); \
		echo "Virtual environment created."; \
		echo "Please activate the virtual environment using:"; \
		echo "  source $(VENV)/bin/activate"; \
		exit 1; \
	elif [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Virtual environment is not activated. Please activate it first."; \
		echo "Use 'source $(VENV)/bin/activate' to activate the environment."; \
		exit 1; \
	else \
		echo "Virtual environment already activated. Installing dependencies..."; \
		$(BIN)/pip install -r requirements.txt; \
		echo "Dependencies installed."; \
	fi

lint:
	@echo "Running linter..."
	@$(BIN)/ruff check .

format:
	@echo "Formatting code..."
	@$(BIN)/ruff check --fix .
	@$(BIN)/black .

test:
	@echo "Running tests..."
	@$(BIN)/pytest

type-check:
	@echo "Running type checker..."
	@$(BIN)/mypy .

update-deps:
	@echo "Updating dependencies..."
	@$(BIN)/pip install --upgrade -r requirements.txt
	@echo "Dependencies updated."

lock-deps:
	@echo "Locking dependencies..."
	@$(BIN)/pip freeze > requirements.txt
	@echo "Dependencies locked in requirements.txt."

clean:
	@echo "Cleaning up virtual environment and cache..."
	@rm -rf $(VENV)  # Remove the virtual environment
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -delete
	@echo "Cleaned up environment and cache files."

all: install lint format test type-check
