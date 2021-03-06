# Django Cookiecutter

Best practices [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/first_steps.html) read about cookiecutter here

## Features

- Django framework [django](https://docs.djangoproject.com/en/3.0/)
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
```
