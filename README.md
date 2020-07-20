# mc\_rtc\_data

[![License](https://img.shields.io/badge/License-BSD%202--Clause-green.svg)](https://opensource.org/licenses/BSD-2-Clause)
[ ![Download](https://api.bintray.com/packages/gergondet/multi-contact/mc_rtc_data%3Amulti-contact/images/download.svg) ](https://bintray.com/gergondet/multi-contact/mc_rtc_data%3Amulti-contact/_latestVersion)

This package provides data for mc\_rtc

This package can be used as a ROS package.

## List of packages

- **mc_env_description** description package for static environment compatible with mc\_rtc "env" robot module
- **mc_int_obj_description** description package for interactive objects compatible with mc\_rtc "object" robot module
- **jvrc_description** description package for the JVRC1 robot

# Installing

## Ubuntu LTS (16.04, 18.04, 20.04)

```bash
# Make sure you have required tools
sudo apt install apt-transport-https lsb-release ca-certificates gnupg
# Add our key
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key 892EA6EE273707C6495A6FB6220D644C64666806
# Add our repository (stable versions)
sudo sh -c 'echo "deb https://dl.bintray.com/gergondet/multi-contact-release $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/multi-contact.list'
# Use this to setup the HEAD version
# sudo sh -c 'echo "deb https://dl.bintray.com/gergondet/multi-contact-head $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/multi-contact.list'
# Update packages list
sudo apt update
# Install packages
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
make intall
```

Or clone in your catkin workspace and build
