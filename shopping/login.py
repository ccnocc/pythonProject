from tkinter import *
import subprocess
from ttkbootstrap import Style
root = Tk()
style = Style()
style = Style(theme='sandstone')

def run1():
    username = inp2.get() # 获取用户名
    password = inp3.get() # 获取密码
    s = '登陆成功'
    txt.insert(END, s)
    inp2.delete(0, END)
    inp3.delete(0, END)
    subprocess.run(['python', 'shoppingstore.py'])

def register():
    subprocess.run(['python', 'register.py'])

__file__ = '登录界面.py'
root.geometry('460x240')
root.title('登陆界面')

lb1 = Label(root, text='登陆界面', font=(20))
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
lb2 = Label(root, text='用户名：')
lb2.place(relx=-0.1, rely=0.3, relwidth=0.8, relheight=0.1)
lb3 = Label(root, text='密码：')
lb3.place(relx=-0.1, rely=0.45, relwidth=0.8, relheight=0.1)

inp2 = Entry(root)
inp2.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.1)
inp3 = Entry(root)
inp3.place(relx=0.35, rely=0.45, relwidth=0.3, relheight=0.1)

btn1 = Button(root, text='登录', command=run1)
btn1.place(relx=0.2, rely=0.6, relwidth=0.25, relheight=0.1)
btn1 = Button(root, text='注册', command=register)
btn1.place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.1)

txt = Text(root)
txt.place(rely=0.8, relheight=0.4)
root.mainloop()

