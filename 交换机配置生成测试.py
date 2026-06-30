
座位号 = 6

学号 = 20255240206



行政楼核心交换机 = f"""!
version 12.2
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname SW_CORE
!
!
!
!
!
ip routing
!
!
!
!
!
!
!
!
!
!
spanning-tree mode pvst
!
!
!
!
interface FastEthernet0/1
 no switchport
 ip address 10.1.0.2 255.255.255.0
 ip access-group 101 in
 duplex auto
 speed auto
!
interface FastEthernet0/2
 no switchport
 ip address 10.1.2.1 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/3
 no switchport
 ip address 10.1.3.1 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/4
!
interface FastEthernet0/5
!
interface FastEthernet0/6
!
interface FastEthernet0/7
!
interface FastEthernet0/8
!
interface FastEthernet0/9
!
interface FastEthernet0/10
!
interface FastEthernet0/11
!
interface FastEthernet0/12
!
interface FastEthernet0/13
!
interface FastEthernet0/14
!
interface FastEthernet0/15
!
interface FastEthernet0/16
!
interface FastEthernet0/17
!
interface FastEthernet0/18
!
interface FastEthernet0/19
!
interface FastEthernet0/20
!
interface FastEthernet0/21
!
interface FastEthernet0/22
!
interface FastEthernet0/23
 no switchport
 ip address 10.1.5.1 255.255.255.0
 ip access-group 100 in
 duplex auto
 speed auto
!
interface FastEthernet0/24
!
interface GigabitEthernet0/1
 channel-group 6 mode on
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface GigabitEthernet0/2
 channel-group 6 mode on
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Port-channel 6
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan90
 ip address 172.{座位号}.90.254 255.255.255.0
!
router ospf 1
 log-adjacency-changes
 network 10.1.0.0 0.0.0.255 area 0
 network 10.1.5.0 0.0.0.255 area 0
 network 10.1.2.0 0.0.0.255 area 0
 network 10.1.3.0 0.0.0.255 area 0
 network 172.{座位号}.90.0 0.0.0.255 area 0
!
ip classless
!
!
access-list 100 deny tcp 172.{座位号}.70.0 0.0.0.255 host 172.{座位号}.90.2 eq ftp
access-list 100 permit ip any any
access-list 101 deny ip 172.{座位号}.80.0 0.0.0.255 172.{座位号}.90.0 0.0.0.255
access-list 101 deny ip 172.{座位号}.80.0 0.0.0.255 172.{座位号}.70.0 0.0.0.255
access-list 101 permit ip any any
!
!
!
!
!
line con 0
!
line aux 0
!
line vty 0 4
 login
!
!
!
end

"""

教学大楼核心交换机 = f"""!
version 12.2
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname SW-JXL
!
!
!
!
!
ip routing
!
!
!
!
!
!
!
!
!
!
spanning-tree mode pvst
!
!
!
!
interface FastEthernet0/1
 no switchport
 ip address 10.1.4.1 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/2
 no switchport
 ip address 10.1.2.2 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/3
!
interface FastEthernet0/4
!
interface FastEthernet0/5
!
interface FastEthernet0/6
!
interface FastEthernet0/7
!
interface FastEthernet0/8
!
interface FastEthernet0/9
!
interface FastEthernet0/10
!
interface FastEthernet0/11
!
interface FastEthernet0/12
!
interface FastEthernet0/13
!
interface FastEthernet0/14
!
interface FastEthernet0/15
!
interface FastEthernet0/16
!
interface FastEthernet0/17
!
interface FastEthernet0/18
!
interface FastEthernet0/19
!
interface FastEthernet0/20
!
interface FastEthernet0/21
!
interface FastEthernet0/22
!
interface FastEthernet0/23
!
interface FastEthernet0/24
 switchport access vlan 10
 switchport mode access
!
interface GigabitEthernet0/1
!
interface GigabitEthernet0/2
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan10
 ip address 172.{座位号}.10.1 255.255.255.0
!
interface Vlan20
 ip address 172.{座位号}.20.254 255.255.255.0
!
interface Vlan30
 ip address 172.{座位号}.30.254 255.255.255.0
!
router ospf 1
 log-adjacency-changes
 network 10.1.2.0 0.0.0.255 area 0
 network 10.1.4.0 0.0.0.255 area 0
 network 172.{座位号}.10.0 0.0.0.255 area 0
 network 172.{座位号}.20.0 0.0.0.255 area 0
 network 172.{座位号}.30.0 0.0.0.255 area 0
!
ip classless
!
!
!
!
!
!
!
line con 0
!
line aux 0
!
line vty 0 4
 login
!
!
!
end

"""

