from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="bryceschober", 
        upload="https://api.bintray.com/conan/bryceschober/bks-conan",
        stable_branch_pattern="release*",
        channel="testing")
    builder.add_common_builds()
    # Give us a foot-hold to manually test conan package options
    for settings, options, env_vars, build_requires, reference in builder.items:
        #options["CppUTest:coverage"] = True
        pass
    builder.run()
