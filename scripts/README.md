

# Usage

This folder contains convenience scripts for creating a library recipe readme and the
recipe status page. Ensure that [list.csv](list.csv) for own recipes and
[transitive.csv](transitive.csv) for external recipes are up to date.

-   **Status page:** run `python make_status.py`. The output will be `Out.md`, which you
    will need to replace the existing README.md in the root folder.
-   **Recipe readme:** run `python lib_readme.py [library]`, where `[library]` is from the
    first column of [list.csv](list.csv), or `ALL`. The output will be
    `Readme_[library].md`. Copy and adjust accordingly, especially the bottom sections.
