#_*_ coding:utf-8_*_
# 简化数据结构的初始化
import math


class Structure1:
    _fields = []

    def __init__(self, *args):
        print("WAHAHAHAHA")
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius**2


#改进版，支持关键字参数
class Structure2:
	_fields=[]
	def __init__(self,*args,**kwargs):
		if len(args)>len(self._fields):
			raise TypeError('Expected {} arguments'.format(len(self._fields)))
		#Set all of the positional arguments
		for name,value in zip(self._fields,args):
			setattr(self,name,value)
		#Set the remaining keyword arguments
		for name in self._fields[len(args):]:
			setattr(self,name,kwargs.pop(name))
		#Check for any remaining unkonwn arguments
		if kwargs:
			raise TypeError('Invalid arguments(s):{}'.format(','.join(kwargs)))

#再改进版，将不在_fields中的名称加入到属性中去：

class Structure3:
	#Class variable that specifies expected fields
	_fields=[]
	def __init__(self,*args,**kwargs):
		if len(args)!=len(self._fields):
			raise TypeError('Expected {} arguments'.format(len(self._fields)))
		#Set the arguments
		for name,value in zip(self._fields,args):
			setattr(self,name,value)
		#Set the additional arguments(if any)
		extra_args=kwargs.keys()-self._fields
		for name in extra_args:
			setattr(self,name,kwargs.pop(name))
		if kwargs:
			raise TypeError('Duplicate values for{}'.format(','.join(kwargs)))


#也可以这样设置属性：self.__dict__.update(xxxx)
#尽管这样也可以正常工作，但是当定义子类的时候问题就来了。当一个子类定义了__slots__或者
#通过property(或描述器)来包装某个属性，那么直接访问实例字典就不起作用了。