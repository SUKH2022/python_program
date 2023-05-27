from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans= Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb.sor.get()
    d=comb_dest.get()
    masg=sor_txt.get(1.0,END)
    textget=change(text=masg,src=s,dest=d)
    dest_text.delete(1.0,END)
    dest_txt.insert(END,textget)
    
root=Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="Light blue")

lab_txt=Label(root,text="Translator",font=("Times New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,widht=300)

frame=Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Times New Roman",20,"bold",fg="Black",bg="red")) 
