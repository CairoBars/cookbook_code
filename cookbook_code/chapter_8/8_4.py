"""创建大量对象时节省内存方法"""
'''
使用slots后节省的内存会跟存储属性的数量和类型有关。 不过，一般来讲，使用到的内
存总量和将数据存储在一个元组中差不多。 为了给你一个直观认识，假设你不使用slots
直接存储一个Date实例， 在64位的Python上面要占用428字节，而如果使用了slots，内
存占用下降到156字节。 如果程序中需要同时创建大量的日期实例，那么这个就能极大的
减小内存使用量了。
尽管slots看上去是一个很有用的特性，很多时候你还是得减少对它的使用冲动。 Python
的很多特性都依赖于普通的基于字典的实现。 另外，定义了slots后的类不再支持一些普
通类特性了，比如多继承。 大多数情况下，你应该只在那些经常被使用到的用作数据结
构的类上定义slots (比如在程序中需要创建某个类的几百万个实例对象)。
关于 __slots__ 的一个常见误区是它可以作为一个封装工具来防止用户给实例增加新的属
性。 尽管使用slots可以达到这样的目的，但是这个并不是它的初衷。 __slots__ 更多的
是用来作为一个内存优化工具。

'''
class Date:
	__slots__=['year','month','day']
	def __init__(self,year,month,day):
		self.year=year
		self.day=day
		self.month=month


#8.5 在类中封装属性名
#Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果

#1.以单个_开头的名字都应该是内部实现
class A:
	def __init__(self):
		self._internal=0 #An internal attribute
		self.public=1 #A public attribute
	def public_method(self):
		'''	A Pulbic method'''
		pass
	def _internal_method(self):
		pass

#2.以双_开头的命名
class B(object):
	"""docstring for B"""
	def __init__(self):
		self.__private=0
	def __private_method(self):
		pass
	def public_method(self):
		pass
		self.__private_method()

#使用双下划线作为开头，会导致访问名称变成其他形式。如：_B__private、_B__private_method

class C(B):
	def __init__(self):
		super().__init__()
		self.__private=1 #Does not override B.__private
	#Does not override B.__private_method()
	def __private_method(self):
		pass

