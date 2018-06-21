#######################################
########## Made by Jonathan Gañán #####
#######################################
#Nyaa-Downloader @ Copyright 2018 Jonathan Gañán
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
#and associated documentation files (the "Software"), to deal in the Software without 
#restriction, including without limitation the rights to use, copy, modify, merge, publish, 
#distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
#Software is furnished to do so, subject to the following conditions:

#NyaaPy @ Copyright 2017 Juanjo Salvador
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
#and associated documentation files (the "Software"), to deal in the Software without 
#restriction, including without limitation the rights to use, copy, modify, merge, publish, 
#distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
#Software is furnished to do so, subject to the following conditions:

from tkinter import ttk
from tkinter import *
import sys
import os
import re
import requests
import time
import shutil
from NyaaPy.nyaa import Nyaa
from pathlib import Path

# Config Ventana
master = Tk()
master.title('Nyaa-Torrent-Downloader v1.0')
master.resizable(width=FALSE, height=FALSE)
master.geometry("980x860+30+30")
home = str(Path.home())
Directorio = os.path.dirname(home + '\Documents' + '\\' + 'Nyaa-Downloader' + '\\')

# Funciones
# Funcion para cuando cambiamos de Idioma
def IdiomaEsp():
	global Lan1, Lan2, Lan3, Lan4, Lan5, Lan6, Lan7, Lan8, Lan9, Lan10, Lan11, ImgDescarga, ImgBuscar
	Lan1 = "Buscando: "
	Lan2 = "Se han encontrado "
	Lan3 = " Resultados"
	Lan4 = "Descargando: "
	Lan5 = "Descarga Finalizada: "
	Lan6 = "Búsqueda:"
	Lan7 = "Categoría:"
	Lan8 = "Resultados de la Búsqueda:"
	Lan9 = ('Anime - AMVs', 'Anime - Traducido al Inglés', 'Anime - No-Traducido al Inglés', 'Anime - RAW', 'Audio - Sin Pérdida', 'Audio - Con Pérdida', 'Literatura - Traducido al Inglés', 'Literatura - No-Traducido al Inglés', 'Literatura - RAW', 'Live Action - Traducido al Inglés', 'Live Action - Idol/Vídeo Promocional', 'Live Action - No-Traducido al Inglés', 'Live Action - RAW', 'Imágenes - Gráficos', 'Imágenes - Fotos', 'Software - Aplicaciones', 'Software - Juegos')
	Lan10 = "Progreso:"
	Lan11 = "No hay nínguna tarea en proceso."
	ImgDescarga = PhotoImage(file="assets/descargar.png")
	ImgBuscar = PhotoImage(file="assets/busca.png")
def IdiomaEng():
	global Lan1, Lan2, Lan3, Lan4, Lan5, Lan6, Lan7, Lan8, Lan9, Lan10, Lan11, ImgDescarga, ImgBuscar
	Lan1 = "Searching: "
	Lan2 = "Search found "
	Lan3 = " Results"
	Lan4 = "Downloading: "
	Lan5 = "Download Ended: "
	Lan6 = "Search:"
	Lan7 = "Category:"
	Lan8 = "Search Results:"
	Lan9 = ('Anime - AMVs', 'Anime - English-Translated', 'Anime - Non-English-Translated', 'Anime - RAW', 'Audio - Lossless', 'Audio - Lossy', 'Literature - English-Translated', 'Literature - Non-English-Translated', 'Literature - RAW', 'Live Action - English-Translated', 'Live Action - Idol/Promotional Video', 'Live Action - Non-English-Translated', 'Live Action - RAW', 'Pictures - Graphics', 'Pictures - Photos', 'Software - Applications', 'Software - Games')
	Lan10 = "Progress:"
	Lan11 = "There's no task in process."
	ImgDescarga = PhotoImage(file="assets/download.png")
	ImgBuscar = PhotoImage(file="assets/search.png")
