# Data Science Project Template
A toolset for collaboritive development and reproducible results in data science projects.
For details take look at the [documentation](#look-at-the-documentation).

## Setup
### Prerequesites
What you need installed on your system:
+ [Python](https://www.python.org/downloads/) (3.8 or higher) added to PATH
+ [git](https://git-scm.com/downloads)
+ [dvc](https://dvc.org/)

Make sure poetry is installed on your system.
```
pip install poetry
```
It is advised to create project environments in the same place as the code.
The following command will configure poetry such that they always will be created there.
```
poetry config virtualenvs.in-project true
```
### Installation
Navigate to the project directory and install all dependencies.
This command will also create a virtual environment for the project.
```
poetry install
```
To activate the virtual environment run
```
poetry shell
```
in your terminal.
Most Terminals from within IDEs activate the environment automatically.

With an activated environment, make sure that pre-commits are enabled.
```
pre-commit install
```

## Look at the Documentation
For more detailed information about the project checkout the documentation.
Use the following command to run the documentation webserver.
```
mkdocs serve
```
The server will automatically reload on any change to the markdown files in the `docs` directory.
