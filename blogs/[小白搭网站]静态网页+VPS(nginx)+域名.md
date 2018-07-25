# 【小白搭网站】静态网页+VPS(nginx)+域名


`注：前端小白，欢迎并感谢各位大佬留言指正！`


[TOC]

## 〇. 网站内容与功能，初步设想
1. 个人简历：本人研究生，19年初毕业，正处于实习和找工作阶段
2. 个人博客：好好学习，天天向上，追求进步，实现自我
3. 中英文转换：至少，简历要有英文版的
4. 留个人Github账号

2018.01.28

## 一. 网页代码

- 首先，大概是找个IDE吧

  **vs-code**：最近用vs-code写python、C++、Matlab，都感觉不错，打算就用它和chrome写网页了。另外，什么html、php还是javascript，这些语言间的关系暂时还未理清，放到后面再慢慢看，然后从中选一个。

- 找别人写好的网页模板

  我们要站在巨人的肩膀上——懒。

- 学习HTML5、CSS

  这大概是基本功吧，也放到后面慢慢看。

此时此刻，我除了俩VPS外还什么都没有，一切从简，先把流程跑通再说其他———[我是长长的破折号]———所以，先下载个静态网页文件，拿来用用。

反正是要放个简历，我的简历是在乔布简历网站上编辑的，于是导出了个html格式的简历文件，姑且命名为”index.html“，以此来做我的第一个网页啦。

2018.07.21

## 二. 虚拟服务器

### 1. VPS选用（virtual private server）

作为学生，我选择带有学生专属优惠的vps，推荐两个如下：

- 国内：腾讯云

  我参与的学生优惠是每月只需付1元，似乎叫什么校园计划，需要申请

- 国外：Digital Ocean

  10$优惠注册链接：[http://www.digitalocean.com/?refcode=a5b36073b3b3](http://www.digitalocean.com/?refcode=a5b36073b3b3); 此外，学生还可从github上申请DO优惠，并与前面的10刀叠加使用

关于搭建VPS，可参见我的另一篇文章：[Shadowsocks服务搭建 (附DigitalOcean搭建VPS)](https://blog.csdn.net/yinhe0330/article/details/80874292) 

### 2. web代理服务的选用

有大约3种可选，贴个对比表格如下：

> 表格出处：[三大WEB服务器对比分析（apache ,lighttpd,nginx）](http://www.blogjava.net/daniel-tu/archive/2008/12/29/248883.html)

| **server**     | **Apache** | **Nginx** | **Lighttpd** |
| -------------- | ---------- | --------- | ------------ |
| Proxy代理      | 非常好     | 非常好    | 一般         |
| Rewriter       | 好         | 非常好    | 一般         |
| Fcgi           | 不好       | 好        | 非常好       |
| 热部署         | 不支持     | 支持      | 不支持       |
| 系统压力比较   | 很大       | 很小      | 比较小       |
| 稳定性         | 好         | 非常好    | 不好         |
| 安全性         | 好         | 一般      | 一般         |
| 技术支持       | 非常好     | 很少      | 一般         |
| 静态文件处理   | 一般       | 非常好    | 好           |
| Vhosts虚拟主机 | 支持       | 不支持    | 支持         |
| 反向代理       | 一般       | 非常好    | 一般         |
| Session sticky | 支持       | 不支持    | 不支持       |

小白表示没怎么看懂，似乎**Nginx**的发展前景不错，就选它了。

### 3. 在VPS上搭建Nginx

- 安装nginx

  ```
  sudo apt-get install nginx
  ```

- 打开nginx配置文件

  ```
  vim /etc/nginx/nginx.conf 
  ```

- 更改http上下文里的server上下文

  ```
  server {
          listen 80;               # 监听本机所有 ip 上的 80 端口，对应访问http
          server_name www.example.com;           # 域名www.example.com 或 你的公网ip
          root /home/ubuntu/web/;    # 站点根目录
          index index.html;
  
          #location / {             # 可有多个 location 用于配置路由地址
          #    try_files index.html =404;
          #}
  }
  ```

- 更改配置后，需重载Nginx服务

  ```
  sudo nginx -s reload
  ```

- 此外，还有重启、停止等命令

  ```
  sudo service nginx restart
  sudo service nginx stop
  ```

  

### 4. 至此，已可通过公网ip与端口，访问网页

- 80端口对应http访问权限（没s哦），如：http://127.0.0.1/cv/chinese

  *注 1：将127.0.0.1替换为你的server_name：即域名或公网ip*

  *注 2：前文提到http的server的root目录配置为：/home/ubuntu/web/，我的静态网页”index.html“放在了/home/ubuntu/web/cv/chinese/目录下*

2018.07.21

## 三. 域名

### 1. 选购

对于学生，推荐NameCheap的*.me域名，因为可以在github学生礼包中，找到为期1年的免费优惠

### 2. 绑定VPS的公网ip

下图是NameCheap域名绑定VPS的公网ip详情：

![1532313008261]([小白搭网站]静态网页+VPS(nginx)+域名.assets/1532313008261.png)

### 3.修改上文server配置，即修改server_name

```
server {
        listen 80;               # 监听本机所有 ip 上的 80 端口，对应访问http
        server_name *.me;           # 域名如example.me
        root /home/ubuntu/web/;    # 站点根目录
        index index.html;
}
```

### 4. 登录域名网址

如：http://yourName.me/cv/chinese

2018.07.23