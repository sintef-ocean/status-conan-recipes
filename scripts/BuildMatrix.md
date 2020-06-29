We build for three compilers, GCC, Clang, and MSVC. Below is the configuration for each
compiler. Take a look at the yaml files in `.github/workflows` for one of the recipes to
see how a build matrix is constructed. We currently build all linux artifacts using docker
images from [conan-io](https://github.com/conan-io/conan-docker-tools) on ubuntu-20.04

| Compiler | Versions       | container/os    | glibc ver. |
| -------- | -------------- | ------------    | ---------- |
| Clang    | 8              | conanio/clang8  | 2.29       |
| Clang    | 9              | conanio/clang9  | 2.30       |
| Clang    | 10             | conanio/clang10 | 2.27       |
| GCC      | 6              | conanio/gcc63   | 2.24       |
| GCC      | 7              | conanio/gcc7    | 2.26       |
| GCC      | 8              | conanio/gcc8    | 2.27       |
| GCC      | 9              | conanio/gcc9    | 2.30       |
| MSVC     | 16: v141, v142 | windows-2019    | -          |

| OS           | glibc   |
|--------------|---------|
| Stretch      | 2.24    |
| Buster       | 2.28    |
| Bullseye     | 2.30(?) |
| Ubuntu 16.04 | 2.23    |
| Ubuntu 18.04 | 2.27    |
| Ubuntu 20.04 | 2.31    |

**Note** OpenSplice are currently built using debian:bullseye for clang due to issues
when using conanio/clangX images.
