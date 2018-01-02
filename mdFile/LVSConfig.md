## 操作系统：ubuntu server 15.04##

### LVS分配方式：
1.  IP隧道+rr（轮询）
1. IP隧道：director分配请求到不同的real server。
1. rr：将外部请求按顺序轮流分配到真实服务器。

### LVS安装

1. ipvsadm安装
```
	>sudo apt-get install ipvsadm
```
### LVS配置

1. touch ipvsadm.sh
```
#! /bin/bash
sudo ipvsadm -C
sudo ipvsadm -At 192.168.0.122:80 -s rr
sudo ipvsadm -at 192.168.0.122:80 -r 124.248.34.28:8088 -i
sudo ipvsadm -at 192.168.0.122:80 -r 124.248.34.24:8088 -i
```

1. chmod +x ipvsadm.sh
1. ./ipvsadm.sh

#### LVS查看
1. sudo ipvsadm -L -c
1. sudo ipvsadm -L --stats
