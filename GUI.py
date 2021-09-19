from tkinter import *
root = Tk()
root.geometry('600x300+0+0')
root.title('Login')
root.configure(bg = 'white')




user_input1 = StringVar()
user_input2 = StringVar()

user_name = Label(font=('arial',13),text = 'Username', bg='white')
user_name.place(x=50, y=80)

user_pass = Label(font=('arial',13),text = 'Password', bg='white')
user_pass.place(x=50, y=120)

username_entry = Entry(textvariable = user_input1, width=40, bd=5)
username_entry.place(x=180, y=83)

password_entry = Entry(textvariable = user_input2, width=40, bd=5)
password_entry.place(x=180, y=120)

def user_Account():
    user_Account = Toplevel()
    user_Account.geometry('1600x800+0+0')
    user_Account.title('Home')

def Register():
    user_Account = Toplevel()
    user_Account.geometry('600x650')
    user_Account.title('Registration')


login_Btn = Button(text = 'Login', command = user_Account, padx=5)
login_Btn.place(x=220, y=160)

login_Btn = Button(text = 'Register', command = Register)
login_Btn.place(x=330, y=160)

root.mainloop()


