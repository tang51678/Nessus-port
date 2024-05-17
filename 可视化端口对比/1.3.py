import pandas as pd
import streamlit as st


def extract_host_port_info(file_path):
    data = pd.read_csv(file_path)
    return data


def analyze_host_ports(data):
    host_port_mapping = {}
    total_unique_ports = 0
    for host, port in zip(data['Host'], data['Port']):
        if port != 0:
            if host not in host_port_mapping:
                host_port_mapping[host] = []
            if port not in host_port_mapping[host]:
                host_port_mapping[host].append(port)
                total_unique_ports += 1
    return host_port_mapping, total_unique_ports


def print_host_port_info(host_port_info, total_hosts, total_unique_ports, file_name):
    st.write(f"{file_name} 文件中:")
    st.write(f"有 {total_hosts} IP主机, 一共(去重后)开放 <font color='red'>{total_unique_ports}</font> 个端口", unsafe_allow_html=True)
    for host, ports in host_port_info.items():
        num_ports = len(ports)
        st.write(f"{host}-IP主机开放了-<font color='red'>{num_ports}</font> 个端口, 分别是这些端口: {', '.join(map(str, ports))}",unsafe_allow_html=True)


def main():
    st.title("主机端口信息展示")

    selected_files = st.file_uploader("上传CSV文件(可同时上传多个文件):", type='csv', accept_multiple_files=True)

    if selected_files:
        total_files_hosts = 0
        total_files_unique_ports = 0
        for file in selected_files:
            st.write(f"## {file.name} 文件信息:")
            data = extract_host_port_info(file)
            host_port_mapping, total_unique_ports = analyze_host_ports(data)
            total_hosts = len(host_port_mapping)
            total_files_hosts += total_hosts
            total_files_unique_ports += total_unique_ports
            print_host_port_info(host_port_mapping, total_hosts, total_unique_ports, file.name)

        st.write(f"#### 所有文件中共有 {total_files_hosts} 个 IP 主机，一共(去重后)开放 <font color='red'>{total_files_unique_ports}</font>个端口。", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
