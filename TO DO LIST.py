import tkinter as tk

root=tk.Tk()
root.geometry("600x420")
root.title("To Do list")
root.configure(bg="#CCCCCC")

def add_command():
    task=ent.get()
    lbox.insert(tk.END,task)
    ent.delete(0,tk.END)

def mark_command():
    pos=lbox.curselection()[0]
    text=lbox.get(pos)
    lbox.delete(pos)
    lbox.insert(tk.END,f"{text}\u2713")

def del_command():
    pos=lbox.curselection()[0]
    lbox.delete(pos)
    
lbl=tk.Label(root,text="Enter task:",font=('calibri',15),fg="#000000",bg="#33CCFF")
lbl.place(x=10,y=15)
lbl.configure(bg="#FFE4B5")

ent=tk.Entry(root,width=50)
ent.place(x=120,y=20)
ent.configure(bg="#99CCFF")

lbox=tk.Listbox(root,width=50,height=20)
lbox.place(x=120,y=70)
lbox.configure(bg="#99CCFF")

btnl=tk.Button(root,text="ADD",font=('calibri',15),width=10, bd=1,fg="#000000",bg="#F4A460",command=add_command)
btnl.place(x=450,y=110)

btn2=tk.Button(root,text="MARK",font=('calibri',15),width=10, bd=1,fg="#000000",bg="#F4A460",command=mark_command)
btn2.place(x=450,y=190)

btn3=tk.Button(root,text="REMOVE",font=('calibri',15),width=10, bd=1,fg="#000000",bg="#F4A460",command=del_command)
btn3.place(x=450,y=270)


root.mainloop()
