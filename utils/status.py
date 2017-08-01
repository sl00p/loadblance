#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import ssh
import re


class HostStatus:

    def __init__(self, host_info):
        self.host_info = host_info
        self.cmd = ["top -b -n 1", "df -h", "ping -c 4 google.com"]
        self.cmd_num = len(self.cmd)
        self.result = []

    def connect(self):
        for cmd_index in range(self.cmd_num):
            self.host_info["cmd"] = self.cmd[cmd_index]
            ret = ssh.remote_ssh(self.host_info)
            if ret:
                print("[I]: {0} connected.".format(self.host_info["ip"]))
                self.host_info["alive"] = "true"
            else:
                print("[I]: {0} not connected.".format(self.host_info["ip"]))
                self.host_info["alive"] = "false"
            self.result.append(ret)

    @staticmethod
    def cpu_status(top_status):
        try:
            pattern = re.compile(r"(\d+.\d+)%us")
            items = pattern.findall(top_status)
            #print(items)
            return items
        except Exception as e:
            print("[E]: Cpu status exception info, {0}.".format(e))

    @staticmethod
    def mem_status(top_status):
        try:
            pattern = re.compile(r"(\d+[kKmMgG]) free")
            items = pattern.findall(top_status)
            #print(items)
            return items
        except Exception as e:
            print("[E]: Memory status exception info, {0}.".format(e))

    @staticmethod
    def disk_status(df_status):
        disk = {}
        if df_status:
            df_status_tmp = df_status.split(' ')
            df_status = []
            for c in df_status_tmp:
                if c != '':
                    df_status.append(c)
            disk["total"] = df_status[7]
            disk["used"]  = df_status[8]
            disk["avail"] = df_status[9]
        else:
            disk["total"] = "None"
            disk["used"]  = "None"
            disk["avail"] = "None"
        return disk

    def extract_cpu(self):
        if self.result[0]:
            self.host_info["cpu"] = self.cpu_status(self.result[0])[0]
        else:
            self.host_info["cpu"] = "None"

    def extract_mem(self):
        if self.result[0]:
            self.host_info["mem"] = self.mem_status(self.result[0])[0]
        else:
            self.host_info["mem"] = "None"

    def extract_disk(self):
        self.host_info["disk"] = self.disk_status(self.result[1])

    def extract_ping(self):
        if self.result[2]:
            print(self.result[2])

    def operate(self):
        self.connect()
        self.extract_cpu()
        self.extract_mem()
        self.extract_disk()

    def return_host_info(self):
        self.operate()
        return self.host_info


if __name__ == "__main__":
    dic = {
        "ip": "23.106.149.91",
        "port": "28665",
        "user": "root",
        "passwd": "******"
    }
    it = HostStatus(dic)
    print(it.return_host_info())
