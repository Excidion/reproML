# reproML
![downloads](https://img.shields.io/badge/dynamic/json?color=green&label=Downloads&query=value&url=https%3A%2F%2Fapi.countapi.xyz%2Fget%2FExcidion%2FreproML_downloads)
![python](https://img.shields.io/badge/Python-3.8+-blue)
![black](https://img.shields.io/badge/code%20style-black-000000.svg)

A toolset for collaboritive development and reproducible results in data science and machine learning projects.

## Prerequsites
This project template requires Python 3.8+
Make sure you have `poetry` and `copier` installed.
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
