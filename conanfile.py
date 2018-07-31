from os import path
from conans import ConanFile, CMake


class CppUTest(ConanFile):
    name = "CppUTest"
    version = "master" # "3.8"
    description = """C /C++ based unit xUnit test framework for unit testing and for test-driving your code"""
    license = "BSD 3-clause \"New\" or \"Revised\" License, https://github.com/cpputest/cpputest/blob/master/COPYING"
    url = "https://cpputest.github.io"
    settings = "os", "compiler", "arch", "build_type"
    source_dir = "{name}-{version}".format(name=name, version=version)
    options = {
        "shared": [True, False],
        "include_pdbs": [True, False],
        "fPIC": [True, False],
        "tests": [True, False],
        "extensions": [True, False]
    }
    default_options = (
        "shared=False",
        "include_pdbs=False",
        "fPIC=False",
        "tests=False",
        "extensions=True"
    )
    scm = {
        "type": "git",
        "subfolder": source_dir,
        "url": "https://github.com/cpputest/cpputest.git",
        "revision": "tags/v{version}".format(version=version)
    }
    if version == "master":
        scm["revision"] = "master"

    def source(self):
        pass

    def build(self):
        cmake = CMake(self)
        #cmake.verbose = True
        cmake.definitions["TESTS"] = self.options.tests
        cmake.configure(source_dir=path.join(self.source_folder, self.source_dir))
        cmake.build()
        if self.options.tests:
            cmake.test()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["CppUTest"]
        if self.options.extensions:
            self.cpp_info.libs.append("CppUTestExt")
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.libs.append("winmm.lib")
