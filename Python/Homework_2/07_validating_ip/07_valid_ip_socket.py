import socket


def check_ip(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False


print(check_ip('127.0.1'))
