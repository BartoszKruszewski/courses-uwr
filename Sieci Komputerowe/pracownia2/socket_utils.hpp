// Bartosz Kruszewski 337568

#pragma once
#include <netinet/in.h>

int create_socket();
void enable_broadcast(int sock);
void bind_socket(int sock);
bool receive_packet(int sock, uint8_t *buf, sockaddr_in &sender);
