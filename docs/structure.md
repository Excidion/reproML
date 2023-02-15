# Technical Structure
This section contains information how the projects files are organized and which tools are used.
Furthermore it gives directions on how to use both tools and structure.

??? question "Why use this project structure?"

    When we think about data analysis, we often think just about the resulting reports, insights, or visualizations. While these end products are generally the main event, it's easy to focus on making the products look nice and ignore the quality of the code that generates them. Because these end products are created programmatically, code quality is still important — ultimately, data science code quality is about correctness and reproducibility.

    It's no secret that good analyses are often the result of very scattershot and serendipitous explorations. Tentative experiments and rapidly testing approaches that might not work out are all part of the process for getting to the good stuff, and there is no magic bullet to turn data exploration into a simple, linear progression.

    That being said, once started it is not a process that lends itself to thinking carefully about the structure of your code or project layout, so it's best to start with a clean, logical structure and stick to it throughout. We think it's a pretty big win all around to use a fairly standardized setup like this one. Here's why:

    **Other people will thank you**

    A well-defined, standard project structure means that a newcomer can begin to understand an analysis without digging in to extensive documentation. It also means that they don't necessarily have to read 100% of the code before knowing where to look for very specific things.

    Well organized code tends to be self-documenting in that the organization itself provides context for your code without much overhead. People will thank you for this because they can:

    + Collaborate more easily with you on this analysis
    + Learn from your analysis about the process and the domain
    + Feel confident in the conclusions at which the analysis arrives

    **Your future self will thank you**

    Ever tried to reproduce an analysis that you did a few months ago or even a few years ago? You may have written the code, but it's now impossible to decipher whether you should use `make_figures.py.old`, `make_figures_working.py` or `new_make_figures01.py` to get things done. Here are some questions we've learned to ask with a sense of existential dread:

    + Are we supposed to go in and join the column X to the data before we get started or did that come from one of the notebooks?
    + Come to think of it, which notebook do we have to run first before running the plotting code: was it "process data" or "clean data"?
    + Where did the shapefiles get downloaded from for the geographic plots?

    These types of questions are painful and are symptoms of a disorganized project. A good project structure encourages practices that make it easier to come back to old work, for example separation of concerns, abstracting analysis as a pipelines, and engineering best practices like version control.


??? tip "Nothing here is binding!"
    Disagree with a couple of the default folder names? Working on a project that's a little nonstandard and doesn't exactly fit with the current structure? Prefer to use a different package than one of the (few) defaults?

    Go for it! This is a lightweight structure, and is intended to be a good starting point for many projects.

    If there is something you notice yourself always changing, maybe even let us know!


