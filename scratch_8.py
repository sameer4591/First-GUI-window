from tkinter import *
from tkinter import messagebox
def handel_login():
    email=email_input.get()
    password=password_input.get()
    print(email,password)
    if(email=="singhsameer2310@gmail.com" and password=="1234"):
        messagebox.showinfo("yayya","login successful")
    else:
        messagebox.showerror("error","login failed")

root= Tk()
root.title('login')
root.minsize(350,600)
root.config(background="sky blue")
text_label=Label(root,text="Welcome to MY LOGIN",fg="red",bg="sky blue")
text_label.pack(pady=(15,5))
text_label.config(font=("vardana",10))
email_label=Label(root,text='Enter the Mail ID :',fg="black",bg="sky blue")
email_label.pack(pady=(20,9))
email_label.config(font=("vardana", 13))
email_input=Entry(root,width=25)
email_input.pack(pady=(15,5))
email_input.config(font=("vardana", 13))
password_label=Label(root,text='Enter your password',fg="black",bg="sky blue")
password_label.pack(pady=(15,5))
password_label.config(font=('vardana',13))
password_input=Entry(root,width=25)
password_input.pack(pady=(15,5))
password_input.config(font=("vardana",13))
submit_btn=Button(root,text="Login",fg="red",bg='yellow',width=20,height=3,command=handel_login)
submit_btn.pack(pady=(10,20))
submit_btn.config(font=("vardana",7))




root.mainloop()