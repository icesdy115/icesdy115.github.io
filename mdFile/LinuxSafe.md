# Linux安全加固
![安全加固项目](./LinuxSafe.jpg)

### 用户帐号
1. 口令生存期
```
[root@wangxu ~]# vim  /etc/login.defs
PASS_MAX_DAYS       90              # 用户的密码不过期最多的天数
PASS_MIN_DAYS       10              # 密码修改之间最小的天数
PASS_WARN_AGE      7                # 口令失效前多少天开始通知用户修改密码
```
2. 口令复杂度
```
[root@wangxu ~]# vim  /etc/pam.d/system-auth,在文件中找到如下内容:
password requisite  pam_cracklib.so 将其修改为:
password requisite  pam_cracklib.so try_first_pass retry=3 dcredit=-1 lcredit=-1 ucredit=-1 ocredit=-1 minlen=8       
# 至少包含一个数字.一个小写字母.一个大写字母.一个特殊字符.且密码长度>=8
```
3. 版本信息
```
[root@wangxu ~]# cat /etc/system-release
CentOS release 6.8 (Final)
```
4. 限制某用户登陆
```
[root@wangxu ~]#vim  /etc/hosts.deny 对配置文件进行修改
添加内容：
#禁止192.168.0.254用户对服务器进行ssh的登陆
sshd : 192.168.0.254  
```
或者用防火墙策略：
```
iptables -I INPUT -s 61.37.81.1 -j DROP
# 61.37.81.1的包全部屏蔽
iptables -I INPUT -s 61.37.81.0/24 -j DROP
# 61.37.81.1到61.37.81.255的访问全部屏蔽
iptables -I INPUT -s 192.168.1.202 -p tcp --dport 80 -j DROP
# 192.168.1.202的80端口的访问全部屏蔽
iptables -I INPUT -s 192.168.1.0/24 -p tcp --dport 80 -j DROP
# 192.168.1.1~192.168.1.1255的80端口的访问全部屏蔽
```
5. 检查是否有除root用户以外UID为0的用户
```
[root@wangxu ~]#  awk -F “：” '($3==0)  {print  $1} ' /etc/passwd
# 操作系统Linux超级用户策略安全基线要求项目，要求除roo外不能有UID为0的用户。
```
6. 登录超时限制
```
[root@wangxu ~]# cp -p /etc/profile /etc/profile_bak
[root@wangxu ~]# vi /etc/profile
TMOUT=300                                 
export TMOUT
```
7. 检查是否使用PAM认证模块禁止wheel组之外的用户su为root
```
[root@wangxu ~]# #vim /etc/pam.d/su       # 新添加以下两行
auth            sufficient      pam_rootok.so
auth            required        pam_wheel.so use_uid
```

### 协议安全
1. 限制root用户远程登录SSH
```
[root@wangxu ~]# grep -v "[[:space:]]*#" /etc/ssh/sshd_config  |grep "PermitRootLogin no"
PermitRootLogin no
protocol   2
```
2. 使用SSH协议进程远程登陆
```
[root@wangxu ~]# cp -p /etc/xinetd.d/telnet /etc/xinetd.d/telnet_bak
[root@wangxu ~]# vi /etc/xinetd.d/telnet   # 把disable项改为yes,即disable = yes.
[root@wangxu ~]# service xinetd restart
```
>使用Telnet这个用来访问远程计算机的TCP/IP协议以控制你的网络设备，相当于在离开某个建筑时大喊你的用户名和口令。很快会有人进行监听，并且他们会利用你安全意识的缺乏。传统的网络服务程序如：ftp、pop和telnet在本质上都是不安全的，因为它们在网络上用明文传送口令和数据，别有用心的人非常容易就可以截获这些口令和数据。SSH是替代Telnet和其他远程控制台管理应用程序的行业标准。SSH命令是加密的并以几种方式进行保密。 在使用SSH的时候，一个数字证书将认证客户端（你的工作站）和服务器（你的网络设备）之间的连接，并加密受保护的口令。

