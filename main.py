# encoding: utf-8

'''
@author: Oyst3r
@contact: oyst3r@icloud.com
@File: main.py
@Time: 2024/11/07
'''

import sys
import os
import datetime
import platform
from module.host_scan import ScanAliveHosts
from module.port_scan import Masportscan
from module.nmap_scan import ScanWithNmap
from module.domain_ip import Get_domain_ip
from module.ip_converter import ipc_to_ips

__title__ = 'Kunmap'
__license__ = 'GPL-3.0'
__python_version__ = sys.version.split()[0]
__platform__ = platform.platform()
__url__ = "https://github.com/Oyst3r1ng/Kunmap"
__version__ = '1.0.0'
__author__ = 'Oyst3r'
__team__ = '36Kun Security Team'
__author_email__ = 'oyst3r@icloud.com'

def show():
    logo = f"""
██╗  ██╗██╗   ██╗███╗   ██╗███╗   ███╗ █████╗ ██████╗
██║ ██╔╝██║   ██║████╗  ██║████╗ ████║██╔══██╗██╔══██╗
█████╔╝ ██║   ██║██╔██╗ ██║██╔████╔██║███████║██████╔╝
██╔═██╗ ██║   ██║██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
██║  ██╗╚██████╔╝██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     - V {__version__} Beta

Kunmap 是一款快速、高效的资产探测端口扫描工具。集成了 masscan 和 nmap，提供从端口扫描到服务识别的一体化体验。
GitHub: {__url__}
作者: {__author__}
团队: {__team__}

    """.strip()
    print(logo)

def main():

    show()
    print("\033[92mKunmap即将启动，请确保 `files` 文件夹中包含所有必要的数据文件\033[0m")
    try:
        if os.path.exists('./files/ipc.txt'):
            ipc_to_ips()
            print("\033[92m开始执行主机存活性检测...\033[0m")
            alive_ips = ScanAliveHosts()
            print("\033[92m主机存活性检测完成，开始执行端口扫描...\033[0m")
            temp_results = Masportscan(alive_ips)
            print("\033[92m端口扫描完成，开始进行服务识别...\033[0m")
            ScanWithNmap(temp_results)
            print("\033[92mKunmap扫描完成，请在 `files` 文件夹中查看扫描结果\033[0m")
        else:
            Get_domain_ip()
            print("\033[92m开始执行主机存活性检测...\033[0m")
            alive_ips = ScanAliveHosts()
            print("\033[92m主机存活性检测完成，开始执行端口扫描...\033[0m")
            temp_results = Masportscan(alive_ips)
            print("\033[92m端口扫描完成，开始进行服务识别...\033[0m")
            ScanWithNmap(temp_results)
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    spend_time = (datetime.datetime.now() - start_time).seconds
    print(f'Kunmap运行总共用时: {spend_time} 秒')
