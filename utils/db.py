#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import os


class Sql:

    def __init__(self, host_info):
        self.host_info = host_info
        path = os.getcwd() + "/../db/host_info.db"
        try:
            self.conn = sqlite3.connect(path)
            self.create()
            if self.check():
                self.update()
            else:
                self.insert()
        except Exception as e:
            print("[E]: Sql init exception info, {0}.".format(e))

    def create(self):
        try:
            self.conn.execute("""CREATE TABLE IF NOT EXISTS HOSTSTATUS 
                (IP TEXT PRIMARY KEY NOT NULL,
                ALIVE TEXT NOT NULL,
                CPU TEXT,
                MEM TEXT,
                DISKTOTAL TEXT,
                DISKUSED TEXT,
                DISKAVAIL TEXT);
                """)
        except Exception as e:
            print("[E]: Sql create exception info, {0}.".format(e))
            self.exit()

    def check(self):
        try:
            cursor = self.conn.execute("SELECT * from HOSTSTATUS WHERE ip == \"{0}\";"
                              .format(self.host_info["ip"]))
            if len(cursor.fetchall()):
                return True
            return False
        except Exception as e:
            print("[E]: Sql check exception info, {0}.".format(e))
            self.exit()

    def insert(self):
        try:
            host_info = self.host_info
            self.conn.execute("""INSERT INTO HOSTSTATUS
                (IP, ALIVE, CPU, MEM, DISKTOTAL, DISKUSED, DISKAVAIL)
                VALUES(\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\");
                """.format(host_info["ip"],
                           host_info["alive"],
                           host_info["cpu"],
                           host_info["mem"],
                           host_info["disk"]["total"],
                           host_info["disk"]["used"],
                           host_info["disk"]["avail"]))
            self.conn.commit()
        except Exception as e:
            print("[E]: Sql insert exception info, {0}.".format(e))
            self.exit()

    def update(self):
        try:
            host_info = self.host_info
            self.conn.execute("""UPDATE HOSTSTATUS SET
                ALIVE = \"{0}\",
                CPU = \"{1}\",
                MEM = \"{2}\",
                DISKTOTAL = \"{3}\", 
                DISKUSED = \"{4}\", 
                DISKAVAIL = \"{5}\" WHERE IP == \"{6}\";
                """.format(host_info["alive"],
                           host_info["cpu"],
                           host_info["mem"],
                           host_info["disk"]["total"],
                           host_info["disk"]["used"],
                           host_info["disk"]["avail"],
                           host_info["ip"]))
            self.conn.commit()
        except Exception as e:
            print("[E]: Sql update exception info, {0}.".format(e))
            self.exit()

    def exit(self):
        try:
            self.conn.close()
        except Exception as e:                          
            print("[E]: Sql exit exception info, {0}.".format(e))

if __name__ == "__main__":
    pass