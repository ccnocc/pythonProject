from tkinter import *
import subprocess
from ttkbootstrap import Style
from PIL import ImageTk, Image
style = Style()
style = Style(theme='pulse')
root = style.master
def login():


    def run1():
        a = inp2.get()
        b = inp2.get()
        s = '登陆成功'
        txt.insert(END, s)
        inp2.delete(0, END)
        inp3.delete(0, END)
        root.destroy()
        shoppingstore()

    def run2():
        register()

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
    btn1 = Button(root, text='注册', command=run2)
    btn1.place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.1)

    txt = Text(root)
    txt.place(rely=0.8, relheight=0.4)
    root.mainloop()

def register():
    root1 = style.master

    def Mysel1():
        dic = {0: '女性', 1: '男性'}
        s = "您的性别是" + dic.get(var1.get())
        lb5.config(text=s)

    def Mysel2():
        dic = {0: '10-20岁', 1: '20-30岁', 2: '30-40岁', 3: '40岁以上'}
        s = "您的年龄是" + dic.get(var2.get())
        lb6.config(text=s)

    def Mysel3():
        dic = {0: '武侠', 1: '科技'}
        s = "您喜欢的书籍类型是" + dic.get(var3.get())
        lb7.config(text=s)

    def run3():
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
    lb1 = Label(root1, text='用户注册', font=(18))
    lb1.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.1)
    lb2 = Label(root1, text='用户名：')
    lb2.place(relx=-0.1, rely=0.1, relwidth=0.8, relheight=0.05)
    lb3 = Label(root1, text='密码：')
    lb3.place(relx=-0.1, rely=0.15, relwidth=0.8, relheight=0.05)

    inp2 = Entry(root1)
    inp2.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.04)
    inp3 = Entry(root1)
    inp3.place(relx=0.35, rely=0.15, relwidth=0.3, relheight=0.04)

    lb4 = Label(root1, text='下面请填写你的基本信息：')
    lb4.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)

    stepp = 0.3
    lb5 = Label(root1, text='请选择性别:')
    lb5.place(relx=0.1, rely=stepp, relwidth=0.8, relheight=0.05)
    var1 = IntVar()
    stepp = stepp + 0.05
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
    btn1 = Button(root1, text='注册', command=run3)
    btn1.place(relx=0.37, rely=stepp, relwidth=0.25, relheight=0.05)

    root1.mainloop()
