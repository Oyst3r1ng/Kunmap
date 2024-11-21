# encoding: utf-8

'''
@author: Oyst3r
@contact: oyst3r@icloud.com
@File: nmap_scan.py
@Time: 2024/11/07
'''

import nmap
import concurrent
from module.web_scan import Title

# 调用 nmap 识别开放端口的服务
def Nmapscan_worker(scan_ip, ports):
    nm = nmap.PortScanner()
    for port in ports:
        try:
            ret = nm.scan(scan_ip, port, arguments='-sV -Pn -T4 -n')
            service_name = ret['scan'][scan_ip]['tcp'][int(port)]['name']
            print(f'[*] 主机 {scan_ip} 的 {port} 端口服务为：{service_name}')
            with open('./files/result.txt', 'a') as f:
                f.writelines(f'[*] 主机 {scan_ip} 的 {port} 端口服务为：{service_name}\n')

            if 'http' in service_name:
                scan_url_port = f'http://{scan_ip}:{port}'
                Title(scan_url_port)
        except nmap.PortScannerError as e:
            print(f"[ERROR] Nmap scan failed for {scan_ip}:{port} - PortScannerError: {e}")
        except Exception as e:
            print(f"[ERROR] Nmap scan failed for {scan_ip}:{port} - {e}")

# 多线程执行 nmap 扫描
def ScanWithNmap(temp_results):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [
            executor.submit(Nmapscan_worker, ip, ports)
            for ip, ports in temp_results.items()
        ]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"[ERROR] Nmap scan exception: {e}")
