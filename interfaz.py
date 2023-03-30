from email import message
from tkinter import messagebox
import gestor
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



def btnSimularClick():
    try:
        filas = int(cajaFilasSimular.get())
        desde = int(cajaParamMostarDesde.get())
        hasta = int(cajaCantMostrar.get())+desde
        probDeA = int(cajaProbDeA.get())
        probDeB = int(cajaProbDeB.get())
        probDeC = int(cajaProbDeC.get())
        tiempoA = float(cajaTiempoA.get())
        tiempoB = float(cajaTiempoB.get())
        tiempoC = float(cajaTiempoC.get())
        probDesperfecto = int(cajaProbDefectuoso.get())
        probDemora = int(cajaProbDemora.get())
        tiempoDemora = float(cajaTiempoDemora.get())
    
    except:
        alert()

    if (validar(filas,hasta,probDeA,probDeB,probDeC,tiempoA,tiempoB,tiempoC,probDesperfecto,probDemora,tiempoDemora)):

        cleanTable(treeResolucion)
        insertarFila(treeResolucion, gestor.empezarSimulacion(probDeA, probDeB, probDeC, tiempoA, tiempoB, tiempoC, probDesperfecto, probDemora, tiempoDemora), 0)

        i = gestor.fila.nroFila

        while i < filas:
            filaSimulada = gestor.calcularSiguienteFila()
            if i >= desde and i < hasta:
                insertarFila(treeResolucion, filaSimulada, i)
            i = gestor.fila.nroFila
        insertarFila(treeResolucion, gestor.calcularSiguienteFila(), filas)

        resultado(round(gestor.fila.promEspera,2))

        del gestor.fila  

    else:
        alert()
def resultado(x):
    lblResultado = tk.Label(p1, text="Resultado: El promedio de espera que se provee en la paradada es de {} minutos. ".format(x), font=("Courier 13 bold"))
    lblResultado.place(x=10, y=710)

def alert():
    messagebox.showinfo(message="Verificar dataos ingresados", title="Alerta")

def habilitarBoton():
    botonSimular["state"] = "normal"

def desabilitarBoton():
    botonSimular["state"] = "disable"

def cleanTable(tabla):
    tabla.delete(*tabla.get_children())


def insertarFila(treeview, fila, n):

    if gestor.fila.nroFila % 2 == 0:
        treeview.insert(parent='', index='end', text=str(n), values=fila, tags = ("even"))
    else:
        treeview.insert(parent='', index='end', text=str(n), values=fila, tags = ("odd"))


# Interfaz
miWindow = tk.Tk()  # Creacion de la ventana contenedora
miWindow.title("Ejercicio 290 - Montuori 79064")
miWindow.geometry("1500x780")
miWindow.resizable(False, False)
# Pestaña
nb = ttk.Notebook(miWindow)
nb.pack(fill='both', expand='yes')

# Creamos Pestañas
p1 = ttk.Frame(nb)


# Interacciones y objetos
# Parametros adicionales:
cajaFilasSimular = tk.Entry(p1, width=6)
cajaFilasSimular.insert(0, 500)
lblFilasSimular = tk.Label(p1, text="Filas a simular")
cajaFilasSimular.place(x=100, y=10)
lblFilasSimular.place(x=5, y=10)


cajaProbDeA = tk.Entry(p1, width=6)
cajaProbDeA.insert(0, 20)
lblProbDeA = tk.Label(p1, text="Prob. de A %")
cajaProbDeA.place(x=275, y=10)
lblProbDeA.place(x=170, y=10)


cajaProbDeB = tk.Entry(p1, width=6)
cajaProbDeB.insert(0, 40)
lblProbDeB = tk.Label(p1, text="Prob. de B %")
cajaProbDeB.place(x=275, y=40)
lblProbDeB.place(x=170, y=40)


cajaProbDeC = tk.Entry(p1, width=6)
cajaProbDeC.insert(0, 40)
lblProbDeC = tk.Label(p1, text="Prob. de C %")
cajaProbDeC.place(x=275, y=70)
lblProbDeC.place(x=170, y=70)


cajaTiempoA = tk.Entry(p1, width=6)
cajaTiempoA.insert(0, 20)
lblTiempoA = tk.Label(p1, text="Tiempo A")
cajaTiempoA.place(x=440, y=10)
lblTiempoA.place(x=350, y=10)



