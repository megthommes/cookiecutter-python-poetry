# Based on:
# https://github.com/fpgmaas/cookiecutter-poetry/blob/main/Makefile
# Florian Maas

.PHONY: install, install-dev, test, test-randomly, format, lint, type-check, validate, check, pre-commit-staged, pre-commit-all, pre-commit-update, clean, update, help

install: ## Install the environment
	@echo "\033[0;36minstall\033[0m"
	@echo "Creating virtual environment using pyenv and poetry"
	@if [ ! -d ".git/hooks" ]; then poetry run pre-commit install; fi

install-dev: ## Install the poetry environment with development and test dependencies
	@echo "\033[0;36minstall-dev\033[0m"
	@echo "Creating virtual environment with development and test dependencies"
	@poetry install --with test, dev
	@if [ ! -d ".git/hooks" ]; then poetry run pre-commit install; fi

test: ## Run tests
	@echo "\033[0;36mtest\033[0m"
	@echo "Running tests"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

test-randomly: ## Run tests in a random order
	@echo "\033[0;36mtest-randomly\033[0m"
	@echo "Running tests in random order"
	@poetry run pytest --randomly-seed=random --cov --cov-config=pyproject.toml --cov-report=xml tests

format: ## Format code
	@echo "\033[0;36mformat\033[0m"
	@echo "Formatting code"
	@poetry run isort .
	@poetry run add-trailing-comma .
	@poetry run pyupgrade --py38-plus .
	@poetry run black .

lint: ## Lint code
	@echo "\033[0;36mlint\033[0m"
	@echo "Linting code"
	@poetry run flake8 .
	@poetry run bandit -r . -f custom

type-check: ## Type-check code
	@echo "\033[0;36mtype-check\033[0m"
	@echo "Type-checking code"
	@poetry run mypy .

validate: ## Run format, lint, and type-check
	@echo "\033[0;36mvalidate\033[0m"
	@$(MAKE) format
	@$(MAKE) lint
	@$(MAKE) type-check

check: ## Run validate and test
	@echo "\033[0;36mcheck\033[0m"
	@$(MAKE) validate
	@$(MAKE) test

pre-commit-staged: ## Run pre-commit checks on staged files
	@echo "\033[0;36mpre-commit-staged\033[0m"
	@echo "Running pre-commit checks on staged files"
	@poetry run pre-commit run --files $(git diff --cached --name-only)

pre-commit-all: ## Run pre-commit checks on all files
	@echo "\033[0;36mpre-commit-all\033[0m"
	@echo "Running pre-commit checks on all files"
	@poetry run pre-commit run --all-files

pre-commit-update: ## Update pre-commit hooks
	@echo "\033[0;36mpre-commit-update\033[0m"
	@echo "Updating pre-commit hooks"
	@poetry run pre-commit autoupdate

clean: ## Clean up build artifacts and caches
	@echo "\033[0;36mclean\033[0m"
	@echo "Cleaning up build artifacts and caches"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.pyc' -delete
	@rm -rf build dist .egg-info *.egg-info .pytest_cache .mypy_cache .coverage coverage.xml
	@rm -rf notebooks/.ipynb_checkpoints node_modules

update: ## Update poetry dependencies
	@echo "\033[0;36mupdate\033[0m"
	@echo "Updating poetry dependencies"
	@poetry update

# Help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "%s%s%s\n", $$1, FS, $$2}' | sort -t: -k1,1 -k2 | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help