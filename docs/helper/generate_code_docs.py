from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

for path in sorted(Path("src").rglob("*.py")):
    module_path = path.relative_to("src").with_suffix("")
    doc_path = path.relative_to("src").with_suffix(".md")
    full_doc_path = Path("code", doc_path)
    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)
        fd.write(f"::: src.{ident}")
        fd.write("\n\toptions:\n\t\tmembers_order: 'source'")  # order docs like source

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("code/index.md", "w") as nav_file:
    header = [
        "# Overview",
        "[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)",
        "![interrogate](../helper/interrogate_badge.svg)",
    ]
    sep = "\n"
    nav_file.write(sep.join(header) + sep * 2)
    nav_file.writelines(nav.build_literate_nav())
