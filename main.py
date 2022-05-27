import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Constantes gráficas
width = 500
heigth = 750

# ___________________________________-Aplicacion Grafica_____________________________________________
root = tk.Tk()
root.configure(background='white')
root.title('Calculadora métodos númericos')

icon = tk.PhotoImage(file="Images/icon.png")
root.iconphoto(False, icon)

root.geometry('%dx%d+%d+%d' % (width, heigth, 20, 20))
root.resizable(height=False, width=False)

# _______________________________________Frames___________________________________________________

top_frame = tk.Frame(root, height=250, width=width, bg="white", bd=2)
top_frame.pack(fill='x')

methods_frame = tk.Frame(root, height=250, width=width, bg="blue", bd=2)
methods_frame.pack(fill='x')

calc_frame = tk.Frame(root, height=150, width=width, bg="red", bd=2)
calc_frame.pack(fill='x')

help_frame = tk.Frame(root, height=150, width=width, bg="grey", bd=2)
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
simple_methods_tabs = ttk.Frame(tabControl, width=width/2)
complex_methods_tabs = ttk.Frame(tabControl)

tabControl.add(simple_methods_tabs, text='Métodos simples')
tabControl.add(complex_methods_tabs, text='Métodos compuestos')
tabControl.pack(fill="x")


simple_methods_frame = tk.Frame(simple_methods_tabs, width=width, height=200,  bg="orange", bd=2)
simple_methods_frame.pack(fill='both')

complex_methods_frame = tk.Frame(complex_methods_tabs, width=width, height=200, bg="green", bd=2)
complex_methods_frame.pack(fill='both')

# ________________________________________Closing protocol______________________________________________
def on_closing():
    if messagebox.askokcancel("Salir", "Seguros que quieres salir?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

# ______________________________________________________________________________________________________

root.mainloop()
