
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

#Creacion métodos CRUD

def crear():
     miConexion=sqlite3.connect("bd")
     miCursor=miConexion.cursor()
     try:
         datos=miLegajo.get(),miNombre.get(),miCargo.get(),miSucursal.get()
         miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?)", (datos))
         miConexion.commit()
     except:
          messagebox.showarning("Ha ocurrido un error en el registro, verifique la conexion a la BD")
          pass
          limpiarCampos()
          mostrar()
def mostrar():
     miConexion=sqlite3.connect("bd")
     miCursor=miConexion.cursor()
     registros=tree.get_children()
     for elemento in registros:
         tree.delete(elemento)

     try:
         miCursor.execute("SELECT * FROM empleado")
         for row in miCursor:
             tree.insert("",0,text=row[0],values=(row[1],row[2],[row3]))
     except:
          pass
        



