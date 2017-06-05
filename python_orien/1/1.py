

class Card:
	def __init__(self,rank,suit):
		self.suit=suit
		self.rank=rank
		self.hard,self.soft=self._points()

class NumberCard(Card):
	def _points(self):
		return int(self.rank),int(self,rank)#返回一个元组啦

class AceCard(Card):
	def _points(self):
		return 1,11

class FaceCard(Card):
	def _points(self):
		return 10,10


class Suit:
	def __init__(self,name,symbol):
		self.name=name
		self.symbol=symbol
Club,Diamon,Heart,Spade=Suit('Club','*'),Suit('Diamon',"*"),Suit('Heart',"%"),Suit('Spade','#')




def card(rank,suit):
	if rank==1:return AceCard('A',suit)
	elif 2<=rank<11:return NumberCard(str(rank),suit)
	elif 11<rank<14:
		name={11:'J',12:'Q',13:'K'}[rank]
	else:
		raise Exception('Rank out of range')


#使用映射的card工厂实现
def card2(rank,suit):
	class={1:AceCard,11:FaceCard,12:FaceCard,13:FaceCard}.get(rank,NumberCard)
	return class_(rank,suit)


class_,rank_str={
	1:(AceCard,'A'),
	11:(FaceCard,'J'),
	12:(FaceCard,'Q'),
	13:(FaceCard,'K'),
	}.get(rank,(NumberCard,str(rank)))
return class_(rank_str,suit)
