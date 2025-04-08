cmake_minimum_required(VERSION 3.10)
cmake_policy(SET CMP0048 NEW)

set(PROJECT_VERSION 1.0.7)
project(mc_rtc_data VERSION ${PROJECT_VERSION})

option(DISABLE_ROS "Disable ROS build" ON)

enable_testing()

if(DISABLE_ROS)
  message(STATUS "Building without ROS support as DISABLE_ROS=ON")
else()
  if(NOT DEFINED ENV{ROS_VERSION})
    message(FATAL_ERROR "ROS_VERSION is not set in the environment")
  endif()
  set(ROS_VERSION $ENV{ROS_VERSION})
endif()

add_subdirectory(jvrc_description)
add_subdirectory(mc_env_description)
add_subdirectory(mc_int_obj_description)
