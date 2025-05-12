sudo nano /etc/frr/daemons
sudo systemctl status frr
vtysh
virbian# show interface
virbian# show ip route
virbian# configure terminal
virbian(config)# router rip
virbian(config-router)# version 2
virbian(config-router)# network 192.168.1.0/24
virbian(config-router)# network 192.168.2.0/24
virbian# copy running-config startup-config
virbian(config-router)# exit
virbian(config)# exit
virbian# show running-config
virbian# show ip rip
ip route