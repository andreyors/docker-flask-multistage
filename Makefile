SHELL=/bin/bash

.PHONY: build
build:
	@docker-compose build

.PHONY: up
up: build
	@docker-compose up -d --remove-orphans

.PHONY: dn
dn:
	@docker-compose down --remove-orphans

.PHONY: rst
rst: dn up

.PHONY: logs
logs:
	@docker-compose logs -f app

.PHONY: ssh
ssh:
	@docker-compose exec app bash

.PHONY: cln
cln:
	@docker kill $(docker ps -q)