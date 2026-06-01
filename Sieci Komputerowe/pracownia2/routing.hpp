// Bartosz Kruszewski 337568

#pragma once
#include <map>
#include <vector>
#include <cstring>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>
#include "interface.hpp"
#include "network.hpp"

constexpr uint16_t ROUTER_PORT = 54321;
constexpr uint32_t INF_DISTANCE = 0xFFFFFFFF;
constexpr int BROADCAST_INTERVAL = 5;
constexpr int MAX_TTL = 3;

struct Route
{
    uint32_t distance;
    uint32_t next_hop;
    bool directly_connected;
    int unreachable_since;
};

void initialize_routes(std::map<Network, Route> &table, const std::vector<Interface> &interfaces);
void print_table(const std::map<Network, Route> &table);
void clean_table(std::map<Network, Route> &table);
void update_interface_state(Interface &iface, Route &route, bool send_ok);
void send_vector(int sock, std::vector<Interface> &interfaces, std::map<Network, Route> &table);
