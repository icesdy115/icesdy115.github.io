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

#### Nginx反向代理设置
1. 创建反向代理配置文件
```
# vi /etc/nginx/conf.d/www.yuming.com.conf
    server
    {
        listen 80;
        server_name www.yuming.com;
        location / {
            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_pass #发布地址http://10.10.10.88:8087;
         }
         #配置Nginx日志
         access_log /dawei/nginxLogs/sejunzhi_access.log main;
    }
```
2. 修改Nginx配置文件
```
# vi /etc/nginx/nginx.conf
user  nginx;
worker_processes  8;
error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;
events {
    worker_connections  1024;
}
http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  /dawei/nginxLogs/access.log  main;
    sendfile        on;
    #tcp_nopush     on;
    keepalive_timeout  65;
    gzip  on;
    send_timeout 120;
    fastcgi_buffers 8 128k;
    client_max_body_size 500m;
    include /etc/nginx/conf.d/www.yuming.com.conf;  #导入域名配置文件名
}
```
3. 启动Nginx
```
# systemctl start nginx.service    #启动Nginx
# nginx -s reload    #重新加载Nginx
```
