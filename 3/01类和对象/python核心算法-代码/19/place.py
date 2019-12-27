#绝对定位布局
import tkinter

root = tkinter.Tk()
root.minsize(300,300)

btn1 = tkinter.Button(root,text = 'button1')
btn1.place(x = 10,y = 10)

btn2 = tkinter.Button(root,text = 'button2')
btn2.place(x = 10,y = 50)

btn3 = tkinter.Button(root,text = 'button3')
btn3.place(x = 10,y = 90)

btn4 = tkinter.Button(root,text = 'button4')
btn4.place(x = 90,y = 10)

btn5 = tkinter.Button(root,text = 'button5')
btn5.place(x = 90,y = 50)

btn6 = tkinter.Button(root,text = 'button6')
btn6.place(x = 90,y = 90)

btneq = tkinter.Button(root,text = '=')
btneq.place(x = 170,y = 10,width = 50 ,height = 110)

btn0 = tkinter.Button(root,text = '0')
btn0.place(x = 10,y = 130,width = 200 ,height = 30)


root.mainloop()
