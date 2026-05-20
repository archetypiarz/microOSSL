import os
from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake, CMakeToolchain

class MicroOSSL(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"

    def requirements(self):
        self.requires("openssl/3.6.2")
    
    def build_requirements(self):
        self.test_requires("gtest/1.17.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        #if self.options.with_fmt:
        #    tc.variables["WITH_FMT"] = True
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if not self.conf.get("tools.build:skip_test", default=False):
            test_folder = os.path.join("test")
            self.run(os.path.join(test_folder, "microOSSL_tests"))
