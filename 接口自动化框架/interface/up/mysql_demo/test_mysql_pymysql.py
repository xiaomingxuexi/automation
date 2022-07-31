
import pymysql
import requests


def query_db(sql):
    # 建立连接
    conn = pymysql.Connect(host="47.92.149.0", port=3366, database="test_db",
                           user="root", password="123456",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()
    # sql = "some sql'"
    # 使用游标执行sql
    cursor.execute(sql)
    print("行数:", cursor.rowcount)
    # 获取行数
    datas = cursor.fetchall()
    print("查询到的数据为:", datas)  # 获取多条数据
    cursor.close()
    conn.close()
    return datas


def test_register():
    phone = "13888888884"
    url = "http://47.92.149.0:9000/register"
    json_data = {
        "phone": phone,
        "password": "123456",
        "name": "张三_2022"
    }
    r = requests.request("POST", url=url, json=json_data)
    print(r.json())
    assert r.json().get("code") == 0
    sql = f"select id from user_info where phone='{phone}'"
    # 第一种方式
    # dat = query_db(sql)
    # print(dat)
    # assert len(dat) == 1
    # 第二种方式
    sql_data = {"sql": sql}
    r = requests.request("POST", url="http://47.92.149.0:9000/execute_sql", json=sql_data)
    print(r.json())
