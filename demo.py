import tkinter as tk

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Chuyển trang trong Tkinter")

# Thiết lập cấu trúc lưới để các frame chồng lên nhau
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Tạo các frame
login_frame = tk.Frame(root)
register_frame = tk.Frame(root)

login_frame.grid(row=0, column=0, sticky='nsew')
register_frame.grid(row=0, column=0, sticky='nsew')
# for frame in (login_frame, register_frame):
#     frame.grid(row=0, column=0, sticky='nsew')

# Trang đăng nhập
login_label = tk.Label(login_frame, text="Trang Đăng Nhập", font=("Arial", 18))
login_label.pack(pady=20)

login_button = tk.Button(login_frame, text="Đăng nhập", font=("Arial", 14))
login_button.pack(pady=10)

switch_to_register = tk.Button(login_frame, text="Chuyển đến trang Đăng Ký", font=("Arial", 14), command=lambda: show_frame(register_frame))
switch_to_register.pack(pady=10)

# Trang đăng ký
register_label = tk.Label(register_frame, text="Trang Đăng Ký", font=("Arial", 18))
register_label.pack(pady=20)

register_button = tk.Button(register_frame, text="Đăng ký", font=("Arial", 14))
register_button.pack(pady=10)

switch_to_login = tk.Button(register_frame, text="Chuyển đến trang Đăng Nhập", font=("Arial", 14), command=lambda: show_frame(login_frame))
switch_to_login.pack(pady=10)

# Hiển thị trang đăng nhập đầu tiên
show_frame(login_frame)

root.mainloop()
