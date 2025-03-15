TARGET = traceroute
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17
SRC = main.cpp traceroute.cpp
OBJ = $(SRC:.cpp=.o)
all: $(TARGET)
$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) $(OBJ) -o $(TARGET)

%.o: %.cpp traceroute.h
	$(CXX) $(CXXFLAGS) -c $< -o $@
