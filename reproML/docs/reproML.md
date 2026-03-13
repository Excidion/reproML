# reproML - Example Project
![python](https://img.shields.io/badge/Python-3.9_to_3.14-blue)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json)](https://github.com/copier-org/copier)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![mkdocs-material](https://img.shields.io/badge/Material_for_MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

A toolset for collaborative development and reproducible results in data science and machine learning projects.

**This documentation is itself a version of the documentation you would get when using this template.**

## Initialize a new project
Make sure you have `uv` [installed](https://docs.astral.sh/uv/getting-started/installation/), for example via `pip install uv`.

You can initialize a project from the command line.
```
uvx copier copy --trust gh:Excidion/reproML <new_project_directory>
```
You wil then be guided through a short questionaire.
This will generate a structure that looks - depending on your answers - something like [this](structure.md#directory-structure).


## Upgrading and changing settings
If you want to upgrade to the newest version of the template or change any of the settings given at initialization, simply run:
```
uvx copier update --trust
```
