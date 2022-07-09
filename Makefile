-include .env
export


lint:
	@mypy crowleer
	@flake8 crowleer

run:
	@python -m crowleer
