<h1 align="center">Kunmap - 更高效的资产收集</h1>

喵喵喵！！！

```
██╗  ██╗██╗   ██╗███╗   ██╗███╗   ███╗ █████╗ ██████╗
██║ ██╔╝██║   ██║████╗  ██║████╗ ████║██╔══██╗██╔══██╗
█████╔╝ ██║   ██║██╔██╗ ██║██╔████╔██║███████║██████╔╝
██╔═██╗ ██║   ██║██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
██║  ██╗╚██████╔╝██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     - V 1.0.0 Beta

Kunmap 是一款快速、高效的资产探测端口扫描工具。集成了 masscan 和 nmap，提供从端口扫描到服务识别的一体化体验。
GitHub: https://github.com/Oyst3r1ng/Kunmap
作者: Oyst3r
团队: 36Kun Security Team
```

![GitHub stars](https://img.shields.io/github/stars/Oyst3r1ng/Kunmap)   ![GitHub release](https://img.shields.io/github/forks/Oyst3r1ng/Kunmap)

![](https://img.shields.io/badge/python-%3E%3D3.2-yellow)

# 0x00 介绍

## 工具介绍

Kunmap 是36Kun安全团队的成员-Oyst3r开发，工具名字便为Kunmap。

Kunmap 是一款高效的资产探测工具🔧，专注于端口扫描探测。该工具集成了两种强大的扫描器：Masscan 和 Nmap。Masscan 负责快速扫描端口，Nmap 则深入探测端口对应的服务信息。通过结合二者的优势，Kunmap 实现了高效与精准的扫描效果。

## 应用场景

- 可以用于甲方安全工作中针对于内网脆弱资产的收集，也是这个工具被开发的初衷！

真实案例-->快速扫描某甲方企业的内网网段的部分资产，期间设备无告警、无异常

- 做为前期打点中信息收集中的一环，快速🔜去识别到高风险的资产，进行下一步的利用

Fofa、Zoomeye、ARL...-->Kunmap...-->Ehole、Poc、Burp...

- ......

# 0x01 安装及使用

Tips：安装以及使用都需要 Python3 的支持⬆️

## 安装

```
git clone https://github.com/Oyst3r1ng/Kunmap.git
cd Kunmap
pip3 install -r requirements.txt

至此安装完成
```

## 使用

项目整体的结构如下

```
├── README.md
├── files
│   ├── http.txt
│   ├── ip.txt
│   ├── ipc.txt
│   ├── masscan.json
│   └── result.txt
├── main.py
├── module
│   ├── domain_ip.py
│   ├── host_scan.py
│   ├── ip_converter.py
│   ├── masscan
│   ├── nmap_scan.py
│   ├── port_scan.py
│   └── web_scan.py
├── requirement.txt
└── resources
```

1. 将目标🎯放入对应的txt文件中

Tips：上图中files目录下共有6个txt文件，其中只有ipc.txt、domain.txt是开始前需要填入的，ipc.txt里面就是放着IP段或者是单个的IP，一行一行分开写即可，然后Kunmap运行后会统一解析成一个个的IP放到ip.txt中。domain.txt里面存放的是域名，Kunmap执行域名解析后会也存到ip.txt中。ip.txt和masscan.json是工具产生的中间文件，可以用于调试。result.txt是最终的结果，Kunmap会对里面的http服务抓取Header和Title存放到http.txt中。

2. 进行如下操作，启动Kunmap

```
cd Kunmap
python3 main.py
```

Tips：完全开源的，里面的各种参数大家伙可以根据自己的需求去修改，Oyst3r后续会考虑把Kunmap加上一些参数，方便大家伙儿在命令行调用main.py的时候就可以调整！

3. 进入files文件夹查看扫描的结果

# 0x03 Todo

1. 结合Ehole，增添指纹识别的功能

2. 魔改工具的流量

3. 增加图形化界面

4. 增加命令行参数

5. ......

# 0x04 Contribute

Kunmap By Oyst3r、36Kun Security Team、Fir3W411团队
