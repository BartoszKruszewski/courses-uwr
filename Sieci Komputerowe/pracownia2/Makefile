CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17
LDFLAGS =

TARGET = router

SRC = main.cpp interface.cpp network.cpp routing.cpp socket_utils.cpp packet.cpp

OBJ_DIR = obj
OBJ = $(SRC:.cpp=.o)
OBJ := $(patsubst %.o,$(OBJ_DIR)/%.o,$(OBJ))

DEPS = interface.hpp network.hpp routing.hpp socket_utils.hpp packet.hpp

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CXX) $(OBJ) -o $@ $(LDFLAGS)

$(OBJ_DIR)/%.o: %.cpp $(DEPS)
	@mkdir -p $(OBJ_DIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR)

distclean: clean
	rm -f $(TARGET)

.PHONY: all clean distclean
