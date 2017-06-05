#_*_ coding:utf-8 _*_

# 为了避免大量可有可无的参数把视图函数弄得一团糟，Flask使用上下文临时把某些对象变为全局可访问。有了
# 上下文，就可以写出如些的属兔函数：

from flask import request
from flask import Flask
from flask import redirect
from flask import abort
from flask import render_template
app = Flask(__name__)
app.debug=True


@app.route('/')
def index():
    # user_agent=request.header.get('User-Agent')
    # return '<p>Your browser is %s</p>'%user_agent
    return 'ggg'


@app.route('/wo/')
def wo():
    #return 'www.baidu.com', 302
    return redirect('http://www.baidu.com')


@app.route('/user/')
@app.route('/user/<id>')
def get_user(id=None):
	comments=['A','B','C','D']
	user=id
	if not user:
		#abort(404)
		return "wahaha"
	#return '<h1>Hello ,%s</h1>'%id
	return render_template('user1.html',comments=comments)



# Flask分为程序上下文和请求上下文
# 程序上下文：
#	current_app:当前激活程序的程序实例
#	g:处理请求时作用临时存储对象。每次请求都会重设这个变量
# 请求上下文：
#	request:请求对象，封装了客户端发出的HTTP请求中的内容
#	session:用户回话，用于存储请求之间需要'记住'的值的词典

# 请求钩子
"""
有时在处理请求之前或之后执行代码会很有用。例如，在请求开始时，我们可能需要创
建数据库连接或者认证发起请求的用户。 为了避免在每个视图函数中都使用重复的代码，
Flask 提供了注册通用函数的功能， 注册的函数可在请求被分发到视图函数之前或之后
调用。
"""

# Flask支持一下4中钩子：
#	before_first_request:注册一个函数，在处理第一个请求之前运行
#	before_request:注册一个函数，在每次请求之前运行
#	after_request:注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行
#	teardown_request:注册一个函数，及时有未处理的异常抛出，也在每次请求后运行
"""
在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量 g。例如， before_
request 处理程序可以从数据库中加载已登录用户，并将其保存到 g.user 中。随后调用视
图函数时，视图函数再使用 g.user 获取用户
"""
app.run()


#----------------------
#模板
#Jinja2常用过滤器：
"""
safe 渲染值时不转义
capitalize 把值的首字母转换成大写，其他字母转换成小
lower 把值转换成小写形式
upper 把值转换成大写形式
title 把值中每个单词的首字母都转换成大写
trim 把值的首尾空格去掉
striptags 渲染之前把值中所有的 HTML 标签都删掉
"""
"""
safe 过滤器值得特别说明一下。默认情况下，出于安全考虑， Jinja2 会转义所有变量。例
如， 如果一个变量的值为 '<h1>Hello</h1>'， Jinja2 会将其渲染成 '&lt;h1&gt;Hello&lt;/
h1&gt;'，浏览器能显示这个 h1 元素，但不会进行解释。很多情况下需要显示变量中存储
的 HTML 代码，这时就可使用 safe 过滤器。
"""