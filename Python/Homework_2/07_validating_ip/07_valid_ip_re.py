import re


def check_ip(ip_address):
    pattern = re.compile('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){2}'
                         '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\\.)?'
                         '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)?$')
    if pattern.match(ip_address):
        return True
    else:
        return False


print(check_ip('127.0.1'))
