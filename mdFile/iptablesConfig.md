## CentOS防火墙iptables基本配置
### iptables安装&配置
- 关闭CentOS自带防火墙firewalld
```
# service firewalld stop
# chkconfig firewalld off
```
- 安装iptables,安装后在/etc/sysconfig目录下会生成iptables文件
```
# yum install iptables-services
```
- iptables配置
```
*filter
:INPUT DROP [0:0]  #禁止所有进入数据
:FORWARD DROP [0:0]  #禁止所有转发数据
:OUTPUT ACCEPT [0:0]
#本地圆环地址就是那个127.0.0.1，是本机上使用的,它进与出都设置为允许
-A INPUT -i lo -j ACCEPT
#只允许源地址192.168.202.121的22端口访问
-A INPUT -s 192.168.202.121 -p tcp --dport 22 -j ACCEPT
COMMIT
```
- 重启iptables
```
# systemctl restart iptables
```

- 设置iptables开机启动
```
# systemctl enable iptables
```

### iptables命令
- 清空当前的所有规则和计数
```
# iptables -F      #清空所有的防火墙规则
# iptables -X      #删除用户自定义的空链
# iptables -Z      #清空计数
```
- 查看iptables规则
```
# iptables -L -n
```