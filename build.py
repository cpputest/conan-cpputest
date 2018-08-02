from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="bryceschober", 
        upload="https://api.bintray.com/conan/bryceschober/bks-conan",
        stable_branch_pattern="release*",
        channel="testing")
    builder.add_common_builds()
    builder.run()
