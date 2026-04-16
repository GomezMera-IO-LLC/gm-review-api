.PHONY: test lint typecheck format deploy install

install:
	pip install -e ".[dev]"

test:
	python -m pytest tests/ -v --tb=short

lint:
	ruff check src/ tests/

typecheck:
	mypy src/

format:
	ruff format src/ tests/
	ruff check --fix src/ tests/

deploy:
	@echo "Deploying stage=$(STAGE)..."
	@echo "Deploy target not yet configured — see gm-review-infra for Terraform."
