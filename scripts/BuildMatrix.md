We build for several compilers, as can be seen in the table above. Take a look at the yaml
files in `.github/workflows` for one of the recipes to see how a build matrix is
constructed. We currently build linux artifacts using docker images from
[conan-io/conan-docker-tools](https://github.com/conan-io/conan-docker-tools/tree/master/modern). Recent
compiler versions should be runtime compatible with Debian/Ubuntu distributions, which use
glibc versions stated below. Take a look at build image tables linked above to get glibc
versions and other relevant information.

*Note* we are currently moving from legacy to modern container images. The old recipes use
legacy build images provided by
[conan-io/conan-docker-tools](https://github.com/conan-io/conan-docker-tools).

| OS           | glibc |
|--------------|-------|
| Buster       | 2.28  |
| Bullseye     | 2.31  |
| Bookworm     | 2.36  |
| Ubuntu 18.04 | 2.27  |
| Ubuntu 20.04 | 2.31  |
| Ubuntu 22.04 | 2.34  |

Find glibc version: `ldd --version`
