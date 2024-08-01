import socket
import struct

def wake_on_lan(mac_address, interface_ip):
    # 将 MAC 地址格式化为没有分隔符的格式
    mac_address = mac_address.replace(':', '').replace('-', '')
    
    # 构建魔术包
    magic_packet = b'\xff' * 6 + (bytes.fromhex(mac_address) * 16)
    
    # 创建一个原始套接字
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # 绑定到指定的网卡 IP 地址
        sock.bind((interface_ip, 0))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, ('<broadcast>', 9))

# 示例用法
mac_address = '00:11:22:33:44:55'
interface_ip = '192.168.1.2'  # 替换为你的网卡 IP 地址
wake_on_lan(mac_address, interface_ip)
