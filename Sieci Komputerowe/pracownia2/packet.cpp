// Bartosz Kruszewski 337568

#include "packet.hpp"
#include <cstring>

PacketData parse_packet(uint8_t *buf, const sockaddr_in &sender)
{
    return {
        ntohl(*(uint32_t *)(buf)),
        buf[4],
        ntohl(*(uint32_t *)(buf + 5)),
        ntohl(sender.sin_addr.s_addr)};
}

uint32_t find_interface_cost(uint32_t src_ip, const std::vector<Interface> &interfaces)
{
    for (const auto &iface : interfaces)
    {
        uint32_t mask = make_mask(iface.prefix);
        if ((src_ip & mask) == iface.net)
            return iface.distance;
    }
    return INF_DISTANCE;
}

uint32_t calculate_total_cost(uint32_t hop_cost, uint32_t distance)
{
    uint64_t total = (uint64_t)hop_cost + distance;
    return total > INF_DISTANCE ? INF_DISTANCE : (uint32_t)total;
}

bool should_add_route(uint32_t distance, uint32_t src_ip)
{
    return !(distance == 0 && src_ip == 0);
}

void update_or_add_route(const PacketData &pd, uint32_t total_cost, std::map<Network, Route> &table)
{
    Network netk{pd.net, pd.prefix};
    auto it = table.find(netk);
    if (it == table.end())
    {
        if (should_add_route(pd.distance, pd.src_ip))
        {
            table[netk] = {total_cost, pd.src_ip, false, pd.distance == INF_DISTANCE ? 0 : -1};
        }
    }
    else
    {
        Route &rt = it->second;
        if (!rt.directly_connected && (rt.next_hop == pd.src_ip || rt.distance > total_cost))
        {
            rt.distance = total_cost;
            rt.next_hop = pd.src_ip;
            rt.unreachable_since = (pd.distance == INF_DISTANCE ? 0 : -1);
        }
    }
}

void handle_packet(uint8_t *buf, const sockaddr_in &sender, const std::vector<Interface> &interfaces, std::map<Network, Route> &table)
{
    PacketData pd = parse_packet(buf, sender);
    uint32_t hop_cost = find_interface_cost(pd.src_ip, interfaces);
    if (hop_cost == INF_DISTANCE)
        return;
    uint32_t total_cost = calculate_total_cost(hop_cost, pd.distance);
    update_or_add_route(pd, total_cost, table);
}
