// Bartosz Kruszewski 337568

#pragma once
#include <string>
#include <vector>
#include "network.hpp"

struct Interface {
    uint32_t ip;
    uint8_t prefix;
    uint32_t distance;
    uint32_t net;
    uint32_t bcast;
    bool reachable;
};

Interface parse_interface_line(const std::string &line);
void read_interfaces(std::vector<Interface> &interfaces);
