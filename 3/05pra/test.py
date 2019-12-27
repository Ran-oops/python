class human:
	def __new__(cls):
		return object.__new__(monkey)
class monkey:
	pass
one=human()
print(one)