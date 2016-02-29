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

## English readme
     
https://github.com/knightliao/pfrock/blob/master/README-en.md

## 主要目标

- 为微服务架构（SOA）而生。可以mock微服务架构（SOA）中各式各样的服务接口请求
- 提供统一的mock服务。通过提供统一的router入口和自定义的sub-routers来实现
- 为敏捷开发提供可行的方案，只需更改配置文件，无须重启即可快速生效快速mock。建议按以下方式进行敏捷开发
    - 服务间定好接口
    - 使用pfrock来提供统一mock服务
    - 通过mock接口，修改配置文件，无须重启pfrock，快速进行接口式开发
    - 联调过程和测试过程，亦可通过pfrock来进行部分接口mock
- 插件式开发，即插即用, 为可扩展性提供良好支持。目前已经支持 静态/动态/自定义 的Mock服务能力

## 可用的插件 

- [pfrock-static-plugin](https://github.com/knightliao/pfrock-static-plugin) :提供文件式或目录结构的静态数据mock服务插件 
- [pfrock-http-plugin](https://github.com/knightliao/pfrock-http-plugin) : 提供动态http服务请求的mock服务插件
- [pfrock-proxy-plugin](https://github.com/knightliao/pfrock-proxy-plugin): 提供远程服务的代理服务插件 

## demos and Quick-Start

https://github.com/knightliao/pfrock-demos

## pypi

https://pypi.python.org/pypi/pfrock

- dev(develop branch): 0.2.1.a2
- master(stable branch)：0.2.1.a2

## 安装 

pip install pfrock==0.2.1.a2

## 使用指南