# Funcion que se ejecuta cuando le damos al botón Buscar
def BuscarBoton():
	Listbox.delete(0, END)
	Diccionario = ""
	Lista = ""
	Valor = 0
	Valordelista = 1
	Palabra = ""
	global Almacen 
	Almacen = []
	Palabra = textoaintroducir.get()
	Valoractual = country.current()
	textoacambiar.set(Lan1 + Palabra)
	Tk.update(master)
	if Valoractual == 0:
		Numero = 1
		Decimal = 1
	elif Valoractual == 1:
		Numero = 1
		Decimal = 2
	elif Valoractual == 2:
		Numero = 1
		Decimal = 3
	elif Valoractual == 3:
		Numero = 1
		Decimal = 4
	elif Valoractual == 4:
		Numero = 2
		Decimal = 1
	elif Valoractual == 5:
		Numero = 2
		Decimal = 2
	elif Valoractual == 6:
		Numero = 3
		Decimal = 1
	elif Valoractual == 7:
		Numero = 3
		Decimal = 2
	elif Valoractual == 8:
		Numero = 3
		Decimal = 3
	elif Valoractual == 9:
		Numero = 4
		Decimal = 1
	elif Valoractual == 10:
		Numero = 4
		Decimal = 2
	elif Valoractual == 11:
		Numero = 4
		Decimal = 3
	elif Valoractual == 12:
		Numero = 4
		Decimal = 4
	elif Valoractual == 13:
		Numero = 5
		Decimal = 1
	elif Valoractual == 14:
		Numero = 5
		Decimal = 2
	elif Valoractual == 15:
		Numero = 6
		Decimal = 1
	elif Valoractual == 16:
		Numero = 6
		Decimal = 2	
	Diccionario = Nyaa.search(category=Numero, keyword=Palabra, subcategory=Decimal)
	for i in range(len(Diccionario)):
		Lista = Diccionario[(Valor)]
		Almacen.append(Lista["name"])
		Almacen.append(Lista["download_url"])
		Listbox.insert(Valor, str(Valordelista) + " - " + Lista["name"])
		Valordelista = Valordelista + 1
		Valor = Valor + 1
	Listbox.curselection()
	textoacambiar.set(Lan2 + str(Valor) + Lan3)
	Tk.update(master)
# Funcion para Tecla Enter
def BuscarEnter(s):
	Listbox.delete(0, END)
	Diccionario = ""
	Lista = ""
	Valor = 0
	Valordelista = 1
	Palabra = ""
	global Almacen 
	Almacen = []
	Palabra = textoaintroducir.get()
	Valoractual = country.current()
	textoacambiar.set(Lan1 + Palabra)
	Tk.update(master)
	if Valoractual == 0:
		Numero = 1
		Decimal = 1
	elif Valoractual == 1:
		Numero = 1
		Decimal = 2
	elif Valoractual == 2:
		Numero = 1
		Decimal = 3
	elif Valoractual == 3:
		Numero = 1
		Decimal = 4
	elif Valoractual == 4:
		Numero = 2
		Decimal = 1
	elif Valoractual == 5:
		Numero = 2
		Decimal = 2
	elif Valoractual == 6:
		Numero = 3
		Decimal = 1
	elif Valoractual == 7:
		Numero = 3
		Decimal = 2
	elif Valoractual == 8:
		Numero = 3
		Decimal = 3
	elif Valoractual == 9:
		Numero = 4
		Decimal = 1
	elif Valoractual == 10:
		Numero = 4
		Decimal = 2
	elif Valoractual == 11:
		Numero = 4
		Decimal = 3
	elif Valoractual == 12:
		Numero = 4
		Decimal = 4
	elif Valoractual == 13:
		Numero = 5
		Decimal = 1
	elif Valoractual == 14:
		Numero = 5
		Decimal = 2
	elif Valoractual == 15:
		Numero = 6
		Decimal = 1
	elif Valoractual == 16:
		Numero = 6
		Decimal = 2	
	Diccionario = Nyaa.search(category=Numero, keyword=Palabra, subcategory=Decimal)
	for i in range(len(Diccionario)):
		Lista = Diccionario[(Valor)]
		Almacen.append(Lista["name"])
		Almacen.append(Lista["download_url"])
		Listbox.insert(Valor, str(Valordelista) + " - " + Lista["name"])
		Valordelista = Valordelista + 1
		Valor = Valor + 1
	Listbox.curselection()
	textoacambiar.set(Lan2 + str(Valor) + Lan3)
	Tk.update(master)
# Para descargar el fichero
def Descarga():	
	Result = Listbox.curselection()
	Valordescarga = 0
	for i in range(len(Result)):
		pb.step(100)
		Tk.update(master)
		Enlace = Result[Valordescarga] * 2 + 1
		Nombre = Result[Valordescarga] * 2
		Valordescarga = Valordescarga + 1
		Porcentaje = 1 / int(len(Result)) * 100
		textoacambiar.set(Lan4 + Almacen[(Nombre)] + " " + str(Valordescarga) + "/" + str(len(Result)))
		URL = Almacen[(Enlace)]
		Barras = URL.split('/')
		Descargar = requests.get(URL)
		home = str(Path.home())
		pb.step(Porcentaje)
		Tk.update(master)
		with open(home + '\Downloads' + '\\' + Barras[4], 'wb') as f:
			f.write(Descargar.content)
			os.startfile(home + '\Downloads' + '\\' + Barras[4], 'open')
		textoacambiar.set(Lan5 + str(Valordescarga) + "/" + str(len(Result)))	
# Reabre la App
def Reiniciar():
    python = sys.executable
    os.execl(python, python, * sys.argv)
