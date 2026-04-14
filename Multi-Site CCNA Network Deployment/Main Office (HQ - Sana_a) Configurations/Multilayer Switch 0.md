```
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
hostname MS0
enable secret 5 $1$mERr$cHiWNBwhSs.7ObyHmLl490
ip routing
spanning-tree mode rapid-pvst
spanning-tree vlan 2,7,20 priority 24576
spanning-tree vlan 3-4 priority 28672
interface Port-channel1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
interface Port-channel2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
interface Port-channel3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
interface Port-channel4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
interface Port-channel5
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
interface Port-channel10
 switchport trunk encapsulation dot1q
 switchport mode trunk
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 channel-group 1 mode active
interface FastEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 channel-group 1 mode active
interface FastEthernet0/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 channel-group 2 mode active
interface FastEthernet0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 channel-group 2 mode active
interface FastEthernet0/5
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 channel-group 4 mode active
interface FastEthernet0/6
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 channel-group 4 mode active
interface FastEthernet0/7
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 channel-group 5 mode active
interface FastEthernet0/8
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 channel-group 5 mode active
interface FastEthernet0/9
 no switchport
 ip address 192.168.5.1 255.255.255.0
 ip access-group CON_TO_INTERNET out
 duplex auto
 speed auto
interface FastEthernet0/10
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 channel-group 3 mode active
interface FastEthernet0/11
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 channel-group 3 mode active
interface FastEthernet0/12
interface FastEthernet0/13
interface FastEthernet0/14
interface FastEthernet0/15
interface FastEthernet0/16
interface FastEthernet0/17
interface FastEthernet0/18
interface FastEthernet0/19
interface FastEthernet0/20
interface FastEthernet0/21
interface FastEthernet0/22
interface FastEthernet0/23
interface FastEthernet0/24
interface GigabitEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 channel-group 10 mode active
interface GigabitEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 channel-group 10 mode active
interface Vlan1
 no ip address
 shutdown
interface Vlan2
 mac-address 0090.0ca6.ed01
 ip address 192.168.2.1 255.255.255.0
 ip helper-address 192.168.7.100
interface Vlan3
 mac-address 0090.0ca6.ed02
 ip address 192.168.3.1 255.255.255.0
 ip helper-address 192.168.7.100
interface Vlan4
 mac-address 0090.0ca6.ed03
 ip address 192.168.4.1 255.255.255.0
 ip helper-address 192.168.7.100
interface Vlan7
 mac-address 0090.0ca6.ed04
 ip address 192.168.7.1 255.255.255.0
 ip access-group SERVERS_ACL out
interface Vlan20
 mac-address 0090.0ca6.ed05
 ip address 192.168.20.1 255.255.255.0
 ip helper-address 192.168.7.100
interface Vlan24
 mac-address 0090.0ca6.ed06
 ip address 192.168.24.254 255.255.255.0
 ip access-group L2_Management out
router ospf 1
 router-id 2.2.2.2
 log-adjacency-changes
 network 192.168.20.0 0.0.0.255 area 0
 network 192.168.2.0 0.0.0.255 area 0
 network 192.168.7.0 0.0.0.255 area 0
 network 192.168.4.0 0.0.0.255 area 0
 network 192.168.3.0 0.0.0.255 area 0
 network 192.168.5.0 0.0.0.255 area 0
 network 192.168.24.0 0.0.0.255 area 0
ip classless
ip flow-export version 9
ip access-list extended SERVERS_ACL
 permit tcp any host 192.168.7.102 eq www
 permit udp any host 192.168.7.101 eq domain
 permit udp any host 192.168.7.100 eq bootps
 permit icmp 192.168.20.0 0.0.0.255 192.168.7.0 0.0.0.255 echo
ip access-list standard remote_in_perm
 permit 192.168.20.0 0.0.0.255
ip access-list extended CON_TO_INTERNET
 permit tcp 192.168.20.0 0.0.0.255 200.1.1.0 0.0.0.3 eq www
 permit icmp 192.168.20.0 0.0.0.255 any echo
 permit tcp any host 200.1.1.1 eq www
 permit tcp host 192.168.7.102 eq www any
 permit udp host 192.168.7.101 eq domain any
 permit udp host 192.168.7.100 eq bootps any
 permit tcp 192.168.20.0 0.0.0.255 any eq telnet
ip access-list extended L2_Management
 permit icmp 192.168.20.0 0.0.0.255 192.168.24.0 0.0.0.255 echo
 permit tcp 192.168.20.0 0.0.0.255 192.168.24.0 0.0.0.255 eq telnet
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
