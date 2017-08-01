#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect


def remote_ssh(host_info):
    try:
        remote_cmd = "ssh {0}@{1} -p {2} \"{3}\"".format(
            host_info["user"],
            host_info["ip"],
            host_info["port"],
            host_info["cmd"])
        child = pexpect.spawn(remote_cmd)
        print("[I]:", remote_cmd)
        try:
            reply = ['password: ', 'continue connecting (yes/no)?']
            idx = child.expect(reply, timeout=15)
            if 0 == idx:
                child.sendline(host_info["passwd"])
            elif 1 == idx:
                child.sendline('yes\n')
        except pexpect.EOF:
            child.close()
        else:
            resp = child.read()
            child.expect(pexpect.EOF)
            child.close()
            return resp.decode('ascii')
    except Exception as e:
        print("[E]: Exception, connect {0} failed.".format(host_info["ip"]))

if __name__ == "__main__":
    dic = {
        "ip": "23.106.149.91",
        "port": "28665",
        "user": "root",
        "passwd": "********",
        "cmd": "top -b -n 1"
    }
    print(remote_ssh(dic))