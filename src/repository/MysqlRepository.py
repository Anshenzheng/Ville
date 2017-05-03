#!Python3
# _*_ encoding: utf-8 _*_

import mysql.connector

from src.model.Config import Config


class MysqlRepository(object):

    def __init__(self):
        self._conn = None

    def getConnection(self):
        if self._conn:
            return self._conn
        else:
            self._conn = self.createConnection(Config.db_config)
            return self._conn


    def createConnection(self, db_config):

        return mysql.connector.connect(db_config['username'], db_config['password'], db_config['db'])

    def execute_update(self, sql):
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.commit()
        cursor.close()

    def execute_query(self, sql):
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.commit()
        cursor.close()

