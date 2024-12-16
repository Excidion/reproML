from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

source_path = "src"
paths = sorted(Path(source_path).rglob("*.py"))

if len(paths) == 0:  # when documenting template itself
    source_path = "reproML/src"
    paths = sorted(Path(source_path).rglob("*.py"))

for path in paths:
    module_path = path.relative_to(source_path).with_suffix("")
    doc_path = path.relative_to(source_path).with_suffix(".md")
    full_doc_path = Path("code", doc_path)
    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "a") as fd:
        ident = ".".join(parts)
        if source_path == "src":
            fd.write(f"::: src.{ident}")
        elif source_path == "reproML/src":
            fd.write(f"::: reproML.src.{ident}")

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("code/index.md", "a") as nav_file:
    nav_file.write("\n")  # guarantee space to contents of index
    nav_file.writelines(nav.build_literate_nav())
