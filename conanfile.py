from conans import ConanFile, CMake, tools
import os


class LibhhashConan(ConanFile):
    name = "libhhash"
    version = "1.0.0"
    license = "MIT"
    url = "https://github.com/coriolanus/libhhash"
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        self.run("git clone git@github.com:coriolanus/libhhash.git")

    def build(self):
        self.run("cd libhhash && make libhhash.a")

    def package(self):
        self.copy("*.h", dst="include", src="libhhash")
        self.copy("*.dll", dst="bin", src="libhhash")
        self.copy("*.so", dst="lib", src="libhhash")
        self.copy("*.a", dst="lib", src="libhhash")
