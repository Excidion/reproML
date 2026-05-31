install:
    uv sync --all-groups --all-extras
    uv run pre-commit install --hook-type pre-push --hook-type post-checkout --hook-type pre-commit

hooks:
    uv run pre-commit run --all-files

docs:
    uv run mkdocs build --strict --site-dir test
    rm -rf test

test:
    uv run ctt
    rm -rf .ctt

check: install hooks docs test
