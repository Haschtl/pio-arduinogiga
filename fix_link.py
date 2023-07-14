from os.path import join, isfile
Import("env")

# Fix compilation of SerialRPC class by adding library.json
# See https://community.platformio.org/t/portenta-and-rpc-missing-asio-hpp-header-framework-arduino-mbed-not-latest/26862/16
lib_json = r"""{
  "name": "rpclib",
  "version": "1.0.0",
  "build": {
    "srcFilter": "+<*> -<.git/> -<.svn/> -<example/> -<examples/> -<test/> -<tests/> -<**/*.cc>"
  }
}
"""
FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-arduino-mbed")
target_file = join(FRAMEWORK_DIR, "libraries", "rpclib" , "library.json")
if not isfile(target_file):
    # put it in there
    with open(target_file, "w") as fp:
        fp.write(lib_json)
    print("[+] Saved library.json for RPCLib fix.")

# Fix linking by declaring start and end properly
for e in env, DefaultEnvironment():
    # This env-variables are set for 50_50 flash-layout
    # defines = [("CM4_BINARY_START", "0x08100000"), ("CM4_BINARY_END", "0x08200000")]
    # This env-variables are set for 75_25 flash-layout
    # defines = [("CM4_BINARY_START", "0x08180000"), ("CM4_BINARY_END", "0x08200000")]
    # This env-variables are set for 100_0 flash-layout
    defines = [("CM4_BINARY_START", "0x60000000"), ("CM4_BINARY_END", "0x60040000"), ("CM4_RAM_END","0x60080000")]
    e.Append(
        LINKFLAGS=["-D%s=%s" % (name, value) for name, value in defines],
        CPPDEFINES=defines
    )