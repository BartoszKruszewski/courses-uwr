// Bartosz Kruszewski 337568

#include "interface.hpp"
#include "routing.hpp"
#include "socket_utils.hpp"
#include "packet.hpp"

#include <chrono>
#include <cstring>
#include <iostream>
#include <map>
#include <vector>
#include <netinet/in.h>

int main()
{
    std::vector<Interface> interfaces;
    std::map<Network, Route> routing_table;

    read_interfaces(interfaces);
    initialize_routes(routing_table, interfaces);

    int sock = create_socket();
    enable_broadcast(sock);
    bind_socket(sock);

    auto last_broadcast = std::chrono::steady_clock::now();

    while (true)
    {
        uint8_t buf[9];
        sockaddr_in sender;
        std::memset(&sender, 0, sizeof(sender));

        if (receive_packet(sock, buf, sender))
        {
            handle_packet(buf, sender, interfaces, routing_table);
        }

        auto now = std::chrono::steady_clock::now();
        auto diff_seconds = std::chrono::duration_cast<std::chrono::seconds>(now - last_broadcast).count();

        if (diff_seconds >= BROADCAST_INTERVAL)
        {
            send_vector(sock, interfaces, routing_table);
            print_table(routing_table);
            clean_table(routing_table);
            last_broadcast = now;
        }
    }

    return 0;
}
