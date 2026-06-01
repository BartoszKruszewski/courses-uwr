// Bartosz Kruszewski 337568

#include "network.hpp"
#include <arpa/inet.h>

bool Network::operator<(const Network &other) const
{
    if (addr < other.addr)
        return true;
    if (addr > other.addr)
        return false;
    return prefix < other.prefix;
}

std::string ip_u32_to_str(uint32_t ip)
{
    in_addr addr;
    addr.s_addr = htonl(ip);
    char buf[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &addr, buf, sizeof(buf));
    return std::string(buf);
}

uint32_t ip_str_to_u32(const std::string &ip)
{
    in_addr addr;
    inet_pton(AF_INET, ip.c_str(), &addr);
    return ntohl(addr.s_addr);
}

uint32_t make_mask(uint8_t prefix)
{
    if (prefix == 0)
        return 0;
    return 0xFFFFFFFF << (32 - prefix);
}
