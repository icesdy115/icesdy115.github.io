## CENTOS SSH配置
### 修改SSH登录端口号
1. 修改ssh配置文件
```
# vi /etc/ssh/sshd_config
>>> port 9922
# vi /etc/ssh/ssh_config
>>> prot 9922
```
2. 重启ssh服务
```
# service sshd restart
```
3. 使用ssh重新登录
```
# ssh username@IP -p prot
```

### SSH限制用户和IP登录
1. 修改ssh配置文件
```
# vi /etc/ssh/sshd_config
>>> allowusers xxx@114.80.100.159
```
1. 重启ssh服务
```
# service sshd restart
```

### 指定尝试密码次数
1. 修改ssh配置文件
```
# vi /etc/ssh/sshd_config
>>> MaxAuthTries  3  #可以允许做3次尝试
```
