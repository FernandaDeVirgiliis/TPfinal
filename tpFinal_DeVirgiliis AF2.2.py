
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


root=Tk()
root.title("Programa CRUD con B.D")
root.geometry("600x350")

miLegajo=StringVar()
miNombre=StringVar()
miCargo=StringVar()
miSucursal=StringVar()

def conexionBBDD():
    miConexion=sqlite3.connect("bd")
    miCursor=miConexion.cursor()

#Creación de tablas
    
    try:
        miCursor.excute
        ('''
            CREATE TABLE empleado (
            LEGAJO INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            CARGO VARCHAR(50),
            SUCURSAL VARCHAR(50)
        ''')
        messagebox.showinfo("CONEXION","Base de datos creada exitosamente")
    except:
        ""

#Eliminar BD
        
def eliminarBBDD():
    miConexion=sqlite3.connect("bd")
    miCursor=miConexion.cursor()
    if messagebox.askyesno(message="Los datos seran eliminados ¿Desea continuar?", tittle="ADVERTENCIA"):
        miCursor.execute("DROPE TABLE empleado")
    else:
        pass


#Salir del programa

def salirPrograma():
    valor=messagebox.askquestion("Salir","¿Desea salir?")
    if valor=="yes":
        root.destroy()

#Limpiar campos

def limpiarCampos():
    miLegajo.set("")
    miNombre.set("")
    miCargo.set("")
    miSucursal.set("")



