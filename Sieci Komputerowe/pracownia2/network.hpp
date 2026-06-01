// Bartosz Kruszewski 337568

#pragma once
#include <cstdint>
#include <string>

struct Network
{
    uint32_t addr;
    uint8_t prefix;

    bool operator<(const Network &other) const;
};

std::string ip_u32_to_str(uint32_t ip);
uint32_t ip_str_to_u32(const std::string &ip);
uint32_t make_mask(uint8_t prefix);
