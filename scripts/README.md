

# Usage

This folder contains convenience scripts for creating a library recipe readme and the
recipe status page. Ensure that <list.csv> is up to date.

-   **Status page:** run `python make_status.py`. The output will be `Out.md`, which you
    will need to replace the existing README.md in the root folder.
-   **Recipe readme:** run `python lib_readme.py <library>`, where `<library>` is from the
    first column of <list.csv>, or `ALL`. The output will be
    `Readme_<library>.md`. Copy and adjust accordingly, especially the bottom sections.
