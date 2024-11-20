import socket
import time

# 获取域名对应 IP
def Get_domain_ip():
    with open('./files/subdomain.txt', 'r') as f:
        for line in f:
            line = line.strip()
            try:
                ip = socket.gethostbyname(line.replace('www.', '') if 'www.' in line else line)
                print(line, ip)
                with open('./files/ip.txt', 'a') as l:
                    l.writelines(f'{ip}\n')
            except socket.gaierror as e:
                print(f"[ERROR] Failed to resolve domain {line}: {e}")
            time.sleep(1)
