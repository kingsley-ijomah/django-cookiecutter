# Django Cookiecutter

Best practices [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/first_steps.html) read about cookiecutter here

## Features

- Django framework [flake8](https://docs.djangoproject.com/en/3.0/)
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Test Coverage with [pytest-cov](https://github.com/pytest-dev/pytest-cov)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)

## Quickstart

```sh
# Install pipx if pipenv and cookiecutter are not installed
python3 -m pip install pipx
python3 -m pipx ensurepath

# Install pipenv using pipx
pipx install pipenv

# Use cookiecutter to create project from this template
pipx run cookiecutter gh:kingsley-ijomah/django-cookiecutter

# Enter project directory
cd <repo_name>

# Initialise git repo
git init

# Install dependencies
pipenv install --dev

#  Create .venv environment directory
PIPENV_VENV_IN_PROJECT=true pipenv shell
```
