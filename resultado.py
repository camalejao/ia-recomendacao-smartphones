from tkinter import *  
from PIL import ImageTk, Image
from pathlib import Path

def mostrar_resultado(celular):
    ws = Tk()
    ws.title('Resultado: ' + celular['modelo'])
    ws.geometry("800x800")

    label1 = Label(ws, pady=20, text=celular['modelo'], font=("system", 32))
    label1.pack()

    label2 = Label(ws, text=celular['descricao'], font=("system", 14), wraplength=700)
    label2.pack()
    
    img = Image.open(Path(celular['imagem']))
    img = img.resize((img.width // 2, img.height // 2))
    img = ImageTk.PhotoImage(img)
    
    cv = Canvas()
    cv.pack(side='bottom', fill='both', expand='yes')
    pos = (800 - img.width()) // 2
    cv.create_image(pos, 50, image=img, anchor='nw')

    ws.mainloop()