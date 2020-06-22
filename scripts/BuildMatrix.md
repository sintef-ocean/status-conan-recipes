We build for three compilers, GCC, Clang, and MSVC. Below is the configuration for each
compiler. Take a look at the yaml files in `.github/workflows` for one of the recipes to
see how a build matrix is constructed.

| Compiler | Versions       | os           | glibc ver. |
| -------- | -------------- | ------------ | ---------- |
| Clang    | 8, 9, 10       | ubuntu-18.04 | 2.27       |
| GCC      | 6              | ubuntu-16.04 | 2.23       |
| GCC      | 7, 8           | ubuntu-18.04 | 2.27       |
| GCC      | 9              | ubuntu-20.04 | 2.31       |
| MSVC     | 16: v141, v142 | windows-2019 | -          |
|----------|----------------|--------------|------------|
|          |                | ubuntu-20.04 | 2.31       |

| Debian   | glibc   |
|----------|---------|
| Stretch  | 2.24    |
| Buster   | 2.28    |
| Bullseye | 2.30(?) |

**Note** qwt with clang 8 and 9 are currently built with ubuntu-20.04 due to transitive
dependencies using glibc 2.28.
