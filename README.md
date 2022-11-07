# Data Science Project Template
A short description of the project.


## DevTools
Some choices regarding technology are made for you when using this template:
+ `git` for version control
+ `dvc` for data versioning, ML workflow automation and experiment management
+ `poetry` for dependecy management
+ `mkdocs-material` and `mkdocstrings` for documentation
+ `black` code formatter, enforced via `pre-commit` hooks


## Project Organization
All folders marked with `<dvc>` are versioned via dvc and so are their subfolders.

```html
├── .dvc               <- Data and model version control managed by dvc.
├── data <dvc>
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been or is being transformed. Put your dask dataframes here.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, (mostly) immutable data dump.
│
├── docs               <- Project documentation.
│   ├── index          <- Landing page
│   ├── technical.md   <- Document code.
│   └── business.md    <- Document business goals.
│
├── models <dvc>       <- Trained and serialized models.
│
├── notebooks          <- Jupyter notebooks.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports <dvc>      <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │                     predictions
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│
└── README.md          <- The top-level README for developers using this project.
```

## Setup
Make sure poetry is installed on your system.
```
pip install poetry
```
Navigate to the project directory and install all dependencies.
```
poetry install
```
To activate the virtual environment run

+ on Windows `env\scripts\activate`
+ on Unix `source env/bin/activate`

in your terminal.

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
