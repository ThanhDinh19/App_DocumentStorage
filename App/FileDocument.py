from Librarys import *

class FileDocument:
    def __init__(self, window, file_name, file_path):
        self.window = window
        self.file_name = file_name
        self.file_path = file_path
        
    file_to_save = "file_document\\files.json"  

    @staticmethod
    def read_file(file_to_encode): #hàm dùng để mã hóa file
        with open(file_to_encode, 'rb') as fi:
            data_encoded = base64.b64encode(fi.read()).decode('utf-8')
        return data_encoded
    
    @staticmethod
    def write_file(file_encoded, output_file): #hàm dùng để giải mã file đã được mã hóa
        data_decoded = base64.b64decode(file_encoded)
        with open(output_file, 'wb') as fi:
            fi.write(data_decoded)

    def load_file(self):
        if os.path.exists(self.file_to_save):
            with open(self.file_to_save, 'r') as fi:
                data_file = json.load(fi)
            return data_file
        return []
    
    def save_file(self):
        data_file = self.load_file()
        file_data_encoded = FileDocument.read_file(self.file_path.get())
        extensions = self.file_path.get().split('.')[-1]
        file = {"Name": self.file_name.get(), "File": file_data_encoded, "Extensions": extensions}
        data_file.append(file)
        with open(self.file_to_save, 'w') as fi_save:
            json.dump(data_file, fi_save, indent = 4, default = lambda x: x.__dict__)

    def save_file_data(self, data_file):
        with open(self.file_to_save, 'w') as fi_save_data:
            json.dump(data_file, fi_save_data, indent = 4, default = lambda x: x.__dict__)
        
    def input_file(self):
        def add():
            try:
                self.save_file()
                name_entry.delete(0, 'end')
                path_entry.delete(0, 'end')
                notification.config(text = "Add successful", fg = "green")
            except:
                name_entry.delete(0, 'end')
                path_entry.delete(0, 'end')
                notification.config(text = "Add failed. Try again", fg = "red")
        def back():
            canvas_main.destroy()

        self.file_name = StringVar()
        self.file_path = StringVar()
        canvas_main = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
        canvas_main.place(x = 50, y = 118)
        title = Label(canvas_main, text="ADD FILE", font=("Time new roman", 14, "bold"), bg = "#e6e6fa")
        name = Label(canvas_main, text = "Name", font=("Time new roman", 12), bg = "#e6e6fa")
        path = Label(canvas_main, text = "Path", font=("Time new roman", 12), bg = "#e6e6fa")
        notification = Label(canvas_main, text = "", bg = "#e6e6fa")
        name_entry = Entry(canvas_main, width = 30, textvariable=self.file_name)
        path_entry = Entry(canvas_main, width = 30, textvariable=self.file_path)
        btn_add = Button(canvas_main, text="Add", width = 5, command=add)
        btn_back = Button(canvas_main, text = "Back", width = 5, command=back)
        title_w = canvas_main.create_window(250, 30, window=title)
        name_w = canvas_main.create_window(110, 80, window = name)
        path_w = canvas_main.create_window(110, 120, window = path)
        name_entry_w = canvas_main.create_window(250, 80, window=name_entry)
        path_entry_w = canvas_main.create_window(250, 120, window=path_entry)
        btn_add_w = canvas_main.create_window(320, 160, window=btn_add)
        btn_back_w = canvas_main.create_window(180, 160, window=btn_back)
        notification_w = canvas_main.create_window(250, 200, window = notification)
    
    

    def read_file_txt(self, data_file, index, show_window):
        name = data_file[index]["Name"]
        file = data_file[index]["File"]
        extension = data_file[index]["Extensions"]
        output_file_path = f"file_document\\outputFile\\{name}.{extension}"
        self.write_file(file, output_file_path)

        with open(output_file_path, 'r', encoding='utf8') as fi_read:
            data = fi_read.readlines()
        text = Text(show_window)
        text.pack(fill='both', expand=True)
        for item in data:
            text.insert('end', item)

    def read_file_docx(self, data_file, index, show_window):
        name = data_file[index]["Name"]
        file = data_file[index]["File"]
        extension = data_file[index]["Extensions"]
        output_file_path = f"file_document\\outputFile\\{name}.{extension}"
        self.write_file(file, output_file_path)

        data = Document(output_file_path)
        text = Text(show_window)
        text.pack(fill='both', expand=True)
        for item in data.paragraphs:
            text.insert('end', item.text+'\n')

    def read_file_pdf(self, data_file, index, show_window):
        name = data_file[index]["Name"]
        file = data_file[index]["File"]
        extension = data_file[index]["Extensions"]
        output_file_path = f"file_document\\outputFile\\{name}.{extension}"
        self.write_file(file, output_file_path)

        data = fitz.open(output_file_path)
        text = Text(show_window)
        text.pack(fill='both', expand=True)
        for index in range(data.page_count):
            page = data.load_page(index)
            text.insert('end', page.get_text())
            text.insert('end', '-'*87+'\n')

    def show_window_paragraphs(self, data_file, index, name_of_file, extension_of_file):
        show_window = Toplevel(self.window)
        show_window.geometry("700x600")
        show_window.title(f"{name_of_file}.{extension_of_file}")
        if extension_of_file == 'txt':
            show_window.iconbitmap("Logo\\txt_logo.ico")
            self.read_file_txt(data_file, index, show_window)
        elif extension_of_file == 'docx':
            show_window.iconbitmap("Logo\\docx_logo.ico")
            self.read_file_docx(data_file, index, show_window)
        else:
            show_window.iconbitmap("Logo\\pdf_logo.ico")
            self.read_file_pdf(data_file, index, show_window)

    def show_file(self):
        data_file = self.load_file()

        def show(file):
            index = file.index
            name = data_file[index]['Name']
            extension = data_file[index]['Extensions']
            self.show_window_paragraphs(data_file, index, name, extension)
        
        def back():
            canvas_main.destroy()

        canvas_main = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
        canvas_main.pack(side='left', fill = 'both', expand=True)

        scrollbar = Scrollbar(canvas_main, orient=VERTICAL, command=canvas_main.yview)  
        scrollbar.pack(side='right', fill='y')

        btn_back = Button(canvas_main, text = "Back", width = 8, command=back)
        canvas_main.create_window((530, 640), window=btn_back)

        canvas_main.config(yscrollcommand=scrollbar.set)   

        file_frame = Frame(canvas_main, bg = '#d3d3d3')
        canvas_main.create_window((0, 0), window=file_frame, anchor='nw')

        row_val = 0
        col_val = 0
        for index, item in enumerate(data_file):
            labelframe_file = LabelFrame(file_frame, text = "")
            file = Button(labelframe_file, text=f"{item['Name']}.{item['Extensions']}", borderwidth=0, relief='flat', command=lambda file = labelframe_file: show(file))
            file.pack()
            labelframe_file.grid(row = row_val, column = col_val, pady = 10, padx = 10, sticky='w')
            labelframe_file.index = index
            labelframe_file.file = file
            col_val += 1
            if col_val == 1:
                col_val = 0
                row_val += 1
    
    def delete_file(self):
        data_file = self.load_file()
        def delete():
            for chk, var in zip(checkButtons, status):
                if var.get():
                    confrim_delete = mb.askyesno("Are you sure you want to delete this file ?")
                    if confrim_delete:
                        chk.pack_forget()
                        checkButtons.remove(chk)
                        status.remove(var)
                        index = chk.index
                        del data_file[index]
                        new_file_data = data_file
                        self.save_file_data(new_file_data)
                    else:
                        return
                    
        def back():
            canvas_main.destroy()
                    
        canvas_main = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
        canvas_main.pack(side='left', fill = 'both', expand=True)
        
        btn_delete = Button(canvas_main, text ="Delete", bg = 'red', command=delete)
        canvas_main.create_window((540, 40), window=btn_delete)
        btn_back = Button(canvas_main, text = "Back", width = 8, command=back)
        canvas_main.create_window((540, 640), window=btn_back)

        scrollbar = Scrollbar(canvas_main, orient=VERTICAL, command=canvas_main.yview)  
        scrollbar.pack(side='right', fill='y')
        canvas_main.config(yscrollcommand=scrollbar.set)

        frameCheckButton = Frame(canvas_main)
        canvas_main.create_window((10, 10), window=frameCheckButton, anchor='nw')
        checkButtons = []
        status = []
        for index, item in enumerate(data_file):
            var = BooleanVar()
            chk = Checkbutton(frameCheckButton, text = f"{item['Name']}.{item['Extensions']}", variable=var)
            chk.pack(pady=5, anchor='w')
            checkButtons.append(chk)
            status.append(var)
            chk.index = index
            
def main():
    root = Tk()
    root.geometry("600x700")
    root.iconbitmap("Logo\\logo_app.ico")
    root.title("NOTE TAKING AND DOCUMENT STORAGE")    

    file = FileDocument(root, "", "")
    file.delete_file()
    

    root.mainloop() 
if __name__ == "__main__":
    main() 
    