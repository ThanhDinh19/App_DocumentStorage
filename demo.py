import tkinter as tk
import tkinter.font as tkFont

def toggle_underline(event):
    # Lấy kiểu font hiện tại của Label
    font = tkFont.Font(font=label.cget("font"))
    
    # Kiểm tra xem font hiện tại có gạch dưới hay không
    underline = font.cget("underline")
    
    # Đảo ngược trạng thái gạch dưới
    if underline:
        font.config(underline=0)
    else:
        font.config(underline=1)
    
    # Cập nhật lại font cho Label
    label.config(font=font)

root = tk.Tk()
root.title("Label with Underline Toggle")

# Tạo Label
label = tk.Label(root, text="Nhấn vào đây để gạch dưới văn bản", font="TkDefaultFont 12")
label.pack(pady=20)

# Gắn sự kiện nhấn chuột vào Label
label.bind("<Button-1>", toggle_underline)

root.mainloop()
