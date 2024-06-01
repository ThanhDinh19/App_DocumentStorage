from Note import *
from ImageDocument import *
from FileDocument import *

def main():
    root = Tk()
    root.geometry("600x700")
    root.iconbitmap("Logo\\logo_app.ico")
    root.title("NOTE TAKING AND DOCUMENT STORAGE") 
    img = Image.open("images\\background_notejpg.jpg") 
    img = img.resize((600, 700), Image.LANCZOS)
    
    lb_title_app = Label(root, text="Applications", font=("Time new roman", 18, "bold")).place(x=230, y=20)
    
    #------note
    def note():
        note = Note(root, "","")
               
        def Exit_():
            canvas_note_main.destroy()

        canvas_note_main = Canvas(root, width = 400, height = 400, bg = "#e6e6fa")
        canvas_note_main.place(x=100, y=120)
        btn_show = Button(root, text = "* SHOW NOTE *", width = 20, height = 2, font=("Time new roman", 10, "bold"), command = note.show_notes)
        btn_input = Button(root, text = "* CREATE NOTE *", width = 20, height = 2, font=("Time new roman", 10, "bold"), command = note.input_note)
        btn_edit = Button(root, text = "* EDIT NOTE *", width = 20, height = 2, font=("Time new roman", 10, "bold"), command = note.edit_note)
        btn_delete = Button(root, text = "* DELETE NOTE *", width = 20, height = 2, font=("Time new roman", 10, "bold"), command=note.delete_note)
        btn_exit = Button(root, text = "Back", width = 8, height = 1, font=("Time new roman", 10, "bold"), command = Exit_)

        btn_show_win = canvas_note_main.create_window(200, 35, window=btn_show)
        btn_input_win = canvas_note_main.create_window(200, 95, window = btn_input)
        btn_edit_win = canvas_note_main.create_window(200, 155, window = btn_edit)
        btn_delete_win = canvas_note_main.create_window(200, 215, window = btn_delete)
        btn_exit_win = canvas_note_main.create_window(200, 275, window = btn_exit)


    #-------Image document
    def image_document():
        img_document = ImageDocument(root, "", "")

        def Exit_():
            canvas_image_main.destroy()

        canvas_image_main = Canvas(root, width = 400, height = 400, bg = "#e6e6fa")
        canvas_image_main.place(x=100, y=120)
        btn_show = Button(root, text = "* SHOW IMAGE *", width = 20, height = 2, font=("Time new roman", 10, "bold"), command = img_document.show_img_upgrade)
        btn_input = Button(root, text = "* SAVE IMAGE *", width = 20, height = 2, font=("Time new roman", 10, "bold"), command = img_document.input_img)
        btn_delete = Button(root, text = "* DELETE IMAGE *", width = 20, height = 2, font=("Time new roman", 10, "bold"), command = img_document.delete_image)
        btn_exit = Button(root, text = "Back", width = 8, height = 1, font=("Time new roman", 10, "bold"), command = Exit_)

        btn_show_win = canvas_image_main.create_window(200, 35, window=btn_show)
        btn_input_win = canvas_image_main.create_window(200, 95, window = btn_input)
        btn_delete_win = canvas_image_main.create_window(200, 155, window= btn_delete)
        btn_exit_win = canvas_image_main.create_window(200, 275, window = btn_exit)

    #-------File document
    def file_document():
        fi_document = FileDocument(root, "", "")

        def Exit_():
            canvas_file_main.destroy()

        canvas_file_main = Canvas(root, width = 400, height = 400, bg = "#e6e6fa")
        canvas_file_main.place(x=100, y=120)
        btn_show = Button(root, text = "* SHOW FILE *", width = 20, height = 2, font=("Time new roman", 10, "bold"), command = fi_document.show_file)
        btn_input = Button(root, text = "* SAVE FILE *", width = 20, height = 2, font=("Time new roman", 10, "bold"), command = fi_document.input_file)
        btn_delete = Button(root, text = "* DELETE FILE *", width = 20, height = 2, font=("Time new roman", 10, "bold"), command = fi_document.delete_file)
        btn_exit = Button(root, text = "Back", width = 8, height = 1, font=("Time new roman", 10, "bold"), command = Exit_)

        btn_show_win = canvas_file_main.create_window(200, 35, window=btn_show)
        btn_input_win = canvas_file_main.create_window(200, 95, window = btn_input)
        btn_delete_win = canvas_file_main.create_window(200, 155, window= btn_delete)
        btn_exit_win = canvas_file_main.create_window(200, 275, window = btn_exit)  

    canvas_main = Canvas(root, width = 400, height = 400, bg = "#e6e6fa")
    canvas_main.place(x=100, y=120)
    func1 = Button(root, text = "Note", width = 20, font = ("Time new roman", 14), command=note)
    func2 = Button(root, text = "Image", width = 20, font = ("Time new roman", 14), command=image_document)
    func3 = Button(root, text = "File", width = 20, font = ("Time new roman", 14), command=file_document)
    func4 = Button(root, text = "Exit", width = 15, font = ("Time new roman", 12), command=exit)

    func1_win = canvas_main.create_window(200, 40, window=func1)
    func2_win = canvas_main.create_window(200, 85, window=func2)   
    func3_win = canvas_main.create_window(200, 130, window=func3)  
    func4_win = canvas_main.create_window(200, 175, window=func4)     
    

    root.mainloop() 
if __name__ == "__main__":
    main()       
