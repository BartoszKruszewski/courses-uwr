1. 
- sudo ip link set enp0s3 name enp-rem1
- sudo ip link set enp0s8 name enp-rem4
2. 
- sudo dhclient -v enp-rem1
- sudo dhclient -v enp-rem4
3.
- sudo ip addr add 192.168.1.1/24 dev enp-rem1
4.
- sudo ip route add default via 192.168.1.2