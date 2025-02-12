We build for several compilers, as can be seen in the table above. Take a look at the yaml
files in `.github/workflows` for one of the recipes to see how a build matrix is
constructed. We have started using standard debian and ubuntu images to build with various
compiler versions, which use glibc versions stated below. Take a look at build image
tables linked above to get glibc versions and other relevant information.

| OS                   | glibc |
|----------------------|-------|
| Debian Buster (10)   | 2.28  |
| Debian Bullseye (11) | 2.31  |
| Debian Bookworm (12) | 2.36  |
| Debian Trixie (13)   | 2.40  |
| Ubuntu 18.04         | 2.27  |
| Ubuntu 20.04         | 2.31  |
| Ubuntu 22.04         | 2.34  |
| Ubuntu 24.04         | 2.39  |

Find glibc version: `ldd --version`
