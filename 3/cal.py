import tkinter
root=tkinter.Tk()
root.geometry('280x395')
#root.maxsize(280,395)
root.title('计算器')
num=tkinter.StringVar()
num.set(0)

#创建Label显示运算结果
label=tkinter.Label(root,textvariable=num,bg='white',font=['黑体',20,'bold'],anchor='e')
label.place(x=20,y=20,width=240,height=30)
isys=False
yslists=[]

def change(no):
    #判断界面原始数字是否为零
    global isys
    if isys==True:
        num.set(no)#按下了运算按钮
        isys=False#将运算标志复位
        pass
    else:
        oldno=num.get()
        if oldno=='0':
            num.set(no)#若初始值为0，直接获取用户输入的值
        else:
            num.set(num.get()+no)#将数字链接起来

def operation(flag):
    #设置运算被按下的标志，被按了是True,没按是False
    global isys
    global yslists
    isys=True
    #将每次运算操作的信息记入一个列表['22','*','8']-->result=eval('',join(['22','*','8']))
    #按下按钮过去界面中已输入的数字
    yslists.append(num.get())
    if flag=='+':
        yslists.append('+')
    if flag == '-':
        yslists.append('-')
    if flag == '*':
        yslists.append('*')
    if flag == '/':
        yslists.append('/')

    yslists.append(flag)
#获取运算结果
def equal():
    global yslists
    #进行运算操作
    #获取当前界面的数字，并且加入运算列表
    yslists.append(num.get())
    print(yslists)
    t='',join(yslists)
    num.set(t)
    #检测最后一位是否是运算符，是就删除
    if t[-1] in '+-*/':
        t=t[0:-1]
    #运算操作
    result=eval(t)
    t.set(result)
    yslists.clear()

#删除操作
def delete():
    if num.get()=='' or num.get()=='0':
        num.set('0')
        return
    else:
        num=len(num.get())
        if num>1:
            strnum=num.get()
            strnum=strnum[0:num-1]
            num.set(strnum)
        else:
            num.set('0')
#清空操作
def clear():
    global yslists
    yslists=[]
    num.set('0')
    isys=False
#正负操作
def fan():
    strnum=num.get()
    if strnum[0]=='-':
        num.set(strnum[1:])
    elif strnum[0]!='-' and strnum !='0':
        num.set('-'+strnum)
button_del=tkinter.Button(root,text = '←',width = 60,height =60,fg='black',command = delete).place(x=20,y=75)

button_clear=tkinter.Button(root,text = 'C',width = 60,height =60,command = clear).place(x=80,y=75)
button_fan=tkinter.Button(root,text = '±',width = 60,height =60,command = fan).place(x=140,y=75)
button_ce=tkinter.Button(root,text = 'CE',width = 60,height =60,command = clear).place(x=200,y=75)

button_1=tkinter.Button(root,text = '1',width = 60,height =60,command = lambda:change('1')).place(x=20,y=135)
button_2=tkinter.Button(root,text = '2',width = 60,height =60,command = lambda:change('2')).place(x=80,y=135)
button_3=tkinter.Button(root,text = '3',width = 60,height =60,command = lambda:change('3')).place(x=140,y=135)
button_jia=tkinter.Button(root,text = '+',width =60,height =60,command = lambda:operation('+')).place(x=200,y=135)

button_4=tkinter.Button(root,text = '4',width = 60,height =60,command = lambda:change('4')).place(x=20,y=195)
button_5=tkinter.Button(root,text = '5',width = 60,height =60,command = lambda:change('5')).place(x=80,y=195)
button_6=tkinter.Button(root,text = '6',width = 60,height =60,command = lambda:change('6')).place(x=140,y=195)
button_jian=tkinter.Button(root,text = '-',width =60,height =60,command = lambda:operation('-')).place(x=200,y=195)

button_7 =tkinter.Button(root,text = '7',width=60,height =60,command = lambda:change('7')).place(x=20,y=255)
button_8 =tkinter.Button(root,text = '8',width=60,height =60,command = lambda:change('8')).place(x=80,y=255)
button_9 =tkinter.Button(root,text = '9',width=60,height =60,command = lambda:change('9')).place(x=140,y=255)
button_cheng =tkinter.Button(root,text = 'x',width =60,height=60,command = lambda:operation('*')).place(x=200,y=255)

button_0 =tkinter.Button(root,text = '0',width =60,height =60,command = lambda:change('0')).place(x=20,y=315)
button_dian =tkinter.Button(root,text = '.',width =60,height=60,command = lambda:change('.')).place(x=80,y=315)
button_deng =tkinter.Button(root,text = '=',width =60,height=60,command = equal).place(x=140,y=315)
button_chu =tkinter.Button(root,text = '/',width =60,height=60,command = lambda:operation('/')).place(x=200,y=315)


root.mainloop()