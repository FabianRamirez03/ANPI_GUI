import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import Metodos

# Constantes gráficas
width = 500
heigth = 670

font = "Calibri"

# _______________________________________Funciones______________________________________________

functions = ["trapecio", "simpson", "boole", "trapecioCompuesto", "simpsonCompuesto", "gaussian"]
args = ["()", "()", "(function_string, a, b)", "()", "(function_string, a, b, puntos)",
        "(function_string, a, b, puntos)"]


def calcular():
    global var, functions, args
    function_string = function_entry.get()
    a = int(a_entry.get())
    b = int(b_entry.get())
    # Checkear continuidad de la función
    puntos = int(points_entry.get())
    values = eval('Metodos.' + functions[var.get()] + args[var.get()])
    setAproxText(values[0])
    setErrorText(values[1])


def setAproxText(text):
    aprox_entry.delete(0, tk.END)
    aprox_entry.insert(0, text)
    return


def setErrorText(text):
    error_entry.delete(0, tk.END)
    error_entry.insert(0, text)
    return


# ___________________________________Aplicacion Grafica_____________________________________________
root = tk.Tk()
root.configure(background='white')
root.title('Calculadora métodos númericos')

icon = tk.PhotoImage(file="Images/icon.png")
root.iconphoto(False, icon)

root.geometry('%dx%d+%d+%d' % (width, heigth, 20, 20))
root.resizable(height=False, width=False)

# _______________________________________Frames___________________________________________________

top_frame = tk.Frame(root, height=225, width=width, bg="white", bd=0)
top_frame.pack(fill='x')

methods_frame = tk.Frame(root, height=250, width=width, bg="white", bd=0)
methods_frame.pack(fill='x')

calc_frame = tk.Frame(root, height=150, width=width, bg="white", bd=0)
calc_frame.pack(fill='x')

help_frame = tk.Frame(root, height=150, width=width, bg="white", bd=0)
help_frame.pack(fill='x')

# ________________________________________Methods Tabs_________________________________________________________
style = ttk.Style()

tab_color = "#E4E4E4"
tab_selected_color = "#FFFFFF"
style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [1, 0, 1, 0]}},
    "TNotebook.Tab": {
        "configure": {"padding": [70, 1], "background": tab_color},
        "map": {"background": [("selected", tab_selected_color)],
                "expand": [("selected", [1, 1, 1, 0])]}}})

style.configure("TNotebook", background='white', borderwidth=0)
style.theme_use("MyStyle")

tabControl = ttk.Notebook(methods_frame, width=width)
simple_methods_tabs = ttk.Frame(tabControl, width=width / 2)
complex_methods_tabs = ttk.Frame(tabControl)

tabControl.add(simple_methods_tabs, text='Métodos simples')
tabControl.add(complex_methods_tabs, text='Métodos compuestos')
tabControl.pack(fill="x")

simple_methods_frame = tk.Frame(simple_methods_tabs, width=width, height=200, bg="white", bd=1)
simple_methods_frame.pack(fill='both')

complex_methods_frame = tk.Frame(complex_methods_tabs, width=width, height=200, bg="white", bd=1)
complex_methods_frame.pack(fill='both')

# ________________________________________Top Frame Content______________________________________________

# Titulo
title_frame = tk.Label(top_frame, text="Calculadora de integrales Definidas", background="white", font=(font, 18))
title_frame.place(x=60, y=10)

# Imagen de la integral
integral_image = Image.open("Images/integral.png")
resize_factor = 0.62
resize_tuple = (int(230 * resize_factor), int(120 * resize_factor))
integral_image = integral_image.resize(resize_tuple)
integral_photoImage = ImageTk.PhotoImage(integral_image)
integral_image_label = tk.Label(top_frame, image=integral_photoImage, borderwidth=0, border=0)
integral_image_label.image = integral_photoImage
integral_image_label.place(x=180, y=45)

# Entry de la integral
function_label = tk.Label(top_frame, text="F(x)   = ", background="white", font=(font, 12))
function_label.place(x=80, y=120)

function_stringVar = tk.StringVar(root, value='x')

