# Status for own Conan recipes

To setup this remote:
`conan remote add [REMOTE] https://artifactory.smd.sintef.no/artifactory/api/conan/conan-local`

*Note* Some recipes are available on conan-center, see further below for details

*Note* We are in the process of refactoring recipes to support conan v2. In this period, some recipes may incur braking changes.

Software | Recipe | Configurations | Conan v2
---|---|---|---
[casadi](https://web.casadi.org/)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-casadi)|[![GCC Conan](https://github.com/sintef-ocean/conan-casadi/workflows/GCC%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-casadi/actions?query=workflow%3A"GCC+Conan")[![Clang Conan](https://github.com/sintef-ocean/conan-casadi/workflows/Clang%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-casadi/actions?query=workflow%3A"Clang+Conan")[![MSVC Conan](https://github.com/sintef-ocean/conan-casadi/workflows/MSVC%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-casadi/actions?query=workflow%3A"MSVC+Conan") |
[clapack](http://www.netlib.org/clapack)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-clapack)|[![Linux GCC](https://github.com/sintef-ocean/conan-clapack/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-clapack/actions?query=workflow%3A"Linux+GCC")[![Linux Clang](https://github.com/sintef-ocean/conan-clapack/workflows/Linux%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-clapack/actions?query=workflow%3A"Linux+Clang")[![Windows MSVC](https://github.com/sintef-ocean/conan-clapack/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-clapack/actions?query=workflow%3A"Windows+MSVC")[![Windows MSVC Clang](https://github.com/sintef-ocean/conan-clapack/workflows/Windows%20MSVC%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-clapack/actions?query=workflow%3A"Windows+MSVC+Clang")[![Macos Apple-Clang](https://github.com/sintef-ocean/conan-clapack/workflows/Macos%20Apple-Clang/badge.svg)](https://github.com/sintef-ocean/conan-clapack/actions?query=workflow%3A"Macos+Apple-Clang") | :ballot_box_with_check:
[coinhsl](http://www.hsl.rl.ac.uk/ipopt/)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-coinhsl)|[![Clang Conan](https://github.com/sintef-ocean/conan-coinhsl/workflows/Clang%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-coinhsl/actions?query=workflow%3A"Clang+Conan") |
[coinmumps](http://mumps.enseeiht.fr)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-coinmumps)|[![GCC Conan](https://github.com/sintef-ocean/conan-coinmumps/workflows/GCC%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-coinmumps/actions?query=workflow%3A"GCC+Conan")[![Clang Conan](https://github.com/sintef-ocean/conan-coinmumps/workflows/Clang%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-coinmumps/actions?query=workflow%3A"Clang+Conan") |
[gnuplot-iostream](https://github.com/dstahlke/gnuplot-iostream)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-gnuplot-iostream)|[![Linux GCC](https://github.com/sintef-ocean/conan-gnuplot-iostream/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-gnuplot-iostream/actions?query=workflow%3A"Linux+GCC")[![Windows MSVC](https://github.com/sintef-ocean/conan-gnuplot-iostream/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-gnuplot-iostream/actions?query=workflow%3A"Windows+MSVC") | :ballot_box_with_check:
[ipopt](https://github.com/coin-or/ipopt)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-ipopt)|[![GCC Conan](https://github.com/sintef-ocean/conan-ipopt/workflows/GCC%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-ipopt/actions?query=workflow%3A"GCC+Conan")[![Clang Conan](https://github.com/sintef-ocean/conan-ipopt/workflows/Clang%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-ipopt/actions?query=workflow%3A"Clang+Conan") |
[libboard](https://github.com/c-koi/libboard)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-libboard)|[![Linux GCC](https://github.com/sintef-ocean/conan-libboard/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-libboard/actions?query=workflow%3A"Linux+GCC")[![Linux Clang](https://github.com/sintef-ocean/conan-libboard/workflows/Linux%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-libboard/actions?query=workflow%3A"Linux+Clang")[![Windows MSVC](https://github.com/sintef-ocean/conan-libboard/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-libboard/actions?query=workflow%3A"Windows+MSVC")[![Windows MSVC Clang](https://github.com/sintef-ocean/conan-libboard/workflows/Windows%20MSVC%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-libboard/actions?query=workflow%3A"Windows+MSVC+Clang")[![Macos Apple-Clang](https://github.com/sintef-ocean/conan-libboard/workflows/Macos%20Apple-Clang/badge.svg)](https://github.com/sintef-ocean/conan-libboard/actions?query=workflow%3A"Macos+Apple-Clang") | :ballot_box_with_check:
[mathgl](http://mathgl.sourceforge.net)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-mathgl)|[![Linux GCC](https://github.com/sintef-ocean/conan-mathgl/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-mathgl/actions?query=workflow%3A"Linux+GCC")[![Windows MSVC](https://github.com/sintef-ocean/conan-mathgl/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-mathgl/actions?query=workflow%3A"Windows+MSVC") | :ballot_box_with_check:
[mavsdk](https://mavsdk.mavlink.io/main/en/index.html)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-mavsdk)|[![Linux GCC](https://github.com/sintef-ocean/conan-mavsdk/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-mavsdk/actions?query=workflow%3A"Linux+GCC")[![Linux Clang](https://github.com/sintef-ocean/conan-mavsdk/workflows/Linux%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-mavsdk/actions?query=workflow%3A"Linux+Clang")[![Windows MSVC](https://github.com/sintef-ocean/conan-mavsdk/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-mavsdk/actions?query=workflow%3A"Windows+MSVC") | :ballot_box_with_check:
[mscl](https://github.com/LORD-MicroStrain/MSCL)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-mscl)|[![Linux GCC](https://github.com/sintef-ocean/conan-mscl/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-mscl/actions?query=workflow%3A"Linux+GCC")[![Linux Clang](https://github.com/sintef-ocean/conan-mscl/workflows/Linux%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-mscl/actions?query=workflow%3A"Linx+Clang")[![Windows MSVC](https://github.com/sintef-ocean/conan-mscl/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-mscl/actions?query=workflow%3A"Windows+MSVC") | :ballot_box_with_check:
[netcdf](https://github.com/Unidata/netcdf-c.git)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-netcdf-c)|[![Linux GCC](https://github.com/sintef-ocean/conan-netcdf-c/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-netcdf-c/actions?query=workflow%3A"Linux+GCC")[![Linux Clang](https://github.com/sintef-ocean/conan-netcdf-c/workflows/Linux%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-netcdf-c/actions?query=workflow%3A"Linux+Clang")[![Windows MSVC](https://github.com/sintef-ocean/conan-netcdf-c/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-netcdf-c/actions?query=workflow%3A"Windows+MSVC")[![Windows MSVC Clang](https://github.com/sintef-ocean/conan-netcdf-c/workflows/Windows%20MSVC%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-netcdf-c/actions?query=workflow%3A"Windows+MSVC+Clang")[![Macos Apple-Clang](https://github.com/sintef-ocean/conan-netcdf-c/workflows/Macos%20Apple-Clang/badge.svg)](https://github.com/sintef-ocean/conan-netcdf-c/actions?query=workflow%3A"Macos+Apple-Clang") | :ballot_box_with_check:
[ogre3d](https://www.ogre3d.org/)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-ogre3d)|[![Linux GCC](https://github.com/sintef-ocean/conan-ogre3d/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-ogre3d/actions?query=workflow%3A"Linux+GCC")[![Linux Clang](https://github.com/sintef-ocean/conan-ogre3d/workflows/Linux%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-ogre3d/actions?query=workflow%3A"Linux+Clang")[![Windows MSVC](https://github.com/sintef-ocean/conan-ogre3d/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-ogre3d/actions?query=workflow%3A"Windows+MSVC") | :ballot_box_with_check:
[opensplice-ce](https://github.com/ADLINK-IST/opensplice)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-opensplice-ce)|[![Linux GCC](https://github.com/sintef-ocean/conan-opensplice-ce/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-opensplice-ce/actions?query=workflow%3A"Linux+GCC")[![Windows MSVC](https://github.com/sintef-ocean/conan-opensplice-ce/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-opensplice-ce/actions?query=workflow%3A"Windows+MSVC") | :ballot_box_with_check:
[qualisys-cpp-sdk]( https://github.com/qualisys/qualisys_cpp_sdk)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-qualisys-cpp-sdk)|[![Linux GCC](https://github.com/sintef-ocean/conan-qualisys-cpp-sdk/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-qualisys-cpp-sdk/actions?query=workflow%3A"Linux+GCC")[![Linux Clang](https://github.com/sintef-ocean/conan-qualisys-cpp-sdk/workflows/Linux%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-qualisys-cpp-sdk/actions?query=workflow%3A"Linux+Clang")[![Windows MSVC](https://github.com/sintef-ocean/conan-qualisys-cpp-sdk/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-qualisys-cpp-sdk/actions?query=workflow%3A"Windows+MSVC") | :ballot_box_with_check:

----
## Deprecated recipes

Software | Recipe | Reason
---|---|---
[hdf5](https://portal.hdfgroup.org/display/HDF5/HDF5)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-hdf5)| Build with conan-center recipe
[miniconda](https://docs.conda.io/)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-miniconda)|Was intended for flang, use intel-fortran instead
[cyclonedds](https://cyclonedds.io/)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-cyclonedds)|Available on conan-center
[cyclonedds-cxx](https://cyclonedds.io/)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-cyclonedds-cxx)|To become available on conan-center
[openblas](https://www.openblas.net/)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-openblas)|To become available on conan-center
[coinbrew](http://github.com/coin-or/coinbrew)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-coinbrew)|Deprecated
[coinglpk](https://www.gnu.org/software/glpk)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-coinglpk)|Available as `glpk` on conan-center
[coinmetis](http://glaros.dtc.umn.edu/gkhome/metis/metis/overview)|[<img src="https://github.com/favicon.ico" height="28">](https://github.com/sintef-ocean/conan-coinmetis)|Available as `metis` on conan-center
----
## Conan recipes in conan-center

We maintain some recipes that are available from conan-center. There are various reasons
for this, as indicated below. We also build some recipes with configurations not being
built on conan-center.

Software | Reason
---|---
hdf5 | Build with options not available from conan-center
netcdf | Custom recipe with pinned version due to a required feature
openblas | Build with option `build_lapack=true`

Add new row to table: See [scripts/README.md](scripts/README.md)

----
## Build matrix configuration for recipes
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
