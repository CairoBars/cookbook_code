#_*_ conding:utf-8_*_
#实现数据模型和类型约束
#在这种情况下，你需要对某些实例属性赋值时进行检查。
#所有你要自定义属性赋值函数，这种情况下最好使用描述器
#Base class.Uses a descriptor to set a value
class Descriptor:
	def __init__(self,name=None,**opts):
		self.name=name
		print("After set ")
		for key,value in opts.items():
			setattr(self,key,value)
	
	def __set__(self,instance,value):
		print("Descriptor")
		print(instance)
		instance.__dict__[self.name]=value

#Descriptor for enforcing types
class Typed(Descriptor):
	except_type=type(None)

	def __set__(self,instance,value):
		print("Typed")
		print(instance)
		if not isinstance(value,self.except_type):
			raise TypeError('expected'+str(self.except_type))
		super().__set__(instance,value)

#Descriptor for enforcing values
class Unsigned(Descriptor):
	def __set__(self,instance,value):
		print("Unsigned")
		print(instance)
		if value<0:
			raise ValueError('Expected>=0')
		super().__set__(instance,value)

class MazSized(Descriptor):
	def __init__(self,name=None,**opts):
		if 'size' not in opts:
			raise TypeError('missing size option')
		super().__init__(name,**opts)

	def __set__(self,instance,value):
		if len(value)>=self.size:
			raise ValueError('size must be <'+str(self.size))
		super().__set__(instance,value)

class Integer(Typed):
	except_type=int 

class UnsignedInteger(Unsigned,Integer):
	pass

class Stock:
	#Specify constrains
	shares=UnsignedInteger("shares")

	def __init__(self,shares):
		self.shares=shares

b=Stock(2)



