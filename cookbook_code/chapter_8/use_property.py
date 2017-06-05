class Person:
	def __init__(self,first_name):
		#第一次初始化时就调用了类里面的first_name的setter方法
		self.first_name=first_name

	@property
	def first_name(self):
		return self._first_name

	print(first_name.setter)
	@first_name.setter
	def first_name(self,value):
		print("ohMyGod")
		self._first_name=value

#子类扩展property

class MyPerson:
	def __init__(self,name):
		print("In MyPerson init")
		self.name=name
	#Getter function
	@property
	def name(self):
		return self.name
	#Setter function
	@name.setter
	def name(self,value):
		print("In MyPerson's setter")
		if not isinstance(value,str):
			raise TypeError('Excepted a string')
		self._name=value
	#Deleter function
	@name.deleter
	def name(self):
		raise AttributeError("Can't delete attribute")

class MySubPerson(MyPerson):
	@property
	def name(self):
		print("Getting name")
		return super().name

	@name.setter
	def name(self,value):
		print("Setting name to ",value)
		super(MySubPerson,MySubPerson).name.__set__(self,value)

	@name.deleter
	def name(self):
		print("Deleting name")
		super(MySubPerson,MySubPerson).name.__delete__(self)


#test sub class
class A:
	def __init__(self):
		print(self)

class B(A):
	def getA(self):
		gg=super()
		print(gg)



