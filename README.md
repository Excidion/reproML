# Data Science Project Template
A toolset for collaboritive development and reproducible results in data science projects.
For details take look at the [documentation](#look-at-the-documentation).

## Setup
### Prerequesites
Make sure poetry is installed on your system.
```
pip install poetry
```
It is advised to create project environments in the same place as the code.
```
poetry config virtualenvs.in-project true
```
### Installation
Navigate to the project directory and install all dependencies.
```
poetry install
```
To activate the virtual environment run

+ on Windows `.venv\scripts\activate`
+ on Unix `source .venv/bin/activate`

in your terminal.
Most Terminals from within IDEs do this automatically.

Make sure that pre-commits are enabled.
```
pre-commit install
```

## Look at the Documentation
Use the following command to run the documentation webserver.
The server will automatically reload on any change.
Very useful for development purposes.
```
mkdocs serve
```

Use the following command to build the documentation website. Use this inside your CI/CD Pipeline.
```
mkdocs build
```
