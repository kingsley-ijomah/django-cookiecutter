import os
import sys


def set_python_version():
    python_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)

    file_names = ["Pipfile"]
    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read()
            contents = contents.replace(r"{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)


SUCCESS = "\x1b[1;32m"
INFO = "\x1b[1;33m"
TERMINATOR = "\x1b[0m"


def main():
    set_python_version()
    print(SUCCESS + "Project successfully initialized" + TERMINATOR)
    print("cd into your project")
    print("Create environment with: " + "PIPENV_VENV_IN_PROJECT=true pipenv shell")
    print("pipenv install")


if __name__ == "__main__":
    main()
