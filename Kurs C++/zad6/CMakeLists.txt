cmake_minimum_required(VERSION 3.24)
project(zad6)

set(CMAKE_CXX_STANDARD 17)

add_executable(zad6 main.cpp Expression.h Expression.cpp OperatorSingleArg.cpp OperatorSingleArg.h OperatorDualArg.h OperatorDualArg.cpp)
