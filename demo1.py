import tkinter as tk

root = tk.Tk()

# Cấu hình hàng và cột với trọng số khác nhau
root.rowconfigure(0, weight=1)  # Hàng đầu tiên
root.rowconfigure(1, weight=3)  # Hàng thứ hai

root.columnconfigure(0, weight=3)  # Cột đầu tiên
root.columnconfigure(1, weight=3)  # Cột thứ hai

# Thêm các widget vào lưới
btn1 = tk.Button(root, text="Button 1", bg="red")
btn2 = tk.Button(root, text="Button 2", bg='yellow')
btn3 = tk.Button(root, text="Button 3", bg="purple")
btn4 = tk.Button(root, text="Button 4", bg="gray")


btn1.grid(row=0, column=0, sticky="nsew")
btn2.grid(row=0, column=1, sticky="nsew")
btn3.grid(row=1, column=0, sticky="nsew")
btn4.grid(row=1, column=1, sticky="nsew")

def toggle_color(): 
    btn1_now_bgcolor = btn1.cget("bg")
    btn2_now_bgcolor = btn2.cget("bg")
    btn3_now_bgcolor = btn3.cget("bg")
    btn4_now_bgcolor = btn4.cget("bg")
    if btn1_now_bgcolor == "red":
        btn1.config(bg="purple")
    else:
        btn1.config(bg="red")

    if btn2_now_bgcolor == "yellow":
        btn2.config(bg="red")
    else:
        btn2.config(bg="yellow")
  
    if btn3_now_bgcolor == "purple":
        btn3.config(bg="gray")
    else:
        btn3.config(bg="purple")

    if btn4_now_bgcolor == "gray":
        btn4.config(bg="yellow")
    else:
        btn4.config(bg="gray")



    btn1.after(250, toggle_color)

toggle_color()

root.mainloop()
