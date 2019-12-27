class fruit:
	pass
class north:
	pass
class south:
	pass
class gift:
	pass
class nogift:
	pass

class apple(fruit,north,gift):
	pass
class banana(fruit,north,nogift):
	pass
class orange(fruit,south,gift):
	pass
class banana(fruit,south,nogift):
	pass