def shoppingstore():
    # 创建主窗口
    root = Tk()
    root.title("商城")


    # 商品列表
    products = [
        {"name": "商品1", "price": 10, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\微信图片_20230323203202.jpg"},
        {"name": "商品2", "price": 20, "type": "类型2",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞1.jpg"},
        {"name": "商品3", "price": 30, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
        {"name": "商品4", "price": 40, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
        {"name": "商品5", "price": 50, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
        {"name": "商品6", "price": 60, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
        {"name": "商品7", "price": 70, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
        {"name": "商品8", "price": 80, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
        {"name": "商品9", "price": 90, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
        {"name": "商品10", "price": 100, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
        # 添加更多商品...
    ]

    # 推荐商品列表
    reproducts = [
        {"name": "商品1", "price": 10, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\微信图片_20230323203202.jpg"},
        {"name": "商品2", "price": 20, "type": "类型2",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞3.jpg"},
        {"name": "商品3", "price": 30, "type": "类型1",
         "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞3.jpg"},

        # 添加更多商品...
    ]

    # 购物车列表
    cart = []

    # 函数：添加商品到购物车
    def add_to_cart(product):
        cart.append(product)
        cart_text.insert(END, f"{product['name']} - ￥{product['price']}\n")

    # 函数：从购物车中删除商品
    def remove_from_cart(product):
        cart.remove(product)
        cart_text.delete(1.0, END)  # 清空购物车文本框
        for item in cart:
            cart_text.insert(END, f"{item['name']} - ￥{item['price']}\n")

    # 函数：结算购物车
    def checkout():
        total_price = sum(product['price'] for product in cart)
        cart_text.insert(END, f"\n总价：￥{total_price}")

    # 创建顶部标题
    title_label = Label(root, text="商城", font=("Arial", 24, "bold"), padx=20, pady=20)
    title_label.pack()

    # 创建滚动条
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    # 创建Canvas
    canvas = Canvas(root, yscrollcommand=scrollbar.set)
    canvas.pack(fill=BOTH, expand=True)

    # 设置滚动条与Canvas的关联
    scrollbar.config(command=canvas.yview)

    # 创建商品展示区域
    product_frame = Frame(canvas)
    canvas.create_window((0, 0), window=product_frame, anchor="nw")

    # 使用Grid布局管理器
    grid_row = 0
    grid_column = 0

    # 推荐界面
    recommend_label = Label(product_frame, text="推荐", font=("Arial", 16))
    recommend_label.grid(row=grid_row, column=grid_column, padx=5, pady=5)

    grid_row = 1

    for product in reproducts:
        # 商品图片
        image_path = product['image']
        img = Image.open(image_path)
        img = img.resize((100, 100))  # 调整图片大小
        photo = ImageTk.PhotoImage(img)
        image_label = Label(product_frame, image=photo)
        image_label.image = photo
        image_label.grid(row=grid_row, column=grid_column, padx=5, pady=5)

        # 商品名称和价格标签
        product_label = Label(product_frame, text=f"{product['name']} - ￥{product['price']}", font=("Arial", 12))
        product_label.grid(row=grid_row, column=grid_column + 3, sticky="w")

        # 商品类型标签
        type_label = Label(product_frame, text=f"类型: {product['type']}", font=("Arial", 10), fg="gray")
        type_label.grid(row=grid_row, column=grid_column + 6, sticky="w")

        # 添加到购物车按钮
        add_button = Button(product_frame, text="加入购物车", command=lambda p=product: add_to_cart(p), bg="#ff4500",
                            fg="white", font=("Arial", 10))
        add_button.grid(row=grid_row, column=grid_column + 9, padx=5, pady=5)

        # 删除按钮
        remove_button = Button(product_frame, text="删除", command=lambda p=product: remove_from_cart(p), bg="#ff4500",
                               fg="white", font=("Arial", 10))
        remove_button.grid(row=grid_row, column=grid_column + 12, padx=5, pady=5)

        # 更新网格索引
        grid_column += 1
        if grid_column == 1:  # 每行显示3个商品
            grid_row += 3  # 为下一行商品预留4个网格空间
            grid_column = 0

    # 推荐界面
    shopping_label = Label(product_frame, text="所有商品", font=("Arial", 16))
    shopping_label.grid(row=grid_row, column=grid_column, padx=5, pady=5)

    grid_row = grid_row + 1

    for product in products:
        # 商品图片
        image_path = product['image']
        img = Image.open(image_path)
        img = img.resize((100, 100))  # 调整图片大小
        photo = ImageTk.PhotoImage(img)
        image_label = Label(product_frame, image=photo)
        image_label.image = photo
        image_label.grid(row=grid_row, column=grid_column, padx=5, pady=5)

        # 商品名称和价格标签
        product_label = Label(product_frame, text=f"{product['name']} - ￥{product['price']}", font=("Arial", 12))
        product_label.grid(row=grid_row, column=grid_column + 3, sticky="w")

        # 商品类型标签
        type_label = Label(product_frame, text=f"类型: {product['type']}", font=("Arial", 10), fg="gray")
        type_label.grid(row=grid_row, column=grid_column + 6, sticky="w")

        # 添加到购物车按钮
        add_button = Button(product_frame, text="加入购物车", command=lambda p=product: add_to_cart(p), bg="#ff4500",
                            fg="white", font=("Arial", 10))
        add_button.grid(row=grid_row, column=grid_column + 9, padx=5, pady=5)

        # 删除按钮
        remove_button = Button(product_frame, text="删除", command=lambda p=product: remove_from_cart(p), bg="#ff4500",
                               fg="white", font=("Arial", 10))
        remove_button.grid(row=grid_row, column=grid_column + 12, padx=5, pady=5)

        # 更新网格索引
        grid_column += 1
        if grid_column == 1:  # 每行显示3个商品
            grid_row += 3  # 为下一行商品预留4个网格空间
            grid_column = 0

    # 更新Canvas的尺寸
    product_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # 创建底部购物车区域
    cart_frame = Frame(root)
    cart_frame.pack(padx=20, pady=20)

    # 购物车标题
    cart_label = Label(cart_frame, text="购物车", font=("Arial", 16))
    cart_label.pack()

    # 购物车内容
    cart_text = Text(cart_frame, height=10, width=30)
    cart_text.pack()

    # 结算按钮
    checkout_button = Button(cart_frame, text="结算", command=checkout, bg="#ff4500", fg="white", font=("Arial", 12))
    checkout_button.pack(pady=10)

    # 结算按钮
    checkout_button = Button(cart_frame, text="结算", command=checkout, bg="#ff4500", fg="white", font=("Arial", 12))
    checkout_button.pack(pady=10)

    # 启动主循环
    root.mainloop()


if __name__ == '__main__':
    login()