# 数据库引擎

## ——— MySQL Engine：innoDB vs myISAM

### MySQL Database Engine简介

#### 1. MySQL

开发公司：瑞典MySQL AB公司

目前归属：[Oracle](https://baike.baidu.com/item/Oracle) 旗下

类别：Relational Database Management System（关系型数据库管理系统）

> 关系数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性

特点：体积小、速度快、成本低、开源

常用搭配组合：Linux + Apache/Nginx + PHP/Perl/Python + MySQL

##### 分支: MariaDB

> MySQL 被 Oracle 收购后，创始人 Michael Widenius 离职，成立开源数据库联盟，创建 MariaDB

> According to Michael Widenius’s own words at a MySQL & MariaDB conference in Santa Clara on April 2014, MariaDB was born to ensure that a free version of MySQL always exists.

> 从 MySQL 转向 MariaDB的代表厂家：谷歌（2013年9月）、RedHat（2013年6月）、维基百科（2013年4月）

起名方式：My 和 Maria 都是 Michael Widenius 的女儿名字

#### 2. Engine

MySQL有多种存储引擎， 如MyISAM、InnoDB、MEMORY(HEAP)、ARCHIVE、MERGE、BDB(BerkeleyDB)、EXAMPLE、FEDERATED、CSV、BLACKHOLE。

功能上的简要对比如下：

| 功能     | MyISAM | InnoDB | Memory | Archieve |
| -------- | ------ | ------ | ------ | -------- |
| 存储限制 | 256T   | 64TB   | RAM    | None     |
| 事务     |        | √      |        |          |
| 全文索引 | √      | √      |        |          |
| 数索引   | √      | √      | √      |          |
| 哈希索引 |        |        | √      |          |
| 数据缓存 |        | √      |        |          |
| 外键     |        | √      |        |          |

### 最常用的2个Engine——innoDB & myISAM

#### 1. innoDB

> InnoDB 给 MySQL 提供了具有[事务](https://baike.baidu.com/item/%E4%BA%8B%E5%8A%A1)(transaction)、[回滚](https://baike.baidu.com/item/%E5%9B%9E%E6%BB%9A)(rollback)和崩溃修复能力(crash recovery capabilities)、多版本[并发控制](https://baike.baidu.com/item/%E5%B9%B6%E5%8F%91%E6%8E%A7%E5%88%B6)(multi-versioned concurrency control)的事务安全(transaction-safe (ACID compliant))型表。
>
> InnoDB 提供了行级锁(locking on row level)。提供与 Oracle 类似的不加锁读取(non-locking read in SELECTs)。InnoDB锁定在行级并且也在SELECT语句提供一个Oracle风格一致的非锁定读。这些特色增加了多用户部署和性能。没有在InnoDB中扩大锁定的需要，因为在InnoDB中行级锁定适合非常小的空间。InnoDB也支持FOREIGN KEY强制。

#### 2. myISAM

优点基本就一个：查询效率高

> myisam在索引层和压缩层的卓越贡献，所以我们经常把myisam用于slave层，供客户端去读取。而myisam在写库操作的时候会产生排他锁，如果写操作一直占用的话，那么其他连接请求一直就处于等待中，从而造成堵塞，甚至能把服务器dang掉。

### 选哪个？

**优缺点、适用范围的对比：**

| 功能               | MyISAM                                                       | InnoDB                                                       |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ACID事务           |                                                              | 提供“提交、回滚、崩溃恢复”的事务安全功能                     |
| 锁                 | locking on **table** level                                   | locking on **row** level<br>*(table level when using "WHERE + LIKE")*<br>non-locking read in SELECTS |
| 效率：<br>并发     | 低                                                           | 高                                                           |
| 效率：<br>增删查改 | 频繁 SELECT + 常规 INSERT<br>且对SELECT性能要求较高：<br>**博客系统** | 经常UPDATE + INSERT，且多用户并发操作                        |
|                    |                                                              |                                                              |

[**Comparison between InnoDB and MyISAM**](https://en.wikipedia.org/wiki/Comparison_of_MySQL_database_engines)

<br><br><br><br>