实验大楼核心交换机 = f"""!
version 12.2
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname SW-SYL
!
!
!
!
!
ip routing
!
!
!
!
!
!
!
!
!
!
spanning-tree mode pvst
!
!
!
!
interface FastEthernet0/1
 no switchport
 ip address 10.1.4.2 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/2
 no switchport
 no ip address
 duplex auto
 speed auto
!
interface FastEthernet0/3
 no switchport
 ip address 10.1.3.2 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/4
!
interface FastEthernet0/5
!
interface FastEthernet0/6
!
interface FastEthernet0/7
!
interface FastEthernet0/8
!
interface FastEthernet0/9
!
interface FastEthernet0/10
!
interface FastEthernet0/11
!
interface FastEthernet0/12
!
interface FastEthernet0/13
!
interface FastEthernet0/14
!
interface FastEthernet0/15
!
interface FastEthernet0/16
!
interface FastEthernet0/17
!
interface FastEthernet0/18
!
interface FastEthernet0/19
!
interface FastEthernet0/20
!
interface FastEthernet0/21
!
interface FastEthernet0/22
!
interface FastEthernet0/23
!
interface FastEthernet0/24
 switchport access vlan 40
!
interface GigabitEthernet0/1
!
interface GigabitEthernet0/2
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan40
 ip address 172.{座位号}.40.254 255.255.255.0
!
interface Vlan50
 ip address 172.{座位号}.50.254 255.255.255.0
!
interface Vlan60
 ip address 172.{座位号}.60.254 255.255.255.0
!
router ospf 1
 log-adjacency-changes
 network 10.1.3.0 0.0.0.255 area 0
 network 10.1.4.0 0.0.0.255 area 0
 network 172.{座位号}.40.0 0.0.0.255 area 0
 network 172.{座位号}.50.0 0.0.0.255 area 0
 network 172.{座位号}.60.0 0.0.0.255 area 0
!
ip classless
!
!
!
!
!
!
!
line con 0
!
line aux 0
!
line vty 0 4
 login
!
!
!
end

"""

学生公寓核心交换机 = f"""!
version 12.2
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname Switch
!
!
!
!
!
ip routing
!
!
!
!
!
!
!
!
!
!
spanning-tree mode pvst
!
!
!
!
interface FastEthernet0/1
 switchport access vlan 70
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface FastEthernet0/2
!
interface FastEthernet0/3
!
interface FastEthernet0/4
!
interface FastEthernet0/5
!
interface FastEthernet0/6
!
interface FastEthernet0/7
!
interface FastEthernet0/8
!
interface FastEthernet0/9
!
interface FastEthernet0/10
!
interface FastEthernet0/11
!
interface FastEthernet0/12
!
interface FastEthernet0/13
!
interface FastEthernet0/14
!
interface FastEthernet0/15
!
interface FastEthernet0/16
!
interface FastEthernet0/17
!
interface FastEthernet0/18
!
interface FastEthernet0/19
!
interface FastEthernet0/20
!
interface FastEthernet0/21
!
interface FastEthernet0/22
!
interface FastEthernet0/23
 no switchport
 ip address 10.1.5.2 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/24
!
interface GigabitEthernet0/1
!
interface GigabitEthernet0/2
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan70
 ip address 172.{座位号}.70.254 255.255.255.0
!
router ospf 1
 log-adjacency-changes
 network 172.{座位号}.70.0 0.0.0.255 area 0
 network 10.1.5.0 0.0.0.255 area 0
!
ip classless
!
!
!
!
!
!
!
line con 0
!
line aux 0
!
line vty 0 4
 login
!
!
!
end

"""

