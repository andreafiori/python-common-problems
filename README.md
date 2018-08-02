# Python problems and solutions

Generic problems with solutions and tests in Python.

## Requirements

- Python >= 2.7
- [Coverage](https://coverage.readthedocs.io/en/coverage-4.5.1a/index.html)

## Tests

### Run all tests:

	python -m unittest discover

### Run single unit test:

	 python -m unittest test.sample

### Running pylint:

	pylint src --disable=missing-docstring && pylint test --disable=missing-docstring

## Create or Update dependencies

    pip freeze > requirements.txt

## Resources

- [Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/runestone/static/pythonds/index.html)
- [Python Algorithms](https://github.com/TheAlgorithms/Python)

## TODO

- Generate coverage
