//test_factorial.cpp

#include <hello.hpp>
# include "gtest/gtest.h"

class HelloClassTest : public ::testing::Test {
protected:
	Hello myHello;
};

TEST_F(HelloClassTest, myHello) {
	EXPECT_EQ("Hello World",myHello.sayHello());
}

