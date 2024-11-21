# encoding: utf-8

'''
@author: Oyst3r
@contact: oyst3r@icloud.com
@File: port_scan.py
@Time: 2024/11/07
'''

import os
import json

# 调用 masscan 扫描开放的端口
def Masportscan(alive_ips):
    temp_results = {}
    ip_str = ','.join(alive_ips)
    os.system(f'../masscan/bin/masscan {ip_str} -p 0-8999 -oJ ./files/masscan.json --rate 1000 --wait 2')
    
    try:
        with open('./files/masscan.json', 'r') as f:
            data = json.load(f)
            for item in data:
                ip = item.get("ip")
                ports = [str(port_info["port"]) for port_info in item.get("ports", [])]
                if ports:
                    if ip not in temp_results:
                        temp_results[ip] = []
                    temp_results[ip].extend(ports)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to parse masscan JSON output: {e}")
    return temp_results
