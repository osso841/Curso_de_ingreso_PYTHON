'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        # declaracion
        candidato_mas_votado = None
        candidato_menos_votado = None
        edad_candidato_menos_votado = None
        votos_maximos = None
        votos_minimos = None
        primer_candidato = True
        edad_total_acumulada = 0
        cantidad_de_candidatos = 0
        cantidad_de_votos = 0

        continuar_carga = True

        #carga de candidatos
        while continuar_carga:
            #nombre
            nombre = prompt(title="ingrese dato", prompt="nombre")

            #edad y validacion
            while True:
                edad = prompt(title="ingrese dato", prompt="edad")
                edad = int(edad)
                if edad >= 25:
                    break
                alert(title="dato incorrecto", message="edad fuera del rango de valores")

            #cantidad de votos y validacion
            while True:
                cantidad_votos_candidato = prompt(title="ingrese datos", prompt="cantidad de votos")
                cantidad_votos_candidato = int(cantidad_votos_candidato)
                if cantidad_votos_candidato >= 0:
                    break
                alert(title="error en carga", message="se ingreso un numero negativo")

            #candidato mas votado
            if primer_candidato or cantidad_votos_candidato > votos_maximos:
                votos_maximos = cantidad_votos_candidato
                candidato_mas_votado = nombre
            #candidato menos votado
            if primer_candidato or cantidad_votos_candidato < votos_minimos:
                votos_minimos = cantidad_votos_candidato
                candidato_menos_votado = nombre
                edad_candidato_menos_votado = edad
                primer_candidato = False 

            #acumulador total de votos
            cantidad_de_votos += cantidad_votos_candidato

            #acumulador edades
            edad_total_acumulada += edad

            #acumulador Cantidad Candidatos
            cantidad_de_candidatos += 1

            #condicion de carga
            continuar_carga = question(title="carga candidatos ", message="desea continuar cargando?")

        #calculo promedio edad candidatos
        promedio = edad_total_acumulada / cantidad_de_candidatos
    
        # mensajes de salida
        mensaje_mas_menos_votado = "candidato mas votado: {0}.\ncandidato menos votado: {1}.\nedad candidato menos votado: {2}\n".format(candidato_mas_votado, candidato_menos_votado, edad_candidato_menos_votado) 

        #mensaje promedio edades y total de votos emitidos
        mensaje_promedio_y_total_votos = "edad promedio de los candidatos: {0}.\ntotal de votos emitidos: {1}.".format(promedio, cantidad_de_votos)

        print(mensaje_mas_menos_votado + mensaje_promedio_y_total_votos)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
