# Data Science Project Template
A short description of the project.


## DevTools
Some choices regarding technology are made for you when using this template:
+ `git` for version control
+ `dvc` for data versioning, ML workflow automation and experiment management
+ `poetry` for dependecy management
+ `mkdocs-material` and `mkdocstrings` for documentation with `mermaid` for diagrams
+ `black` code formatter, enforced via `pre-commit` hooks


## Project Organization
All folders marked with `<dvc>` are versioned via dvc and so are their subfolders.

```html
├── .dvc               <- Metadata managed by dvc, do not touch.
│
├── data <dvc>         <- All data files belong into one of this folders subfolder
│   ├── interim        <- Intermediate data that has been or is being transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, unedited data dump.
│
├── docs               <- Project documentation.
│   ├── index          <- Landing page
│   ├── technical.md   <- Document code.
│   └── business.md    <- Document business goals.
│
├── models <dvc>       <- Trained and serialized models and other artifacts
│   └── logs           <- Logfiles and plots from training and prediction
│
├── notebooks          <- Jupyter notebooks.
│
├── references         <- Data dictionaries, manuals, and helper materials.
│
├── reports <dvc>      <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reports
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   ├── data           <- Scripts to download or generate data
│   ├── features       <- Scripts to turn raw data into features for modeling
│   ├── models         <- Scripts for training and prediction
│   └── visualization  <- Scripts to create visualizations
│
├── poetry.lock        <- Full dependency list. Managed by poetry, do no touch.
├── pyproject.toml     <- Project configuration, define dependencies here.
│
└── README.md          <- The top-level README for developers using this project.
```

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
This is mainly for development purposes.
The server will automatically reload on any change.
```
mkdocs serve
```

Use the following command to build the documentation website. Use this inside your CI/CD Pipeline.
```
mkdocs build
```
