cmake_minimum_required(VERSION 3.1)
cmake_policy(SET CMP0048 NEW)
project(mc_rtc_data VERSION 1.0.1)

enable_testing()

add_subdirectory(jvrc_description)
add_subdirectory(mc_env_description)
add_subdirectory(mc_int_obj_description)
