#_*_ coding:utf-8 _*_

#为了避免大量可有可无的参数把视图函数弄得一团糟，Flask使用上下文临时把某些对象变为全局可访问。有了
#上下文，就可以写出如些的属兔函数：

from flask import request
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
	user_agent=request.header.get('User-Agent')
	return '<p>Your browser is %s</p>'%user_agent


#Flask分为程序上下文和请求上下文
