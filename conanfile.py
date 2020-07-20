# -*- coding: utf-8 -*-
#

from conans import python_requires
import conans.tools as tools
import os

base = python_requires("Eigen3ToPython/latest@multi-contact/dev")

class MCRTCDataConan(base.Eigen3ToPythonConan):
    name = "mc_rtc_data"
    version = "1.0.3"
    description = "Environments/Robots description for mc_rtc"
    topics = ("robotics", "data")
    url = "https://github.com/jrl-umi3218/mc_rtc_data"
    homepage = "https://github.com/jrl-umi3218/mc_rtc_data"
    author = "Pierre Gergondet <pierre.gergondet@gmail.com>"
    license = "BSD-2-Clause"
    exports = ["LICENSE"]
    exports_sources = ["CMakeLists.txt", "conan/CMakeLists.txt", "cmake/*", "jvrc_description/*", "mc_env_description/*", "mc_int_obj_description/*", "mc_rtc_data/*"]
    generators = "cmake"
    settings = "os", "arch"
    requires = ()

    def config_options(self):
        del self.options.python2_version
        del self.options.python3_version

    def package_id(self):
        pass

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        tools.rmdir(os.path.join(self.package_folder, "lib", "pkgconfig"))
        for f in [".catkin", "_setup_util.py", "env.sh", "setup.bash", "local_setup.bash", "setup.sh", "local_setup.sh", "setup.zsh", "local_setup.zsh", ".rosinstall"]:
            p = os.path.join(self.package_folder, f)
            if os.path.exists(p):
              os.remove(p)

