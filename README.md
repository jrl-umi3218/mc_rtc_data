# mc\_rtc\_data

[![License](https://img.shields.io/badge/License-BSD%202--Clause-green.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Hosted By: Cloudsmith](https://img.shields.io/badge/OSS%20hosting%20by-cloudsmith-blue?logo=cloudsmith)](https://cloudsmith.com)

This package provides data for mc\_rtc

This package can be used as a ROS package.

## List of packages

- **mc_env_description** description package for static environment compatible with mc\_rtc "env" robot module
- **mc_int_obj_description** description package for interactive objects compatible with mc\_rtc "object" robot module
- **jvrc_description** description package for the JVRC1 robot

# Installing

## Ubuntu LTS (16.04, 18.04, 20.04)

You must first setup our package mirror:

```
curl -1sLf \
  'https://dl.cloudsmith.io/public/mc-rtc/stable/setup.deb.sh' \
  | sudo -E bash
```

You can also choose the head mirror which will have the latest version of this package:

```
curl -1sLf \
  'https://dl.cloudsmith.io/public/mc-rtc/stable/setup.deb.sh' \
  | sudo -E bash
```

You can then install the package:

```bash
sudo apt install mc-rtc-data
# Install in a ROS-compatible way
sudo apt install ros-${ROS_DISTRO}-mc-rtc-data
```

## Conan

Install the latest version using [conan](https://conan.io/)

```bash
conan remote add multi-contact https://api.bintray.com/conan/gergondet/multi-contact
# Install the latest release
conan install mc_rtc_data/latest@multi-contact/stable
# Or install the latest development version
# conan install mc_rtc_data/latest@multi-contact/dev
```

## Manually build from source

### Dependencies

To compile you need the following tools and libraries:

 * [Git]()
 * [CMake]() >= 2.8

### Building

```sh
git clone --recursive https://github.com/jrl-umi3218/mc_rtc_data
mkdir mc_rtc_data/_build
cd mc_rtc_data/_build
cmake ..
make install
```

Or clone in your catkin workspace and build
