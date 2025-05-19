.PHONY: run-dev run-prod format lint

run-dev:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

run-prod:
	poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000

format:
	poetry run black .
	poetry run isort .

lint:
	poetry run black --check .
	poetry run isort --check-only .