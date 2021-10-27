
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
    miConexion=sqlite3.connect("mydatabase")
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
    miConexion=sqlite3.connect("mydatabase")
    miCursor=miConexion.cursor()
    if messagebox.askyesno(message="Los datos seran eliminados ¿Desea continuar?", tittle="ADVERTENCIA"):
        miCursor.execute("DROP TABLE empleado")
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
    miConexion=sqlite3.connect("mydatabase.db")
    miCursor=miConexion.cursor()
    datos=miLegajo.get(),miNombre.get(),miCargo.get(),miSucursal.get()
    print(datos)
    consulta=("INSERT INTO empleado VALUES (?,?,?,?)")
    resultado=miCursor.execute(consulta,[miLegajo.get(),miNombre.get(),miCargo.get(),miSucursal.get()])
    miConexion.commit()
    
    messagebox.showinfo("BBDD","Registro insertado con éxito")



def mostrar():
     miConexion=sqlite3.connect("mydatabase.db")
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
        

#Creacion de tabla
tree=ttk.Treeview(height=10, columns=('#1','#2','#3'))
tree.place(x=0, y=130)
tree.heading('#0', text="Legajo", anchor=CENTER)
tree.heading('#1', text="Nombre", anchor=CENTER)
tree.heading('#2', text="Puesto", anchor=CENTER)
tree.heading('#3', text="Sucursal", anchor=CENTER)


    
#Creacion de funcion UDPATE
def actualizar():
     miConexion=sqlite3.connect("mydatabase.db")
     miCursor=miConexion.cursor()
     try:
         datos=miNombre.get(),miCargo.get(),miSucursal.get()
         miCursor.execute("INSERT empleado SET NOMBRE=?,PUESTO=?,SUCURSAL=? WHERE Legajo=+miLegajo.get()(datos))")
         miConexion.commit()

     except:
          messagebox.showwarning("Ha ocurrido un error al actualizar el registro")
          pass
          limpiarCampos()
          mostrar()
    
#Creacion de funcion ELIMINAR

def eliminar():
    miConexion=sqlite3.connect("mydatabase.db")
    miCursor=miConexion.cursor()
    try:
        if messagebox.askyesno(message="Está segurx que desea eliminar el registro?", title="Advertencia"):
            miCursor.execute("DELETE FROM empleado WHERE Legajo=+miLegajo.get()")
            miConexion.commit()
    except:
         messagebox.showwarning("Ha ocurrido un error al eliminar los registros")
         pass
         limpiarCampos()
         mostrar()



###################

#Colocaciónd de elementos en la ventana
##Menu        

menubar=Menu(root)
menubasedat=Menu(menubar, tearoff=0)
menubasedat.add_command(label="Conectar", command=conexionBBDD)
menubasedat.add_command(label="Eliminar base de datos", command=eliminarBBDD)
menubar.add_cascade(label="Inicio", menu=menubasedat)


ayudamenu=Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Limpiar campos", command=limpiarCampos)

menubar.add_cascade(label="Ayuda", menu=ayudamenu)


l1=Label(root, text="Legajo")
l1.place(x=50,y=10)
e1=Entry(root, textvariable=miLegajo)
e1.place(x=100,y=10)

l2=Label(root, text="Nombre y Apellido")
l2.place(x=50,y=40)
e2=Entry(root, textvariable=miNombre, width=50)
e2.place(x=100,y=40)

l3=Label(root, text="Puesto")
l3.place(x=50,y=70)
e3=Entry(root, textvariable=miCargo)
e3.place(x=100,y=70)

l4=Label(root, text="Sucursal")
l4.place(x=230,y=10)
e4=Entry(root, textvariable=miSucursal, width=10)
e4.place(x=280,y=10)

b1=Button(root, text="Crear", command=crear)
b1.place(x=50,y=100)


b2=Button(root, text="Leer", command=mostrar)
b2.place(x=180,y=100)

b3=Button(root, text="Actualizar", command=actualizar)
b3.place(x=320,y=100)

b4=Button(root, text="Eliminar", bg="red", command=eliminar)
b4.place(x=450,y=100)


###############




root.config(menu=menubar)

         


root.mainloop()
        
    
