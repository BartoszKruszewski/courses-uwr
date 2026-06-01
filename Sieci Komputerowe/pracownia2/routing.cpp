// Bartosz Kruszewski 337568

#include "routing.hpp"
#include <iostream>

void initialize_routes(std::map<Network, Route> &table, const std::vector<Interface> &interfaces) {
    for (const auto &iface : interfaces) {
        Network net{iface.net, iface.prefix};
        table[net] = {iface.distance, 0, true, -1};
    }
}

void print_table(const std::map<Network, Route> &table) {
    std::cout << "[== Routing Table ==]\n";
    for (const auto &[net, rt] : table) {
        std::cout << ip_u32_to_str(net.addr) << "/" << (int)net.prefix << " distance ";
        if (rt.distance == INF_DISTANCE)
            std::cout << "unreachable";
        else
            std::cout << rt.distance;

        if (rt.directly_connected)
            std::cout << " connected directly\n";
        else if (rt.distance != INF_DISTANCE)
            std::cout << " via " << ip_u32_to_str(rt.next_hop) << "\n";
        else
            std::cout << " unreachable\n";
    }
    std::cout << "[===================]\n";
}

void clean_table(std::map<Network, Route> &table) {
    for (auto it = table.begin(); it != table.end();) {
        Route &r = it->second;
        if (!r.directly_connected && r.distance == INF_DISTANCE) {
            if (r.unreachable_since == -1) r.unreachable_since = 0;
            else if (++r.unreachable_since >= MAX_TTL) {
                it = table.erase(it);
                continue;
            }
        }
        ++it;
    }
}

void update_interface_state(Interface &iface, Route &route, bool send_ok) {
    if (!send_ok && iface.reachable) {
        iface.reachable = false;
        if (route.directly_connected && route.distance != INF_DISTANCE) {
            route.distance = INF_DISTANCE;
            route.unreachable_since = 0;
        }
    } else if (send_ok && !iface.reachable) {
        iface.reachable = true;
        if (route.directly_connected) {
            route.distance = iface.distance;
            route.unreachable_since = -1;
        }
    }
}

void send_vector(int sock, std::vector<Interface> &interfaces, std::map<Network, Route> &table)
{
    for (size_t i = 0; i < interfaces.size(); i++)
    {
        Interface &iface = interfaces[i];

        sockaddr_in addr;
        std::memset(&addr, 0, sizeof(addr));
        addr.sin_family = AF_INET;
        addr.sin_port = htons(ROUTER_PORT);
        addr.sin_addr.s_addr = htonl(iface.bcast);

        bool send_ok = true;

        for (std::map<Network, Route>::const_iterator it = table.begin(); it != table.end(); ++it)
        {
            const Network &net = it->first;
            const Route &rt = it->second;

            uint8_t buf[9];
            uint32_t net_be = htonl(net.addr);
            uint32_t dist_be = htonl(rt.distance);

            std::memcpy(buf, &net_be, 4);
            buf[4] = net.prefix;
            std::memcpy(buf + 5, &dist_be, 4);

            ssize_t sent = sendto(sock, buf, 9, 0, reinterpret_cast<sockaddr *>(&addr), sizeof(addr));
            if (sent < 0)
            {
                send_ok = false;
            }
        }

        Network iface_net;
        iface_net.addr = iface.net;
        iface_net.prefix = iface.prefix;

        std::map<Network, Route>::iterator it = table.find(iface_net);
        if (it != table.end())
        {
            update_interface_state(iface, it->second, send_ok);
        }
    }
}
