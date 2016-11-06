cmake_minimum_required(VERSION 3.0.2)

############################################################
#### CONFIGURE CMAKE VARIABLES
############################################################
set (PROJECT_NAME bookmarkt)
set (CMAKE_MODULE_DIR ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/CMakeModules/")
set (CMAKE_BINARY_DIR "${CMAKE_CURRENT_SOURCE_DIR}/build/")
set (EXECUTABLE_OUTPUT_PATH "${CMAKE_CURRENT_SOURCE_DIR}/bin/")

project( ${PROJECT_NAME} )

############################################################
#### INCLUDE CMAKE MODULES & SETUP
############################################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

############################################################
#### MANAGE PROJECT VERSION
############################################################

############################################################
#### TURN ON USING SOLUTION FOLDERS
############################################################
set_property ( GLOBAL PROPERTY USE_FOLDERS ON )

############################################################
#### SET BUILD VARIABLES
############################################################
# add_definitions( -DCONFIG_DIR="/Users/vlnk/.autobahn" )
# add_definitions( -DSCRIPTS_DIR="/Users/vlnk/Scripts" )
# add_definitions( -DLANGUAGES_DIR="${CMAKE_CURRENT_SOURCE_DIR}/languages" )

############################################################
#### SET CONFIGURATION VARS
############################################################
set( CMAKE_VERBOSE_MAKEFILE off )
set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11" )

############################################################
#### ADD SUBDIRECTORIES
############################################################
add_subdirectory( src )
# add_subdirectory( tests )

############################################################
#### ADD EXECUTABLE
############################################################
add_executable ( ${PROJECT_NAME} ${SOURCE_FILES} )
