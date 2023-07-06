from tkinter import *
from tkinter import messagebox
from mysql.connector import *
from random import randint


class Login:
    def __init__(self):
        root = Tk()
        root.title("Login")
        root.geometry("500x300+500+250")
        root.configure(background="#eb1e1e")

        title = Label(root, text="Login Page", font=("arial", 20, "bold"), bg="#eb1e1e")
        title.place(x=250, y=15)

        username = StringVar()
        password = StringVar()
        username_entry = Entry(root, width=30, textvariable=username)
        password_entry = Entry(root, width=30, textvariable=password, show="*")
        user = Label(root, text="Username:", font=("arial", 10, "bold"), bg="#eb1e1e")
        passw = Label(root, text="Password:", font=("arial", 10, "bold"), bg="#eb1e1e")
        user.place(x=180, y=100)
        passw.place(x=180, y=150)
        username_entry.place(x=270, y=100)
        password_entry.place(x=270, y=150)
        image = PhotoImage(file="download.png")
        image_label = Label(root, image=image, width=150, height=150)
        image_label.place(x=10, y=50)

        checkbox1 = IntVar()

        def show():
            if checkbox1.get() == 1:
                password_entry.config(show="")
            else:
                password_entry.config(show="*")

        checkbox = Checkbutton(root, text="Show Password", variable=checkbox1, command=show, font=("arial", 10, "bold"),
                               bg="#eb1e1e")
        checkbox.place(x=270, y=200)

        def check(username1):
            try:
                conn = connect(host="localhost", user="root", passwd="", database="python_mini_project")
                cursor = conn.cursor()
                statement = f"SELECT username from users WHERE username='{username1}';"
                cursor.execute(statement)
                result = cursor.fetchall()
                if username1 == "admin":
                    messagebox.showinfo("Login", "Login Successful\n Welcome Admin")
                    root.destroy()
                    import admin
                    admin.Admin("admin")
                elif username.get() == "" or password.get() == "":
                    messagebox.showerror("Error", "Please enter username and password")
                else:
                    messagebox.showinfo("Success", "Login Successful")
                    root.destroy()
                    import home
                    home = home.Home(username1)

            except Error as e:
                print(e)

        def login():
            check(username_entry.get())

        def SIgnup():
            root.destroy()
            import signup
            signup.Signup()

        submit = Button(root, text="Submit", font=("arial", 10, "bold"), bg="white", command=login)
        submit.place(x=250, y=250)
        signup = Button(root, text="Sign Up", font=("arial", 10, "bold"), bg="white", command=SIgnup)
        signup.place(x=330, y=250)
        cancel = Button(root, text="Cancel", font=("arial", 10, "bold"), bg="white", command=root.destroy)
        cancel.place(x=410, y=250)
        root.mainloop()


if __name__ == '__main__':
    Login()
