#_*_ coding:utf-8 _*_
#要改变实例的字符串表示，可以重新定义__str__()和__repr__()方法

class Pair:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __repr__(self):
		return 'Pair({0.x!r},{0.y!r})'.format(self)
	def __str__(self):
		return '({0.x!r},{0.y!r})'.format(self)


#自定义字符串的格式化

_formats={
	'ymd'='{d.year}-{d.month}-{d.day}',
	'mdy'='{d.month}/{d.day}/{d.year}',
	'dmy'='{d.day}/{d.month}/{d.year}'
}

#为了自定义字符串，我们需要在类上面定义__format__()方法。例如：
class Date:
	def __init__(self,year,month,day):
		self.year=year
		self.month=month
		self.day=day
	def __format__(self,code):
		if code='':
			code='ymd'

		fmt=_formats[code]
		return fmt.format(d=self)