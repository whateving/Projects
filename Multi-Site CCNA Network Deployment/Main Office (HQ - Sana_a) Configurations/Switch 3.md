```
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
hostname S3
enable secret 5 $1$mERr$cHiWNBwhSs.7ObyHmLl490
spanning-tree mode rapid-pvst
spanning-tree extend system-id
interface Port-channel5
 switchport mode trunk
 switchport nonegotiate
interface Port-channel6
 switchport mode trunk
 switchport nonegotiate
interface FastEthernet0/1
 switchport access vlan 3
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security mac-address sticky 0010.117B.318A
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/2
 switchport access vlan 3
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security mac-address sticky 000B.BEE9.ED7A
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/3
 switchport access vlan 4
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security mac-address sticky 00D0.BCAD.0358
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/4
 switchport access vlan 4
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security mac-address sticky 0006.2AB6.AA2E
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/5
 switchport mode trunk
 switchport nonegotiate
 channel-group 5 mode passive
interface FastEthernet0/6
 switchport mode trunk
 switchport nonegotiate
 channel-group 5 mode passive
interface FastEthernet0/7
 switchport mode trunk
 switchport nonegotiate
 channel-group 6 mode passive
interface FastEthernet0/8
 switchport mode trunk
 switchport nonegotiate
 channel-group 6 mode passive
interface FastEthernet0/9
interface FastEthernet0/10
interface FastEthernet0/11
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
interface Vlan1
 no ip address
 shutdown
interface Vlan24
 ip address 192.168.24.5 255.255.255.0
ip default-gateway 192.168.24.253
line con 0
 password 7 0822455D0A16
 logging synchronous
 login
 history size 30
 exec-timeout 0 0
line vty 0 4
 password 7 08224F4008
 login
line vty 5 15
 password 7 08224F4008
 login
end

```
