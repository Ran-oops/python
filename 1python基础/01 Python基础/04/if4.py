#巢状分支

#校门
schooldoor = True
builddoor = True
e classdoor = True
#教室门



#校外走进教室

#检测校门是否打开
if schooldoor == True:#校门开着
    print('校门已开，高高兴兴走进学校，来到楼门前')
    #检测楼门是否打开
    if builddoor == True:#楼门开着
        print('楼门已开，走进大楼，来到了教室门前')
        #检测教室门是否打开
        if classdoor == True:#教室门开
            print('教室门已开，走进教室，好好学习天天想上！')
        else:
            print('教室门没开，王姐，把教室门打开，我们要进去学习')
    else:
        print('楼门没开，张大爷，给我开个门！')
else:
    print('校门没开，高大爷，给我开个门！主要不要你的后门！')
