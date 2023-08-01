import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: oscar
apellido: alonso
---
Ejercicio: instrucion_if_04
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, 
transformarlo en número y calcular si es adolescente (edad entre 13 y 17 años). Se deberá informar utilizando el Dialog alert.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        #entrada
        edad = self.txt_edad.get()

        #parseo de la variable
        edad_int = int(edad)

        #consultar si es adolescente
        if edad_int >= 13 or edad_int <= 17:
            mensaje = "es adolescente"
        else:
            mensaje = "no es adolescente"
        
        #salida
        alert(title="es adolescente?", message=mensaje)

        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
