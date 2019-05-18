#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:21:30 2019

@author: couto
"""
from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox



ruta = ''
    
    
def nuevo():
    mensaje.set('Nuevo fichero')
    texto.delete(1.0, END)

def abrir():
    
    #Beware pof the last comma in filetypes, it's needed
    global ruta
    ruta = FileDialog.askopenfilename(initialdir='.',
                                          title="Abrir un fichero",
                                          filetypes=(
                                                  ("txt files", "*.txt"),)
                                          ) 
    if ruta != '':
        fichero = open(ruta, 'r')
        contenido = fichero.read()                                          
        texto.delete(1.0, END)
        texto.insert(END, contenido)
        fileName = ruta.split("/")[-1]
        root.title(fileName + " - Mi editor")
        mensaje.set(ruta)
    else:
        MessageBox.showwarning('Warning', 'ruta seleccionada no valida \n {}'.format(ruta))

        
    
def guardar():
    global ruta
    if ruta != '':
        contenido = texto.get(1.0, "end")
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        MessageBox.showinfo('Info', 'Fichero Guardado correctamente')
   
    
    
def guardar_como():
    print("Guardando como")
    fichero = FileDialog.asksaveasfilename(initialdir = ".",title = "Guardar fichero",filetypes = (("Text files","*.txt"),))
    ruta = fichero.name
    if fichero is not None:
        contenido = texto.get(1.0, "end")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set(ruta)
    else: 
        MessageBox.askokcancel("Confirmación requerida","Confirme que desea sobreescribir el fichero existente")



root = Tk()
root.title("Mi editor")


#Menu archivo
menubar = Menu(root)
root.config(menu=menubar)

#Items del menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command = nuevo)
filemenu.add_command(label="Abrir", command = abrir)
filemenu.add_command(label="Guardar", command = guardar)
filemenu.add_command(label="Guardar Como", command = guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

#Items engadidos
menubar.add_cascade(label="Archivo", menu=filemenu)


#Text Area
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(padx=6, pady=4, bd = 0, font=("Consolas",12))



#Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido a tu editor')
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side ='left')

#loop
root.mainloop()