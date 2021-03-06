install: config
test: unit_test
build: dist
all: lint test build

POETRY = poetry

config:
	$(POETRY) install --no-interaction

lint:
	$(POETRY) run mypy nowledge_iface

unit_test:
	$(POETRY) run pytest -vv test/

dist: $(shell find nowledge_iface -type f)
	$(POETRY) build

clean:
	rm -rf dist .pytest_cache .mypy_cache

.PHONY: config unit_test dist