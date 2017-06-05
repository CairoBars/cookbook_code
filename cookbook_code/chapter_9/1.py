#_*_ coding:utf-8_*_
import time
from functools import wraps

def timethis(func):
	'''
	Decorator that reports the execution time
	'''
	#@wraps(func)注解很重要，它能保留原始函数的元数据
	@wraps(func)
	def wrapper(*args,**kwargs):
		start=time.time()
		result=func(*args,**kwargs)
		end=time.time()
		print(func.__name__,end-start)
		return result
	return wrapper



@timethis
def countdown(n):
	''' Counts down'''
	print("GGG")
	while  n>0:
		n-=1

countdown(10000)

#@wrap的一个重要特征是它能让你通过属性__wrapped__直接访问被包装函数


#这是python3 独有的，如果用python2运行会报错，说没有__wrapped__属性
gg=countdown.__wrapped__
gg(10000)
print(countdown.__name__)


#如果有多个包装器，那么访问__wrapped__属性的行为是不可预知的，应该避免这样做
def decorator1(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		print("Decorator 1")
		return func(*args,**kwargs)
	return wrapper

def decorator2(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		print("Decorator 2")
		return func(*args,**kwargs)
	return wrapper


@decorator1
@decorator2
def add(x,y):
	return x+y

print(add(3,6))

#定义一个带参数的装饰器

import logging
def logged(level,name=None,message=None):
	def decorator(func):
		logname=name if name else func.__module__
		log=logging.getLogger(logname)
		logmsg=message if message else func.__name__

		@wraps(func)
		def wrapper(*args,**kwargs):
			log.log(level,logmsg)
			return func(*args,**kwargs)
		return wrapper
	return decorator

#Example use
@logged(logging.DEBUG)
def add(x,y):
	return x+y

@logged(logging.CRITICAL,'example')
def spam():
	print('Spam!')
