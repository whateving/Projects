```
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
hostname R1
enable secret 5 $1$mERr$cHiWNBwhSs.7ObyHmLl490
ip cef
no ipv6 cef
spanning-tree mode pvst
interface FastEthernet0/0
no ip address
duplex auto
speed auto
interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 192.168.10.254 255.255.255.0
ip helper-address 192.168.7.100
interface FastEthernet0/0.11
encapsulation dot1Q 11
ip address 192.168.11.254 255.255.255.0
ip helper-address 192.168.7.100
interface FastEthernet0/0.22
encapsulation dot1Q 22
ip address 192.168.22.254 255.255.255.0
interface FastEthernet0/1
no ip address
duplex auto
speed auto
shutdown
interface Serial0/0/0
no ip address
encapsulation frame-relay
interface Serial0/0/0.301 point-to-point
ip address 192.168.13.2 255.255.255.0
frame-relay interface-dlci 301
ip access-group ACL_to_Server_and_Internet out
clock rate 2000000
interface Serial0/0/1
no ip address
clock rate 2000000
shutdown
interface Vlan1
no ip address
shutdown
router ospf 1
router-id 5.5.5.5
log-adjacency-changes
network 192.168.13.0 0.0.0.255 area 0
network 192.168.10.0 0.0.0.255 area 3
network 192.168.11.0 0.0.0.255 area 3
network 192.168.22.0 0.0.0.255 area 3
ip classless
ip flow-export version 9
ip access-list standard remote_in_perm
permit 192.168.20.0 0.0.0.255
ip access-list extended ACL_to_Server_and_Internet
permit tcp any host 192.168.7.102 eq www
permit udp any host 192.168.7.101 eq domain
permit udp any host 192.168.7.100 eq bootps
permit tcp any host 200.1.1.1 eq www
permit icmp any any echo-reply
permit tcp 192.168.22.0 0.0.0.255 eq telnet 192.168.20.0 0.0.0.255
line con 0
history size 30
exec-timeout 0 0
password 7 0822455D0A16
logging synchronous
login
line aux 0
line vty 0 4
access-class remote_in_perm in
password 7 08224F4008
login
line vty 5 15
access-class remote_in_perm in
password 7 08224F4008
login
end

```
