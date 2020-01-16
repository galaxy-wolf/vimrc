import subprocess
import os

USER_NAME = 'zhaoqi'
BAD_IP = '192.168.0.1'

def get_percent(s):
    ret = ''
    for c in s:
        if '0' <= c <= '9':
            ret += c
    return int(ret)


def get_ip_from_str(s):
    ret = ''
    for c in s:
        if '0' <= c <= '9' or c == '.':
            ret += c
    return ret


def get_my_ip():
    # b'192.168.1.1\\n'
    ret = subprocess.Popen("ipconfig | grep -ia 'IPv4' | sed -n 2p | grep -iao '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'", shell=True, stdout=subprocess.PIPE).stdout.read()
    ret = get_ip_from_str(str(ret))
    return ret, ret[:ret.rfind('.')], ret[ret.rfind('.')+1:]


def get_u18_ip():
    my_ip, a, b = get_my_ip()
    print('my ip is %r %r %r' % (my_ip, a, b))
    b = int(b)
    for bb in range(b+1, 256):
        ip = '{a}.{b}'.format(a=a, b=str(bb))
        if is_good_ip(ip):
            return ip
        print('test %r failed' % ip)
    return ''


def is_good_ip(ip):
    cmd = "ping " + str(ip) + " -i 1 -w 1000 -n 1"
    ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    if BAD_IP in str(ret):
        return False

    cmd = "ping " + str(ip) + " -i 1 -w 1000 -n 1 | grep -iao '[0-9]\{1,3\}%'"
    # -i 1 TTL
    ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    ret = str(ret)
    ret = get_percent(ret)
    if ret > 0:
        return False
    return True


def set_alias():
    ip = get_u18_ip()
    if not ip:
        print('error: ip not found!')
        return 
    cmd = "cat ~/.ssh/id_rsa.pub | ssh-copy-id " + USER_NAME + "@" + ip
    ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    print(ret)
    cmd = "alias u18=ssh " + USER_NAME + "@" + ip
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    os.system(cmd)
    print('now you can use "u18" to connect to your ubuntu!')


if __name__ == '__main__':
    set_alias()
