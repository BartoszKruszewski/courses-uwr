// Bartosz Kruszewski 337568

#include "interface.hpp"
#include <sstream>
#include <iostream>

Interface parse_interface_line(const std::string &line) {
    std::stringstream ss(line);
    std::string cidr, placeholder;
    uint32_t dist;
    ss >> cidr >> placeholder >> dist;

    size_t slash = cidr.find('/');
    std::string ip_str = cidr.substr(0, slash);
    uint8_t prefix = static_cast<uint8_t>(std::stoi(cidr.substr(slash + 1)));
    uint32_t ip = ip_str_to_u32(ip_str);
    uint32_t mask = make_mask(prefix);

    Interface iface{ip, prefix, dist, ip & mask, (ip & mask) | ~mask, true};
    return iface;
}

void read_interfaces(std::vector<Interface> &interfaces) {
    std::string line;
    std::getline(std::cin, line);
    int n = std::stoi(line);
    interfaces.resize(n);
    for (int i = 0; i < n; ++i) {
        std::getline(std::cin, line);
        interfaces[i] = parse_interface_line(line);
    }
}
