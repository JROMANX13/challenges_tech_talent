from tkinter import *

# Crear la ventana principal
root = Tk()
root.title("Calculadora básica")
root.resizable(0, 0)  # Impide el cambio de tamaño
root.geometry("292x306")

# Variables globales
num1 = None
num2 = None
operacion = None

def envia_boton(valor):
    """Inserta el valor en la pantalla de la calculadora."""
    anterior = pantalla.get()
    pantalla.delete(0, END)
    pantalla.insert(0, str(anterior) + str(valor))

def igual():
    """Realiza la operación y muestra el resultado en la pantalla."""
    try:
        global num2
        num2 = float(pantalla.get())
        pantalla.delete(0, END)
        
        if operacion == "+":
            pantalla.insert(0, num1 + num2)
        elif operacion == "-":
            pantalla.insert(0, num1 - num2)
        elif operacion == "*":
            pantalla.insert(0, num1 * num2)
        elif operacion == "/":
            pantalla.insert(0, num1 / num2)
    except (NameError, ValueError):
        pantalla.insert(0, "Error")

def seleccionar_operacion(op):
    """Selecciona la operación y guarda el primer número."""
    global num1, operacion
    num1 = float(pantalla.get())
    pantalla.delete(0, END)
    operacion = op

def despejar():
    """Limpia la pantalla."""
    pantalla.delete(0, END)

# Caja de texto
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=('arial', 18, 'bold'))
pantalla.grid(row=0, padx=2, pady=2, columnspan=4)

# Botones numéricos
for i in range(1, 10):
    Button(root, text=str(i), width=9, height=3, bg="white", fg="red", 
           borderwidth=0, cursor="hand2", command=lambda x=i: envia_boton(x)).grid(row=(i-1)//3 + 1, column=(i-1)%3, padx=1, pady=1)

Button(root, text="0", width=9, height=3, bg="white", fg="red", 
       borderwidth=0, cursor="hand2", command=lambda: envia_boton(0)).grid(row=4, column=1, padx=1, pady=1)

# Botón de igual
Button(root, text="=", width=9, height=3, bg="red", fg="white", 
       borderwidth=0, cursor="hand2", command=igual).grid(row=4, column=0, padx=1, pady=1)

# Botones de operaciones
operaciones = [
    ("+", 1, 3),
    ("-", 2, 3),
    ("*", 3, 3),
    ("/", 4, 3)
]

for op, row, col in operaciones:
    Button(root, text=op, width=9, height=3, bg="deep sky blue", fg="black", 
           borderwidth=0, cursor="hand2", command=lambda x=op: seleccionar_operacion(x)).grid(row=row, column=col, padx=1, pady=1)

# Botón de punto
Button(root, text=".", width=9, height=3, bg="spring green", fg="black", 
       borderwidth=0, cursor="hand2", command=lambda: envia_boton(".")).grid(row=4, column=2, padx=1, pady=1)

# Botón de despejar
Button(root, width=40, height=3, text="Borrar", bg="deep sky blue", 
       fg="black", borderwidth=0, cursor="hand2", command=despejar).grid(row=5, column=0, columnspan=4, padx=1, pady=1)

# Iniciar el bucle principal
mainloop()
