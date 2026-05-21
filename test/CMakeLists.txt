include(CTest)

add_executable(microOSSL_tests
  main_test.cpp
)

find_package(GTest REQUIRED)
find_package(OpenSSL REQUIRED)
target_link_libraries(microOSSL_tests 
  PRIVATE 
  GTest::GTest
  GTest::Main
  openssl::openssl
)
