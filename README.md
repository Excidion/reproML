# reproML
![python](https://img.shields.io/badge/Python-3.9_to_3.12-blue)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json)](https://github.com/copier-org/copier)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mkdocs-material](https://img.shields.io/badge/Material_for_MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

A toolset for collaborative development and reproducible results in data science and machine learning projects.

## Prerequisites
Make sure you have [`uv`](https://docs.astral.sh/uv/) installed.
```
pip install uv
```

## Usage
Initialize a project from the command line:
```
uv run --with copier copier copy --trust https://github.com/Excidion/reproML my_new_project
```
This will generate a structure that looks - depending on your answers - something like this:
```
├── data               <- All data files belong into one of this folders subfolder
│   ├── interim        <- Intermediate data that has been or is being transformed
│   ├── processed      <- The final data sets for modeling
│   └── raw            <- The original, unedited data dump
│
├── docs               <- Project documentation
│   ├── code           <- Generated at build time
│   ├── helper         <- Helper files for docs deployment
│   ├── notebooks      <- Your most polished notebooks, integrated into the docs
│   ├── index.md       <- Landing page, describe the project and team
│   ├── business.md    <- Document business context and goals
│   ├── ethics.md      <- Ethics checklist (optional).
│   ├── model.md       <- Document modeling from data to ML
│   └── structure.md   <- Document tools and technical organization
│
├── models             <- Trained and serialized models and other artifacts
│   └── logs           <- Logfiles from training and prediction
│
├── notebooks          <- Jupyter notebooks
│
├── references         <- Data dictionaries, manuals, and helper materials.
│
├── reports            <- Generated analysis as HTML, PDF, etc.
│   └── figures        <- Generated graphics and figures to be used in reports
│
├── src                <- Source code for use in this project.
│   ├── data           <- Scripts to download or generate data
│   ├── features       <- Scripts to turn raw data into features for modeling
│   ├── models         <- Scripts for training and prediction
│   └── visualization  <- Scripts to create visualizations
│
├── pyproject.toml     <- Project configuration and dependencies.
├── uv.lock            <- Full dependency lockfile
├── .python-version    <- Specifies Python version
│
├── .copier-answers.yml <- Settings given at project init
│
└── README.md          <- The top-level README for developers using this project.
```
