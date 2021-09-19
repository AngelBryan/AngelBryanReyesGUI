import tkinter as tk
from tkinter import ttk, StringVar

# initialize window
root = tk.Tk()
root.geometry('600x300+0+0')
root.title('Login')
root.configure(bg='white')

user_input1 = StringVar()
user_input2 = StringVar()

user_name = ttk.Label(root, text="Username", font="arial 13", bg='white')
user_name.place(x=50, y=80)

user_pass = ttk.Label(root, text="Password", font="arial 13", bg='white')
user_pass.place(x=50, y=120)

username_entry = ttk.Entry(root, textvariable=user_input1, width=40, bd=5)
username_entry.place(x=180, y=83)

password_entry = ttk.Entry(root, textvariable=user_input2, width=40, bd=5)
password_entry.place(x=180, y=120)


def user_account():
    login_win = tk.Toplevel()
    login_win.geometry('1600x800+0+0')
    login_win.title('Home')


def register():
    register_win = tk.Toplevel()
    register_win.geometry('600x650')
    register_win.title('Registration')


login_Btn = tk.Button(root, text='Login', command=user_account, padx=5)
login_Btn.place(x=220, y=160)

login_Btn = tk.Button(root, text='Register', command=register)
login_Btn.place(x=330, y=160)

root.mainloop()
