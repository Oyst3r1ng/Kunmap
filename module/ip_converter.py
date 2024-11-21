# encoding: utf-8

'''
@author: Oyst3r
@contact: oyst3r@icloud.com
@File: ip_converter.py
@Time: 2024/11/07
'''

import IPy

# 将 IPC 转为 IP
def ipc_to_ips():
    readPath = './files/ipc.txt'
    writePath = './files/ip.txt'
    with open(writePath, 'w') as writeFile:
        with open(readPath, 'r') as f:
            for line in f:
                ip_c = line.strip('\n')
                ip = IPy.IP(ip_c)
                for line in ip:
                    if '.0' not in str(line).strip('\n'):
                        writeFile.write(f'{str(line)}\n')