3. 禁止root用户登陆FTP
```
[root@wangxu ~]# cat /etc/pam.d/vsftpd
auth       required     pam_listfile.so item=user sense=deny file=/etc/vsftpd/ftpusers onerr=succeed
# 其中file=/etc/vsftpd/ftpusers即为当前系统上的ftpusers文件.
[root@wangxu ~]#echo "root" >> /etc/vsftpd/ftpusers
daemon
bin
sys
lp
uucp
nuucp
listen
nobody
noaccess
nobody4
root
```
4. 禁止匿名FTP
```
[root@wangxu ~]# vim  /etc/vsftpd/vsftpd.conf
anonymous_enable=NO    # 如果存在anonymous_enable则修改,如果不存在则手动增加
```
5. 预防Flood攻击
```
[root@wangxu ~]# vim  /etc/sysctl.conf
[root@wangxu ~]# net.ipv4.tcp_syncookies = 1
[root@wangxu ~]# sysctl  -p  //让命令生效
```

### 认证权限
1. 文件与目录缺省权限控制
```
[root@wangxu ~]# cp /etc/profile /etc/profile.bak
[root@wangxu ~]# vim /etc/profile
umask 027
[root@wangxu ~]# source /etc/profile
```
2. 配置用户最小权限
```
[root@wangxu ~]# chmod 644 /etc/passwd
[root@wangxu ~]# chmod 400 /etc/shadow
[root@wangxu ~]# chmod 644 /etc/group
```

### 日志审计
>什么是日志？简单地说，日志就是计算机系统、设备、软件等在某种情况下记录的信息。具体的内容取决于日志的来源。例如，Linux操作系统会记录用户登录和注销的消息，防火墙将记录ACL通过和拒绝的消息，磁盘存储系统在故障发生或者在某些系统认为将会发生故障的情况下生成日志信息。日志中有大量信息，这些信息告诉你为什么需要生成日志，系统已经发生了什么。

>例如，Web服务器一般会在有人访问Web页面请求资源（图片、文件等等）的时候记录日志。如果用户访问的页面需要通过认证，日志消息将会包含用户名。这就是日志数据的一个例子：可以使用用户名来判断谁访问过一个资源。通过日志，IT管理人员可以了解系统的运行状况，安全状况，甚至是运营的状况。

1. 启用远程日志功能
```
[root@wangxu ~]# vim /etc/rsyslog.conf
###增加如下内容:
*.*    @Syslog日志服务器IP     ###注意：*和@之间存在的是tab键，非空格。
```
>Linux上通常可以通过rsyslog来实现系统日志的集中管理，这种情况下通常会有一个日志服务器，然后每个机器配置自己日志通过rsyslog来写到远程的日志服务器上。
rsyslog是一个开源工具，被广泛用于Linux系统以通过TCP/UDP协议转发或接收日志消息。rsyslog守护进程可以被配置成两种环境，一种是配置成日志收集服务器，rsyslog进程可以从网络中收集其它主机上的日志数据，这些主机会将日志配置为发送到另外的远程服务器。rsyslog的另外一个用法，就是可以配置为客户端，用来过滤和发送内部日志消息到本地文件夹（如/var/log）或一台可以路由到的远程rsyslog服务器上。
假定你的网络中已经有一台已经配置好并启动的rsyslog服务器，本指南将为你展示如何来设置CentOS系统将其内部日志消息路由到一台远程rsyslog服务器上。这将大大改善你的系统磁盘空间的使用，尤其是当你还没有一个用于/var目录的独立的大分区。

2. 检查是否记录安全事件日志
```
[root@wangxu ~]# vim  /etc/syslog.conf 或者 /etc/rsyslog.conf
# 在文件中加入如下内容:*.err;kern.debug;daemon.notice     /var/log/messages
[root@wangxu ~]# chmod 640 /var/log/messages
[root@wangxu ~]# service rsyslog restart
```
