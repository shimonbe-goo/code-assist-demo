import os
import subprocess


def ping_host(host):
    return os.system("ping -c 1 " + host)


def run_backup(path):
    subprocess.call("tar czf backup.tar.gz " + path, shell=True)


def read_log(filename):
    f = open("logs/" + filename)
    return f.read()


def calculate(expr):
    return eval(expr)
