## 简介
这是基于[百度应用引擎（BAE）][bae]，利用python，搭建一个简单web服务的示例，主要展示对BAE的MySQL云数据库的插入及读取数据。示例中使用了webpy框架的基本功能。

本示例的应用背景是利用[Arduino][arduino]为中心的传感器收集环境数据到云端，通过分析数据，自动调节家电到最合适的工作状态。

## 功能
本示例只采用了http的GET方法，通过参数`type`的值判断是插入还是读取。

向数据库插入一条纪录的方法：

			http://3.jiyeqian.duapp.com/?type=put&id=t001&temperature=25

向数据库读出纪录的方法：

			http://3.jiyeqian.duapp.com/?type=get&id=t001
			
或者（type的默认值是get）：

			http://3.jiyeqian.duapp.com/?id=t001								
## 注意

* 在线编写代码时，python代码对齐引发的错误将在保存代码时给出，形如：
```Sorry: IndentationError: ('unexpected indent', ('/appid9g79s4e8ej/3/index.py', 56, 2, '\t c = db.cursor()```。
* http访问出现```internal server error```是pyhon语法错误引起的。
* BAE提供的phpMyAdmin是管理数据库的利器。


## 资料
* BAE的入门指导：[http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt/start](http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt/start) 和 [http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt/python](http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt/python)
* webpy的入门指导：[http://webpy.org/docs/0.3/tutorial](http://webpy.org/docs/0.3/tutorial)
* 利用python访问BAE的数据库：[http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt/python/mysql](http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt/python/mysql)
* 关于webpy的渲染模板：[http://webpy.org/docs/0.3/templetor](http://webpy.org/docs/0.3/templetor) 

# 建议

提供本地调试的sdk编写代码更方便。在线编写python代码对齐是个大问题，本地编写线上调试太折腾。



[bae]: http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt "百度应用引擎(BAE)"
[arduino]: http://www.arduino.cc "Arduino"

