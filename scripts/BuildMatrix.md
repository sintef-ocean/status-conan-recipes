We build for three compilers, GCC, Clang, and MSVC. Below is the configuration for each
compiler. Take a look at the yaml files in `.github/workflows` for one of the recipes to
see how a build matrix is constructed.

| Compiler | Versions       | os           |
| -------- | -------------- | ------------ |
| Clang    | 8, 9, 10       | ubuntu-20.04 |
| GCC      | 6, 7, 8, 9     | ubuntu-20.04, 6: ubuntu-18.04 |
| MSVC     | 16: v141, v142 | windows-2019 |
