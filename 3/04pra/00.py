class human:
	age=21
	sex='female'
	color='yellow'
	eye=1.2

	def say():
		print('能说会道')
	def run():
		print('有人是变态啊~')


wxw=human()
'''
print(wxw)
print(type(wxw))
print(id(wxw))
print(human)
print(type(human))
'''
#print(human.__dict__)
#print(wxw.__dict__)
#print(human.sex)
#print(human.eye)
'''
human.say()
print(human.say)


human.hope='halo'
human.tell=lambda:print('actually I love you ')
human.tell()
human.sa=lambda:print('你是不是大笨蛋')
human.sa()
def nikuai():
	print('you should tell me that you love me')
human.kuai=nikuai
human.kuai()
print(human.__dict__)

human.color='blue'
print(human.color)
del human.sex
del human.color
'''
print(wxw.__dict__)
print(wxw.sex)
wxw.sex='male'
print(wxw.sex)
print(wxw.__dict__)
wxw.say=lambda:print('你是大笨蛋吗？')
wxw.say()
wxw.do=lambda:print('我爱你啊！')
wxw.do()
del wxw.say
print(wxw.__dict__)
print(human.__dict__)
del wxw.do
print(wxw.__dict__)
