#让对象支持上下午管理
#为了让一个对象兼容with语句，你需要实现__enter__()和__exit()方法

from socket import socket,AF_INET,SOCK_STREAM

class LazyConnection(object):
	"""docstring for LazyConnection"""
	def __init__(self,address,family=AF_INET,type=SOCK_STREAM):
		self.address=address
		self.family=family
		self.type=type
		self.sock=None

	def __enter__(self):
		if self.sock is not None:
			raise RuntimeError('Already connected')
		self.sock=socket(self.family,self.type)
		self.sock.connect(self.address)
		return self.sock 

	def __exit__(self,exc_ty,exc_val,tb):
		self.sock.close()
		self.sock=None

#LazyConnection类建立连接和关闭是使用with语句自动完成的
from functools import partial
conn=LazyConnection(('www.python.org',80))
with conn as s:
	#conn.__enter__() executes：connection open
	s.send(b'GET /index.html HTTP/1.0\r\n')
	s.send(b'Host: www.python.org\r\n')
	s.send(b'\r\n'
	resp = b''.join(iter(partial(s.recv, 8192), b''))	
	#conn.__exit__() executes: connection closed


"""
不管 with 代码块中发生什么，上面的控制流都会执行完，就算代码块中发生了异常也是
一样的。 事实上， __exit__() 方法的第三个参数包含了异常类型、异常值和追溯信息(如
果有的话)。 __exit__() 方法能自己决定怎样利用这个异常信息，或者忽略它并返回一个
None值。 如果 __exit__() 返回 True ，那么异常会被清空，就好像什么都没发生一样，
with 语句后面的程序继续在正常执行。
还有一个细节问题就是 LazyConnection 类是否允许多个 with 语句来嵌套使用连接。 很
显然，上面的定义中一次只能允许一个socket连接，如果正在使用一个socket的时候又重
复使用 with 语句， 就会产生一个异常了。不过你可以像下面这样修改下上面的实现来解
决这个问题：

"""

class LazyConnection:
	def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
		self.address = address
		self.family = family
		self.type = type
		self.connections = []
	def __enter__(self):
		sock = socket(self.family, self.type)
		sock.connect(self.address)
		self.connections.append(sock)
		return sock
	def __exit__(self, exc_ty, exc_val, tb):
		self.connections.pop().close()
	# Example use
	from functools import partial
		conn = LazyConnection(('www.python.org', 80))
		with conn as s1:
			pass
			with conn as s2:
				pass
	# s1 and s2 are independent socket





# s1 and s2 are independent sockets

		