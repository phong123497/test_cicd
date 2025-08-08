## Python CI example (GitHub Actions)

This folder is a minimal Python project with tests and a ready-to-use GitHub Actions workflow.

### What's included
- Simple `hello` module under `src/`
- Pytest tests under `tests/`
- Linting with `flake8` and formatting check with `black`
- GitHub Actions workflow in `.github/workflows/python-ci.yml`

### Local development
```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\\Scripts\\activate
pip install -r requirements-dev.txt

# run linters and tests
flake8 .
black --check .
pytest -q --cov=src --cov-report=term-missing
```

### CI
The workflow runs on pushes and pull requests, across multiple Python versions.

