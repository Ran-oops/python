fp = open('test.txt','r+')

fp.seek(4)

fp.truncate()

fp.close()
