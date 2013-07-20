#-*- coding:utf-8 -*-

import web
import MySQLdb
from bae.core import const

# 指定bae的mysql数据库名
mysql_name = 'iXTjFtyghAUQWLytOXzs'

# 设置urls，将任意输入用index类解析
urls = ('/(.*)', 'index')

# 指定渲染模板目录
render = web.template.render("templates/")

# 创建表单"env_info"
def db_create_table():
   db = db_open()
   cursor = db.cursor()
   cmd = '''CREATE TABLE IF NOT EXISTS env_info (
         id int(4) auto_increment,
		 equip_id char(10) not null,
		 temperature int(2),
		 time timestamp default current_timestamp,
         primary key (id))'''
   cursor.execute(cmd)
   db_close(db)

# 连接数据库
def db_open():
	db = MySQLdb.connect(
		host = const.MYSQL_HOST, 
		port = int(const.MYSQL_PORT), 
		user = const.MYSQL_USER, 
		passwd = const.MYSQL_PASS, 
		db = mysql_name)
	return db

# 关闭数据库
def db_close(db):
	db.close()

# 创建数据库    
info = db_create_table()

# 插入一条纪录到数据库指定表单“env_info”
def insert_data(i):
	db = db_open()
	c = db.cursor()	
	c.executemany("""INSERT INTO env_info (equip_id, temperature) VALUES (%s, %s)""", [(i.id, i.temperature)])
	db_close(db)

# 从数据库抽取所有满足条件的纪录    
def get_data(i):
	db = db_open()
	c = db.cursor()
	c.execute("""SELECT * FROM env_info WHERE equip_id = %s""", i.id)
	rows = c.fetchall() 
	db_close(db)
	return rows

# 根据urls设置响应
class index: 
    def GET(self, type):
		i = web.input(type = "get")
        
		if i.type.lower() == "get":
			rows = get_data(i)
			return render.index(rows)               
		elif i.type.lower() == "put":          
			insert_data(i)          
			return "insert a environment record"         
		
		return "wrong type!"         
        
app = web.application(urls, globals()).wsgifunc()

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)