import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk


'''
    Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:


    1 -nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx"

    2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,  
    medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.

    3- Validar todos los datos.

    4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones.

    5- Una vez ingresada la cantidad se debe pedir por cada excursión 
    el importe y el tipo de excursión (caminata  o vehículo). 
    informar cual es el precio más caro, el más barato y el promedio

    6- Informar cual es el tipo de excursión (caminata  o vehículo) más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)
'''


class App(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()


        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Tour 🚂", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

   
    def btn_mostrar_on_click(self):

        #entrada nombre
        nombre_str = prompt(title="ingrese su nombre", prompt="nombre")
        #validacion entrada
        while not nombre_str or not nombre_str.isdigit():
            nombre_str = prompt(title="ingrese su nombre", prompt="nombre")

        #entrada edad
        edad_str = prompt(title="ingrese su edad", prompt="edad")
        #validacion
        while not edad_str.isdigit() or edad_str == None:
            edad_str = prompt(title="ingrese su edad")

        #entrada genero
        genero_str = prompt(title="ingrese su genero", prompt="genero: 'Masculino' - 'Femenino' - 'Otro' ")
        #validacion
        while type(genero_str) is not str or genero_str == None:
            genero_str = prompt(title= "ingrese su genero")

        #entrada altura
        altura = prompt(title="ingrese su altura", prompt="altura")
        #validacion
        while type(altura) is not str or genero_str == None:
            altura = prompt(title="ingrese su altura", prompt="altura")

        #parseo de altura
        altura = float(altura)

        #proceso
        if altura <= 140:
            msg_altura = "bajo"
        elif altura <= 170:
            msg_altura = "medio"
        elif altura <= 190:
            msg_altura = "alto"
        else:
            msg_altura = "muy alto"

        mensaje = "usted es {0} tiene {1} de edad y su género es {2} y segun su altura es {3}".format(nombre_str, edad_str, genero_str,msg_altura)


        #salida
        alert(title="salida", message=mensaje)





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()