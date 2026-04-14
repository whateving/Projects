```
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
hostname S6
enable secret 5 $1$mERr$cHiWNBwhSs.7ObyHmLl490
spanning-tree mode rapid-pvst
spanning-tree extend system-id
interface FastEthernet0/1
switchport mode trunk
interface FastEthernet0/2
switchport access vlan 15
switchport mode access
switchport port-security
switchport port-security mac-address sticky
switchport port-security mac-address sticky 0006.2AD4.EB69
spanning-tree portfast
spanning-tree bpduguard enable
interface FastEthernet0/3
switchport access vlan 16
switchport mode access
switchport port-security
switchport port-security mac-address sticky
switchport port-security mac-address sticky 000B.BE8C.EA4E
spanning-tree portfast
spanning-tree bpduguard enable
interface FastEthernet0/4
interface FastEthernet0/5
interface FastEthernet0/6
interface FastEthernet0/7
interface FastEthernet0/8
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
interface Vlan23
ip address 192.168.23.1 255.255.255.0
ip default-gateway 192.168.23.254
ip access-list standard remote_in_perm
permit 192.168.20.0 0.0.0.255
line con 0
password 7 0822455D0A16
logging synchronous
login
history size 30
exec-timeout 0 0
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
