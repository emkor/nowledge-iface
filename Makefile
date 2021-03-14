install: config
test: unit_test
build: dist
all: test build

config:
	poetry install --no-interaction

unit_test:
	pytest -vv test/

dist: $(shell find nowledge_iface -type f)
	poetry build

clean:
	rm -rf dist .pytest_cache

.PHONY: config unit_test dist