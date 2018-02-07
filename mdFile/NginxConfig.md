### Nginx安装配置
#### CentOS安装Nginx
1. 使用root权限用户登录服务器
2. 配置nginx安装源
```
# rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
```
3. 安装nginx
```
# yum install nginx
```
#### Nginx配置发布静态页面
1. 将静态页面放到服务器上
2. 打开Nginx配置文件
```
# vi /etc/nginx/nginx.conf
```
3. 在http节点中加入如下配置
```
server {
    #listen       80;
    server_name  #IP地址或域名;
    root #静态文件放置路径：/home/test/;
    index #首页显示的静态页面：upgradPage.html;
    #access_log  logs/host.access.log  main;
    location / {
        #proxy_pass http://192.168.202.121:8081;
        #proxy_set_header Host $host;
        #proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      }
 }
```
