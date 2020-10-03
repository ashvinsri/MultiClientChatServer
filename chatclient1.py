import socket
import threading
from tkinter import *
top=Tk()
top.geometry("400x400")
top.title("Prabhat")
top.maxsize(400,400)
large_font=('Verdana',10)
f=Canvas(top,bg="pink",width=400,height=380)
f.place(x=0,y=0)
topl=Label(top,bg="red",fg="white",wraplength=100)
topl.pack(anchor="center")
vbar=Scrollbar(top)
sf=("Algerian",20)
msglist=Listbox(top,height=30,width=80,yscrollcommand=vbar.set,bg="pink",font=sf,fg="green")
vbar.pack(side=RIGHT,fill=Y)
msglist.pack(side=RIGHT,fill=BOTH)
msglist.pack()
e1=Entry(top,width=35,font=large_font,relief=RAISED)
e1.place(x=2,y=378)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '192.168.137.1'
port = 8888
sock.connect((host,port))
topl.config(text="Connection Eastablished")
def sendmsg(event=None):
        messeg=e1.get()
        if messeg:
            messeg="\nPrabhat-->"+messeg
            sock.send(str.encode(messeg,"utf-8"))
            msglist.insert(END,messeg)
            
            
def run():
    ithread=threading.Thread(target=sendmsg)
    ithread.daemon=True
    ithread.start()
    while True:
        data=sock.recv(1024)
        if not data:
            break
        msglist.insert(END,data)
        

   

t=threading.Thread(target=run)
t.daemon=True
t.start()
b1=Button(top,width=15,text="Send",bg="lightgreen",fg="white",command=sendmsg)
b1.place(x=260,y=378)
top.mainloop()




    
