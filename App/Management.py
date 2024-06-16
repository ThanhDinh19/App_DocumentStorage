from Note import *
from ImageDocument import *
from FileDocument import *

#===============================================================Sign In Account=====================================================================
def SignInAccount():
    sign_in = Tk()
    sign_in.geometry("500x400")
    sign_in.title("DocMemo")
    sign_in.iconbitmap("Logo\\logo_doc_memo.ico")
    sign_in.config(bg='#008080')
    
    file_account_data = "file_accounts\\accounts.json"

    def on_click_emailEntry(event):
        if email_entry.get() == "Email address":
            email_entry.delete(0, 'end')
            email_entry.config(fg='black')
            
    def on_click_password(event):
        if password_entry.get() == "Password":
            password_entry.delete(0, 'end')
            password_entry.config(fg='black', show='*')    

    def load_accounts(file_account_data):
        if os.path.exists(file_account_data):
            with open(file_account_data, 'r', encoding ='utf8') as fi_load:
                data = json.load(fi_load)
                return data
        else:
            return []
         
    def login_account(file_account_data):
        flag = False
        data = load_accounts(file_account_data)
        if len(data) == 0:
            canvas_login.create_window((123, 165), window=notification_label)
            notification_label.config(text="Couldn't find your DocMemo Account")
            return 
        for item in data:
            if item["Email"] == email_entry.get() and item["Password"] == password_entry.get():
                flag = True
                break
        if flag == True:
            sign_in.destroy()
            App()
        else:
            canvas_login.create_window((95, 165), window=notification_label)
            notification_label.config(text="Incorrect email or password.")

    def check_email(email):
        pattern = r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}'
        ck = re.match(pattern, email)
        return ck
    
    def check_password(password):
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[1-9]', password):
            return False
        return True
    
    def check_email_existence(data, account):
        for item in data:
            if item["Email"] == account["Email"]: #if the email already exists, the user must enter another email.
                return True 
        return False
    
    def create_an_account(file_account_data):
        data=load_accounts(file_account_data)
        
        ck_email = check_email(create_email_entry.get())   
        ck_password = check_password(create_password_entry.get())
        if ck_email is None:
            register_notification_label.config(text="Invalid email, please try again.", fg="maroon")
            canvas_register.create_window((100, 165), window=register_notification_label)
            return
        
        account = {"Email": create_email_entry.get(), "Password": create_password_entry.get()}

        if check_email_existence(data, account) == True: #email already exists
            register_notification_label.config(text="The email already exists,\nplease enter another email.", fg="maroon", justify='left')
            canvas_register.create_window((92, 168), window=register_notification_label)
            return
            
        if ck_password == False:
            register_notification_label.config(text="Password is not strong enough.", fg="maroon")
            canvas_register.create_window((103, 165), window=register_notification_label)
            return
         
        data.append(account)
        with open(file_account_data, 'w') as fi:
            json.dump(data, fi, indent=4, default = lambda x: x.__dict__)
        register_notification_label.config(text="Sign Up Success.", fg="limegreen")
        canvas_register.create_window((68, 165), window=register_notification_label)

    def show_login(frame):
        frame.tkraise() 

    login_frame = Frame(sign_in)
    register_frame = Frame(sign_in)
    login_frame.grid(row=0, column=0, sticky='nsew')
    register_frame.grid(row=0, column=0, sticky='nsew')
    login_frame.config(bg='#008080')
    register_frame.config(bg='#008080')
    
    #title
    title_of_app = Label(login_frame, text = "DocMemo", fg = "black", bg = "#008080", font=("Time new roman", 13, 'bold')).pack(padx=210)
    text1 = Label(login_frame, text = "Sign in to DocMemo", font=("Time new roman", 13, 'bold'), bg = "#008080", fg = "black").pack()
    text2 = Label(login_frame, text = "Use your account", bg = "#008080", fg = "black").pack()
    
    #canvas login contains wedgets
    canvas_login = Canvas(login_frame, width = 280, height = 230, bg = "gray")  
    #wedgets of canvas login
    email_label = Label(canvas_login, text="Email address", fg='black', bg = "gray")
    password_label = Label(canvas_login, text="Password",bg = "gray", fg='black')
    email_entry = Entry(canvas_login, width = 40, fg = 'gray',highlightthickness=1, highlightbackground="black", highlightcolor="#008080")
    email_entry.insert(0, "Email address")
    email_entry.bind("<FocusIn>", on_click_emailEntry)
    password_entry = Entry(canvas_login, width = 40, fg = 'gray', highlightthickness=1, highlightbackground="black", highlightcolor="#008080")
    password_entry.insert(0, "Password")
    password_entry.bind("<FocusIn>", on_click_password)
    btn_sign_in = Button(canvas_login, text="Sign in", width = 34, bg='#008080', fg='black', command = lambda f = file_account_data: login_account(f))
    notification_label = Label(canvas_login, text = "", fg='maroon', bg = "gray")
    CreateAnAccount = Label(canvas_login, text="Create an account", fg="blue", bg='gray', cursor='hand2')
    CreateAnAccount.bind("<Button-1>", lambda event, frame = register_frame: show_login(frame))

    #button to back login frame
    btn_back = Button(register_frame, text="<", width=3, command=lambda frame = login_frame: show_login(frame))
    btn_back.place(x=5, y = 5)
    #title
    title_of_app = Label(register_frame, text = "DocMemo", fg = "black", bg = "#008080", font=("Time new roman", 13, 'bold')).pack(padx=210)
    text1 = Label(register_frame, text = "Sign up to DocMemo", font=("Time new roman", 13, 'bold'), bg = "#008080", fg = "black").pack()
    
    #canvas register constains wedgets
    canvas_register = Canvas(register_frame, width = 280, height = 230, bg = 'gray')
    #wedgets of canvas register
    create_email_label = Label(canvas_register, text="Create email", fg='black', bg='gray')
    create_password_label = Label(canvas_register, text="Create password", fg='black', bg='gray')
    create_email_entry = Entry(canvas_register, width=40, highlightthickness=1, highlightbackground="black", highlightcolor="#008080")
    create_password_entry = Entry(canvas_register, width=40, highlightthickness=1, highlightbackground="black", highlightcolor="#008080")
    btn_sign_up = Button(canvas_register, text="Sign up", width = 34, bg='#008080', fg='black', command = lambda f = file_account_data: create_an_account(f))
    register_notification_label = Label(canvas_register, text = "", fg='maroon', bg = "gray") #notification
    
    #create window for weigets in canvas login
    canvas_login.create_window((63, 26), window=email_label)
    canvas_login.create_window((145, 50), window=email_entry)
    canvas_login.create_window((50, 75), window=password_label)
    canvas_login.create_window((145, 100), window=password_entry)
    canvas_login.create_window((145, 135), window=btn_sign_in)
    canvas_login.create_window((68, 210), window=CreateAnAccount)

    #create window for weigets in canvas register
    canvas_register.create_window((54, 26), window=create_email_label)
    canvas_register.create_window((145, 50), window=create_email_entry)
    canvas_register.create_window((65, 75), window=create_password_label)
    canvas_register.create_window((145, 100), window=create_password_entry)
    canvas_register.create_window((145, 135), window=btn_sign_up)

    canvas_login.pack(pady=10)
    canvas_register.pack(pady=10)
    
    show_login(login_frame)
    
    sign_in.mainloop()
#===============================================================APPLICATION=========================================================================
def App():
    root = Tk()
    root.geometry("600x700")
    root.iconbitmap("Logo\\logo_doc_memo.ico")
    root.title("NOTE TAKING AND DOCUMENT STORAGE") 
    img = Image.open("images\\background_notejpg.jpg") 
    img = img.resize((600, 700), Image.LANCZOS)
    lb_title_app = Label(root, text="DocMemo", fg = "#0074D9", font=("Time new roman", 18, "bold")).place(x=230, y=20)
    
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

def main():
    SignInAccount()

if __name__ == "__main__":
    main()    
