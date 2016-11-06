from conans import ConanFile, CMake

class PlaygroundConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators  = "cmake", "txt"
    # default_options = "Poco:shared=True", "OpenSSL:shared=True"

    def configure(self):
        if self.settings.os == "Linux":
            self.settings.compiler = "clang"
            self.settings.compiler.libcxx = "libstdc++11"
            self.settings.compiler.version = "3.8"

    def imports(self):
        self.copy("*.dll", dst = "bin", src = "bin") # From bin to bin
        self.copy("*.dylib*", dst = "bin", src = "lib") # From lib to bin

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run('cmake --build . %s' % cmake.build_config)
