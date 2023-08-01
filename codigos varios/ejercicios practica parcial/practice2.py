import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
    Ejercicio de parcial 2: 
    Centro de cómputos
    Ingresar el nombre de los 5 candidatos a presidente de Berlinberlin, la edad de cada uno y la cantidad de votos que sacó en las elecciones.
    Informar: 
    a) el candidato con más votos
    b) el candidato con menos votos
    c) el promedio de edades de los candidatos
    d) total de votos emitidos
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self): 
        #declaracion de constante
        CANTIDAD_CANDIDATOS = 2

        #declaracion
        acumulador_votos_totales = 0
        acumulador_edad_candidato = 0
        primer_candidato = True

        for i in range(0, CANTIDAD_CANDIDATOS, 1):
            #entrada de valores
            nombre = prompt(title="datos candidatos", prompt="ingrese nombre")

            edad = prompt(title="datos candidatos", prompt="ingrese edad")
            edad = int(edad)

            cantidad_votos = prompt(title= "datos candidatos", prompt="ingrese cantidad de votos")
            cantidad_votos = int(cantidad_votos)

            #calculo candidato mas votado
            if primer_candidato or cantidad_votos > mayor_cantidad_votos:
                mayor_cantidad_votos = cantidad_votos
                candidato_mas_votado = nombre #salida print

            #calculo candidato menos votado
            if primer_candidato or cantidad_votos < menor_cantidad_votos:
                menor_cantidad_votos = cantidad_votos
                candidato_menos_votado = nombre #salida print
                primer_candidato = False

            #acumulador edad candidatos
            acumulador_edad_candidato += edad

            #acumulador votos
            acumulador_votos_totales += cantidad_votos #salida print

        #promedio de edades candidatos
        promedio_edad_candidato = acumulador_edad_candidato / CANTIDAD_CANDIDATOS #salida print

        mensaje = "DATOS DE LAS ELECCIONES:\nel candidato con mas votos {}\nel candidato con menos votos: {}\nel promedio de edad de los candidatos: {}\ntotal de votos emitidos: {}".format(candidato_mas_votado, candidato_menos_votado, promedio_edad_candidato, acumulador_votos_totales)

        alert(title="datos elecciones", message=mensaje)




            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()