function_entry = tk.Entry(top_frame, bd=1, background='white', font=(font, 12), justify=tk.CENTER, width=32, textvariable=function_stringVar)
function_entry.place(x=150, y=122)

zero_stringVar = tk.StringVar(root, value='0')

# Entry de a
a_label = tk.Label(top_frame, text="a  =", background="white", font=(font, 12))
a_label.place(x=130, y=170)

a_entry = tk.Entry(top_frame, bd=1, background='white', font=(font, 12), justify=tk.CENTER, width=5, textvariable=zero_stringVar)
a_entry.place(x=180, y=170)

# Entry de b
b_label = tk.Label(top_frame, text="b  =", background="white", font=(font, 12))
b_label.place(x=280, y=170)

b_entry = tk.Entry(top_frame, bd=1, background='white', font=(font, 12), justify=tk.CENTER, width=5, textvariable=zero_stringVar)
b_entry.place(x=330, y=170)

# ________________________________________Complex method tab Content______________________________________________

var = tk.IntVar()
trapecio_radio = tk.Radiobutton(simple_methods_frame, text="Trapecio", variable=var, value=0, font=(font, 12),
                                background="white")
trapecio_radio.place(x=170, y=40)

simpson_radio = tk.Radiobutton(simple_methods_frame, text="Simpson", variable=var, value=1, font=(font, 12),
                               background="white")
simpson_radio.place(x=170, y=80)

boole_radio = tk.Radiobutton(simple_methods_frame, text="Regla de Boole", variable=var, value=2, font=(font, 12),
                             background="white")
boole_radio.place(x=170, y=120)

# ________________________________________Simple method tab Content______________________________________________


trapecio_complex_radio = tk.Radiobutton(complex_methods_frame, text="Trapecio compuesto", variable=var, value=3,
                                        font=(font, 12), background="white")
trapecio_complex_radio.place(x=60, y=40)

simpson_complex_radio = tk.Radiobutton(complex_methods_frame, text="Simpson compuesto", variable=var, value=4,
                                       font=(font, 12), background="white")
simpson_complex_radio.place(x=60, y=80)

gaussian_radio = tk.Radiobutton(complex_methods_frame, text="Cuadraturas Gaussian", variable=var, value=5,
                                font=(font, 12), background="white")
gaussian_radio.place(x=60, y=120)

# Entry de puntos a utilizar
points_label = tk.Label(complex_methods_frame, text="Puntos a utilizar =", background="white", font=(font, 12))
points_label.place(x=260, y=80)


points_entry = tk.Entry(complex_methods_frame, bd=1, background='white', font=(font, 12), justify=tk.CENTER, width=6, textvariable=zero_stringVar)
points_entry.place(x=400, y=80)

# ________________________________________Calc tab Content______________________________________________

# Boton para calcular
calc_photoImage = tk.PhotoImage(file="Images/button_calcular.png")
calc_button = tk.Button(calc_frame, image=calc_photoImage, borderwidth=0, background="white", command=calcular)
calc_button.place(x=180, y=2)

# Entry de la aproximación
aprox_label = tk.Label(calc_frame, text="Aproximación =", background="white", font=(font, 12))
aprox_label.place(x=60, y=80)

aprox_entry = tk.Entry(calc_frame, bd=1, background='white', font=(font, 12), justify=tk.CENTER, width=22)
aprox_entry.place(x=180, y=80)

# Entry del error
error_label = tk.Label(calc_frame, text="Error =", background="white", font=(font, 12))
error_label.place(x=60, y=110)

error_entry = tk.Entry(calc_frame, bd=1, background='white', font=(font, 12), justify=tk.CENTER, width=22)
error_entry.place(x=180, y=110)

# ________________________________________Help tab Content______________________________________________

# Boton para ayuda
help_photoImage = tk.PhotoImage(file="Images/button_ayuda.png")
help_button = tk.Button(help_frame, image=help_photoImage, borderwidth=0, background="white")
help_button.place(x=210, y=2)


# ________________________________________Closing protocol______________________________________________
def on_closing():
    if messagebox.askokcancel("Salir", "Seguros que quieres salir?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

# ______________________________________________________________________________________________________

root.mainloop()
