config:
	poetry install --no-interaction

test:
	pytest -vv test/

build: $(shell find nowledge_iface -type f)
	poetry build

clean:
	rm -rf dist .pytest_cache

.PHONY: config test clean