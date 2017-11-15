CENTOS SSH端口修改
##CENTOS SSH端口修改
1. 修改ssh配置文件
```bash
# vi /etc/ssh/sshd_config
>>> port 9922
# vi /etc/ssh/ssh_config
>>> prot 9922
```
2. 重启ssh服务
```bash
# service sshd restart
```
3. 使用ssh重新登录
```bash# ssh username@IP -p prot
```
