import socket
import threading
import time
import sys
from tkiner import*

box=Tk()
box.geometry("500x500")
box.config(bg="white")





start = PhotoImage(file=#insertlater)
button=Button(root,image=start,command=func, borderwidth=2)
button.place(x=90, y=20))

msg=StringVar()
msgbox=Entry(root,textvariable=message,font=("Arial",12,"normal"), border=2, width=2)

send = PhotoImage(file=#insertlater)
msgbutton=Button(root,image=send,command=threadsendmsg,borderwidth=2)
msgbutton.place(x=200,y=300)
 
lstbx=Listbox(root,height=20,width=43)
lstbx.place(x=15,y=80)
 
user_name = Label(root,text =" Number" ,width=10)
 
root.mainloop()















socket = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 8080 

socket.bind((host, port))

name = input('Enter name: ')
 
new_socket.listen(1) 
conn, add = new_socket.accept()
client = (conn.recv(1024)).decode()
 
conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)