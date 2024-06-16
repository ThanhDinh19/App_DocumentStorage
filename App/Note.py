from Librarys import *

class n:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class Note:
    filename = "note_document\\notes.json"
    def __init__(self, window, title, content):
        self.window = window
        self.title = title
        self.content = content

    @staticmethod
    def load_file_note(filename):
        data_notes = []
        if os.path.exists(filename):
            try: 
                with open(filename, "r", encoding="utf8") as fi_load:
                    data = json.load(fi_load)
                    if data == 0:
                        return data_notes
                    else:
                        for item in data:
                            note = n("", "")
                            note.title = item.get('title', '')
                            note.content = item.get('content', '')
                            data_notes.append(note)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            with open(filename, "w") as fi:
                json.dump(data_notes, fi, indent = 4, default = lambda x: x.__dict__)
        return data_notes

    @staticmethod
    def save_note_list(filename, list_notes):
        try: 
            with open(filename, 'w', encoding = 'utf8') as fi_save:
                json.dump(list_notes, fi_save, indent = 4, default=lambda x: x.__dict__, ensure_ascii=False)
        except FileNotFoundError as e_fi:
            print(f"Error: {e_fi}")
        except ValueError as e_va:
            print(f"Error: {e_va}")

    @staticmethod
    def save_note(filename, note, data_notes):
        data_notes.append(note)     
        with open(filename, "w", encoding="utf8") as fi_save:
            json.dump(data_notes, fi_save, indent = 4, default = lambda x: x.__dict__, ensure_ascii=False)
    
    def save_notes(self):
        filename = Note.filename
        data_notes = Note.load_file_note(filename)
        note = {
            "title": self.title.get(1.0, END).rstrip("\n"),
            "content": self.content.get(1.0, END).rstrip("\n")
        }
        Note.save_note(filename, note, data_notes)              
            
    def clear_text_input(self):
        self.title.delete(1.0, END)
        self.content.delete(1.0, END)

    def functions_input(self):
        self.save_notes()
        self.clear_text_input()
        mb.showinfo("Save successfully !")

    def list_notes_to_show(self, canvas_show_main, canvas_lstbox, scrollbar, listbox_titles, list_titles):

        def Exit_():
            canvas_show_main.destroy()

        lb = Label(canvas_show_main, text = "NOTES", font=("Time new roman", 16, "bold"))
        btn_exit = Button(canvas_show_main, text = "Back", width = 10, command = Exit_)
        btn_exit.place(x=390, y = 340)
        lb_win = canvas_show_main.create_window(250, 30, window = lb)

        scrollbar.config(command = listbox_titles.yview)
        for index, item in enumerate(list_titles):
            listbox_titles.insert(index*2 + 1, " + "+item)
            listbox_titles.insert(index*2 + 2, "-"*60)

    # hiển thị danh sách note
    def show_notes(self):
        list_titles = []
        filename = Note.filename
        data_notes = self.load_file_note(filename)
        for item in data_notes:
            t = item.title
            list_titles.append(t)

        def show(event):
            
            def Exit_():
                canvas_show.destroy()

            selected_indices = listbox_titles.curselection()
            index = int(selected_indices[0])
            if index % 2 == 0 and selected_indices:
                canvas_show = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
                canvas_show.place(x = 50, y = 118)
                lb_title = Label(canvas_show, text = "", font=("Time new roman", 16, "bold"),  bg = "#f0f8ff")
                lb_design = Label(canvas_show, text="_"*80, bg = "#E6E6FA") 
                text_container = Text(canvas_show, width = 55, height = 15)
                btn_back = Button(canvas_show, text="Back", width=8, activebackground="#a9a9a9", command=Exit_)

                lb_title_win = canvas_show.create_window(260, 30, window=lb_title)
                lb_design_win = canvas_show.create_window(250, 60, window=lb_design)
                text_container_win = canvas_show.create_window(250, 200, window=text_container)
                btn_back_win = canvas_show.create_window(440, 350, window=btn_back)

                selected_titles = listbox_titles.get(index)
                lb_title.config(text=selected_titles[3:])
                title = selected_titles[3:]
                content = next((item.content for item in data_notes if item.title == title), None)
            
                text_container.insert(END, content)      
            else:
                return
                  
        canvas_show_main = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
        canvas_show_main.place(x = 50, y = 118)

        canvas_lstbox = Canvas(canvas_show_main)
        canvas_lstbox.place(x=70, y=80)

        scrollbar = Scrollbar(canvas_lstbox, orient = VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox_titles = Listbox(canvas_lstbox, yscrollcommand=scrollbar.set, font=("Time new roman", 12), width=30, height=15)
        listbox_titles.pack(fill = BOTH)

        self.list_notes_to_show(canvas_show_main, canvas_lstbox, scrollbar, listbox_titles, list_titles)
        listbox_titles.bind("<<ListboxSelect>>", show)

    #Create note
    def input_note(self): 
        def Exit_():
            canvas.destroy()
        canvas = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
        canvas.place(x = 50, y = 118)
        self.title = Text(self.window, width = 15, height = 1)
        self.content = Text(self.window, width = 30, height = 10)
        lb_canvas_title = Label(self.window, text = "CREATE NOTE", font = ("Time New Roman", 15, "bold"))
        lb_title = Label(self.window, text="Title", font = ("Time New Roman", 10))
        lb_content = Label(self.window, text="Content", font = ("Time New Roman", 10))
        btn = Button(self.window, text = "Save", width=10, activebackground="#a9a9a9", command = self.functions_input)
        btn_input_exit = Button(canvas, text = "Back", width=8, activebackground="#a9a9a9", command=Exit_)

        title_canvas_input = canvas.create_window(255, 15, window = lb_canvas_title)
        title_win = canvas.create_window(219, 60, window = self.title)
        content_win = canvas.create_window(278, 165, window = self.content)
        lb_title_win = canvas.create_window(115, 59, window = lb_title)
        lb_content_win = canvas.create_window(125, 95, window = lb_content)
        btn_win = canvas.create_window(360, 270, window=btn)
        btn_input_exit_win = canvas.create_window(190, 270, window=btn_input_exit)
   
    def list_note_to_edit(self, listbox, scrollbar, canvas_main, canvas_lstbox, list_titles):
        def Exit_():
            canvas_main.destroy()
        lb1 = Label(canvas_main, text = "NOTES", font=("Time new roman", 16, "bold"))
        btn_exit = Button(canvas_main, text = "Back", width = 10, command = Exit_)
        btn_exit.place(x=390, y = 340)

        scrollbar.config(command=listbox.yview)
        for index, item in enumerate(list_titles):
            listbox.insert(END," - "+item)
           
        lb1_win = canvas_main.create_window(250, 30, window = lb1)


    #Edit note    
    def edit_note(self):
        filename = Note.filename
        data_notes = Note.load_file_note(filename)
        list_titles = []
        for item in data_notes:
            t = item.title
            list_titles.append(t)

        def edit(event):

            def Exit_():
                canvas_edit_main.destroy()       

            def Save_():               
                edited_notes = {
                    "title": title_text.get("1.0", "end-1c"),
                    "content": content_text.get("1.0", "end-1c")
                }

                data_notes[index] = edited_notes
                Note.save_note_list(filename, data_notes)
                mb.showinfo("Edited successfully !")
                   
            index = listbox_title.curselection()[0]
            select_item = listbox_title.get(index) #lấy title được chọn(chưa dùng)

            canvas_edit_main = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
            canvas_edit_main.place(x = 50, y = 118)    

            title_main = Label(canvas_edit_main, text = "EDIT NOTE", font=("Time new roman", 14, "bold"))

            title_lb = Label(canvas_edit_main, text = "Title", width = 11, font=("Time new roman", 10, "bold")) 
            content_lb = Label(canvas_edit_main, text = "Content", width = 11, font=("Time new roman", 10, "bold"))
            
            title_text = Text(canvas_edit_main, width = 30, height = 1)
            content_text = Text(canvas_edit_main, width = 30, height = 10)
            
            
            title_text.insert("1.0", data_notes[index].title)
            content_text.insert("1.0", data_notes[index].content)

            btn_edit_save = Button(canvas_edit_main, text = "Save", width=10, activebackground="#a9a9a9", command=Save_)
            btn_edit_exit = Button(canvas_edit_main, text = "Back", width=8, activebackground="#a9a9a9", command=Exit_)

            title_main_win = canvas_edit_main.create_window(250, 30, window=title_main)
            title_lb_win = canvas_edit_main.create_window(100, 75, window = title_lb)
            content_lb_win = canvas_edit_main.create_window(100, 120, window = content_lb)
            title_text_win = canvas_edit_main.create_window(280, 75, window = title_text)
            content_text_win = canvas_edit_main.create_window(280, 190, window = content_text)
            btn_edit_save_win = canvas_edit_main.create_window(360, 293, window=btn_edit_save)
            btn_edit_exit_win = canvas_edit_main.create_window(195, 293, window = btn_edit_exit)

        canvas_main = Canvas(self.window, width = 500, height = 400, bg = "#e6e6fa")
        canvas_main.place(x = 50, y = 118)

        canvas_lstbox = Canvas(canvas_main)
        canvas_lstbox.place(x=70, y=80)                
        
        scrollbar = Scrollbar(canvas_lstbox, orient = VERTICAL)
        scrollbar.pack(side = RIGHT, fill = Y)
        listbox_title = Listbox(canvas_lstbox, yscrollcommand=scrollbar.set, font=("Time new roman", 12), width=30, height=15)
        listbox_title.pack(fill = BOTH)

        self.list_note_to_edit(listbox_title, scrollbar, canvas_main, canvas_lstbox, list_titles)
        listbox_title.bind("<<ListboxSelect>>", edit)
    
          
    def delete_note(self):
        filename = Note.filename
        data_notes = Note.load_file_note(filename)
        frame = Frame(self.window, bg = "#e6e6fa")
        frame.pack(fill="both", expand=True)
        treev = t.Treeview(frame, column=(1,2), show="headings", height = '20')
        treev.column("1", anchor = W, width=145)
        treev.column("2", anchor = W, width=290)           
        treev.heading(1, text = "Title")
        treev.heading(2, text = "Content")
        for index, item in enumerate(data_notes):
            treev.insert('', 'end', iid=index, values=(str(item.title), "."*90))
        treev.place(x=90,y= 130)

        lb_title = Label(frame, text="NOTES", font = ("Time new roman", 20, "bold"), bg = "#e6e6fa")
        lb_title.place(x=260,y= 20)

        def delete():
            selected_item = treev.selection()[0]
            index = selected_item
            value_title = treev.item(index, 'values')[0]
            notes = data_notes
            for note in notes:
                if note.title == value_title:
                    notes.remove(note)
                    break
            Note.save_note_list(filename, notes)
            treev.delete(selected_item)

        def confrim_delete():
            confirm = mb.askyesno("Are you sure you want to delete it ?") 
            if confirm:
                delete()
            else:
                return

        def back():
            frame.destroy() 
        btn_delete = Button(frame, text="Delete", width=8, relief='raised', bg="#ff4500", command=confrim_delete)
        btn_delete.place(x=460, y =565)
        btn_back = Button(frame, text="Back", width=8, relief='raised', command=back)
        btn_back.place(x=90, y = 565)

    




