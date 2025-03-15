#ifndef TRACEROUTE_H
#define TRACEROUTE_H

#include <iostream>
#include <vector>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <poll.h>
#include <unistd.h>
#include <random>

#define MAX_HOPS 30
#define PACKETS_PER_TTL 3
#define TIMEOUT 1000


struct HopInfo {
    std::string ip;
    double response_time;
};

unsigned short checksum(void *b, int len);
void send_packet(int sockfd, sockaddr_in &dest_addr, int seq, int id);
std::vector<HopInfo> receive_icmp_response(int sockfd, sockaddr_in &recv_addr, int expected_id);
bool is_own_packet(char *buffer, int expected_ttl);
void print_hop_info(int ttl, const std::vector<HopInfo> &responses);
void configure_socket_and_send_packets(int sockfd, sockaddr_in &dest_addr, int ttl, int id);

#endif // TRACEROUTE_H
