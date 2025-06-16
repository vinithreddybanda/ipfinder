import tkinter as tk
from tkinter import messagebox 
from socket import gethostbyname
from socket import gethostname
 
def ipFinder(outputMsg, inputValue):
    try:
        ipAddress = gethostbyname(inputValue.get())
        outputMsg.config(text="The IP of domain " + inputValue.get() + " is \"" + ipAddress + "\"")
    except Exception:
      messagebox.showerror('Error','invalid host name or Check Internet connection')
 
Tk = tk.Tk()
 
Tk.geometry("400x400")


#get my hostname 
my_hostname = gethostname() 
#display my hostname 
lbl1 = tk.Label(Tk, text="Your Host Name:"+my_hostname,background='#191919', foreground="#ffffff", font=("Courier", 15)) 
#get my ip
my_ip = gethostbyname(my_hostname) 
#display my IP 
lbl2 = tk.Label(Tk, text=my_hostname+"IP:"+my_ip,background='#191919', foreground="#ffffff", font=("Courier", 15)) 
lbl1.grid(column=0, row=0) 
lbl2.grid(column=0, row=2)
 
inputString = tk.StringVar()
 
websiteName = tk.Label(Tk, text="Enter domain:", background='#191919', foreground="#ffffff", font=("Courier", 15))
input_entry = tk.Entry(Tk, textvariable=inputString)
websiteName.grid(row=4)
input_entry.grid(row=4, column=1)
 
outputMsg = tk.Label(Tk, background='#191919', foreground="#ffffff", font=("Courier", 15))
outputMsg.grid(row=7, columnspan=3)
 
button = tk.Button(Tk, text="Check IP",background='#5c5c5c', foreground="#ffffff", font=("Courier", 15), command=lambda : ipFinder(outputMsg, inputString))
button.grid(row=9, columnspan=4)
 
Tk.title('Domain-IP Checker')
Tk.configure(background='#191919')

Tk.mainloop()
