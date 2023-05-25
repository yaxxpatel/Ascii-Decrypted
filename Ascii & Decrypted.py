# -*- coding: utf-8 -*-
"""
Created on Thu May 25 12:28:45 2023

@author: yaxxp
"""

from tkinter import*

root= Tk()
root.title("Ascii & Decrypted Converter")

root.geometry("500x500")
root.configure(background="light blue")

user_input = Entry(root)
user_input.place(relx=0.5,rely=0.5,anchor=CENTER)
ascii_code = Label(root)
decrypted_code = Label(root)

def Converter():
    user_input_get = user_input.get()
    for lettter in user_input_get :
        ascii_code["text"] += str(ord(Letter)) + "   "
        decrypt_ascii = int(ord(Letter))
        decrypment = decrypt_ascii - 1
        decrypted_code["text"] += chr(decrypment)
        
btn = Button(root, text = "show Decrypt and Ascii Code", command= Converter, bg= "cyan", fg="black")
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
ascii_code.place(relx=0.5,rely=0.7, anchor=CENTER)

user_input.pack()
btn.pack()
ascii_code.pack()
decrypted_code.pack()

root.mainloop()