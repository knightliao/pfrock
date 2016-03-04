# pfrock

A plugin-based server for running fake HTTP and socket services (especially SOA service) using Python.
    
       _ (`-.            _  .-')                          .-. .-')
      ( (OO  )          ( \( -O )                         \  ( OO )
     _.`     \   ,------.,------.  .-'),-----.    .-----. ,--. ,--.
    (__...--''('-| _.---'|   /`. '( OO'  .-.  '  '  .--./ |  .'   /
     |  /  | |(OO|(_\    |  /  | |/   |  | |  |  |  |('-. |      /,
     |  |_.' |/  |  '--. |  |_.' |\_) |  |\|  | /_) |OO  )|     ' _)
     |  .___.'\_)|  .--' |  .  '.'  \ |  | |  | ||  |`-'| |  .   \
     |  |       \|  |_)  |  |\  \    `'  '-'  '(_'  '--'\ |  |\   \
     `--'        `--'    `--' '--'     `-----'    `-----' `--' '--'

## 开发进度

- dev(develop branch): 0.2.3
- master(stable branch)：0.2.3

## English readme
     
https://github.com/knightliao/pfrock/blob/master/README-en.md

## 主要目标

- 为微服务架构（SOA）而生。
    - 可以mock微服务架构（SOA）中各式各样的服务接口请求
    - 统一的mock服务。通过提供统一的router入口和自定义的sub-routers来实现
- 强大的功能
    - 配置文件式设计，零开发成本
    - 更改配置文件，无须重启，自动生效
    - 输入自定义匹配 url, method(GET/POST/PUT/DELETE/HEAD); 输出自定义 静态文件/静态目录/动态handler/header
- 开放式设计
    - 插件式开发，即插即用, 为可扩展性提供良好支持。目前系统核心已经支持 静态/动态/自定义 的Mock服务能力
    - 开放性，利用python动态能力，可以与各种中间件交互，登录redis/Q/db/hadoop

## 可用的插件 

- [pfrock-static-plugin](https://github.com/knightliao/pfrock-static-plugin) :提供文件式或目录结构的静态数据mock服务插件 
- [pfrock-http-plugin](https://github.com/knightliao/pfrock-http-plugin) : 提供动态http服务请求的mock服务插件
- [pfrock-proxy-plugin](https://github.com/knightliao/pfrock-proxy-plugin): 提供远程服务的代理服务插件 



## 快速安装 

pip install pfrock==0.2.3

(pypi: https://pypi.python.org/pypi/pfrock)

## Quick-Start

### demo目录结构

    - demo
        - mocks
            - handler
                - hello_world.py
                - __init__.py
            - static
                - a.json
                - b.json
            - __init__.py
        - __init__.py
        - pfrockfile.json        

### 启动

    ➜  pfrock git:(master) ✗
    ➜  pfrock git:(master) ✗ cd demo
    ➜  demo git:(master) ✗ pfrockpy
       _ (`-.            _  .-')                          .-. .-')
      ( (OO  )          ( \( -O )                         \  ( OO )
     _.`     \   ,------.,------.  .-'),-----.    .-----. ,--. ,--.
    (__...--''('-| _.---'|   /`. '( OO'  .-.  '  '  .--./ |  .'   /
     |  /  | |(OO|(_\    |  /  | |/   |  | |  |  |  |('-. |      /,
     |  |_.' |/  |  '--. |  |_.' |\_) |  |\|  | /_) |OO  )|     ' _)
     |  .___.'\_)|  .--' |  .  '.'  \ |  | |  | ||  |`-'| |  .   \
     |  |       \|  |_)  |  |\  \    `'  '-'  '(_'  '--'\ |  |\   \
     `--'        `--'    `--' '--'     `-----'    `-----' `--' '--'
    pfrock version 0.2.2
    [I 2016-03-04 14:07:05,231 pfrock.core MainThread __init__:19] started server 8888 with autoreload mod
    
### 静态文件 json get 请求

    ➜  ~  curl http://localhost:8888/api1/json
    {
      "a": "bddd33e34"
    }%

### 静态文件 json post请求

    ➜  ~  curl -X POST -d {} http://localhost:8888/api1/json
    {
      "a": "bddd33e34"
    }%

### 静态目录 json get 请求

    ➜  ~  curl http://localhost:8888/api1/b.json
    {
        "b": "bbb"
    }%

### 动态能力 get

    ➜  ~  curl 'http://localhost:8888/api'
    Hello, world 1! 1%                                                                                                                                            ➜  ~

### 代理能力

    ➜  ~  curl 'http://localhost:8888/'
        
## Tutorial

## more demos

https://github.com/knightliao/pfrock-demos

## 敏捷开发建议

建议按以下方式进行敏捷开发

- 服务间定好接口
- 使用pfrock来提供统一mock服务
- 通过mock接口，修改配置文件，无须重启pfrock，快速进行接口式开发
- 联调过程和测试过程，亦可通过pfrock来进行部分接口mock, 避免部分服务不稳定影响整体服务能力

## 群·联系·讨论

- pfrock技术QQ群: 545511264 
- 搜索引擎推荐：[sov5搜索引擎, 支持谷歌网页搜索和电影搜索](http://sov5.com)
- [disconf](https://github.com/knightliao/disconf) Distributed Configuration Management Platform(分布式配置管理平台)
- python论坛推荐：[Django中国社区](http://www.django-china.cn/)
- 我的微信：knightliao