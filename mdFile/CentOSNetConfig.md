## CentOS网络配置

### 安装时配置
> 可以在安装系统时，在配置界面配置网络，配置完成后在/etc/sysconfig/net-scripts目录中生成配置文件

### 安装后配置
> 系统安装完成后/etc/sysconfig/net-scripts目录下会生成默认的网络配置文件

1. 修改配置文件/etc/sysconfig/net-scripts/ifcfg-enp0s3
```
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static  #默认为DHCP，修改为static
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
NAME=enp0s3
UUID=df146854-5a43-4ad6-9533-f8ee8aac72a8
DEVICE=enp0s3  #网卡名称
ONBOOT=yes   #默认为NO，修改为yes
IPADDR=192.168.202.251  #IP地址
GATEWAY=192.168.202.1   #网关
DNS1=114.114.114.114    #DNS
```
2. 重启网络
```
# service network restart
```

### 其他
1. CentOS Mini版本安装后默认没有```ifconfig | netstat```等网络命令，如需查看IP可使用```ip a```命令
1. 安装网络命令工具包
```
# yum install net-tools
```
1. 关闭网卡 ```ifdown```
1. 启动网卡 ```ifup```
