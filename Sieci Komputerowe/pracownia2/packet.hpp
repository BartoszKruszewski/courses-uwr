// Bartosz Kruszewski 337568

#pragma once
#include "routing.hpp"
#include "interface.hpp"
#include <netinet/in.h>

struct PacketData
{
    uint32_t net;
    uint8_t prefix;
    uint32_t distance;
    uint32_t src_ip;
};

PacketData parse_packet(uint8_t *buf, const sockaddr_in &sender);
uint32_t find_interface_cost(uint32_t src_ip, const std::vector<Interface> &interfaces);
uint32_t calculate_total_cost(uint32_t hop_cost, uint32_t distance);
bool should_add_route(uint32_t distance, uint32_t src_ip);
void update_or_add_route(const PacketData &pd, uint32_t total_cost, std::map<Network, Route> &table);
void handle_packet(uint8_t *buf, const sockaddr_in &sender, const std::vector<Interface> &interfaces, std::map<Network, Route> &table);
