#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from utils import status
from utils import db


def update():
    path = os.getcwd() + "/../host/iplist.cfg"
    try:
        with open(path, "r") as f:
            new_dict = json.load(f)
        for index in range(len(new_dict)):
            host = status.HostStatus(new_dict[str(index)])
            host_info = host.return_host_info()
            it = db.Sql(host_info)
    except Exception as e:
        print("[E]: Host exception info, {0}.".format(e))

if __name__ == "__main__":
    update()