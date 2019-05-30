.DEFAULT_GOAL := all

.PHONY: all
all: check test

.PHONY: clean
clean:
	rm -f *.mid *.midi

.PHONY: check
check: lint type-check

.PHONY: lint
lint:
	flake8 .

.PHONY: type-check
type-check:
	mypy .

.PHONY: test
test:
	python3 -m unittest
