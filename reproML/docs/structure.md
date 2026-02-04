# Technical Structure
This section contains information how the projects files are organized and which tools are used.
Furthermore it gives directions on how to use both tools and structure.

This project was generated from the [reproML](https://github.com/Excidion/reproML) copier template.

??? note "Guiding Principles"

    + **Reproducibility is everything**:
    You should always be able to reproduce identical results just based on the same raw data and source code.
    Ideally you will never have to hear these words:
    "Well, it worked on my machine."

    + **Start small and grow**:
    This structure will help you get a head-start when your are starting a project with just yourself, your laptop and the best of intentions.
    But it will also make things easier when that project grows into a team with a cloud budget and great ambitions.

    + **FOSS first**:
    This project is built on top of free and open source software and this is by explicit choice.
    New Projects should not be locked into a specific software vendor by default.
    If your project uses proprietary software, go ahead - but I did not want to cherry-pick a specific vendor for everyone.

    + **Minimal & flexible**:
    In the same spirit, this structure is not intended to be rigid.
    The intention is to provide a dependable foundation for your next project to build from.


??? info "Acknowledgements & Inspirations"

    The main influnces when defining this structure were the following:

    + **drivendata**[^1] for the starting point of this structure and many good opinions.
    You will find many direct and indirect quotes on this page.

    + **iterative**[^2] for workflow best practices

    + **writethedocs**[^3] for opinions on documentation

    + **black**[^4] for opinions on code formatting

    + **sighalt**[^5] for opinions on logging

    I have referenced the relevant author(s) and/or source of inspiration wherever relevant and with a link to the original content in the footnote.


[^1]: Quoted from and inspired by [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science), their [opinions](https://cookiecutter-data-science.drivendata.org/opinions/) and [motivation](https://cookiecutter-data-science.drivendata.org/why/).
[^2]: Quoted from and inspired by [iterative/example-get-started](https://github.com/iterative/example-get-started)
[^3]: Quoted from and inspired by [writethedocs](https://www.writethedocs.org/guide/docs-as-code/)
[^4]: Quoted from and inspired by [psf/black](https://black.readthedocs.io/en/stable/)
[^5]: Quoted from and inspired by [sighalt](https://www.roessler.dev/)


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


## FAQ
??? error "ERROR: failed to push data to the cloud - config file error: no remote specified"
    When pushing your first commits to the remote you might encounter the error message above.
    The reason behind this that dvc wants to push your data, just as git pushes your code.
    By default, no remote data storage is configured and therefore dvc complains.

    To fix this use the [this command](https://dvc.org/doc/command-reference/remote/add#remote-add):
    `dvc remote add -d <remote name> <remote url>`
    You can use a number of [remote storage backends](https://dvc.org/doc/command-reference/remote/add#supported-storage-types).

    If you don't want to add a remote storage (yet), you can also use `git push --no-verify` to skip the synchronization.


??? question "How do I install new packages?"
    You can [install packages via uv](https://docs.astral.sh/uv/concepts/projects/#managing-dependencies)
    ```
    uv add <package-name>
    ```
    The packages is then installed and added to the `pyproject.toml` and `uv.lock`.
    Commit these changes so everyone else that uses your code will have the same dependencies installed.


??? question "How do I make a diagrams and flowchart?"
    You can design flowcharts in you markdown files.
    You can find some examples [here](https://squidfunk.github.io/mkdocs-material/reference/diagrams/#usage) and more advanced syntax [here](https://mermaid.js.org/syntax/flowchart.html)


??? question "How do I use dvc with git?"
    Instead of tracking a file (eg. `data.csv`) directly, you track it's `data.csv.dvc` file with git.
    To create this file and therefore start tracking the original file with dvc execute:
    ```
    dvc add `data.csv`
    ```
    If you change `data.csv` later can simply add the chages again with the same command.

    You can always check on the status of all your tracked files with
    ```
    dvc status
    ```
    If you want to stop tracking a file you can just delete the file and commit the deletion of the dvc file:
    ```
    git rm data.csv.dvc
    ```

## Opinions
There are some opinions and assumptions implicit in the project structure.
These are derived from experience gained with past data science projects.
Some of the opinions are about workflows, and some of the opinions are about tools that make things easier.
The following section contains some of the thoughts which this project is built upon.
If you care to add your own, please reach out to share them.


### Automate as many qualitiy checks as possible
We use [pre-commit](https://pre-commit.com/) hooks to automatically run extensive checks before comitting changes.
Becasue every part of quality assurance that can be automated, should be.


### Documentation should be close to code[^3]
Having no documentation is bad.
Having Documentation that is out of date is even worse.
If documenting takes too much effort, your documentation is doomed to be out of date.
These observations lead to three decisions that keep documentation close to the code and easy to maintain.

+ Documentation is versioned within the repository.

+ Document in simple markdown files to keep effort low.
Markdown can be rendered to beautiful web pages (like this one) via [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).
If you use GitHub or GitLab, this template comes with code to automatically publish your site.
If you are feeling fancy you can even define
[diagrams](https://squidfunk.github.io/mkdocs-material/reference/diagrams/#usage),
[tables](https://squidfunk.github.io/mkdocs-material/reference/data-tables/#usage),
and [checklists](https://squidfunk.github.io/mkdocs-material/reference/lists/#using-task-lists)
inside markdown.

+ Source code documentation is automatically generated from [docstrings](https://peps.python.org/pep-0257/#what-is-a-docstring) with [mkdocstrings-python](https://mkdocstrings.github.io/python/) and [mkdocs-api-autonav](https://github.com/tlambert03/mkdocs-api-autonav).
A pre-commit hook using [interrogate](https://interrogate.readthedocs.io/) checks if the docstrings exist.
Another pre-commit hook using [pydoclint](https://github.com/jsh9/pydoclint) ensures that the docstring fits the actual function definition.


### Code styles are not worth fighting over[^4]
Even though code quality is important - nobody likes debating about indentation aesthetics or pedantic formatting standards.
This is why this template comes with one predefined.

We use an automatic code formatter ([ruff](https://docs.astral.sh/ruff/)) to enforce it's style via pre-commit hooks.
This style is compliant with [black](https://black.readthedocs.io/en/stable/) and [flake8](https://flake8.pycqa.org) and any settings can be configured via the `pyproject.toml`.
See [here](https://docs.astral.sh/ruff/configuration/) for more details.

In the same spirit, we picked the *google*-style for docstrings.
It's what we like, but most importantly, it's (the only one) supported by all of `mkdocstrings-python`, `interrogate` and `pydoclint`.


### Raw data should be immutable[^1]
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
    A new download at a later time might change the dataset you get.
    This is can be accounted for in two ways:

    + If possible, include statements in your SQL query that limit the time window of data.
    + The `data/raw` folder is versioned by `dvc` and thus changes in raw data can be tracked.


### Notebooks are for exploration and communication only[^1]
Jupyter Notebooks are very effective for exploratory data analysis.
However, these tools can not be effective as reproducible pieces of software.

Since notebooks are challenging objects for source control (diffs are not human-readable and merging is near impossible), it is recommended not to collaborate directly with others on the same notebook.
There are two hints for using notebooks effectively:

+ Follow a naming convention that shows the order the analysis was done in. We use the format `<step>-<description>.ipynb` (e.g., `01-visualize-distributions.ipynb`).

+ Refactor the good parts into `.py` files.
Don't write code to do the same task in multiple notebooks.
For example, if it's a data preprocessing task, put it in a script in `src/data/`.

Since the project is structured like a Python package you can import your code and use it in notebooks with a cell like the following:
```python
# always reload modules so that as you change code in src, it gets loaded
%load_ext autoreload
%autoreload 2

from src.data import make_dataset
```
Treat the notebooks as kind of an explratory *playground* but nothing more.
They can be great to test ideas, but are **never considered to be delivered software**.

??? tip "Integrate Notebooks into the documentation"
    Maybe you have one analysis in one of your notebooks that you are really proud of.
    It was used to make a decision within the project or show the status to an important stakeholder.
    You can *promote* this notebook to be part of the documentation.
    Simply copy it from `notebooks/*.ipynb` to `docs/notebooks/*.ipynb`.
    Then it will become rendered as a subpage of [this](/notebooks/).


### Data Science has to be reproducible[^1]
Data Science projects are by nature scientific, so one should try to follow scientific principles where ever possible and feasible.
Reproducibility or repeatability is a major principle underpinning the scientific method.
Therefore we should be striving for our work to produce computations which can be executed again with identical results.


#### Build reproducible environments
The first step in reproducing an analysis is reproducing the computational environment it was run in.
You need the same tools, the same libraries, and the same versions to make everything play nicely together.
For this we use [uv](https://docs.astral.sh/uv/) which can handle your dependencies as well setup your environments.
This has a couple of advantages over the classic `requirements.txt`:

+ Manage Python installations and environments:
Because different projects will require different versions of the same packages and/or even different python versions it's best practice to use (virtual) [environments](https://docs.astral.sh/uv/pip/environments/). Furthermore uv can also manage [python versions](https://docs.astral.sh/uv/concepts/python-versions/) for you.

+ Resolve dependencies automatically:
If one of your used packages requires `numpy>1.10` and another `numpy<1.24` uv can figure out a version of numpy that satisfies both.

+ Less headache when collaborating over different operating systems:
Everyone on a Mac who ever got at `pip freeze > requirements.txt` from a colleague using Windows will understand.
This also comes in handy if you want to deploy your code to the cloud.

+ Differentiate between different categories of dependencies:
Because your deployment in the cloud does not need a code formatter.
For more details see uv's [development](https://docs.astral.sh/uv/concepts/dependencies/#development-dependencies) and [optional](https://docs.astral.sh/uv/concepts/dependencies/#optional-dependencies) dependencies.


#### Deliver reproducible results
Some challenges arise when trying to combine the advandtages of version control with the experimental nature of data science projects.
To solve the most common ones this template uses [dvc](https://dvc.org/) to:

+ [Version datasets, models and more](https://dvc.org/doc/use-cases/versioning-data-and-models#versioning-data-and-models):
Keep large files alongside code and share them via [cloud storage](https://dvc.org/doc/command-reference/remote/add#supported-storage-types).
Fully integrated into the git workflow, no manual copying or downloading necessary.

+ [Define reproducible pipelines](https://dvc.org/doc/user-guide/pipelines/defining-pipelines):
Pipelines represent data workflows that you want to reproduce reliably — so the results are consistent.
All workflows are defined in a human readable format within a `dvc.yaml` file.
In combination with the aforementioned versioning you will have full transparency which version of code produced which version of an artefact (eg. dataset, model, report, ...).

+ [Track experiments](https://dvc.org/doc/use-cases/experiment-tracking):
Quickly iterate on experiment ideas, with automatic bookkeeping of data dependencies, code, parameters, artifacts, ML models, and their metrics.
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


if __name__ == "__main__":
    main()

```
Using this will automatically log the start and end of every function you decorate with it.
Depening on the log level, you'll even be able to trace arguments and return values.
```bash
$ uv run src/model/train.py
# 2038-01-19 03:14:08,000 INFO    __main__.main START
# 2038-01-19 03:14:08,001 DEBUG   __main__.main INPUTS:
# 2038-01-19 03:14:08,002 INFO    src.model.io.save_model START
# 2038-01-19 03:14:08,003 DEBUG   src.model.io.save_model INPUTS: model=42, model_name='model'
# 2038-01-19 03:14:08,004 INFO    src.model.io.get_path START
# 2038-01-19 03:14:08,005 DEBUG   src.model.io.get_path INPUTS: model_name='model'
# 2038-01-19 03:14:08,006 INFO    src.model.io.get_path END
# 2038-01-19 03:14:08,007 DEBUG   src.model.io.get_path OUTPUT: 'models/model.cldpkl'
# 2038-01-19 03:14:08,008 INFO    src.model.io.save_model END
# 2038-01-19 03:14:08,009 DEBUG   src.model.io.save_model OUTPUT: None
# 2038-01-19 03:14:08,010 INFO    __main__.main END
# 2038-01-19 03:14:08,011 DEBUG   __main__.main OUTPUT: None
```
Forcing yourself to only log via decorators can have some positive side effects:
If you feel like you would like to add some logging within a function, this can be an indicator that the code block in question is a candidate to be refactored into a separate function.

See [here](https://www.roessler.dev/remove-visual-noise-of-logging-code-by-using-python-decorators.html) for more detailed illustration and examples.


### No secrets in version control[^1]
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

load_dotenv()

database_url = os.getenv("DATABASE_URL")
```
