"""调用父类的方法"""
"""如何在子类中调用父类某个已经被覆盖的方法"""
"""super()的一个常见用法在__init__()确保父类被正确的初始化了"""
class A:
	def spam(self):
		print('A.spam')
class B:
	def spam(self):
		print('B.spam')
		super().spam()

class Proxy:
	def __init__(self,obj):
		self._obj=obj
	#Delegate attribute lookup to internal obj
	def __getattr__(self,name):
		return getattr(self._obj,name)
	#Deleagate attribute assignment
	def __setattr__(self,name,value):
		if name.startswith('_'):
			super().__setattr__(name,value) #Call original __setattr__
		else:
			setattr(self._obj,name,value)

