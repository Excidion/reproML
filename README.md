# reproML
![python](https://img.shields.io/badge/Python-3.9+-blue)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mkdocs-material](https://img.shields.io/badge/Material_for_MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

A toolset for collaborative development and reproducible results in data science and machine learning projects.

## Prerequsites
Make sure you have [`poetry`](https://github.com/python-poetry/poetry) and [`copier`](https://github.com/copier-org/copier) installed.
```
pip install poetry copier
```
It is advised to create project environments in the same place as the code.
The following command will configure poetry such that they always will be created there.
```
poetry config virtualenvs.in-project true
```

## Usage
Initialize a project from the command line:
```
copier https://github.com/Excidion/reproML my_new_project
```
