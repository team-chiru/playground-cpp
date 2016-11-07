from conans import ConanFile, CMake
import os

channel = os.getenv("CONAN_CHANNEL", "playground-cpp")
username = os.getenv("CONAN_USERNAME", "team-chiru")
name = "Bookmarkt"
version = "0.1"

class PlaygroundConan(ConanFile):
    license = "MIT"
    url = "https://github.com/team-chiru/playground-cpp"
    settings = "os", "compiler", "build_type", "arch"
    generators  = "cmake", "txt"
    exports = "*"
    # default_options = "Poco:shared=True", "OpenSSL:shared=True"
    #requires = "%s/%s@%s/%s" % (name, version, username, channel)

    def configure(self):
        if self.settings.os == "Linux":
            self.settings.compiler = "clang"
            self.settings.compiler.libcxx = "libstdc++11"
            self.settings.compiler.version = "3.8"

    def package_info(self):
        self.cpp_info.libs = [name]

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run('cmake --build . %s' % cmake.build_config)
