设置windows与Linux文件共享

windows文件共享给Linux

- 在windows机器上创建一个文件夹（gongxiang）并将其设置为共享文件夹

- 在linux机器上创建挂载目录/mnt/windows

# mkdir /mnt/windows
# mount -o username=administrator,password=123456 //192.168.1.101/gongxiang /mnt/windows

samba设置

- 安装samba

# yum install samba

- 配置samba
a. 设置开机启动

# chkconfig smb on
# chkconfig nmb on

- 新建smb用户用于访问Linux共享文件

# useradd smb      # 新建用户
# smbpasswd -a smb  # 修改密码

- samba配置文件/etc/samba/smb.conf

[tmp]
comment = Tmp Directories
path = /tmp                        # 共享的Linux目录
public = no                        # 目录不公开
writeable = yes                    # 可写
browseable = yes                    # 可读
valid users = smb                  # 访问用户，上面新建的，也可以使用原来已有的

- 关闭防火墙

# service firewalld stop

- 启动samba

# service samba start  # 启动
# systemctl restart smb.service # 重启
# systemctl restart nmb.service

- 修改SELinux的实时运行模式

# setenforce 0

- 查看samba链接状态

# smbstatus
