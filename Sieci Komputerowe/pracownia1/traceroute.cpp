#include "traceroute.h"
#include <cstring>
#include <cstdlib>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <sys/time.h>


unsigned short checksum(void *b, int len) {
    unsigned short *buf = reinterpret_cast<unsigned short *>(b);
    unsigned int sum = 0;
    for (; len > 0; len -= 2) sum += *buf++;
    sum = (sum >> 16) + (sum & 0xFFFF);
    return ~sum;
}

void send_packet(int sockfd, sockaddr_in &dest_addr, int seq, int id) {
    icmp packet{};
    packet.icmp_type = ICMP_ECHO;
    packet.icmp_code = 0;
    packet.icmp_id = id;
    packet.icmp_seq = seq;
    packet.icmp_cksum = checksum(&packet, sizeof(packet));
    sendto(sockfd, &packet, sizeof(packet), 0, (sockaddr *)&dest_addr, sizeof(dest_addr));
}

bool is_own_packet(char *buffer, int expected_id) {
    struct ip *ip_header = (struct ip*)(buffer);
    struct icmp *icmp_header = (struct icmp*)(buffer + (ip_header->ip_hl * 4));
    struct ip *original_icmp_header = (struct ip*)(buffer + (ip_header->ip_hl * 4) + sizeof(icmp));

    int recv_type = (int)icmp_header->icmp_type;
    int recv_id = recv_type == ICMP_ECHOREPLY ? icmp_header->icmp_id 
                : recv_type == ICMP_TIMXCEED ? original_icmp_header->ip_id
                : -1;

    return recv_id == expected_id;
}

std::vector<HopInfo> receive_icmp_response(int sockfd, sockaddr_in &recv_addr, int expected_id) {
    char buffer[512];
    socklen_t addr_len = sizeof(recv_addr);
    pollfd pfd = {sockfd, POLLIN, 0};
    std::vector<HopInfo> responses;
    struct timeval start, end;
    int bad_packets_number = 0;
    
    int i = 0;
    while (i++ < PACKETS_PER_TTL + bad_packets_number) {
        gettimeofday(&start, nullptr);
        if (poll(&pfd, 1, TIMEOUT) > 0) {
            if (recvfrom(sockfd, buffer, sizeof(buffer), 0, (sockaddr *)&recv_addr, &addr_len) > 0) {
                gettimeofday(&end, nullptr);
                double elapsed = (end.tv_sec - start.tv_sec) * 1000.0 + (end.tv_usec - start.tv_usec) / 1000.0;

                if (is_own_packet(buffer, expected_id)) {
                    responses.push_back({inet_ntoa(recv_addr.sin_addr), elapsed});
                }
                else {
                    bad_packets_number++;
                }
            }
        }
    }
    return responses;
}

void print_hop_info(int ttl, const std::vector<HopInfo> &responses) {
    std::cout << ttl << ". ";
    if (responses.empty()) {
        std::cout << "* ???";
    } else {
        std::vector<std::string> ips;
        double total_time = 0;
        for (const auto &hop : responses) {
            if (std::find(ips.begin(), ips.end(), hop.ip) == ips.end()) {
                ips.push_back(hop.ip);
            }
            total_time += hop.response_time;
        }
        for (const auto &ip : ips) std::cout << ip << " ";
        if (responses.size() == PACKETS_PER_TTL) {
            std::cout << "[" << total_time / responses.size() << " ms]";
        } else {
            std::cout << "???";
        }
    }
    std::cout << std::endl;
}

void configure_socket_and_send_packets(int sockfd, sockaddr_in &dest_addr, int ttl, int id) {
    setsockopt(sockfd, IPPROTO_IP, IP_TTL, &ttl, sizeof(ttl));
    for (int i = 0; i < PACKETS_PER_TTL; i++) {
        send_packet(sockfd, dest_addr, ttl * PACKETS_PER_TTL + i, id);
    }
}
