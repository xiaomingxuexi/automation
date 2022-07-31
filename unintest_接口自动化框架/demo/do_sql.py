"""
python 操作 mysql:
1.连接数据库,获取操作对象
2.执行sql语句(查询为主)------>execute()
3.获取结果------------------>fetchone() # 查询一条    fetchall() # 查询多条   result # 返回受影响的行数


Navicat连接数据库:
连接名           随意的
主机             192.168.88.8
端口             3306
用户             root
密码             root

python连接    mysql：
连接名           随意的
主机             192.168.88.8
端口             3306
用户             root
密码             root
数据库           cola_all

"""
import pymysql

connection=pymysql.Connect(
    host='192.168.88.8',
    user='root',
    password='root',
    database='cola_all',
    port=3306

)
# print(connection)
cursor=connection.cursor()  # 数据库操作对象(中介)   python和数据库;  cursor

sql1='select * from cola_member where phoneNumber="18888888888"'
sql2='select * from cola_member'
sql3='select * from cola_member where phoneNumber="18888888888" or phoneNumber="13111111111" or phoneNumber="13177777777"'

result=cursor.execute(sql3) # result是受影响的行数;

# print(result)

# data1 = cursor.fetchone()  # 结果是以元组的形式进行返回的!
# data2 = cursor.fetchone()  # 结果是以元组的形式进行返回的!
# data3 = cursor.fetchone()  # 结果是以元组的形式进行返回的!
# data4 = cursor.fetchone()  # 结果是以元组的形式进行返回的!提取之后,数据就没了
# print(data1)
# print(data2)
# print(data3)
# print(data4)

data1 = cursor.fetchall() # 结果是以元组嵌套元组的形式返回的,只查询一条的时候,还是元组嵌套元组的形式；
print(data1)
