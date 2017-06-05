def test_func(x="GGGGGGGG"):
	'''
	my test function
	'''
	a=1
	def gg():
		nonlocal a
		a+=1
		print(a)
	gg()




from functools import partial


#setattr(object,name,value) For example setattr(x,'foobar',123) is equivalent to x.foobar=123
count=0

def attach_wrapper(obj,func=None):
	print("obj",obj)
	print(func)
	if func is None:
		print("1")
		return partial(attach_wrapper,obj)
		#return attach_wrapper
	print("2")
	print(func.__name__)
	setattr(obj,func.__name__,func)
	return func


def jj():
	print("In jj")

@attach_wrapper(jj)
def kk():
	print("RRRR")

	

