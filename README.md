# PythonCoding

Typical Python project scaffold using Poetry for dependency management.

## Project structure

```text
.
├── pyproject.toml
├── README.md
└── src
    └── pythoncoding
        └── __init__.py
```

## Quick start

```bash
poetry install
poetry run python -c "import pythoncoding; print(pythoncoding.__version__)"
```