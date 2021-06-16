# Queries and Testing

This folder contains two scripts, one which holds queries to interogate the wine.owl ontology, and one with unit tests (both in Python). Before using them, please be sure you have installed rdflib version 5.0.0, which is required to parse the ontology.

## Wine Queries
The query file, [wine_queries.py](wine_queries.py), provides functions which can load the wine.owl ontology and query it. These functions are described in docstrings within the file.

## Wine Test
The test file, [wine_tests.py](wine_tests.py), uses `unittest` to test each query in [wine_queries.py](wine_queries.py). These tests can be run with the following command from this directory:

```
python -m unittest wine_tests.py
```
These tests are integrated through GitHub Actions to run on push or pull request events.
