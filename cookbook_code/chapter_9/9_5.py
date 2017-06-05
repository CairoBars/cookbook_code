"""可自定义属性的装饰器"""
from functools import wraps ,partial
import logging
#Utility decorator to attach a function as a attribute of obj
def attach_wrapper(obj,func=None):
	print("In attach_wrapper")
	print(func)
	if func is None:
		return partial(attach_wrapper,obj)
	setattr(obj,func.__name__,func)
	return func

def logged(level,name=None,message=None):
	def decorator(func):
		logname=name if name else func.__name__
		log=logging.getLogger(logname)
		logmsg=message if message else func.__name__
		print("1")
		@wraps(func)
		def wrapper(*args,**kwargs):
			print("level:%s,msg:%s",level,logmsg)
			log.log(level,logmsg)
			return func(*args,**kwargs)

		#Attach setter functions
		@attach_wrapper(wrapper)
		def set_level(newlevel):
			nonlocal level
			level=newlevel

		@attach_wrapper(wrapper)
		def set_message(newmsg):
			nonlocal logmsg
			logmsg=newmsg
		return wrapper
	return decorator

#Example use
@logged(logging.DEBUG)
def add(x,y):
	return x+y

#add(2,3)

#add.set_message("GGSIMIDA")

#add(2,3)



#日记装饰器的修改版本
def logged2(func=None,*,level=logging.DEBUG,name=None,message=None):
	if func is None:
		print("1")
		return partial(logged2,level=level,name=name,message=message)
	print("2")
	logname=name if name else func.__module__
	print(func.__module__)
	log=logging.getLogger(logname)
	logmsg=message if message else func.__name__

	@wraps(func)
	def wrapper(*args,**kwargs):
		log.log(level,logmsg)
		return func(*args,**kwargs)

	return wrapper

print("suited logged2:--------------------")

@logged2
def test_suit():
	print(test_suit.__module__)


@logged2(message="GGGG")
def test_suit2():
	pass;

