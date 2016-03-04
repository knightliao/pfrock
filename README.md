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

- dev(develop branch): 0.2.2
- master(stable branch)：0.2.2

## English readme
     
https://github.com/knightliao/pfrock/blob/master/README-en.md

## 主要目标

- 为微服务架构（SOA）而生。
    - 可以mock微服务架构（SOA）中各式各样的服务接口请求
    - 统一的mock服务。通过提供统一的router入口和自定义的sub-routers来实现
- 强大的功能
    - 配置文件式设计，零开发成本
    - 更改配置文件，无须重启，自动生效
    - 输入自定义匹配 url, method; 输出自定义 静态文件/静态目录/动态handler/header
- 开放式设计
    - 插件式开发，即插即用, 为可扩展性提供良好支持。目前系统核心已经支持 静态/动态/自定义 的Mock服务能力
    - 开放性，利用python动态能力，可以与各种中间件交互，登录redis/Q/db/hadoop

## 可用的插件 

- [pfrock-static-plugin](https://github.com/knightliao/pfrock-static-plugin) :提供文件式或目录结构的静态数据mock服务插件 
- [pfrock-http-plugin](https://github.com/knightliao/pfrock-http-plugin) : 提供动态http服务请求的mock服务插件
- [pfrock-proxy-plugin](https://github.com/knightliao/pfrock-proxy-plugin): 提供远程服务的代理服务插件 



## 快速安装 

pip install pfrock==0.2.2

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
    
### 静态文件 json请求

    ➜  ~  curl http://localhost:8888/api1/json
    {
      "a": "bddd33e34"
    }%

### 静态目录 json get 请求

    ➜  ~  curl -v http://localhost:8888/api1/b.json
    *   Trying 127.0.0.1...
    * Connected to localhost (127.0.0.1) port 8888 (#0)
    > GET /api1/b.json HTTP/1.1
    > Host: localhost:8888
    > User-Agent: curl/7.43.0
    > Accept: */*
    >
    < HTTP/1.1 200 OK
    < Content-Length: 18
    < Accept-Ranges: bytes
    < Server: TornadoServer/4.3
    < Last-Modified: Fri, 04 Mar 2016 06:11:58 GMT
    < Etag: "a0b604ab6dcf3ec7dda01fba7fbb61f3"
    < Date: Fri, 04 Mar 2016 06:12:00 GMT
    < Content-Type: application/json
    <
    {
        "b": "bbb"
    * Connection #0 to host localhost left intact
    }%

### 静态目录 json get 请求

    ➜  ~  curl http://localhost:8888/api1/b.json
    {
        "b": "bbb"
    }%

### 动态能力

    ➜  ~  curl 'http://localhost:8888/api'
    Hello, world 1! 1%                                                                                                                                            ➜  ~

### 代理能力

    ➜  ~  curl 'http://localhost:8888/'
        
## Tutorial

## more demos

https://github.com/knightliao/pfrock-demos

## 建议

- 建议按以下方式进行敏捷开发
    - 服务间定好接口
    - 使用pfrock来提供统一mock服务
    - 通过mock接口，修改配置文件，无须重启pfrock，快速进行接口式开发
    - 联调过程和测试过程，亦可通过pfrock来进行部分接口mock