cajaTiempoB = tk.Entry(p1, width=6)
cajaTiempoB.insert(0, 40)
lblTiempoB = tk.Label(p1, text="Tiempo B")
cajaTiempoB.place(x=440, y=40)
lblTiempoB.place(x=350, y=40)


cajaTiempoC = tk.Entry(p1, width=6)
cajaTiempoC.insert(0, 120)
lblTiempoC = tk.Label(p1, text="Tiempo C")
cajaTiempoC.place(x=440, y=70)
lblTiempoC.place(x=350, y=70)


cajaProbDemora = tk.Entry(p1, width=6)
cajaProbDemora.insert(0, 30)
lblProbDemora = tk.Label(p1, text="Prob. Demora %")
cajaProbDemora.place(x=630, y=10)
lblProbDemora.place(x=510, y=10)


cajaTiempoDemora = tk.Entry(p1, width=6)
cajaTiempoDemora.insert(0, 5)
lblTiempoDemora = tk.Label(p1, text="Tiempo Demora")
cajaTiempoDemora.place(x=630, y=40)
lblTiempoDemora.place(x=510, y=40)


cajaProbDefectuoso = tk.Entry(p1, width=6)
cajaProbDefectuoso.insert(0, 10)
lblProbDefectuoso = tk.Label(p1, text="Prob. Defectuoso %")
cajaProbDefectuoso.place(x=630, y=70)
lblProbDefectuoso.place(x=510, y=70)


cajaParamMostarDesde = tk.Entry(p1, width=6)
cajaParamMostarDesde.insert(0, 0)
lblParamMostarDesde = tk.Label(p1, text="Mostrar desde:")
cajaParamMostarDesde.place(x=850, y=10)
lblParamMostarDesde.place(x=710, y=10)


cajaCantMostrar = tk.Entry(p1, width=6)
cajaCantMostrar.insert(0, 500)
lblCantMostrar = tk.Label(p1, text="Cantidad a mostrar:")
cajaCantMostrar.place(x=850, y=40)
lblCantMostrar.place(x=710, y=40)


def validar(filas,hasta,probDeA,probDeB,probDeC,tiempoA,tiempoB,tiempoC,probDesperfecto,probDemora,tiempoDemora):

    if (hasta > filas):
        return False
    elif ((probDeA + probDeB + probDeC) != 100):
        return False
    elif (probDemora > 100 or probDesperfecto > 100):
        return False
    else:
        return True
  
    


botonSimular = tk.Button(p1, text="Simular", padx=10,
                         pady=5, command=btnSimularClick, state="normal")


botonSimular.place(x=950, y=10)



# Treeview Resolucion del ejercicio

headerColas =  ["Nro Fila", "Reloj (min)", "Rnd Llegada", "Tiempo de Llegada", "Rnd Demora", "Existe Demora",
                "Rnd Desperfecto", "Existe Desperfecto", "Proxima Llegada", "Acu. Autobuses", "Promedio Espera"]
                     
treeResolucion = ttk.Treeview(p1, height=29, column=[
                              f"#{cantidad}" for cantidad in range(1, len(headerColas) + 1)], show='headings')
treeResolucion.place(x=8, y=95)


for i in range(len(headerColas)):
    treeResolucion.column("#" + str(i + 1), anchor=tk.CENTER, width=130, minwidth=len(headerColas[i]) * 8 + 5,
                          stretch=True)
    treeResolucion.heading("#" + str(i + 1), text=headerColas[i])
    
vsb = ttk.Scrollbar(p1, orient="vertical", command=treeResolucion.yview)
vsb.pack(side='right', fill='y')
treeResolucion.configure(yscrollcommand=vsb.set)
vsb = ttk.Scrollbar(p1, orient="horizontal", command=treeResolucion.xview)
vsb.pack(side='bottom', fill='x')
treeResolucion.tag_configure("odd",background="#eee")
treeResolucion.tag_configure("even",background="#ddd")
treeResolucion.configure(xscrollcommand=vsb.set)






# Añadimos Pestañas al window
nb.add(p1, text="Ejercicio")


miWindow.mainloop()