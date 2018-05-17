# Cloud-Robot-ROS

Training Project Cloud Robot Based on ROS

中山大学数据科学与计算机学院软件工程软件综合实训项目

面向机器人的软件软件设计与开发实训



## 1. 开发配置

开发环境：Ubuntu 16.04

开发平台：ROS Kinetic Kame

Python: python3.5

C++: C++11

### 1.1 Ubuntu16.04 安装 python3.5

在终端下输入以下命令：

```shell
# 安装python3.5
$ sudo apt-get install python3

# 安装pip
$ sudo apt install python-pip
```

### 1.2 配置virtualenv

在终端下输入以下命令：

```shell
# 安装virtualenv
$ sudo pip install virtualenv

# 创建venv
$ virtualenv rosenv -p /usr/bin/python3.5

# 安装依赖包
$ pip install -r requirements.txt
```

开发时需要先进入虚拟环境通过输入命令`source venv/bin/activate`，退出时输入命令`deactivate`



## 2. 文件结构

```
|-rosproject/
    |-msg/
    |-images/                       # 相关图片
    |-scripts/                      # 脚本文件夹
    	|-static/                   # 静态文件
    		|-css/                  # css样式文件
    			|-style.css
    		|-images/               # 图片、图标
    			|-favicon.ico
    		|-js/                   # js文件
    			|-jquery.js
    			|-webcam.js
   		|-templates/                # html模版
   			|-index.html
        |-cloud_server.py           # 服务器节点
        |-object_detection.py       # 物体检测识别
        |-web_server.py             # web端
    |-CMakeLists.txt                # 程序包元信息
    |-package.xml
    |-README.md                     # README
    |-requirements.txt              # python依赖包文件
```



## 3. 项目架构

![system](./images/system.png)



![details](./images/details.png)



## 4. 项目进度

已完成：

* 物体检测模块

* web端

未完成：

* 服务器节点
* 机器人节点
* 数据库



## 团队协作

Tower: <https://tower.im/projects/b6a5296a02404e99a69ec330ca8bcb3f/>