#coding:utf-8
import pymysql
# from decimal import Decimal
#1.连接数据库
#host 主机名或ip  user 用户名 paswd 用户对应的密码  db 要连接的数据库
conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='ca2')
#2.创建操作游标,创建了mysql的操作链接
a_conn=conn.cursor()
#3.一般我们操作数据库会执行这样一条语句
#set names utf8 设置输入输出的数据的字符集为utf8
a_conn.execute('set names utf8')
# a_conn.execute('set autocommit=1')
#4.插入数据
sql='insert into jy(uid,price,createtime) VALUE (%d,%f,"%s")'%(1,1.23,'2017-11-22 12:00:00')
# a_conn.execute(sql)
# conn.commit()
# parm=('NULL',1,1.23,'2017-11-22')
# cursor.execute(sql,parm)

#5.查询
sql2='select * from jy where price={0}'.format(1.23)
a_conn.execute(sql2)
print sql2
#得到结果集
#（1）fetchone   #得到一条结果集
# result=a_conn.fetchone()
# print result
#2.fetchamany #得到n条结果集，返回形式为元祖嵌套集合
# result2=a_conn.fetchmany(2)
# print result2
#3.fetchall() 得到所有的结果集，返回形式为元祖嵌套集合
# result3=a_conn.fetchall()
# print result3

#6.更新操作,使用sql+parm方式
#（1）结构清晰
#（2）防止SQL注入，安全性
sql="select * from jy where Id =%s"
parm=(2.1,2)
a_conn.execute(sql,parm)


#7.提交所有操作产生结果
conn.commit()

#8.关闭连接
# (1)关闭游标
a_conn.close()
#（2）断开连接
conn.close()

#9.拓展
#(1)executemany() 执行多条sql语句
sql=('sql1','sql2')
parm=((''),(''))
a_conn.executemany(sql,parm)
