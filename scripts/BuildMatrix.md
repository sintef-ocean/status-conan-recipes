We build for three compilers, GCC, Clang, and MSVC. Below is the configuration for each
compiler. Take a look at the yaml files in `.github/workflows` for one of the recipes to
see how a build matrix is constructed.

| Compiler | Versions       | libcxx      | os           |
| -------- | -------------- | ----------- | ------------ |
| Clang    | 8, 9, 10       | libstdc++11 | ubuntu-20.04 |
| GCC      | 6              | libstdc++   | ubuntu-18.04 |
| GCC      | 7, 8, 9        | libstdc++11 | ubuntu-20.04 |
| MSVC     | 16: v141, v142 | \-          | windows-2019 |
