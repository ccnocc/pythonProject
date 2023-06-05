from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style

# 创建主窗口
root = Tk()
root.title("商城")

# 创建样式对象
style = Style()
style = Style(theme='lumen')#'cyborg''flatly''journal''lumen''minty''pulse''sandstone''simplex''solar''superhero'


# 商品列表
products = [
    {"name": "商品1", "price": 10, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\微信图片_20230323203202.jpg"},
    {"name": "商品2", "price": 20, "type": "类型2", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞1.jpg"},
    {"name": "商品3", "price": 30, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
    {"name": "商品4", "price": 40, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
    {"name": "商品5", "price": 50, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
    {"name": "商品6", "price": 60, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
    {"name": "商品7", "price": 70, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
    {"name": "商品8", "price": 80, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
    {"name": "商品9", "price": 90, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
    {"name": "商品10", "price": 100, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞2.jpg"},
    # 添加更多商品...
]

# 推荐商品列表
reproducts = [
    {"name": "商品1", "price": 10, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\微信图片_20230323203202.jpg"},
    {"name": "商品2", "price": 20, "type": "类型2", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞3.jpg"},
    {"name": "商品3", "price": 30, "type": "类型1", "image": r"C:\Users\dell\Desktop\课程\数字图像处理\images\李瑞3.jpg"},

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

#推荐界面
recommend_label = Label(product_frame, text="推荐", font=("Arial", 16))
recommend_label.grid(row=grid_row , column=grid_column, padx=5, pady=5)

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
    product_label.grid(row=grid_row, column=grid_column+3, sticky="w")

    # 商品类型标签
    type_label = Label(product_frame, text=f"类型: {product['type']}", font=("Arial", 10), fg="gray")
    type_label.grid(row=grid_row , column=grid_column+6, sticky="w")


    # 添加到购物车按钮
    add_button = Button(product_frame, text="加入购物车", command=lambda p=product: add_to_cart(p), bg="#ff4500", fg="white", font=("Arial", 10))
    add_button.grid(row=grid_row , column=grid_column+9, padx=5, pady=5)

    # 删除按钮
    remove_button = Button(product_frame, text="删除", command=lambda p=product: remove_from_cart(p), bg="#ff4500", fg="white", font=("Arial", 10))
    remove_button.grid(row=grid_row , column=grid_column+12, padx=5, pady=5)

    # 更新网格索引
    grid_column += 1
    if grid_column == 1:  # 每行显示3个商品
        grid_row += 3  # 为下一行商品预留4个网格空间
        grid_column = 0

#推荐界面
shopping_label = Label(product_frame, text="所有商品", font=("Arial", 16))
shopping_label.grid(row=grid_row , column=grid_column, padx=5, pady=5)

grid_row = grid_row+1

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
    product_label.grid(row=grid_row, column=grid_column+3, sticky="w")

    # 商品类型标签
    type_label = Label(product_frame, text=f"类型: {product['type']}", font=("Arial", 10), fg="gray")
    type_label.grid(row=grid_row , column=grid_column+6, sticky="w")


    # 添加到购物车按钮
    add_button = Button(product_frame, text="加入购物车", command=lambda p=product: add_to_cart(p), bg="#ff4500", fg="white", font=("Arial", 10))
    add_button.grid(row=grid_row , column=grid_column+9, padx=5, pady=5)

    # 删除按钮
    remove_button = Button(product_frame, text="删除", command=lambda p=product: remove_from_cart(p), bg="#ff4500", fg="white", font=("Arial", 10))
    remove_button.grid(row=grid_row , column=grid_column+12, padx=5, pady=5)

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

# 启动主循环
root.mainloop()
