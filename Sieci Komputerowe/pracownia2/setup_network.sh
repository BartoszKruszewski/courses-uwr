#!/bin/bash

set -e

NAMESPACES=(v1 v2 v3 v4)

echo "[*] Deleting old namespaces (if they exist)..."
for NS in "${NAMESPACES[@]}"; do
    sudo ip netns del $NS 2>/dev/null || true
done

echo "[*] Creating namespaces..."
for NS in "${NAMESPACES[@]}"; do
    sudo ip netns add $NS
    sudo ip netns exec $NS ip link set lo up
done

echo "[*] Creating veth pairs for networks local0 to local3..."
sudo ip link add veth-loc0-v1 type veth peer name veth-loc0-v2
sudo ip link add veth-loc1-v2 type veth peer name veth-loc1-v3
sudo ip link add veth-loc2-v3 type veth peer name veth-loc2-v4
sudo ip link add veth-loc3-v4 type veth peer name veth-loc3-v1

echo "[*] Assigning veth interfaces to namespaces..."
sudo ip link set veth-loc0-v1 netns v1
sudo ip link set veth-loc0-v2 netns v2

sudo ip link set veth-loc1-v2 netns v2
sudo ip link set veth-loc1-v3 netns v3

sudo ip link set veth-loc2-v3 netns v3
sudo ip link set veth-loc2-v4 netns v4

sudo ip link set veth-loc3-v4 netns v4
sudo ip link set veth-loc3-v1 netns v1

echo "[*] Renaming interfaces inside namespaces..."
sudo ip netns exec v1 ip link set veth-loc0-v1 name veth-loc0
sudo ip netns exec v1 ip link set veth-loc3-v1 name veth-loc3

sudo ip netns exec v2 ip link set veth-loc0-v2 name veth-loc0
sudo ip netns exec v2 ip link set veth-loc1-v2 name veth-loc1

sudo ip netns exec v3 ip link set veth-loc1-v3 name veth-loc1
sudo ip netns exec v3 ip link set veth-loc2-v3 name veth-loc2

sudo ip netns exec v4 ip link set veth-loc2-v4 name veth-loc2
sudo ip netns exec v4 ip link set veth-loc3-v4 name veth-loc3

echo "[*] Assigning IP addresses..."
sudo ip netns exec v1 ip addr add 10.0.0.1/24 dev veth-loc0
sudo ip netns exec v1 ip addr add 10.0.3.2/24 dev veth-loc3

sudo ip netns exec v2 ip addr add 10.0.0.2/24 dev veth-loc0
sudo ip netns exec v2 ip addr add 10.0.1.1/24 dev veth-loc1

sudo ip netns exec v3 ip addr add 10.0.1.2/24 dev veth-loc1
sudo ip netns exec v3 ip addr add 10.0.2.1/24 dev veth-loc2

sudo ip netns exec v4 ip addr add 10.0.2.2/24 dev veth-loc2
sudo ip netns exec v4 ip addr add 10.0.3.1/24 dev veth-loc3

echo "[*] Enabling interfaces..."
sudo ip netns exec v1 ip link set veth-loc0 up
sudo ip netns exec v1 ip link set veth-loc3 up

sudo ip netns exec v2 ip link set veth-loc0 up
sudo ip netns exec v2 ip link set veth-loc1 up

sudo ip netns exec v3 ip link set veth-loc1 up
sudo ip netns exec v3 ip link set veth-loc2 up

sudo ip netns exec v4 ip link set veth-loc2 up
sudo ip netns exec v4 ip link set veth-loc3 up

echo "[✓] Network ready!"
echo
echo "You can now run the program in each namespace:"
echo "  sudo ip netns exec v1 ./router < conf_v1.txt"
echo "  sudo ip netns exec v2 ./router < conf_v2.txt"
echo "  sudo ip netns exec v3 ./router < conf_v3.txt"
echo "  sudo ip netns exec v4 ./router < conf_v4.txt"