校分部核心交换机 = f"""!
version 12.2
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname SW-XFB
!
!
!
!
!
ip routing
!
!
!
!
!
!
!
!
!
!
spanning-tree mode pvst
!
!
!
!
interface FastEthernet0/1
 no switchport
 ip address 10.1.6.2 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/2
 no switchport
 ip address 172.{座位号}.80.254 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/3
 no switchport
 ip address 172.{座位号}.81.254 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/4
!
interface FastEthernet0/5
!
interface FastEthernet0/6
!
interface FastEthernet0/7
!
interface FastEthernet0/8
!
interface FastEthernet0/9
!
interface FastEthernet0/10
!
interface FastEthernet0/11
!
interface FastEthernet0/12
!
interface FastEthernet0/13
!
interface FastEthernet0/14
!
interface FastEthernet0/15
!
interface FastEthernet0/16
!
interface FastEthernet0/17
!
interface FastEthernet0/18
!
interface FastEthernet0/19
!
interface FastEthernet0/20
!
interface FastEthernet0/21
!
interface FastEthernet0/22
!
interface FastEthernet0/23
!
interface FastEthernet0/24
!
interface GigabitEthernet0/1
!
interface GigabitEthernet0/2
!
interface Vlan1
 no ip address
 shutdown
!
router ospf 1
 log-adjacency-changes
 network 10.1.6.0 0.0.0.255 area 1
 network 172.{座位号}.80.0 0.0.0.255 area 1
 network 172.{座位号}.81.0 0.0.0.255 area 1
!
ip classless
!
!
!
!
!
!
!
line con 0
!
line aux 0
!
line vty 0 4
 login
!
!
!
end

"""

校本部边界路由器 = f"""!
version 12.4
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname RT-XBB
!
!
!
enable password cisco
!
!
!
!
!
!
username RT-XFB password 0 123456
!
!
!
!
!
!
!
spanning-tree mode pvst
!
!
!
!
interface FastEthernet0/0
 ip address 10.1.0.1 255.255.255.0
 ip nat inside
 duplex auto
 speed auto
!
interface FastEthernet0/1
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface Serial0/0/0
 ip address 10.1.1.1 255.255.255.0
 encapsulation ppp
 ppp authentication pap
 ip nat outside
 clock rate 128000
!
interface Serial0/0/1
 ip address 202.168.100.2 255.255.255.0
 ip nat outside
!
interface FastEthernet1/0
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
router ospf 1
 log-adjacency-changes
 redistribute static subnets 
 redistribute connected subnets 
 network 10.1.0.0 0.0.0.255 area 0
 network 10.1.1.0 0.0.0.255 area 1
 default-information originate
!
ip nat inside source static 172.{座位号}.90.3 202.168.100.200 
ip classless
ip route 0.0.0.0 0.0.0.0 Serial0/0/1 
!
!
!
!
!
!
!
line con 0
!
line aux 0
!
line vty 0 4
 password {学号}
 login
line vty 5 15
 password {学号}
 login
!
!
!
end

"""

校分部边界路由器 = f"""!
version 12.4
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname RT-XFB
!
!
!
!
!
!
!
!
!
!
!
!
!
!
spanning-tree mode pvst
!
!
!
!
interface FastEthernet0/0
 ip address 10.1.6.1 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/1
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface Serial0/0/0
 ip address 10.1.1.2 255.255.255.0
 encapsulation ppp
 ppp pap sent-username RT-XFB password 0 123456
!
interface Serial0/0/1
 no ip address
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
router ospf 1
 log-adjacency-changes
 network 10.1.1.0 0.0.0.255 area 1
 network 10.1.6.0 0.0.0.255 area 1
!
ip classless
!
!
!
no cdp run
!
!
!
!
!
line con 0
!
line aux 0
!
!
!
!
end

"""




config_data = 行政楼核心交换机
f = open(f"./DATA/OUT/{座位号}行政楼核心交换机.txt", 'w')
f.write(config_data)
f.close()

config_data = 教学大楼核心交换机
f = open(f"./DATA/OUT/{座位号}教学大楼核心交换机.txt", 'w')
f.write(config_data)
f.close()

config_data = 实验大楼核心交换机
f = open(f"./DATA/OUT/{座位号}实验大楼核心交换机.txt", 'w')
f.write(config_data)
f.close()

line vty 0 4
 login
config_data = 学生公寓核心交换机
f = open(f"./DATA/OUT/{座位号}学生公寓核心交换机.txt", 'w')
f.write(config_data)
f.close()

config_data = 校分部核心交换机
f = open(f"./DATA/OUT/{座位号}校分部核心交换机.txt", 'w')
f.write(config_data)
f.close()

config_data = 校本部边界路由器
f = open(f"./DATA/OUT/{座位号}校本部边界路由器.txt", 'w')
f.write(config_data)
f.close()

config_data = 校分部边界路由器
f = open(f"./DATA/OUT/{座位号}校分部边界路由器.txt", 'w')
f.write(config_data)
f.close()