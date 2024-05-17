import pandas as pd
import os

def extract_host_port_info(file_path):
    data = pd.read_csv(file_path)
    return data

def analyze_host_ports(data):
    host_port_mapping = {}
    for host, port in zip(data['Host'], data['Port']):
        if port != 0:  # 排除端口号为0的请求
            if host in host_port_mapping:
                if port not in host_port_mapping[host]:  # 去重
                    host_port_mapping[host].append(port)
            else:
                host_port_mapping[host] = [port]
    return host_port_mapping

def print_host_port_info(host_port_info, file_name):
    print(f"{file_name} 文件中:")
    total_hosts = len(host_port_info)
    print(f"有 {total_hosts} IP主机.")
    for host, ports in host_port_info.items():
        num_ports = len(ports)
        print(f"{host}-IP主机开放了-{num_ports}个端口, 分别是这些端口: {', '.join(map(str, ports))}")

def main():
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    for file_name in csv_files:
        data = extract_host_port_info(file_name)
        host_port_mapping = analyze_host_ports(data)
        print_host_port_info(host_port_mapping, file_name)

if __name__ == "__main__":
    main()
