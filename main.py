import tkinter as tk
from tkinter import messagebox



#Email Validator Function
def validate_email():
    email=email_entry.get()
    ns=nc=nch=0
    if len(email)>=6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@")==1):
                if (email[-4]=='.') ^ (email[-3]=='.'):
                    for ch in email:
                        if ch.isspace():
                            ns=1  
                        elif ch.isalpha():
                            if ch.isupper():
                                nc=1
                        elif ch.isdigit():
                            continue
                        elif ch=='_' or ch=='.' or ch=='@':
                            continue
                        else:
                            nch=1
                    if ns or nc or nch:
                        result_label.config(text="Invalid Emaiil!",fg="red")#print out the message for invalid Email
                    else:
                        result_label.config(text="Valid Email",fg="green")#print out the message for Valid Email
    
                else:
                    result_label.config(text="Invalid Emaiil!",fg="red")#print out the message for invalid Email
            else:
                result_label.config(text="Invalid Emaiil!",fg="red")#print out the message for invalid Email
        else:
            result_label.config(text="Invalid Emaiil!",fg="red")#print out the message for invalid Email
    else:
        result_label.config(text="Invalid Emaiil!",fg="red")#print out the message for invalid Email

#Creating the main tkinter GUI
root=tk.Tk()

#Giving Title for our tkinter GUI
root.title("Email Validator")
root.geometry()
root.resizable(True, True)

tk.Label(root, text="Enter your Email: ",font=("Arial",12)).pack(pady=10)
email_entry=tk.Entry(root, width=35, font=("Arial",11))
email_entry.pack()

tk.Button(root, text="Validate", command=validate_email, font=("Arial",11)).pack(pady=10)
result_label=tk.Label(root, text="", font=("Arial",12))
result_label.pack()

root.mainloop()
