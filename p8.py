class mech:
	def __init__ (self, price):
		self.price = price
	def __add__ (self, other):
		res = self.price + other.amount
		return res
	def __sub__ (self, other):
		res = self.price - other.amount
		return res
class bee:
	def __init__ (self, amount):
		self.amount = amount
	def __sub__ (self, other):
		res = self.amount - other.price
		return res
m = mech(750)
b = bee(350)

r1 = m + b; print(r1)
r2 = m - b; print(r2)
r3 = b - m; print(r3)