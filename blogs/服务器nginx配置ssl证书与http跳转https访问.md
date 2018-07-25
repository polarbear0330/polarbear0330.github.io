# Nginx配置ssl证书+仅https访问

**注：**默认已获取如下3个文件

- 由openssl生成

  ```
  example_com.key
  example_com.csr
  ```

- 颁发的ssl证书

  ```
  example_com.crt
  ```

<br>

## 1. 找到nginx配置文件

```shell
vim /etc/nginx/nginx.conf
```

注：修改`nginx.conf`的server上下文时，若不存在server，则在`http{}`中添加`server{}`即可

## 2. 配置https与ssl_crt

此处开一个server监控443

```
server {
        listen 443 ssl;
        server_name example.com;

        root /home/ubuntu/web/;
        index index.html;

        ssl on;
        ssl_certificate /yourPath/example_com.crt;
        ssl_certificate_key /yourPath/example_com.key;
        }
```

## 3. http一律跳转至https安全连接

另开个server监控80，负责跳转

```
server {
        listen 80;
        server_name     example.com;
        return 301 https://example.com$request_uri;
        }
```

## 4. 重载nginx

```shell
nginx -s reload
```

<br>

<br>

---

在为域名购买ssl时，卖方网站会提供详细的认证流程，按部就班地做就行。

最终认证成功后，会颁发一个ssl_certification（证书），即“example_com.crt”，但此时还不能访问https。

<br>

**本文主要讲述了：得到certification之后的事。**

**继而完成https的访问**

2018.07.25

<br>

<br>

参考文献：

[Nginx 配置 SSL 证书 + 搭建 HTTPS 网站教程](https://www.cnblogs.com/chjbbs/p/5748369.html) 