# Importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from login import DataBaser

# Criar nossa Janela
jan = Tk()
jan.title('DP Systems - Acess Panel')
jan.geometry('600x300')
jan.configure(background='white')
jan.resizable(width=False, height=False)
jan.attributes('-alpha', 0.9)

# ========== Carregar imagens
logo = PhotoImage(file='icons/logo.png')

# ====== WIDGETS ====================== #
left_frame = Frame(jan, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
left_frame.pack(side=LEFT)

right_frame = Frame(jan, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
right_frame.pack(side=RIGHT)

logo_label = Label(left_frame, image=logo, bg='MIDNIGHTBLUE')
logo_label.place(x=50, y=100)

# Username
user_label = Label(right_frame, text='Username: ', font=('Verdana', 20),
                   bg='MIDNIGHTBLUE', fg='White')
user_label.place(x=5, y=100)

user_entry = ttk.Entry(right_frame, width=25)
user_entry.place(x=130, y=105)

# Password
pass_label = Label(right_frame, text='Password: ', font=('Verdana', 20),
                   bg='MIDNIGHTBLUE', fg='White')
pass_label.place(x=5, y=150)

pass_entry = ttk.Entry(right_frame, width=25, show='•')
pass_entry.place(x=130, y=152)


def login():
    user = user_entry.get()
    password = pass_entry.get()
    DataBaser.cursor.execute("""
    SELECT * FROM users
    WHERE user = ? AND password = ?
    """, (user, password))
    print('Selected')
    verify_login = DataBaser.cursor.fetchone()
    try:
        if user in verify_login and password in verify_login:
            messagebox.showinfo(title='Login info', message='Login confirmed. Welcome ')
    except:
        messagebox.showinfo(title='Login info', message='Denied acess.')
    

# Buttons
login_button = ttk.Button(right_frame, text='Login', width=20, command=login)
login_button.place(x=140, y=225)


def register():
    """
    Removendo Widgets de login e inserindo widgets de cadastro
    """
    login_button.place(x=5000)
    register_button.place(x=5000)

    name_label = Label(right_frame, text='Name: ', font=('Verdana', 20),
                       bg='MIDNIGHTBLUE', fg='White')
    name_label.place(x=5, y=5)
    name_entry = ttk.Entry(right_frame, width=28)
    name_entry.place(x=100, y=9)

    email_label = Label(right_frame, text='E-mail: ', font=('Verdana', 20),
                        bg='MIDNIGHTBLUE', fg='White')
    email_label.place(x=5, y=50)
    email_entry = ttk.Entry(right_frame, width=28)
    email_entry.place(x=100, y=53)

    def register_on_db():
        name = name_entry.get()
        email = email_entry.get()
        user = user_entry.get()
        password = pass_entry.get()

        if name == '' or email == '' or user == '' or password == '':
            messagebox.showerror(title='Register error', message='Some field is empty')
        else:
            DataBaser.cursor.execute("""
            INSERT INTO users(name, email, user, password) VALUES(?, ?, ?, ?)
            """, (name, email, user, password))
            DataBaser.conn.commit()
            messagebox.showinfo(title='Register info', message='Account successfully created')

    register_user = ttk.Button(right_frame, text='Register', width=20, command=register_on_db)
    register_user.place(x=140, y=225)

    def back_to_login():
        """
        Removendo widgets de cadastro
        """
        name_label.place(x=5000)
        name_entry.place(x=5000)
        email_label.place(x=5000)
        email_entry.place(x=5000)
        register_user.place(x=5000)
        back.place(x=5000)
        register_button.place(x=185, y=260)
        login_button.place(x=140, y=225)

    back = ttk.Button(right_frame, text='Back', width=10, command=back_to_login)
    back.place(x=185, y=260)


register_button = ttk.Button(right_frame, text='Register', width=10, command=register)
register_button.place(x=185, y=260)

jan.mainloop()
