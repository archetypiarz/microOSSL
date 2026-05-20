#include <gtest/gtest.h>
#include <iostream>

class MainTest : public ::testing::Test {
};

TEST_F(MainTest, HelloWorldTest) {
  std::cout << "Hello world" << std::endl;
  EXPECT_TRUE(true);
}
