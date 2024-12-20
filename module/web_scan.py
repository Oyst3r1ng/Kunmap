# encoding: utf-8

'''
@author: Oyst3r
@contact: oyst3r@icloud.com
@File: web_scan.py
@Time: 2024/11/07
'''

import requests
import chardet
import re

# 获取网站的 Web 应用程序名和网站标题信息
def Title(scan_url_port):
    try:
        r = requests.get(scan_url_port, timeout=3, verify=False)
        r_detectencode = chardet.detect(r.content)
        actual_encode = r_detectencode['encoding']
        response = re.findall(r'<title>(.*?)</title>', r.content.decode(actual_encode), re.S)
        
        title = response[0] if response else 'Unknown'
        banner = r.headers.get('server', 'Unknown')
        
        print(f'\033[31m[+]{scan_url_port.ljust(30)} {banner.ljust(20)} Title: {title}\033[0m')
        
        with open('./files/http.txt', 'a') as f:
            f.write(f'{scan_url_port.ljust(30)} {banner.ljust(20)} Title: {title}\n')

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to get title for {scan_url_port}: {e}")
    except Exception as e:
        print(f"[ERROR] Error occurred while processing {scan_url_port}: {e}")
