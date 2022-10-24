from cgitb import grey
from fileinput import filename
from genericpath import isfile
import tkinter as tk 
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("Executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, background='gray')
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)



canvas = tk.Canvas(root, height=500, width=500, background="#263D42")
canvas.pack()

frame = tk.Frame(root, background='white')
frame.place(relheight=0.8, relwidth= 0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", fg="white", padx=10, pady=10, background="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", fg="white", padx=10, pady=10, background="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

#Once i've closed the file, it'll be saved 
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

