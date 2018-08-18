# 数据库引擎

## ———MySQL Engine：innoDB vs myISAM

### MySQL Database Engine简介

#### 1. MySQL



#### 2. Engine

MySQL有多种存储引擎， 如MyISAM、InnoDB、MEMORY(HEAP)、ARCHIVE、MERGE、BDB(BerkeleyDB)、EXAMPLE、FEDERATED、CSV、BLACKHOLE。

功能上的简要对比如下：

| 功能     | MyISAM | InnoDB | Memory | Archieve |
| -------- | ------ | ------ | ------ | -------- |
| 存储限制 | 256T   | 64TB   | RAM    | None     |
| 事务     |        | √      |        |          |
| 全文索引 | √      |        |        |          |
| 数索引   | √      | √      | √      |          |
| 哈希索引 |        |        | √      |          |
| 数据缓存 |        | √      |        |          |
| 外键     |        | √      |        |          |

### 最常用的2个Engine——innoDB & myISAM

#### 1. innoDB



#### 2. myISAM



### 选哪个？

**优缺点、适用范围的对比：**

| 功能               | MyISAM                                                       | InnoDB                                                       |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ACID事务           |                                                              | 提供“提交、回滚、崩溃恢复”的事务安全功能                     |
| 锁                 | locking on **table** level                                   | locking on **row** level<br>*(table level when using "WHERE + LIKE")*<br>non-locking read in SELECTS |
| 效率：<br>并发     | 低                                                           | 高                                                           |
| 效率：<br>增删查改 | 频繁 SELECT + 常规 INSERT<br>且对SELECT性能要求较高：<br>**博客系统** | 经常UPDATE + INSERT，且多用户并发操作                        |
|                    |                                                              |                                                              |
|                    |                                                              |                                                              |
|                    |                                                              |                                                              |
|                    |                                                              |                                                              |

<br><br><br><br>