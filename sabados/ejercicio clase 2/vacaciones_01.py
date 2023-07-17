import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk


'''
    Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:


    1 -nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx" ----

    2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,  
    medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura. ----

    3- Validar todos los datos. ---

    4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones. ----

    5- Una vez ingresada la cantidad se debe pedir por cada excursión 
    el importe y el tipo de excursión (caminata  o vehículo). 
    informar cual es el precio más caro, el más barato y el promedio ----

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
        #declaracion de variables
        contador_excursiones = 0
        nombre_excursion_cara = ""
        precio_excursion_cara = None
        nombre_excursion_barata = ""
        precio_excursion_barata = None

        #acumulador cual es la excursion mas elegida
        acumulador_caminata = 0
        acumulador_vehiculo = 0


        #entrada datos con validacion
        nombre = prompt(title="introduzca nombre", prompt="nombre")
        while not nombre or nombre.isdigit():
            nombre = prompt(title="introduzca el nombre nuevamente", prompt="nombre")

        edad = prompt(title="introduzca Edad", prompt="edad")
        while not edad.isdigit():
            edad = prompt(title="introduzca Edad", prompt="edad")

        genero = prompt(title="introduzca su genero", prompt="femenino - masculino - otros")
        while not(genero == "femenino" or genero == "masculino" or  genero == "otros"):
            genero = prompt(title="introduzca su genero", prompt="femenino - masculino - otros")

        altura = prompt(title="introduzca su altura", prompt="altura (cm)")
        while not altura.isdigit():
            altura = prompt(title="introduzca su altura", prompt="altura (cm)")

        # En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones.
        cantidad_excursiones = int(prompt(title="cantidad de excursiones. maximo 12", prompt="introduzca cantidad excursiones"))
        while not (0 < cantidad_excursiones < 12):
            cantidad_excursiones = int(prompt(title="cantidad de excursiones. maximo 12", prompt="Introduzca cantidad excursiones"))

        #parseo de variables
        altura = int(altura)

        #determinacion de altura
        if altura < 140:
            msg_altura = "bajo"
        elif altura < 170:
            msg_altura = "mediano"
        elif altura < 190:
            msg_altura = "alto"
        else:
            msg_altura = "muy alto"


        #carga tipo y costo de excurciones
        while contador_excursiones < cantidad_excursiones:
            #entrada actividad con validacion
            nombre_actividad = prompt(title="actividad recreativa", prompt="actividad (caminata(c) - vehiculo(v))")
            while not (nombre_actividad == "c" or nombre_actividad == "v"):
                nombre_actividad = prompt(title="actividad recreativa", prompt="actividad (caminata - vehiculo)")

            #entrada costo con validacion
            costo_excursion = int(prompt(title="costo excursion", prompt="precio"))
            while costo_excursion < 0:
                costo_excursion = prompt(title="costo excursion", prompt="precio")

            #correcion nombre completo
            match nombre_actividad:
                case "c":
                    nombre_actividad = "caminata"
                    acumulador_caminata += 1
                case "v":
                    nombre_actividad = "vehiculo"
                    acumulador_vehiculo += 1

            #inicializacion variables
            if not (precio_excursion_cara and precio_excursion_barata):
                nombre_excursion_cara = nombre_actividad
                nombre_excursion_barata = nombre_actividad
                precio_excursion_cara = costo_excursion 
                precio_excursion_barata = costo_excursion 
            elif precio_excursion_cara < costo_excursion: #actualizamos precio excursion cara y su nombre
                precio_excursion_cara = costo_excursion
                nombre_excursion_cara = nombre_actividad
            elif precio_excursion_barata > costo_excursion: #actualizamos precio excursion barata y su nombre
                precio_excursion_barata = costo_excursion
                nombre_excursion_barata = nombre_actividad

            #verificacion de pasos
            print("ingreso excursion cara: {0}, costo {1}. \ningreso excrusion barata {2}, costo {3}.".format(nombre_excursion_cara, precio_excursion_cara, nombre_excursion_barata, precio_excursion_barata))

            #incremento
            contador_excursiones += 1

        # actividad que se realizo una mayor cantidad de veces
        if acumulador_vehiculo > acumulador_caminata:
            msg_excursion = "vehiculo"
        elif acumulador_vehiculo < acumulador_caminata:
            msg_excursion = "caminata"
        else:
            msg_excursion = "misma cantidad de actividades"

        #precio promedio de excursiones mas barata y mas cara
        costo_promedio_excursiones = (precio_excursion_barata + precio_excursion_cara) / 2

        #mensaje de salida
        mensaje = "usted es {0} tiene {1} de edad, su género es {2} y usted es {3}. \nusted realizara {4} excursiones. \nla excursion mas cara es {5} y cuesta ${6}\nla excursion mas barata es {7} y cuesta ${8}\nel precio promedio es: {9}\nexcursion mas requerida: {10}".format(nombre, edad, genero, msg_altura, cantidad_excursiones, nombre_excursion_cara, precio_excursion_cara, nombre_excursion_barata, precio_excursion_barata, costo_promedio_excursiones, msg_excursion)

        #salida
        alert(title="datos", message=mensaje)




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()