#include "traceroute.h"
#include <cstdlib>
#include <cerrno>
#include <netdb.h>
#include <sys/socket.h>
#include <unistd.h>
#include <algorithm>


int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cerr << "Use: " << argv[0] << " <IP_adress>" << std::endl;
        return EXIT_FAILURE;
    }
    
    sockaddr_in dest_addr{};
    dest_addr.sin_family = AF_INET;
    if (inet_pton(AF_INET, argv[1], &dest_addr.sin_addr) != 1) {
        std::cerr << "Bad IP_adress input!" << std::endl;
        return EXIT_FAILURE;
    }
    
    int sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sockfd < 0) {
        perror("socket");
        return EXIT_FAILURE;
    }
    
    sockaddr_in recv_addr{};
    std::string target_ip = inet_ntoa(dest_addr.sin_addr);
    int process_id = getpid() % 65536;
    
    for (int ttl = 1; ttl <= MAX_HOPS; ttl++) {
        configure_socket_and_send_packets(sockfd, dest_addr, ttl, process_id);
        std::vector<HopInfo> responses = receive_icmp_response(sockfd, recv_addr, process_id);
        print_hop_info(ttl, responses);
        if (!responses.empty() && std::find_if(responses.begin(), responses.end(), 
            [&](const HopInfo &resp) { return resp.ip == target_ip; }) != responses.end()) {
            break;
        }
    }
    
    close(sockfd);
    return EXIT_SUCCESS;
}
