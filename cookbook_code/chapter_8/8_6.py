"""创建可管理的属性"""
#自定义属性的一个简单方法就是将它定义为一个property
class Person:
	def __init__(self,first_name):
		self.first_name=first_name

	#Getter function
	@property
	def first_name(self):
		return self._first_name

	#Setter function
	@first_name.setter
	def first_name(self,value):
		if not isinstance(value,str)
			raise TypeError('Expected a string')
		self._first_name=value

	#Deleter function(optional)
	@first_name.deleter
	def first_name(self):
		raise AttributeError("Can't delete attribute")

#第一个方法是个getter函数，它使得first_name成为一个属性

#其他两个方法给first_name属性添加setter和deleter方法。

#property的一个关键特性是它看上去跟普通的attribute没什么两样



#在__init__()方法中也进行类型检查：
class Person:
	def __init__(self,first_name):
		self.set_first_name(first_name)

	#Getter function
	def get_first_name(self):
		return self.first_name

	#Setter function
	def set_first_name(self,value):
		if not isinstance(value,str):
			raise TypeError('Expected a string')

	#Deleter function(optional)
	def del_first_name(self):
		raise AttributeError("Can't not delete attribute")

	#Make a property from existing get/set methods
	name=property(get_first_name,set_first_name,del_first_name)

"""
一个property属性其实就是一系列相关绑定方法的集合。如果你去查看拥有property的
类， 就会发现property本身的fget、fset和fdel属性就是类里面的普通方法。比如:
>>> Person.first_name.fget
<function Person.first_name at 0x1006a60e0>
>>> Person.first_name.fset
<function Person.first_name at 0x1006a6170>
>>> Person.first_name.fdel
<function Person.first_name at 0x1006a62e0>
>>>

"""

#Property还是一个定义动态计算attribute的方法。这种类型的attributes并不会被实际的存储，
#而是在需要的时候计算出来：
import math
class Circle:
	def __init__(self,radius):
		self.radius=radius
	@property
	def area(self):
		return math.pi*self.radius**2
	@property 
	def diameter(self):
		return self.radius**2
	@property 
	def perimeter(self):
		return 2*math.pi*self.radius
		
