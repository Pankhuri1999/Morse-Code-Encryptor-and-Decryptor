import encrypt as cipher
import decrypt as decipher   

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import appBackEnd

def vp_start_gui():
    
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    appBackEnd.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    appBackEnd.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):

        
        _bgcolor = 'white'
        _fgcolor = 'black'  

        top.geometry("1000x500+390+200")
        top.minsize(150, 1)
        top.maxsize(1900, 1030)
        top.resizable(1, 1)
        top.title("Morse Code Converter")
        top.iconbitmap('MorseIcon.ico')
        top.configure(background="pink")

        self.text1 = tk.Entry(top)
        self.text1.place(relx=0.300, rely=0.275,height=100, relwidth=0.304)
        self.text1.configure(background="white")
        self.text1.configure(insertbackground="black")

        self.text2 = tk.Message(top)
        self.text2.place(relx=0.300, rely=0.690,height=100, relwidth=0.304)
        self.text2.configure(background="white")
        self.text2.configure(highlightcolor="black")
        self.text2.configure(width=100)
        
        def call():
            plain_text =self.text1.get().upper()
            ans=cipher.encryptor(plain_text)
            self.text2.configure(text=ans)

        def get():
            encrypted_text =self.text1.get()
            x=decipher.decryptor(encrypted_text)
            self.text2.configure(text=x)

        self.button1 = tk.Button(top)
        self.button1.place(relx=0.300, rely=0.520, height=33, width=106)

        self.button1.configure(highlightcolor="black")
        self.button1.configure(pady="0")
        self.button1.configure(text='''Encrypt''',command=call)

        self.button2 = tk.Button(top)
        self.button2.place(relx=0.443, rely=0.520, height=33, width=106)
  
        self.button2.configure(highlightcolor="black")
        self.button2.configure(pady="0")
        self.button2.configure(text='''Decrypt''',command=get)

        self.label1 = tk.Label(top)
        self.label1.place(relx=0.130, rely=0.050, height=90, width=1100)
        self.label1.configure(background="skyblue")

        self.label1.configure(foreground="black")
        self.label1.configure(text='''ENCRYPT  AND  DECRYPT  TOOL''',font=("times",50))

        self.label2 = tk.Label(top)
        self.label2.place(relx=0.300, rely=0.210, height=26, width=300)
        self.label2.configure(background="skyblue")
 
        self.label2.configure(text='''Type your input''',font=("times",15,'bold'))

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.label3 = tk.Label(top)
        self.label3.place(relx=0.300, rely=0.625, height=26, width=400)
        self.label3.configure(background="skyblue")

        self.label3.configure(text='''Your output is displayed below''',font=("times",15,'bold'))

if __name__ == '__main__':
    vp_start_gui()
