# encoding: utf-8

'''
@author: Oyst3r
@contact: oyst3r@icloud.com
@File: host_scan.py
@Time: 2024/11/07
'''

import nmap3
import concurrent.futures

# 获取主机存活性
def HostAlive(scan_ip):
    nm = nmap3.PortScanner()
    try:
        nm.scan(scan_ip, arguments='-sn -Pn')
        return scan_ip if nm.all_hosts() else None
    except nmap3.PortScannerError as e:
        print(f"[ERROR] Nmap scan failed for {scan_ip}: {e}")
    except Exception as e:
        print(f"[ERROR] Failed to scan {scan_ip} for host status: {e}")
    return None

# 扫描所有主机存活性
def ScanAliveHosts():
    alive_ips = []
    with open('./files/ip.txt', 'r') as f:
        ip_list = [line.strip() for line in f]
    total_ips = len(ip_list)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_ip = {executor.submit(HostAlive, ip): ip for ip in ip_list}
        for index, future in enumerate(concurrent.futures.as_completed(future_to_ip), start=1):
            ip = future_to_ip[future]
            result = future.result()
            if result:
                alive_ips.append(result)
                print(f"[*]{result} is alive.")
            else:
                print(f"[*]{ip} is not alive.")

            progress = (index / total_ips) * 100
            print(f"[*]Scanning progress: {progress:.2f}% ({index}/{total_ips})")
    
    return alive_ips
