from tkinter import *
from ttkbootstrap import Style
root1 = Tk()
style = Style()
style = Style(theme='sandstone')

def Mysel1():
    dic={0:'女性',1:'男性'}
    s="您的性别是"+dic.get(var1.get())
    lb5.config(text=s)

def Mysel2():
    dic = {0: '10-20岁', 1: '20-30岁',2:'30-40岁',3:'40岁以上'}
    s = "您的年龄是" + dic.get(var2.get())
    lb6.config(text=s)

def Mysel3():
    dic = {0: '武侠', 1: '科技'}
    s = "您喜欢的书籍类型是" + dic.get(var3.get())
    lb7.config(text=s)

def run1():
    def close_window():
        root2.destroy()
    root1.destroy()
    root2 = Tk()
    root2.geometry('160x80')
    root2.title('注册界面')
    lb = Label(root2, text='注册成功', font=(18))
    lb.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.2)
    btn = Button(root2, text='OK', command=close_window)
    btn.place(relx=0.2, rely=0.35, relwidth=0.25, relheight=0.2)
    root2.mainloop()


root1.geometry('460x628')
root1.title('注册界面')
lb1=Label(root1, text='用户注册', font=(18))
lb1.place(relx=0.1,rely=0,relwidth=0.8,relheight=0.1)
lb2=Label(root1, text='用户名：')
lb2.place(relx=-0.1,rely=0.1,relwidth=0.8,relheight=0.05)
lb3=Label(root1, text='密码：')
lb3.place(relx=-0.1,rely=0.15,relwidth=0.8,relheight=0.05)

inp2=Entry(root1)
inp2.place(relx=0.35,rely=0.1,relwidth=0.3,relheight=0.04)
inp3=Entry(root1)
inp3.place(relx=0.35,rely=0.15,relwidth=0.3,relheight=0.04)

lb4 = Label(root1, text='下面请填写你的基本信息：')
lb4.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)

stepp=0.3
lb5 = Label(root1, text='请选择性别:')
lb5.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)
var1 = IntVar()
stepp = stepp+0.05
rd51 = Radiobutton(root1, text='女性', variable=var1, value=0, command=Mysel1)
rd51.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)
stepp = stepp + 0.05
rd52 = Radiobutton(root1, text='男性', variable=var1, value=1, command=Mysel1)
rd52.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)

lb6 = Label(root1, text='请选择年龄:')
stepp = stepp + 0.05
lb6.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)
var2 = IntVar()
rd61 = Radiobutton(root1, text='10-20岁', variable=var2, value=0, command=Mysel2)
stepp = stepp + 0.05
rd61.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)
rd62 = Radiobutton(root1, text='20-30岁', variable=var2, value=1, command=Mysel2)
stepp = stepp + 0.05
rd62.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)
rd63 = Radiobutton(root1, text='30-40岁', variable=var2, value=2, command=Mysel2)
stepp = stepp + 0.05
rd63.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)
rd64 = Radiobutton(root1, text='40岁以上', variable=var2, value=3, command=Mysel2)
stepp = stepp + 0.05
rd64.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)


lb7 = Label(root1, text='请选择喜欢的书籍类型:')
stepp = stepp + 0.05
lb7.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)
var3 = IntVar()
rd71 = Radiobutton(root1, text='武侠', variable=var3, value=0, command=Mysel3)
stepp = stepp + 0.05
rd71.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)
rd72 = Radiobutton(root1, text='科技', variable=var3, value=1, command=Mysel3)
stepp = stepp + 0.05
rd72.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)

stepp = stepp + 0.1
btn1 = Button(root1, text='注册', command=run1)
btn1.place(relx=0.37, rely=stepp, relwidth=0.25, relheight=0.05)



root1.mainloop()