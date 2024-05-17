from tkinter import *
from tkinter import filedialog, messagebox

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    if filename == "Untitled" or filename is None:
        saveAs()
    else:
        t = text.get(0.0, END)
        try:
            with open(filename, 'w') as f:
                f.write(t.rstrip())
        except Exception as e:
            messagebox.showerror("Error", f"Unable to save file: {e}")

def saveAs():
    global filename
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if f is None:
        return
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
        filename = f.name
    except Exception as e:
        messagebox.showerror("Error", f"Unable to save file: {e}")

def openFile():
    f = filedialog.askopenfile(mode='r')
    if f is not None:
        t = f.read()
        text.delete(0.0, END)
        text.insert(0.0, t)
        global filename
        filename = f.name

root = Tk()
root.title('My Python Text Editor')
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)

text = Text(root, wrap='word')
text.pack(expand=YES, fill=BOTH)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
