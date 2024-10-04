# pyRCSwitch
# Python module to wrap the RCSwitch Common Library
#
# See: https://github.com/latchdevel/pyRCSwitch
#
# Copyright (c) 2024 Jorge Rivera. All right reserved.
# License GNU Lesser General Public License v3.0.

cmake_minimum_required(VERSION 3.18)

project(pyRCSwitch LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)

if(NOT BUILD_COMPILER)
  # Set complier identification
  SET(BUILD_COMPILER "${CMAKE_CXX_COMPILER_ID} ${CMAKE_CXX_COMPILER_VERSION}" )
  MESSAGE( STATUS "C++ compiler: " ${BUILD_COMPILER} )
endif()

# VERSION_INFO is defined by setup.py and passed into the C++
if(NOT VERSION_INFO)
  # Set version info
  SET(VERSION_INFO "undefined" )
endif()
MESSAGE( STATUS "Module version: " ${VERSION_INFO} )

# Check if set CMAKE_BUILD_TYPE var
if(NOT CMAKE_BUILD_TYPE)
  # Set default build type to "release" set -O3 -DNDEBUG
  set(DEFAULT_BUILD_TYPE "RELEASE")
  SET(CMAKE_BUILD_TYPE ${DEFAULT_BUILD_TYPE})
  MESSAGE( STATUS "Build type set to default: " ${CMAKE_BUILD_TYPE} )
else()
  # Check if set and valid CMAKE_BUILD_TYPE var
  STRING( TOUPPER "${CMAKE_BUILD_TYPE}" CMAKE_BUILD_TYPE )
  if((CMAKE_BUILD_TYPE STREQUAL "DEBUG") OR (CMAKE_BUILD_TYPE STREQUAL "RELEASE"))
    # If no has parent directory show message
    if(NOT hasParent)
      MESSAGE( STATUS "Build type set to: " ${CMAKE_BUILD_TYPE} )
    endif()
  else()
    MESSAGE( FATAL_ERROR "If set CMAKE_BUILD_TYPE it must be 'release' or 'debug'")
  endif()
endif()

# Setting build type to "debug" add only -g 
if(CMAKE_BUILD_TYPE STREQUAL "DEBUG") 
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DDEBUG")
endif()

# Set C++ flags
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -pedantic")
elseif(MSVC)
  set(MSVC_DISABLED_WARNINGS_LIST
    "C4996" # warning C4996: 'may be unsafe/disable deprecation'
            # To disable deprecation, use _CRT_SECURE_NO_WARNINGS.
  )
  string(REPLACE "C" " -wd" MSVC_DISABLED_WARNINGS_STR ${MSVC_DISABLED_WARNINGS_LIST})
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -W4 ${MSVC_DISABLED_WARNINGS_STR}")
endif()

# Add pybind11 directory
add_subdirectory( libs/pybind11 EXCLUDE_FROM_ALL )

# Add RCSwitch Common Library directory
add_subdirectory( libs/rc-switch-lib EXCLUDE_FROM_ALL )

# Add pyRCSwith Pyhon module C++ source code
pybind11_add_module( ${PROJECT_NAME} pyRCSwitch.cpp )

# Add pyRCSwitch static library to link Python mudule
target_link_libraries( ${PROJECT_NAME} PRIVATE RCSwitch )

# Shared libraries need flag -fPIC
set_property( TARGET ${PROJECT_NAME} PROPERTY POSITION_INDEPENDENT_CODE TRUE ) 

# Enable interprocedural optimizations if supported by the compiler
include(CheckIPOSupported)
check_ipo_supported(RESULT iporesult)
if(iporesult)
  message (STATUS "IPO supported")
  set_property( TARGET ${PROJECT_NAME} PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE )
else()
  message (STATUS "IPO not supported")
endif()

# VERSION_INFO is defined by setup.py and passed into the C++ code here
target_compile_definitions( ${PROJECT_NAME} PRIVATE VERSION_INFO=${VERSION_INFO} )

# If macOS system, builds a Mach-O universal binary with 2 architectures: x86_64 and arm64 for Apple M processors
if (APPLE) 
  set_property( TARGET ${PROJECT_NAME} PROPERTY COMPILE_FLAGS "-arch arm64 -arch x86_64" )
  set_property( TARGET ${PROJECT_NAME} PROPERTY LINK_FLAGS "-arch arm64 -arch x86_64" )
  set( CMAKE_OSX_DEPLOYMENT_TARGET "11.0" )
endif()