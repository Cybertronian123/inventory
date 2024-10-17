.PHONY: runserver
runserver:
	poetry run python -m inventory.manage runserver

.PHONY: install
install:
	poetry install

.PHONY: test
	poetry run python -m inventory.manage test

.PHONY: migrate
migrate: 
	poetry run python -m inventory.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m inventory.manage makemigrations

.PHONY: superuser
superuser:
	poetry run python -m inventory.manage createsuperuser

.PHONY: update
update: install migrate ;

