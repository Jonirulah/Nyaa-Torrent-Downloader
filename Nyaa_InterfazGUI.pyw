
from tkinter import ttk
from tkinter import *
import os
import requests
import shutil
from NyaaPy.nyaa import Nyaa
from pathlib import Path

# Config Ventana
master = Tk()
master.title('Nyaa-Torrent-Downloader v1.2')
master.resizable(width=FALSE, height=FALSE)
master.geometry("980x860+30+30")

master.iconbitmap("icon.ico")
home = str(Path.home())
Directorio = os.path.dirname(home + '\Documents' + '\\' + 'Nyaa-Downloader' + '\\')

# Funciones
# Funcion para cuando cambiamos de Idioma
def IdiomaEsp():
	global Lan1, Lan2, Lan3, Lan4, Lan5, Lan6, Lan7, Lan8, Lan9, Lan10, Lan11, ImgDescarga, ImgBuscar, seedersactivos, leechersactivos
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
	seedersactivos = "0"
	leechersactivos = "0"
	ImgDescarga = PhotoImage(file="assets/descargar.png")
	ImgBuscar = PhotoImage(file="assets/busca.png")

def IdiomaEng():
	global Lan1, Lan2, Lan3, Lan4, Lan5, Lan6, Lan7, Lan8, Lan9, Lan10, Lan11, ImgDescarga, ImgBuscar, seedersactivos, leechersactivos
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
	seedersactivos = "0"
	leechersactivos = "0"
	ImgDescarga = PhotoImage(file="assets/download.png")
	ImgBuscar = PhotoImage(file="assets/search.png")

# Funcion que se ejecuta cuando le damos al botón Buscar
def BuscarBoton():
	Listbox.delete(0, END)
	Valordelista = 1
	global Almacen, Almacen2
	Almacen = []
	Almacen2 = []
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
		Lista = Diccionario[(i)]
		Almacen.append(Lista["name"])
		Almacen.append(Lista["download_url"])
		Almacen2.append(Lista["seeders"])
		Almacen2.append(Lista["leechers"])
		Listbox.insert(i, str(Valordelista) + " - " + Lista["name"])
		Valordelista = Valordelista + 1
	Listbox.curselection()
	textoacambiar.set(Lan2 + str(i) + Lan3)
	Tk.update(master)
	master.after(675, seedleech)

# Funcion para Tecla Enter
def BuscarEnter(s):
	Listbox.delete(0, END)
	Valordelista = 1
	global Almacen, Almacen2
	Almacen = []
	Almacen2 = []
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
		Lista = Diccionario[(i)]
		Almacen.append(Lista["name"])
		Almacen.append(Lista["download_url"])
		Almacen2.append(Lista["seeders"])
		Almacen2.append(Lista["leechers"])
		Listbox.insert(i, str(Valordelista) + " - " + Lista["name"])
		Valordelista = Valordelista + 1
	textoacambiar.set(Lan2 + str(i) + Lan3)
	Tk.update(master)
	master.after(900, seedleech)

# Para descargar el fichero
def Descarga():
	Result = Listbox.curselection()
	print(Result)
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

# Cambia el Contenido del Fichero Language.cfg a Spanish
def FicheroaEspanol():
	with open((Directorio + '\\' + "Language.cfg"), "r") as file:
		lineasfichero = file.readlines()
		lineasfichero[0] = ("Language = Spanish")
		file.close()
	with open((Directorio + '\\' + "Language.cfg"), "w") as file:
		file.writelines(lineasfichero)
		file.close()

# Cambia el Contenido del Fichero Language.cfg a English
def FicheroaIngles():
	with open((Directorio + '\\' + "Language.cfg"), "r") as file:
		lineasfichero = file.readlines()
		lineasfichero[0] = ("Language = English")
		file.close()
	with open((Directorio + '\\' + "Language.cfg"), "w") as file:
		file.writelines(lineasfichero)
		file.close()

# Funciones de los Botones (Lenguaje)
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

# Auto Update Leech after searching 675ms update
def seedleech():
	CalcSemillas = 0
	CalcLeechers = 0
	global Almacen2
	Result = Listbox.curselection()
	master.after(675, seedleech)
	CalcSemillas = Result[0] * 2
	CalcLeechers = Result[0] * 2 + 1
	Semillas = Almacen2[(CalcSemillas)]
	Leechers = Almacen2[(CalcLeechers)]
	seeders.set(Semillas)
	leechers.set(Leechers)


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
texto3.place(x=30, y=105)
textoaintroducir = Entry(master, width=30, bd=2, font=("Verdana", 13, "bold"))
textoaintroducir.pack(anchor="nw", padx=30)
countryvar = StringVar()
country = ttk.Combobox(textvariable=countryvar, width=32, state="readonly")
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
Listbox = Listbox(master, height=30, width=100, bd=2, activestyle="dotbox", font=("Arial", 12, "bold"), selectmode=EXTENDED)
Listbox.pack(anchor="w", padx=30, pady=49)
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
seeders = StringVar(value=seedersactivos)
leechers = StringVar(value=leechersactivos)
texto5 = Label(master, textvariable=textoacambiar, bg="black", fg="white", font=("Verdana", 9))
texto5.pack(anchor="nw")
texto5.place(x=144, y=798)
textoseed = Label(master, textvariable=seeders, bg="black", fg="green", font=("Verdana", 9, "bold"))
textoseed.pack(anchor="nw")
textoseed.place(x=740, y=755)
textoleech = Label(master, textvariable=leechers, bg="black", fg="red", font=("Verdana", 9, "bold"))
textoleech.pack(anchor="nw")
textoleech.place(x=740, y=785)
texto8 = Label(master, text="Seeders:", bg="black", fg="white", font=("Verdana", 9, "bold"))
texto8.pack(anchor="nw")
texto8.place(x=660, y=755)
texto9 = Label(master, text="Leechers:", bg="black", fg="white", font=("Verdana", 9, "bold"))
texto9.pack(anchor="nw")
texto9.place(x=660, y=785)
master.bind('<Return>', BuscarEnter)

mainloop()
