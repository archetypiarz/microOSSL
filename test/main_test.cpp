#include <gtest/gtest.h>
#include <openssl/rsa.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <iostream>

class MainTest : public ::testing::Test {
};

TEST_F(MainTest, publicRsaKeyGeneratedProperly) {
  EVP_PKEY *pkey = EVP_RSA_gen(4096);
  if (pkey == NULL){
    ERR_print_errors_fp(stderr);
    std::cout << "Key generation failed.\n";
  }

  EXPECT_EQ(4096, EVP_PKEY_get_bits(pkey));
}
