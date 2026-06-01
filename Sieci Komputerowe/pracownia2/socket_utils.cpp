// Bartosz Kruszewski 337568

#include "socket_utils.hpp"
#include <sys/socket.h>
#include <unistd.h>
#include <cstring>
#include <cstdio>

int create_socket()
{
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0)
        perror("socket");
    return sock;
}

void enable_broadcast(int sock)
{
    int broadcast = 1;
    setsockopt(sock, SOL_SOCKET, SO_BROADCAST, &broadcast, sizeof(broadcast));
}

void bind_socket(int sock)
{
    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(54321);
    addr.sin_addr.s_addr = htonl(INADDR_ANY);
    if (bind(sock, (sockaddr *)&addr, sizeof(addr)) < 0)
        perror("bind");
}

bool receive_packet(int sock, uint8_t *buf, sockaddr_in &sender)
{
    fd_set fds;
    FD_ZERO(&fds);
    FD_SET(sock, &fds);

    timeval tv{1, 0};
    if (select(sock + 1, &fds, NULL, NULL, &tv) > 0)
    {
        socklen_t len = sizeof(sender);
        return recvfrom(sock, buf, 9, 0, (sockaddr *)&sender, &len) == 9;
    }
    return false;
}