# Cambia el Contenido del Fichero Language.cfg a  Spanish
def FicheroaEspanol():
	with open((Directorio + '\\' + "Language.cfg"), "r") as file:
		lineasfichero = file.readlines()
		lineasfichero[0] = ("Language = Spanish")
		file.close()
	with open((Directorio + '\\' + "Language.cfg"), "w") as file:
		file.writelines(lineasfichero)
		file.close()
		
def FicheroaIngles():
	with open((Directorio + '\\' + "Language.cfg"), "r") as file:
		lineasfichero = file.readlines()
		lineasfichero[0] = ("Language = English")
		file.close()
	with open((Directorio + '\\' + "Language.cfg"), "w") as file:
		file.writelines(lineasfichero)	
		file.close()
# Funciones de los Botones
def Espanol():
	FicheroaEspanol()
	Reiniciar()
def English():
	FicheroaIngles()
	Reiniciar()

# Si el directorio no existe (First-Startup)
if not os.path.exists(Directorio):
	os.makedirs(Directorio)
	CualIdioma = open((Directorio + '\\' + "Language.cfg"), "w")
	CualIdioma.write("Language = English")
	CualIdioma.close()

QueIdioma = open((Directorio + '\\' + "Language.cfg"), "r")
IdiomaSeleccionado = QueIdioma.read()
if IdiomaSeleccionado == "Language = English":
	IdiomaEng()
elif IdiomaSeleccionado == "Language = Spanish":
	IdiomaEsp()
else:
	QueIdioma.close()
	shutil.rmtree(Directorio, ignore_errors=False)
	raise SystemExit()
	
# Config TODA LA INTERFAZ
ImgEsp = PhotoImage(file="assets/esp.png")
ImgEng = PhotoImage(file="assets/eng.png")
photo = PhotoImage(file="assets/fondo app.png")
wallpaper = Label(master,image=photo)
wallpaper.place(x=0, y=0, relwidth=1, relheight=1)
wallpaper.image=photo
textoinv = Frame(master)
textoinv.pack(anchor="nw", padx=30, pady=10)
texto1 = Label(master, text=Lan6, bg="black", fg="white", font=("Verdana", 14, "bold"))
texto1.pack(anchor="nw", padx=30, pady=5)
texto2 = Label(master, text=Lan7, bg="black", fg="white", font=("Verdana", 14, "bold"))
texto2.pack(anchor="nw", padx=30, pady=5)
texto2.place(x=500, y=30)
texto3 = Label(master, text=Lan8, bg="black", fg="white", font=("Verdana", 14, "bold"))
texto3.pack(anchor="nw", pady=5)
texto3.place(x=30, y=115)
textoaintroducir = Entry(master, width=30, bd=2, font=("Verdana", 13, "bold"))
textoaintroducir.pack(anchor="nw", padx=30)
countryvar = StringVar()
country = ttk.Combobox(textvariable=countryvar, width=30, state="readonly") 
country['values'] = Lan9
country.bind('<<ComboboxSelected>>')
country.pack(anchor="n")
country.current(1)
country.place(x=500, y=63)
boton = Button(master, bd=0, command=BuscarBoton)
boton.pack(anchor="ne", pady=20)
boton.place(x=785, y=32)
botonesp = Button(master, image=ImgEsp, bd=0, command=Espanol)
botonesp.pack(anchor="ne", pady=4)
botonesp.place(x=928, y=2)
botoneng = Button(master, image=ImgEng, bd=0, command=English)
botoneng.pack(anchor="ne", pady=4)
botoneng.place(x=952, y=2)
boton.config(image=ImgBuscar, width=140, height=60)
Listbox = Listbox(master, height=30, width=100, bd=2, activestyle="dotbox", font=("Arial", 12), selectmode=EXTENDED)
Listbox.pack(anchor="w", padx=30, pady=61)
boton2 = Button(master, bd=0, command=Descarga)
boton2.pack(anchor="ne", pady=20)
boton2.place(x=785, y=750)
boton2.config(image=ImgDescarga, width=140, height=60)
pb = ttk.Progressbar(master, orient='horizontal', mode='determinate')
pb.pack(expand=True,fill=NONE)
pb.place(x=140, y=760, width=475, height=30)
texto4 = Label(master, text=Lan10, bg="black", fg="white", font=("Verdana", 14, "bold"))
texto4.pack(anchor="nw")
texto4.place(x=22, y=760)
textoacambiar = StringVar(value=Lan11)
texto5 = Label(master, textvariable=textoacambiar, bg="black", fg="white", font=("Verdana", 9))
texto5.pack(anchor="nw")
texto5.place(x=144, y=798)
master.bind('<Return>', BuscarEnter)

mainloop()