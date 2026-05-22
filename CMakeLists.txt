cmake_minimum_required(VERSION 4.1)

project(
  microOSSL
  VERSION 0.1
  LANGUAGES CXX
)

add_subdirectory(src)
add_subdirectory(test)

add_custom_target(
    copy-compile-commands ALL
    ${CMAKE_COMMAND} -E copy_if_different
        ${CMAKE_BINARY_DIR}/compile_commands.json
        ${CMAKE_CURRENT_LIST_DIR}
)
