```
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
hostname S2
enable secret 5 $1$mERr$cHiWNBwhSs.7ObyHmLl490
spanning-tree mode rapid-pvst
spanning-tree extend system-id
interface Port-channel3
 switchport mode trunk
 switchport nonegotiate
interface Port-channel4
 switchport mode trunk
 switchport nonegotiate
interface FastEthernet0/1
 switchport access vlan 3
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security mac-address sticky 0090.2B85.9B5D
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/2
 switchport access vlan 3
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security mac-address sticky 00E0.A3B5.958D
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/3
 switchport access vlan 4
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security mac-address sticky 0060.5C2B.7813
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/4
 switchport access vlan 4
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security mac-address sticky 0009.7C15.8764
 spanning-tree portfast
 spanning-tree bpduguard enable
interface FastEthernet0/5
 switchport mode trunk
 switchport nonegotiate
 channel-group 4 mode passive
interface FastEthernet0/6
 switchport mode trunk
 switchport nonegotiate
 channel-group 4 mode passive
interface FastEthernet0/7
 switchport mode trunk
 switchport nonegotiate
 channel-group 3 mode passive
interface FastEthernet0/8
 switchport mode trunk
 switchport nonegotiate
 channel-group 3 mode passive
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
 ip address 192.168.24.4 255.255.255.0
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
