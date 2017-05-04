#!Python3
# _*_ encoding: utf-8 _*_

import pymysql.connections

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

        return pymysql.connect(host=db_config['host'],
                               port=db_config['port'],
                               user=db_config['username'],
                               password=db_config['password'],
                               db=db_config['db'])



    def execute_update(self, sql):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql)
            cursor.commit()
        finally:
            cursor.close()

    def execute_query(self, sql):
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        cursor.close()

    def save(self, sql):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        finally:
            cursor.close()

if __name__ == '__main__':
    mysql = MysqlRepository()
    insert_sql = "insert into house(title, room_number, floor, size, campus_name, source) values('Large house', \
                 2, 3, 80.0, 'jianzhong', 'Personal')"
    mysql.save(insert_sql)
    mysql.execute_query("select * from house")
