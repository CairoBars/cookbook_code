def a():
	def b():
		print("B")

	
	print(a.__name__)
	setattr(a,b.__name__,b)
	return a


g=a()
g.b()
print("-----------------------------------------")


def my_partical(func, *args, **keywords):
	def newfunc(*fargs, **fkeywords):
		newkeywords = keywords.copy()
		newkeywords.update(fkeywords)
		return func(*(args + fargs), **newkeywords)
	newfunc.func = func
	print(func)
	newfunc.args = args
	print(args)
	newfunc.keywords = keywords
	print(keywords)
	return newfunc





def xx(x,y):
	print(x)
	print(y)
	pass;

x=my_partical(xx,2)
print(x)
print(x.args)
x(3)


print("test __dict__-----------------------------------------")

def show_dic():
	show_dic.a=2333
	print(show_dic.__dict__)

show_dic()


print("test wrapper:-------------------------------------------")
from functools_code import wraps


def my_decorator(func):
	@wraps(func)#这里已经返回了一个wrapper2对象，看源码可知
	def wrapper2(*args,**keywords):
		print(wrapper2.__name__)
		print(wrapper2.__doc__)
		return func(*args,**keywords) #执行并返回结果或没有结果，而不是直接返回对象
	return wrapper2


@my_decorator
def test_dec():
	"""RRRRR"""
	print("test pass")


test_dec()

print("finally become:",test_dec)





"""
def my_decorator(func,mes=None):
	def ggsimida(name,*args,**keywords):
		print("GGGGG")
		return func(*args,**keywords)
	return ggsimida

@my_decorator
def bb():
	pass

bbb=bb("GGGGG")
"""





	



