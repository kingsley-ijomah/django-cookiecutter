# {{cookiecutter.repo_name}}

## Bootstrap

Start a new django project

```bash
# check what shell you are using
echo $0

# put this in .zshrc (zsh) / .bash_profile (bash) / .bashrc (ubuntu desktop)
# it forces pipenv to create .venv directory within project
# this allows us to point to python and other dependencies

echo -e 'export PIPENV_VENV_IN_PROJECT=2' >> ~/.zshrc

# start a new env
pipenv shell

# Install dependencies
pipenv install --dev

# create new django project within src directory
django-admin startproject <project-name> src
```

### check what shell you are using

`echo $0`

### put this in .zshrc (zsh) / .bash_profile (bash) / .bashrc (ubuntu desktop)

<!-- put pyenv path into shell -->
<!-- put in shell to enable shims and autocompletion -->

```
echo -e 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc`

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc
```
