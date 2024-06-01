from Librarys import *

class ImageDocument:
    file_input_img = "image_document\\Images.json"
    def __init__(self, window, img_path, img_name):
        self.img_path = img_path
        self.img_name = img_name
        self.window = window
    
    @staticmethod
    def read_img(img_path):
        with open(img_path, 'rb') as fi_img:
            encode_img = base64.b64encode(fi_img.read()).decode('utf-8') #mã hóa hình ảnh và chuyển đổi dưới dạng văn bản sử dụng mã hóa utf8
        return encode_img    
    
    @staticmethod
    def write_img(encode_img, output_path):
        img = base64.b64decode(encode_img) #giải mã hình ảnh (kết quả là dữ liệu nhị phân gốc dưới dạng chuỗi byte)
        with open(output_path, 'wb') as fi_w:
            fi_w.write(img)

    @staticmethod
    def save_img(img_name, img_path, file_input_img):
        data = ImageDocument.load_img(file_input_img)#tải sữ liệu
        img_data = ImageDocument.read_img(img_path)#mã hóa ảnh
        img = {"Name": img_name, "Img": img_data}
        data.append(img)
        with open(file_input_img, 'w') as fi_save:
            json.dump(data, fi_save, indent = 4, default=lambda x: x.__dict__)

    def save_data_img(data_images, file_save):
        with open(file_save, 'w') as fi_save_data:
            json.dump(data_images, fi_save_data, indent = 4, default = lambda x: x.__dict__)


    @staticmethod
    def load_img(fi_input_img):
        if os.path.exists(fi_input_img):
            with open(fi_input_img, 'r') as fi_load:
                data = json.load(fi_load)
                return data
        else:
            return []
            
    def input_img(self):
        self.img_name = StringVar()
        self.img_path = StringVar()

        def add():
            imgName = self.img_name.get()
            imgPath = self.img_path.get()
            try:
                ImageDocument.save_img(imgName, imgPath, ImageDocument.file_input_img)
                notification.config(text = "Add successful", fg = "green")
                name_entry.delete(0, 'end')
                path_entry.delete(0, 'end')
            except:
                name_entry.delete(0, 'end')
                path_entry.delete(0, 'end')
                notification.config(text = "Add failed. Try again", fg = "red")

        def back():
            canvas_main.destroy()

        canvas_main = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
        canvas_main.place(x = 50, y = 118)
        title = Label(canvas_main, text="ADD IMAGE", font=("Time new roman", 14, "bold"), bg = "#e6e6fa")
        name = Label(canvas_main, text = "Name", font=("Time new roman", 12), bg = "#e6e6fa")
        path = Label(canvas_main, text = "Path", font=("Time new roman", 12), bg = "#e6e6fa")
        notification = Label(canvas_main, text = "", bg = "#e6e6fa")
        name_entry = Entry(canvas_main, width = 30, textvariable=self.img_name)
        path_entry = Entry(canvas_main, width = 30, textvariable=self.img_path)
        btn_add = Button(canvas_main, text="Add", width = 5, command=add)
        btn_back = Button(canvas_main, text = "Back", width = 5, command=back)
        title_w = canvas_main.create_window(250, 30, window=title)
        name_w = canvas_main.create_window(50, 80, window = name)
        path_w = canvas_main.create_window(50, 120, window = path)
        name_entry_w = canvas_main.create_window(250, 80, window=name_entry)
        path_entry_w = canvas_main.create_window(250, 120, window=path_entry)
        btn_add_w = canvas_main.create_window(320, 160, window=btn_add)
        btn_back_w = canvas_main.create_window(180, 160, window=btn_back)
        notification_w = canvas_main.create_window(250, 200, window = notification)


    def list_imgs_to_show(self, canvas_show_main, canvas_lstbox, scrollbar, listbox, list_names):  
        def Exit_():
            canvas_show_main.destroy()

        lb = Label(canvas_show_main, text = "IMAGES", font=("Time new roman", 16, "bold"))
        btn_exit = Button(canvas_show_main, text = "Back", width = 10, command = Exit_)
        btn_exit.place(x=390, y = 340)
        lb_win = canvas_show_main.create_window(250, 30, window = lb)

        scrollbar.config(command = listbox.yview)
        for index, item in enumerate(list_names):
            listbox.insert(index*2 + 1, "* "+item)
            listbox.insert(index*2 + 2, " "*60)
        
    def show_img(self): #hàm hiển thị ảnh kiểu cũ
        file_img = ImageDocument.file_input_img
        data = ImageDocument.load_img(file_img)
        names = []
        if len(data) != 0:
            for item in data:
                names.append(item['Name'])

        def show(event):
            outputImage = ImageDocument.file_output_img
            selected_indices = listbox.curselection()
            index = int(selected_indices[0])
            if index % 2 == 0 and selected_indices:
                
                name_img = listbox.get(index)[2:] #lấy nội dung từ listbox ngay mục index               
                image = next((item['Img'] for item in data if item['Name'] == name_img), None)            
                try:
                    path_output_img = f"image_document\\outputImage\\{name_img+".jpg"}"
                    
                    ImageDocument.write_img(image, path_output_img)  
                    img = Image.open(path_output_img)
                    img = img.resize((380, 280), Image.LANCZOS) 
                    img_tk = ImageTk.PhotoImage(img)

                    image_window = Toplevel(self.window)
                    image_window.geometry("400x300")
                    image_window.iconbitmap("Logo\\gallery.ico")
                    image_window.title("Image")
                    lb_img = Label(image_window, image=img_tk)
                    lb_img.pack(fill='both', expand=True)          
                    image_window.img_tk = img_tk
                except(NameError, TypeError, ValueError) as err:
                    mb.showinfo(f"Error: {err}")
            else:
                return

        canvas_show_main = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
        canvas_show_main.place(x = 50, y = 118)

        canvas_lstbox = Canvas(canvas_show_main)
        canvas_lstbox.place(x=30, y=80)

        scrollbar = Scrollbar(canvas_lstbox, orient = VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(canvas_lstbox, yscrollcommand=scrollbar.set, font=("Time new roman", 12), width=30, height=15)#lstbox chứa name img
        listbox.pack(fill = BOTH)
        self.list_imgs_to_show(canvas_show_main, canvas_lstbox, scrollbar, listbox, names)  
        listbox.bind("<<ListboxSelect>>", show)


    def show_img_upgrade(self):  #hàm hiển thị ảnh đã được cải tiến
        file_img = ImageDocument.file_input_img
        data = ImageDocument.load_img(file_img)
        row_val = 0
        col_val = 0

        list_img_resize = [] #list này điều chỉ điều chỉnh lại kích thước cho button
        list_img = ImageDocument.list_images() #list đường dẫn của tất cả hình ảnh được lưu
        
        for img in list_img:
            image = Image.open(img)
            image = image.resize((90, 80), Image.LANCZOS)
            imageTk = ImageTk.PhotoImage(image)
            list_img_resize.append(imageTk)

        def show(photo):
            index = photo.index
            img = data[index]['Img']
            name_img = data[index]['Name']
            
            path_output_img = f"image_document\\outputImage\\{name_img+".jpg"}"
            ImageDocument.write_img(img, path_output_img)  
            img = Image.open(path_output_img)
            img = img.resize((380, 280), Image.LANCZOS) 
            img_tk = ImageTk.PhotoImage(img)
            image = img_tk

            image_window = Toplevel(self.window)
            image_window.geometry("400x300")
            image_window.iconbitmap("Logo\\gallery.ico")
            image_window.title("Image")
            lb_img = Label(image_window, image=image)
            lb_img.pack(fill='both', expand=True)          
            image_window.image = image

        def back():
            canvas_main.destroy()

        canvas_main = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
        canvas_main.pack(side='left', fill = 'both', expand=True)

        scrollbar = Scrollbar(canvas_main, orient=VERTICAL, command=canvas_main.yview)  
        scrollbar.pack(side='right', fill='y')

        btn_back = Button(canvas_main, text = "Back", width = 8, command=back)
        canvas_main.create_window((530, 640), window=btn_back)

        canvas_main.config(yscrollcommand=scrollbar.set)   

        img_frame = Frame(canvas_main, bg = '#e6e6fa')
        canvas_main.create_window((0, 0), window=img_frame, anchor='nw')

        canvas_main.img_tk_list = []
        for index, item in enumerate(data):
            labelframe_img = LabelFrame(img_frame, text ="")
            img = Button(labelframe_img, image=list_img_resize[index], borderwidth=0, relief='flat', command = lambda photo = labelframe_img: show(photo))
            img.pack()
            name = Label(labelframe_img, text = item['Name'])
            name.pack()
            labelframe_img.grid(row = row_val, column = col_val, pady = 10, padx = 10)
            img_tk = list_img_resize[index]
            canvas_main.img_tk_list.append(img_tk)
            labelframe_img.index = index
            
            col_val += 1
            if col_val == 4:
                col_val = 0
                row_val += 1
        
        #cập nhật lại kích thước của frame chứa hình ảnh sau khi các hình ảnh được thêm vào
        img_frame.update_idletasks()
        #cập nhật lại vùng cuộn khi các nội dung con bên trong được thêm vào
        canvas_main.config(scrollregion=canvas_main.bbox("all"))
        
    @staticmethod
    def list_images():
        list_img = []
        file_img = ImageDocument.file_input_img
        data = ImageDocument.load_img(file_img)
        for item in data:
            path_img = f"image_document\\images_to_delete\\{item['Name']+".jpg"}" #hàm này dùng lại cho show image tên file là images_to_delete cũng không vấn đề
            ImageDocument.write_img(item['Img'], path_img)
            list_img.append(path_img)
        return list_img
    
    @staticmethod
    def find_img_to_delete(data_images, name_img):
        index = next((index_photo for index_photo, photo in enumerate(data_images) if photo['Name'] == name_img), None)  
        return index
        
    def delete_image(self):
        file_img = ImageDocument.file_input_img
        data = ImageDocument.load_img(file_img)

        row_val = 0
        col_val = 0

        list_img_resize = []
        list_img = ImageDocument.list_images() #list đường dẫn của tất cả hình ảnh được lưu
        
        for img in list_img:
            image = Image.open(img)
            image = image.resize((90, 80), Image.LANCZOS)
            imageTk = ImageTk.PhotoImage(image)
            list_img_resize.append(imageTk)

        def back():
            canvas_main.destroy()

        def delete(photo):
            confrim_delete = mb.askyesno("Are you sure you want to delete this photo ?")
            if confrim_delete:
                index = photo.index
                del data[index]  
                ImageDocument.save_data_img(data, file_img)       
                photo.grid_forget()
                photo.destroy()
            else:
                return
            
        canvas_main = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
        canvas_main.pack(side='left', fill = 'both', expand=True)

        scrollbar = Scrollbar(canvas_main, orient=VERTICAL, command=canvas_main.yview)  
        scrollbar.pack(side='right', fill='y')

        btn_back = Button(canvas_main, text = "Back", width = 8, command=back)
        canvas_main.create_window((530, 640), window=btn_back)

        canvas_main.config(yscrollcommand=scrollbar.set)   

        img_frame = Frame(canvas_main, bg = '#e6e6fa')
        canvas_main.create_window((0, 0), window=img_frame, anchor='nw')

        canvas_main.img_tk_list = []
        for index, item in enumerate(data):
            labelframe_img = LabelFrame(img_frame, text ="")
            img = Button(labelframe_img, image=list_img_resize[index], borderwidth=0, relief='flat', command=lambda photo = labelframe_img: delete(photo))
            img.pack()
            name = Label(labelframe_img, text = item['Name'])
            name.pack()
            labelframe_img.grid(row = row_val, column = col_val, pady = 10, padx = 10)
            img_tk = list_img_resize[index]
            canvas_main.img_tk_list.append(img_tk)
            labelframe_img.index = index
            
            col_val += 1
            if col_val == 4:
                col_val = 0
                row_val += 1
        
        #cập nhật lại kích thước của frame chứa hình ảnh sau khi các hình ảnh được thêm vào
        img_frame.update_idletasks()
        #cập nhật lại vùng cuộn khi các nội dung con bên trong được thêm vào
        canvas_main.config(scrollregion=canvas_main.bbox("all"))
    
        # def on_canvas_configure(event):
        #     canvas.configure(scrollregion=canvas.bbox("all"))
        # canvas.bind('<Configure>', on_canvas_configure)