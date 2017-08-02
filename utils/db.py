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
            self.delete()
        except Exception as e:
            print("[E]: Sql init exception info, {0}.".format(e))

    def create(self):
        sql = """CREATE TABLE IF NOT EXISTS HOSTSTATUS (
              IP TEXT PRIMARY KEY NOT NULL, ALIVE TEXT NOT NULL,
              CPU TEXT, LOAD TEXT, MEM TEXT, DISKTOTAL TEXT, 
              DISKAVAIL TEXT, NETWORK TEXT, CONNECT TEXT);
              """
        try:
            self.conn.execute(sql)
        except Exception as e:
            print("[E]: Sql create exception info, {0}.".format(e))
            self.exit()

    def check(self):
        sql = "SELECT * from HOSTSTATUS WHERE ip == \"{0}\";" \
            .format(self.host_info["ip"])
        try:
            cursor = self.conn.execute(sql)
            if len(cursor.fetchall()):
                return True
            return False
        except Exception as e:
            print("[E]: Sql check exception info, {0}.".format(e))
            self.exit()

    def insert(self):
        host_info = self.host_info
        sql = """INSERT INTO HOSTSTATUS (IP, ALIVE, CPU, LOAD, MEM, 
              DISKTOTAL, DISKAVAIL, NETWORK, CONNECT)
              VALUES(\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", 
              \"{5}\", \"{6}\", \"{7}\", \"{8}\");
              """.format(host_info["ip"],
                         host_info["alive"],
                         host_info["cpu"],
                         host_info["load"],
                         host_info["mem"],
                         host_info["disk"]["total"],
                         host_info["disk"]["avail"],
                         host_info["net"],
                         host_info["connect"])
        try:
            self.conn.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("[E]: Sql insert exception info, {0}.".format(e))
            self.exit()

    def update(self):
        host_info = self.host_info
        sql = """UPDATE HOSTSTATUS SET ALIVE = \"{0}\",
              CPU = \"{1}\", LOAD = \"{2}\", MEM = \"{3}\", DISKTOTAL = \"{4}\",
              DISKAVAIL = \"{5}\", NETWORK = \"{6}\", CONNECT = \"{7}\"
              WHERE IP == \"{8}\";
              """.format(host_info["alive"],
                         host_info["cpu"],
                         host_info["load"],
                         host_info["mem"],
                         host_info["disk"]["total"],
                         host_info["disk"]["avail"],
                         host_info["net"],
                         host_info["connect"],
                         host_info["ip"])
        try:
            self.conn.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("[E]: Sql update exception info, {0}.".format(e))
            self.exit()

    def delete(self):
        sql = "DELETE FROM HOSTSTATUS WHERE ALIVE == \"false\";"
        try:
            self.conn.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("[E]: Sql delete exception info, {0}.".format(e))
            self.exit()

    def cpu_low(self):
        sql = "SELECT * FROM HOSTSTATUS ORDER BY CPU ASC;"
        try:
            cursor = self.conn.execute(sql)
            for row in cursor:
                return row[0]
        except Exception as e:
            print("[E]: Query cpu exception info, {0}.".format(e))
            self.exit()

    def load_low(self):
        sql = "SELECT * FROM HOSTSTATUS ORDER BY LOAD ASC;"
        try:
            cursor = self.conn.execute(sql)
            for row in cursor:
                return row[0]
        except Exception as e:
            print("[E]: Query load exception info, {0}.".format(e))
            self.exit()

    def mem_high(self):
        sql = "SELECT * FROM HOSTSTATUS ORDER BY MEM DESC;"
        try:
            cursor = self.conn.execute(sql)
            for row in cursor:
                return row[0]
        except Exception as e:
            print("[E]: Query memory exception info, {0}.".format(e))
            self.exit()

    def disk_high(self):
        sql = "SELECT * FROM HOSTSTATUS ORDER BY DISKAVAIL DESC;"
        try:
            cursor = self.conn.execute(sql)
            for row in cursor:
                return row[0]
        except Exception as e:
            print("[E]: Query disk exception info, {0}.".format(e))
            self.exit()

    def net_low(self):
        sql = "SELECT * FROM HOSTSTATUS ORDER BY NETWORK ASC;"
        try:
            cursor = self.conn.execute(sql)
            for row in cursor:
                return row[0]
        except Exception as e:
            print("[E]: Query network exception info, {0}.".format(e))
            self.exit()

    def connect_low(self):
        sql = "SELECT * FROM HOSTSTATUS ORDER BY CONNECT ASC;"
        try:
            cursor = self.conn.execute(sql)
            for row in cursor:
                return row[0]
        except Exception as e:
            print("[E]: Query connect exception info, {0}.".format(e))
            self.exit()

    def exit(self):
        try:
            self.conn.close()
        except Exception as e:                          
            print("[E]: Sql exit exception info, {0}.".format(e))

if __name__ == "__main__":
    pass