import tkinter as tk
from ttkbootstrap import Style

def send_message():
    message = input_box.get()
    chat_log.insert(tk.END, "You: " + message + "\n")
    # 在这里添加发送消息的代码，可以将消息发送给客服或者进行其他处理
    input_box.delete(0, tk.END)

# 创建主窗口
window = tk.Tk()
window.title("客服界面")
style = Style()
style = Style(theme='cyborg')


# 创建聊天记录文本框
chat_log = tk.Text(window, height=20, width=50)
chat_log.pack()

# 创建消息输入框
input_box = tk.Entry(window, width=50)
input_box.pack()

# 创建发送按钮
send_button = tk.Button(window, text="发送", command=send_message)
send_button.pack()

# 运行主循环
window.mainloop()
