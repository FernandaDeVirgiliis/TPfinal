import sqlite3

con = sqlite3.connect('mydatabase.db')
from tkinter import *
from tkinter import messagebox
import sqlite3


root=T()
root.tittle("aplicacion CRUD CON B.D)
root.geometry("500x350")

miLegajo=StringVar()
miNombre=StringVar()
miCargo=StringVar()
miSucursal=StringVar()

def conexionBBDD():
    miConexion=sqlite3.connect("bd")
    miCursor=miConexion.cursor()
