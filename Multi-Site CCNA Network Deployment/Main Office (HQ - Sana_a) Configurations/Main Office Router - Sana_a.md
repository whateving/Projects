```
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
hostname OFR
enable secret 5 $1$mERr$cHiWNBwhSs.7ObyHmLl490
ip cef
no ipv6 cef
username R2 password 7 0822455D0A16
spanning-tree mode pvst
interface FastEthernet0/0
 ip address 192.168.6.2 255.255.255.0
 ip ospf 1 area 0
 ip nat inside
 duplex auto
 speed auto
interface FastEthernet0/1
 ip address 192.168.5.2 255.255.255.0
 ip ospf 1 area 0
 ip nat inside
 duplex auto
 speed auto
interface Serial0/0/0
 no ip address
 encapsulation frame-relay
interface Serial0/0/0.102 point-to-point
 ip address 192.168.12.1 255.255.255.0
 frame-relay interface-dlci 102
 ip ospf 1 area 0
 ip nat inside
 clock rate 2000000
interface Serial0/0/0.103 point-to-point
 ip address 192.168.13.1 255.255.255.0
 frame-relay interface-dlci 103
 ip ospf 1 area 0
 ip nat inside
 clock rate 2000000
interface Serial0/0/1
 ip address 192.168.14.1 255.255.255.0
 encapsulation ppp
 ppp authentication chap
 ip ospf 1 area 0
 ip nat inside
 clock rate 2000000
interface Ethernet0/1/0
 ip address dhcp
 ip access-group INTERNET_CONNECTION_ACL out
 ip nat outside
 duplex auto
 speed auto
interface Vlan1
 no ip address
 shutdown
router ospf 1
 router-id 10.10.10.10
 log-adjacency-changes
 default-information originate
ip nat inside source list NAT-ACL interface Ethernet0/1/0 overload
ip nat inside source static tcp 192.168.7.102 80 100.1.1.2 80 
ip classless
ip route 0.0.0.0 0.0.0.0 100.1.1.254 
ip flow-export version 9
ip access-list standard remote_in_perm
 permit 192.168.20.0 0.0.0.255
ip access-list standard NAT-ACL
 permit 192.168.0.0 0.0.255.255
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
