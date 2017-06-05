#延时计算属性

class lzayproperty:
	def __init__(self,func):
		#导入这个函数时，这里就运行了，并且初始化self为lazyproperty
		#fun为对象的函数：area和perimeter
		self.func=func
		print("1")
		print(self)
		print(func)
	def __get__(self,instance,cls):
		if instance is None:
			print("2")
			print(self)
			return self
		else:
			#第一次调用Circle.area,self为lzeyproperty,instance为Circle Object
			#cls为Circle

			value=self.func(instance)
			setattr(instance,self.func.__name__,value)
			return value


import math
class Circle:
	def __init__(self,radius):
		self.radius=radius
	@lzayproperty
	def area(self):
		print("Computing area")
		return math.pi*self.radius**2
	@lzayproperty
	def perimeter(self):
		print('Computing perimeter')
		return 2*math.pi*self.radius
"""
	很多时候，构造一个延时计算属性的主要目的是为了提升性能。
	当一个描述器被放入一个类的定义时，每次访问属性时它的__get__()、__set()__和__delete__()方法都会被调用
	。不过如果一个描述器仅仅只定义了一个__get()__方法的话，它比通常的具有更弱的绑定。特别
	地，只有当被访问属性不在实例底层的字典中时__get__()方法才会被触发
"""

def lazyproperty2(func):
	name='_lazy_'+func.__name__
	print(name)
	@property
	def lazy(self):
		print("The self is:",self)
		print("The name is: ",name)
		if hasattr(self,name):
			return getattr(self,name)
		else:
			value=func(self)
			setattr(self,name,value)
			return value
	return lazy 

class Circle2:
	def __init__(self,radius):
		self.radius=radius
	@lazyproperty2	#lzayproperty2(area(self))->#lazy(self)
	def area(self):
		print("Computing area")
		return math.pi*self.radius**2
	print(area) #<property object at 0x0*****>
	@lazyproperty2
	def perimeter(self):
		print('Computing perimeter')
		return 2*math.pi*self.radius


#这个方法有一个缺点，那就是所有get操作都必须被定向到属性getter函数上去

class myClass:

	@property
	def ohMyGod(self):
		print("OOOOOOOO")
		