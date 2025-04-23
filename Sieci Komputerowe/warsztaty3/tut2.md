sudo dhclient -v enp-rem4
sudo ip addr add 192.168.4.1/24 dev enp-rem4
ip route del default
sudo nano /etc/frr/daemons
sudo systemctl start frr
virbian(config-router)# version 2
virbian(config-router)# network 192.168.1.0/24
virbian(config-router)# network 192.168.2.0/24
virbian# copy running-config startup-config
virbian(config-router)# exit
virbian(config)# exit
