# CentOS7更换国内阿里源

## 阿里云Linux安装镜像源地址：<http://mirrors.aliyun.com/>

## CentOS系统更换软件安装源

1. 服务器安装wget

  ```
  # yum -y install wget
  ```

2. 备份原镜像文件，以免出错后可以恢复

  ```
  # mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
  ```

3. 下载新的CentOS-Base.repo 到/etc/yum.repos.d/

  ```
  # wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
  ```

4. 运行yum makecache生成缓存

  ```
  # yum clean all
  # yum makecache
  # yum -y update
  ```
