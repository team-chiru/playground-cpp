function set_cpp_compiler() {
    if [ $# -ne 1 ]; then
      echo "missing argument: compiler name"
      exit 1
    fi

    case $1 in
        "clang")
            export CC=clang
            export CXX=clang++
            ;;
        "gcc")
            export CC=gcc-4.9
            export CXX=g++-4.9
            ;;
        *)
            export CC=gcc
            export CXX=g++
            #enlever -6 pour prendre apple llvm
            ;;
    esac
}
