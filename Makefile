.DEFAULT_GOAL := all

.PHONY: all
all: check test

.PHONY: clean
clean:
	rm -f *.mid *.midi

.PHONY: install
install:
	pip3 install --upgrade -r requirements.txt -r dev-requirements.txt

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
