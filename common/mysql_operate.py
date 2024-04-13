# @Time:2024-04-13 23:11
# @Author:HuangYong
import pymysql
from common.yaml_config import GetConf


class MysqlOperate:

    def __init__(self):
        mysql_conf = GetConf().get_mysql_config()
        self.host = mysql_conf["host"]
        self.db = mysql_conf["db"]
        self.port = mysql_conf["port"]
        self.user = mysql_conf["user"]
        self.password = mysql_conf["password"]
        self.conn = None
        self.cur = None

    def __conn_db(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                        port=self.port, charset="utf8")
        except Exception as e:
            print(e)
            return False
        self.cur = self.conn.cursor()
        return True

    def __close__conn(self):
        self.cur.close()
        self.conn.close()
        return True

    def __commit(self):
        self.conn.commit()
        return True

    def query(self, sql):
        self.__conn_db()
        self.cur.execute(sql)
        query_data = self.cur.fetchall()
        if query_data == ():  # 如果这个数据为空元组
            query_data = None
            print("没有获取到数据，表为空")
        else:
            pass
        self.__close__conn()
        return query_data

    def insert_uodate_table(self, sql):
        self.__conn_db()
        self.cur.execute(sql)
        self.__commit()
        self.__close__conn()


if __name__ == '__main__':
    result = MysqlOperate().query("select * from user;")
    print(result[0][1])