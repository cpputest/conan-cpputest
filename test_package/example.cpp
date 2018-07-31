#include <CppUTest/TestHarness.h>
#include <CppUTestExt/TestRegistry.h>
#include <CppUTestExt/CommandLineTestRunner.h>
#include <CppUTestExt/MockSupportPlugin.h>

TEST_GROUP(FirstTestGroup)
{
};

TEST(FirstTestGroup, FirstTest)
{
   CHECK_TRUE(true);
}

int main(int argc, const char** argv)
    MockSupportPlugin mockPlugin;
    TestRegistry::getCurrentRegistry()->installPlugin(&mockPlugin);

    CommandLineTestRunner runner(argc, argv, TestRegistry::getCurrentRegistry());
    return runner.runAllTestsMain();
}
