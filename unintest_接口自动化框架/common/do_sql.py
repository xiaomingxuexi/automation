import pymysql

class DoSQL:
    def __init__(self):
        self.connection=pymysql.Connect(
            host='192.168.88.8',
            port=3306,
            user='root',
            password='root',
            database='cola_all'
        )
        self.connection.cursor()
        self.cursor = self.connection.cursor()
        # 关闭时候,先关闭cursor,再关闭connection

    def select_one(self,sql): # Excel中自己输的
        self.connection.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchone()


    def select_all(self,sql):
        self.connection.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def select_count(self,sql):
        self.connection.commit()
        return self.cursor.execute(sql)


    # 自行封装删除和修改
    def delete(self,sql):
        self.cursor.execute(sql)
        self.connection.commit()


    def insert(self,sql):
        self.cursor.execute(sql)
        self.connection.commit()


    def close(self):
        self.cursor.close()
        self.connection.close()


if __name__ == '__main__':
    do_sql=DoSQL()
    # do_sql.select_one('sql1')
    # do_sql.select_one('sql2')
    # do_sql.select_one('sql3')
    sql1 = 'select * from cola_member where phoneNumber="18888888888"'
    sql2 = 'select * from cola_member'
    sql3 = 'select * from cola_member where phoneNumber="18888888888" or phoneNumber="13111111111" or phoneNumber="13177777777"'

    print(do_sql.select_one(sql1))
    print(do_sql.select_count(sql2))
    print(do_sql.select_all(sql3))

    do_sql.close()


