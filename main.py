from module.host_scan import ScanAliveHosts
from module.port_scan import Masportscan
from module.nmap_scan import ScanWithNmap
from module.domain_ip import Get_domain_ip
from module.ip_converter import ipc_to_ips
import os
import datetime

def main():

    try:
        if os.path.exists('./files/ipc.txt'):
            ipc_to_ips()
            alive_ips = ScanAliveHosts()
            temp_results = Masportscan(alive_ips)
            ScanWithNmap(temp_results)
        else:
            Get_domain_ip()
            alive_ips = ScanAliveHosts()
            temp_results = Masportscan(alive_ips)
            ScanWithNmap(temp_results)
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    spend_time = (datetime.datetime.now() - start_time).seconds
    print(f'The program is running: {spend_time} second')
