TARGET = traceroute
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17
SRC = main.cpp traceroute.cpp
OBJ = $(SRC:.cpp=.o)
DEPS = traceroute.h

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) $(OBJ) -o $(TARGET)

%.o: %.cpp $(DEPS)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)
