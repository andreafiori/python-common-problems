# Python problems and solutions

[![Build Status](https://travis-ci.org/andreafiori/python-coding-dojo.svg?branch=master)](https://travis-ci.org/andreafiori/python-coding-dojo)

Generic problems with solutions and tests in Python.

## Requirements

- Python >= 3.0
- [Coverage](https://coverage.readthedocs.io/en/coverage-4.5.1a/index.html)

## Tests

Install pytest:

    pip install pytest

Run all tests:

    pytest

Stop pytest after first failure

    pytest -x

Run single unit test:

    pytest <path_to_file.py>

Es: pytest tests/algorithms/strings/test_stringutil.py

### Generate code coverage

Install coverage:

    pip install coverage

Show coverage:

    coverage run -m pytest

Generate HTML reports:

    coverage html

### Running pylint:

	pylint src --disable=missing-docstring && pylint test --disable=missing-docstring

## Create or Update dependencies

    pip freeze > requirements.txt

## Resources

- [Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/runestone/static/pythonds/index.html)
- [Python Algorithms](https://github.com/TheAlgorithms/Python)
- [Python best practices](https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5)
- [Python best practices on Real Python](https://realpython.com/tutorials/best-practices/)
- [File naming conventions](https://softwareengineering.stackexchange.com/questions/308972/python-file-naming-convention)
