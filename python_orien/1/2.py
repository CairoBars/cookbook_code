#print()函数会调用str()来生成要输出的对象
#字符串的format()函数也可以使用这些方法。当我们使用{!r}或者{!s}格式时，我们实际上分别调用了
#__repr__()或者__str__()方法
class Card:
	insure=False
	def __init__(self,rank,suit):
		self.suit=suit
		self.rank=rank
		self.hard,self.soft=self._points()
class NumberCard(Card):
	def _points(self):
		return int(self.rank),int(self.rank)