## Directory structure
This is your first overview how to find your way around this project.
```
├── .dvc               <- Metadata managed by dvc, do not touch.
│
├── data <dvc>         <- All data files belong into one of this folders subfolder
│   ├── interim        <- Intermediate data that has been or is being transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, unedited data dump.
│
├── docs               <- Project documentation.
│   ├── helper         <- Helper files for docs deployment. You can ignore these.
│   ├── index.md       <- Landing page, describe the project and team.
│   ├── business.md    <- Document business context and goals.
│   ├── code.md        <- Document code.
│   └── structure.md   <- Ducoment tools and technical organization. You are here.
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
All folders marked with `<dvc>` are versioned via dvc and so are their subfolders.


## Tools
Some choices regarding technology are made for you when using this template:
For motivation whese precisely these tools where chosen see the section about [opinions](#opinions).

+ `git` for version control
+ `dvc` for data versioning, ML workflow automation and experiment management
+ `poetry` for dependecy management
+ `mkdocs-material` and `mkdocstrings` for documentation with [`mermaid`](https://squidfunk.github.io/mkdocs-material/reference/diagrams/) for diagrams
+ `black` code formatter, enforced via `pre-commit` hooks


## Opinions
There are some opinions and assumptions implicit in the project structure.
These are derived from experience gained with past data science projects.
Some of the opinions are about workflows, and some of the opinions are about tools that make things easier.
The following section contains some of the thoughts which this project is built upon.
If you care to add your own, please reach out to share them.


### Code styles are not worth fighting over
Even though code quality is important - nobody likes debating about indentation aesthetics or pedantic formatting standards.
That is why this template uses an automatic code formatter ([black](https://black.readthedocs.io/en/stable/)) and enforces it's style via pre-commit hooks.


### Raw data should be immutable
Don't ever edit your **raw data**, especially not manually, and especially not in Excel. 
Don't overwrite your raw data. 
Don't save multiple versions of the raw data. 
Treat the data (and its format) as immutable as possible. 
The code you write should move the raw data through a pipeline to your final analysis. 
You shouldn't have to run all of the steps every time you want to make a new figure, but anyone should be able to reproduce the final products with only the code in `src` and the data in `data/raw`.

??? tip "Processed and interim data is mutable"
    
    Data in and after processing is very much mutable.
    The suggestions for immutability apply only to the folder `data/raw`.
    The contents of folders `data/interim` and `data/processed` have to be able to change. 

??? question "What if my data changes over time?"
    
    Imagine the scenario where you pull your data from an SQL database into `data/raw`.
    Since you (probalby) only have limited control over that database, the data a new download would produce might change in the future.
    This is not ideal, but can be accounted for:

    + If possible, include statements in your SQL query that limit the time window of data.
    + The `data/raw` folder is still versioned by `dvc` and thus changing raw data can be accounted for.


### Notebooks are for exploration and communication only

Jupyter Notebooks are very effective for exploratory data analysis.
However, these tools can be less effective as reproducible pieces of software.

Since notebooks are challenging objects for source control (diffs are not human-readable and merging is near impossible), it is recommended not to collaborate directly with others on the same notebook. 
There are two hints for using notebooks effectively:

+ Follow a naming convention that shows the order the analysis was done in. We use the format `<step>-<description>.ipynb` (e.g., `01-visualize-distributions.ipynb`).

+ Refactor the good parts into `.py` files.
Don't write code to do the same task in multiple notebooks.
For example, if it's a data preprocessing task, put it in a script in `src/data/` and load data from `data/interim`.

Since the project is structured like a Python package you can import your code and use it in notebooks with a cell like the following:
```python
# OPTIONAL: Load the "autoreload" extension so that code can change
%load_ext autoreload

# OPTIONAL: always reload modules so that as you change code in src, it gets loaded
%autoreload 2

from src.data import make_dataset
```


### Build reproducible environments

The first step in reproducing an analysis is always reproducing the computational environment it was run in.
You need the same tools, the same libraries, and the same versions to make everything play nicely together.
For this we use poetry which can handle your dependencies as well setup your environments.
This has a couple of advantages over the classic `requirements.txt`:

+ Resolve dependencies automatically:
If one of your used packages requires `numpy>1.10` and another `numpy<1.24` poetry will figure out a version of numpy that satisfies both.

+ Less headache when collaborating over different operating systems:
Everyone on a Mac who ever got at `requirements.txt` from a colleague on Windows will understand.
This also comes handy if you want to deploy your code to the cloud.

+ Differentiate between different categories of dependencies:
Because you deployment in the cloud does not need a jupyter kernel or a code formatter.


### No secrets in version control
You really don't want to leak your AWS secret key or Postgres username and password on Github.
To ensure this we use `python-dotenv`.
Create a file named `.env` in the project root folder. 
Thanks to the `.gitignore`, this file should never get committed into the version control repository. 
Here's an example how that file might look like:
```ini
DATABASE_URL=postgres://username:password@localhost:5432/dbname
AWS_ACCESS_KEY=myaccesskey
AWS_SECRET_ACCESS_KEY=mysecretkey
OTHER_VARIABLE=something
```
In your code you can access these screts like this: 
```python
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path)

database_url = os.environ.get("DATABASE_URL")
```


### FOSS first
This project is built on top of free and open source software and this is by explicit choice.
The idea is that no project should be locked into a specific software vendor by default.
In this way we want to put the least amount of limits on you and avoid unecessary costs.

If your project uses proprietary software, go ahead - but we did not want to cherry-pick a specific vendor for everyone.

This need for flexibility one of the reasons for choosing `dvc` for data version control and experiment tracking.
It is open source and supports all major cloud prviders (and more) as [remote storage backends](https://dvc.org/doc/user-guide/data-management/remote-storage#supported-storage-types).
