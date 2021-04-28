cmake_minimum_required(VERSION 3.1)
cmake_policy(SET CMP0048 NEW)
project(mc_int_obj_description VERSION 1.0.4)

if(NOT DISABLE_ROS)
  find_package(catkin QUIET)
endif()

if(catkin_FOUND)

  catkin_package()

else()

  set(CATKIN_PACKAGE_SHARE_DESTINATION share/mc_rtc/${PROJECT_NAME})

  include(CMakePackageConfigHelpers)
  set(VERSION_CONFIG "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake")
  set(PROJECT_CONFIG "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake")
  set(CONFIG_INSTALL_DIR "lib/cmake/${PROJECT_NAME}")

  configure_file("${CMAKE_CURRENT_SOURCE_DIR}/../cmake/ConfigVersion.cmake.in" "${VERSION_CONFIG}" @ONLY)
  configure_package_config_file("${CMAKE_CURRENT_SOURCE_DIR}/../cmake/Config.cmake.in" "${PROJECT_CONFIG}" INSTALL_DESTINATION "${CONFIG_INSTALL_DIR}")

  install(FILES "${VERSION_CONFIG}" "${PROJECT_CONFIG}" DESTINATION "${CONFIG_INSTALL_DIR}")
  install(FILES package.xml DESTINATION "${CATKIN_PACKAGE_SHARE_DESTINATION}")

endif()

install(DIRECTORY convex/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/convex)
install(DIRECTORY meshes/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/meshes)
install(DIRECTORY rsdf/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/rsdf)
install(DIRECTORY urdf/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf)
