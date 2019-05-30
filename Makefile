.DEFAULT_GOAL := all

.PHONY: all
all: check test

.PHONY: clean
clean:
	rm -f *.mid *.midi

.PHONY: check
check:
	flake8 .

.PHONY: test
test:
	python3 -m unittest
