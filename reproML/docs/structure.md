# Technical Structure
This section contains information how the projects files are organized and which tools are used.
Furthermore it gives directions on how to use both tools and structure.

This project was generated from the [reproML](https://github.com/Excidion/reproML) copier template.

??? note "Guiding Principles"

    + **Reproducibility**:
    You should always be able to reproduce identical results just based on the same raw data and source code.
    Ideally you will never have to hear these words:
    "Well, it worked on my machine."

    + **Adaptability**:
    This structure will help you get a head-start when your are starting a project with just yourself, your laptop and the best of intentions.
    But it will also make things easier when that project grows into a team with a cloud budget and great ambitions.
    In the same spirit, this structure is not intended to be rigid.
    The intention is to provide a dependable foundation for your next project to build from.

    + **FOSS first**:
    This project is built on top of free and open source software and this is by explicit choice.
    New Projects should not be locked into a specific software vendor by default.
    If your project uses proprietary software, go ahead - but I did not want to cherry-pick a specific vendor for everyone.


??? info "Acknowledgements & Inspirations"

    The main influnces when defining this structure were the following:

    + **drivendata**[^1] for the starting point of this structure and many good opinions.
    You will find many direct and indirect quotes on this page.

    + **writethedocs**[^3] for opinions on documentation and tooling

    + **black**[^4] for opinions on code formatting

    + **sighalt**[^5] for his opinion on logging

    + **The Twelve-Factor Manifesto**[^6] for opinions on configs

    I have referenced the relevant author(s) and/or source of inspiration wherever relevant and with a link to the original content in the footnote or text.


[^1]: Quoted from and inspired by [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science), their [opinions](https://cookiecutter-data-science.drivendata.org/opinions/) and [motivation](https://cookiecutter-data-science.drivendata.org/why/)
[^3]: Quoted from *Write The Docs*' [principles](https://www.writethedocs.org/guide/writing/docs-principles/#documentation-principles) and inpsired by their [opinions on tooling](https://www.writethedocs.org/guide/docs-as-code/)
[^4]: Quoted from [psf/black](https://black.readthedocs.io/en/stable/)
[^5]: Inspired by [sighalt's opinion on logging](https://www.roessler.dev/remove-visual-noise-of-logging-code-by-using-python-decorators.html)
[^6]: Quoted from [The Twelve-Factor Manifesto](https://12factor.net/config)


??? question "Why use this project structure?"

    Directly quoted from drivendata[^1]:

    > When we think about data analysis, we often think just about the resulting reports, insights, or visualizations.
    > While these end products are generally the main event, it's easy to focus on making the products look nice and ignore the quality of the code that generates them.
    > Because these end products are created programmatically, code quality is still important!
    > And we're not talking about bikeshedding the indentation aesthetics or pedantic formatting standards — ultimately, data science code quality is about correctness and reproducibility.
    >
    > It's no secret that good analyses are often the result of very scattershot and serendipitous explorations.
    > Tentative experiments and rapidly testing approaches that might not work out are all part of the process for getting to the good stuff, and there is no magic bullet to turn data exploration into a simple, linear progression.
    >
    > That being said, once started it is not a process that lends itself to thinking carefully about the structure of your code or project layout, so it's best to start with a clean, logical structure and stick to it throughout.
    > We think it's a pretty big win all around to use a fairly standardized setup like this one.
    > Here's why:
    >
    > **Other people will thank you**
    >
    > A well-defined, standard project structure means that a newcomer can begin to understand an analysis without digging in to extensive documentation. It also means that they don't necessarily have to read 100% of the code before knowing where to look for very specific things.
    >
    > Well organized code tends to be self-documenting in that the organization itself provides context for your code without much overhead. People will thank you for this because they can:
    >
    > + Collaborate more easily with you on this analysis
    > + Learn from your analysis about the process and the domain
    > + Feel confident in the conclusions at which the analysis arrives
    >
    > **You will thank you**
    >
    >Ever tried to reproduce an analysis that you did a few months ago or even a few years ago?
    > You may have written the code, but it's now impossible to decipher whether you should use `make_figures.py.old`, `make_figures_working.py` or `new_make_figures01.py` to get things done.
    > Here are some questions we've learned to ask with a sense of existential dread:
    >
    > + Are we supposed to go in and join the column X to the data before we get started or did that come from one of the notebooks?
    > + Come to think of it, which notebook do we have to run first before running the plotting code: was it "process data" or "clean data"?
    > + Where did the shapefiles get downloaded from for the geographic plots?
    >
    > These types of questions are painful and are symptoms of a disorganized project.
    > A good project structure encourages practices that make it easier to come back to old work, for example separation of concerns, abstracting analysis as a DAG, and engineering best practices like version control.


## Directory structure
This is your first overview how to find your way around this project.
```
├── .dvc               <- Metadata managed by dvc, do not touch.
│
├── data <dvc>         <- All data files belong into one of this folders subfolder
│   ├── raw            <- The original, unedited data dump
│   ├── interim        <- Intermediate data that has been or is being transformed
│   └── processed      <- The data sets used for modeling
│
├── docs               <- Project documentation.
│   ├── helper         <- Helper files for docs deployment. You can ignore these.
│   ├── index.md       <- Landing page, describe the project and team.
│   ├── context.md     <- Document context and goals.
│   ├── model.md       <- Document modeling from data to ML.
│   ├── ethics.md      <- Ethics checklist (optional)
│   ├── notebooks/     <- Your most polished notebooks, integrated into the docs
│   ├── code/          <- Automatically generated code documentation
│   └── structure.md   <- Document tools and technical organization. You are here.
│
├── models <dvc>       <- Trained and serialized models and other artifacts
│   └── logs           <- Logfiles from training and prediction
│
├── notebooks          <- Jupyter notebooks.
│
├── references         <- Data dictionaries, manuals, and helper materials.
│
├── reports <dvc>      <- Generated analysis as HTML, PDF, etc.
│   └── figures        <- Generated graphics and figures to be used in reports
│
├── src                <- Source code for use in this project.
│   ├── data           <- Scripts to download, process or generate data
│   ├── features       <- Functions to turn data into features
│   ├── model          <- Scripts for training and prediction
│   └── visualization  <- Scripts to create visualizations
│
├── .pre-commit-config.yaml <- Automated quality checks
│
├── .python-version    <- Exactly what it says, do not touch.
│
├── .github/workflows  <- CICD code for GitHub (optional)
├── .gitlab-ci.yml     <- CICD code for GitLab (optional)
│
├── .reproML.yml       <- Settings given at project init, do not touch.
│
├── pyproject.toml     <- Project configuration and dependencies.
├── uv.lock            <- Full dependency list. Managed by uv, do not touch.
│
└── README.md          <- The top-level README for developers using this project.
```
All folders marked with `<dvc>` are versioned via dvc and so are their subfolders.


## Opinions
There are some opinions and assumptions implicit in the project structure.
These are derived from experience gained with past data science projects.
Some of the opinions are about workflows, and some of the opinions are about tools that make things easier.
The following section contains some of the thoughts which this project is built upon.
If you care to add your own, please reach out to share them.


### Automate as many qualitiy checks as possible
Use [pre-commit](https://pre-commit.com/) hooks to automatically run checks before comitting changes.
Becasue every part of quality assurance that can be automated, should be.


### Documentation should be close to code

> "Consider incorrect documentation to be worse than missing documentation."
> - Write The Docs[^3] Community's ["current"](https://www.writethedocs.org/guide/writing/docs-principles/#current)-principle

Having no documentation slows you down.
Having documentation that is wrong leads might lead you onto the wrong path, which is worse.

> "Store sources as close as possible to the code which they document."
> - Write The Docs[^3] Community's ["nearby"](https://www.writethedocs.org/guide/writing/docs-principles/#nearby)-principle

If documenting takes too much effort, your documentation is doomed to be out of date.
These observations lead to three decisions that keep documentation close to the code and easy to maintain.

+ Documentation is versioned within the repository.

+ Documention is written in simple markdown files so you don't even have to leave your code editor.
Markdown is rendered to beautiful web pages (like this one) via [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).
If you are feeling fancy you can even define
[diagrams](https://squidfunk.github.io/mkdocs-material/reference/diagrams/#usage),
[tables](https://squidfunk.github.io/mkdocs-material/reference/data-tables/#usage),
and [checklists](https://squidfunk.github.io/mkdocs-material/reference/lists/#using-task-lists)
inside markdown.

+ Source code documentation is automatically generated from [docstrings](https://peps.python.org/pep-0257/#what-is-a-docstring) with [mkdocstrings-python](https://mkdocstrings.github.io/python/) and [mkdocs-api-autonav](https://github.com/tlambert03/mkdocs-api-autonav).
A pre-commit hook using [interrogate](https://interrogate.readthedocs.io/) checks if [all](https://www.writethedocs.org/guide/writing/docs-principles/#complete) docstrings exist.
Another pre-commit hook using [pydoclint](https://github.com/jsh9/pydoclint) ensures that the docstring fits the actual function definition.


### Code styles are not worth fighting over
Everybody likes debating about code aesthetics or pedantic standards, but you should
> "agree to cede control over (...) formatting" and
> "save time and mental energy for more important matters". - black[^4]

This is why this template comes with an automatic code formatter ([ruff](https://docs.astral.sh/ruff/)) and enforces it via pre-commit hooks.
Per default, ruff is [mostly](https://docs.astral.sh/ruff/formatter/black/) compliant with black and any [rules](https://docs.astral.sh/ruff/rules/) can be [configured](https://docs.astral.sh/ruff/configuration/) via the `pyproject.toml`.
The defaults are great and ensure the diffs for merges and code reviews are as small as possible.

In the same spirit, just use  the *google*-style for docstrings.
It's elegant, but most importantly, it's (the only one) supported by all of `mkdocstrings-python`, `interrogate` and `pydoclint`, which is required for [this](#documentation-should-be-close-to-code).


### Raw data should be immutable
> Don't ever edit your raw data, especially not manually, and especially not in Excel.
> (...)
> Don't overwrite your raw data.
> Don't save multiple versions of the raw data.[^1]

Treat the data (and its format) as immutable as possible.
There are multiple good reasons for this:

+ It is impossible know which artifacts in the raw data that you want to *clean* right now might later turn out to be relevant information.
An example could be missing values which hint at an underlying mechanic in the data generation process that you are yet to learn about.
Even part of the data files metadata could become relevant as part of the analysis.

+ Immutable raw data is a requirement if you want to [treat your modeling pipeline as a DAG](#modeling-pipelines-are-directed-acyclic-graphs).


??? tip "Processed and interim data is mutable"

    Data in and after processing is very much mutable.
    The suggestions for immutability apply only to the folder `data/raw`.
    The contents of folders `data/interim` and `data/processed` will change based on how your code prosses the raw data.

??? question "What if my data changes over time?"

    Imagine the scenario where you pull your data from an SQL database into `data/raw`.
    A new download at a later time might change the dataset you get.
    This is can be accounted for in multiple ways, for exmaple:

    + If possible, include statements in your SQL query that limit the time window of the downloaded data.
    + Version the `data/raw` folder with `dvc` and allow changes in raw data to be tracked.


### Notebooks are not considered delivered results
> Notebooks (...) are very effective for exploratory data analysis because they enable rapid iteration and visualization of results.
> However, these tools can be less effective for reproducing an analysis.[^1]

Treat notebooks as kind of an explratory *playground* or a but nothing more.
They can be great to test ideas, but, because of their shortcomings in reproducibility, should never considered to be delivered software.

There are two suggestions for using notebooks effectively:

+ Do not to collaborate directly with others on the same notebook.
The diffs in git are a nightmare to work with.

+ If you catch yourself writing the same code in multiple notebooks:
> Refactor the good parts into source code[^1]

Since the project is structured like a Python package you can import your code and use it in notebooks with a cell like the following:
```python
# always reload modules so that as you change code in src, it gets loaded
%load_ext autoreload
%autoreload 2

from src.data import make_dataset
```

??? tip "Integrate Notebooks into the documentation"
    Maybe you have one analysis in one of your notebooks that you are really proud of.
    It was used to make a decision within the project or show the status to an important stakeholder.
    You can *promote* this notebook to be part of the documentation.
    Simply copy it from `notebooks/*.ipynb` to `docs/notebooks/*.ipynb`.
    Then it will become rendered as a subpage of [this](/notebooks/).


### Data Science has to be reproducible
Data Science projects are by nature scientific, so one should try to follow scientific principles where ever possible and feasible.
Reproducibility or repeatability is a major principle underpinning the scientific method.
Therefore one should be striving to produce computations which can be executed again with identical results.


#### Modeling pipelines are directed acyclic graphs
> The best way to ensure reproducibility is to treat your [modeling] pipeline as a directed acyclic graph ([DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph)).
> This means each step of your [pipeline] is a node in a directed graph with no loops.
> You can run through the graph forwards to recreate any analysis output, or you can trace backwards from an output to examine the combination of code and data that created it.[^1]

The code you write should move the raw data through a pipeline to your final outputs.
You should not have to run all of the steps every time you want to make a new figure, but anyone should be able to reproduce the final products with only the code in `src` and the data in `data/raw`.
This approach requires that you [treat raw data as immutable](#raw-data-should-be-immutable).
Treating your analysis as a DAG is one of those concepts almost everyone in the data universe seems to agree on, so it should also help you integrate with their[^7] tools and platforms if you desire to do so.
[^7]: All of [dvc](https://doc.dvc.org/command-reference/dag), [databricks](https://www.databricks.com/glossary/dag), [snowflake](https://docs.snowflake.com/en/user-guide/tasks-graphs), [dbt](https://www.getdbt.com/blog/dag-use-cases-and-best-practices), [airflow](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html) see data pipelines as [directed acyclic graphs](https://en.wikipedia.org/wiki/Directed_acyclic_graph). And probably more.


#### Build reproducible environments
> The first step in reproducing an analysis is always replicating the computational environment it was run in.
> You need the same tools, the same libraries, and the same versions to make everything play nicely together.[^1]

For this, [uv](https://docs.astral.sh/uv/) handles your dependencies as well as the setup your environments.
This has a couple of advantages over the classic `requirements.txt` + `python -m venv`:

+ **Manage Python installations and environments**:
Because different projects will require different versions of the same packages or even different python versions it's best practice to use (virtual) [environments](https://docs.astral.sh/uv/pip/environments/). Furthermore uv can also manage different [python versions](https://docs.astral.sh/uv/concepts/python-versions/) for you.

+ **Resolve dependencies automatically**:
If one of your used packages requires `numpy>1.10` and another `numpy<1.24` uv can figure out a version of numpy that satisfies both.

+ **Less headache when collaborating over different operating systems**:
Everyone on a Mac who ever got at `pip freeze > requirements.txt` from a colleague using Windows will understand.
This also comes in handy if you want to deploy your code to the cloud.

+ **Differentiate between different groups of dependencies**:
Because your deployment in the cloud probably does not need a code formatter.
For more details see uv's [dependency groups](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-groups).


#### Version control everything (that you reasonably can)
Some challenges arise when trying to combine the advandtages of version control with the experimental nature of data science projects.
To solve the most common ones this template uses [dvc](https://dvc.org/) to:

+ [Version artifacts](https://dvc.org/doc/use-cases/versioning-data-and-models#versioning-data-and-models) (datasets, models, plots):
Track revisions of large files efficiently together with the code that produced them, directly integrated into the git workflow.
Automatically backup and share these artifacts in [cloud storage](https://dvc.org/doc/command-reference/remote/add#supported-storage-types) or on your local drive.
Even if you are not allowed to store datasets (e.g. when handling sensitive data), keeping just models versioned can help.

+ [Define reproducible pipelines](https://dvc.org/doc/user-guide/pipelines/defining-pipelines):
Pipelines represent data workflows as [DAGs](#modeling-pipelines-are-directed-acyclic-graphs) that can be reproduced reliably.
Workflows can be defined in a [`dvc.yaml`](https://doc.dvc.org/user-guide/project-structure/dvcyaml-files) file.
In combination with the aforementioned versioning you will can have full transparency which version of code produced which version of an artifact.

+ [Track experiments](https://dvc.org/doc/use-cases/experiment-tracking):
Quickly iterate on experiment ideas, with automatic bookkeeping of data dependencies, code, parameters, artifacts, models, and metrics.
Compare metrics and plots between experiment directly within [VS Code](https://marketplace.visualstudio.com/items?itemName=Iterative.dvc).


### Logging should not obscure logic[^5]
Logging is not part of the logic of the code, but must live near it for obvious reasons.
Typically this results in logging statements before and after each block (or even line) of code, which does not help readability.
This is why this template uses the [logdecorator](https://github.com/sighalt/logdecorator) package to implement a custom [log](code/src/log.md) dectorator which can be used like this:
(Also  all the imported functions have been decorated with `@log`.)
```py
# src/model/train.py
from src.log import log
from src.model.io import save_model


@log
def main():
    """Builds a model and saves it to the file system."""
    model = 42
    save_model(model, "model")

```
Using this will automatically log the start and end of every function you decorate with it.
Depening on the log level, you'll even be able to trace arguments and return values.
```bash
$ ./just run src/model/train.py
# 2038-01-19 03:14:08,000 INFO    train.py.main START
# 2038-01-19 03:14:08,001 DEBUG   train.py.main INPUTS:
# 2038-01-19 03:14:08,002 INFO    src.model.io.save_model START
# 2038-01-19 03:14:08,003 DEBUG   src.model.io.save_model INPUTS: model=42, model_name='model'
# 2038-01-19 03:14:08,004 INFO    src.model.io.get_path START
# 2038-01-19 03:14:08,005 DEBUG   src.model.io.get_path INPUTS: model_name='model'
# 2038-01-19 03:14:08,006 INFO    src.model.io.get_path END
# 2038-01-19 03:14:08,007 DEBUG   src.model.io.get_path OUTPUT: 'models/model.cldpkl'
# 2038-01-19 03:14:08,008 INFO    src.model.io.save_model END
# 2038-01-19 03:14:08,009 DEBUG   src.model.io.save_model OUTPUT: None
# 2038-01-19 03:14:08,010 INFO    train.py.main END
# 2038-01-19 03:14:08,011 DEBUG   train.py.main OUTPUT: None
```
Forcing yourself to only log via decorators can have some positive side effects:
If you feel like you would like to add some logging within a function, this can be an indicator that the code block in question is a candidate to be refactored into a separate function.

See [here](https://www.roessler.dev/remove-visual-noise-of-logging-code-by-using-python-decorators.html) for more detailed illustration and examples.


### No configurations in version control
Ideally none of the projects configuration - hostnames of databases and APIs or secrets like tokens and passwords - should be in the git repository.
All of these parameters should be handed to the code via environment variables.

> A litmus test for whether an app has all config correctly factored out of the code is whether the codebase could be made open source at any moment, without compromising any credentials.[^6]

To store your secrets create a file named `.env` in the project root folder and enter your configration parameters:
```ini
DATABASE_URL=postgres://localhost:1337/dbname
DATBASE_USER=myusername
DATABASE_PASSWORD=topsneaky
```
Scripts run via [`just`](https://github.com/casey/just) automatically load these entries as environment variables.
```
./just run src/script.py
```
In your code you can access these screts like this:
```python
# src/script.py
import os

database_url = os.getenv("DATABASE_URL")
```
Thanks to the `.gitignore`, the `.env` file will not get committed into the git repository.

Alternatively you can also use [`python-dotenv`](https://pypi.org/project/python-dotenv/) to load secrets from `.env` files.

## First steps

### Installing a package
You can [install packages via uv](https://docs.astral.sh/uv/concepts/projects/#managing-dependencies):
```
uv add <package-name>
```
The packages is then installed into the virtual envrionment and added to the `pyproject.toml` and `uv.lock`.
Commit these changes so everyone else that uses your code will have the same dependencies installed.

### Creating a diagram
You can design flowcharts in you markdown files.
You can find some examples [here](https://squidfunk.github.io/mkdocs-material/reference/diagrams/#usage) and more advanced syntax [here](https://mermaid.js.org/syntax/flowchart.html).

### Versioning a dataset with dvc
Instead of tracking a file (eg. `data.csv`) directly, you track it's `data.csv.dvc` file with git.
To create this file and therefore start tracking the original file with dvc execute:
```
dvc add `data.csv`
```
If you change `data.csv` later can simply add it again with the same command, just like you would do with code file versioned in git.

You can always check on the status of all your tracked files with
```
dvc status
```
If you want to stop tracking a file you can just delete the file and then commit the deletion of the dvc file:
```
git rm data.csv.dvc
```

### Pushing your first commit
Don't forget to activate all pre-commit hooks,
```
uv run pre-commit install --hook-type pre-push --hook-type post-checkout --hook-type pre-commit
```
before you:
```
git commit -m "Did the thing."
```
To make sure the quality checks are actually run.

When pushing your first commits to the remote you might encounter the following error message:
```bash
$ git push
"ERROR: failed to push data to the cloud - config file error: no remote specified"
```
The reason behind this that dvc wants to push your data, just as git pushes your code.
By default, no remote data storage is configured and therefore dvc complains.

To add a remote use [this command](https://dvc.org/doc/command-reference/remote/add#remote-add):
```
dvc remote add -d <remote name> <remote url>
```
There are a number of [remote storage backends](https://dvc.org/doc/command-reference/remote/add#supported-storage-types) available.

If you don't want to add a remote storage (yet), you can also use `git push --no-verify` to skip the synchronization.
But it makes more sense to add a "local remote" as a temporary solution:
```
dvc remote add -d local /path/where/you/want/the/data/stored
```
