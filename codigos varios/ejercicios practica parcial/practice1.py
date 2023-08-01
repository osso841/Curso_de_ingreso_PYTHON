import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
    Ejercicio de parcial 1:

    Se pide cargar la ficha médica para 11 jugadores de fútbol.
    Se solicita Nombre, Edad, Peso(ej: 60.5kg) y Altura(ej: 1.65mt).
    A) Nombre del jugador más joven.
    B) El peso del jugador más alto.
    C) Promedio de altura del equipo.
    D) Promedio de peso del equipo.
    E) Cantidad de jugadores que superen el promedio de altura y de peso del equipo.

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
        #declaracion de constantes
        CANTIDAD_DE_JUGADORES = 2

        #declaracion de lista
        peso_jugadores = []
        altura_jugadores = []


        #declaraciones jugador mas joven
        primer_jugador_joven = True
        nombre_jugador_joven = ""

        #declaraciones del jugador mas alto
        primer_jugador_alto = True
        Peso_jugador_alto = 0

        #acumulador altura jugadores
        altura_acumulada_jugadores = 0

        # acumulador peso jugadores
        peso_acumulado_jugadores = 0

        #jugadores con altura por encima de la media
        jugadores_mas_altos = 0

        #jugadores con peso por encima de la media
        jugadores_mas_peso = 0

        for jugador in range(0, CANTIDAD_DE_JUGADORES, 1):
            #entrada 
            nombre = prompt(title="datos ficha medica", prompt="ingrese nombre jugador:" ) #salida print

            edad = prompt(title="datos ficha medica", prompt="ingrese edad jugador:")
            edad = int(edad)

            peso = prompt(title="datos ficha medica", prompt="ingrese peso jugador (kg): ")
            peso = float(peso)


            altura = prompt(title="datos ficha medica", prompt="ingrese altura jugador (mtr): ")
            altura = float(altura)


            # A) Nombre del jugador más joven.
            if primer_jugador_joven or edad < edad_jugador_joven:
                edad_jugador_joven = edad
                nombre_jugador_joven = nombre #salida print
                primer_jugador_joven = False

            # B) El peso del jugador más alto.
            if primer_jugador_alto or altura > jugador_mas_alto:
                jugador_mas_alto = altura
                Peso_jugador_alto = peso #salida print
                primer_jugador_alto = False


            # C) Promedio de altura del equipo.
            altura_jugadores.append(altura)

            # D) Promedio de peso del equipo.
            peso_jugadores.append(peso)

        #calculo peso y altura promedio
        for i in altura_jugadores:
            altura_acumulada_jugadores += i

        for i in peso_jugadores:
            peso_acumulado_jugadores += i

        promedio_altura = altura_acumulada_jugadores / CANTIDAD_DE_JUGADORES #salida print
        promedio_peso = peso_acumulado_jugadores / CANTIDAD_DE_JUGADORES #salida print

        for i in altura_jugadores:
            if i > promedio_altura:
                jugadores_mas_altos += 1 #salida print

        for i in peso_jugadores:
            if i > promedio_peso:
                jugadores_mas_peso += 1 #salida print

        print("DATOS GENERALES EQUIPO:\nnombre jugador mas joven: {}\npeso del jugador mas alto: {:.2f}kg\npromedio de altura del equipo: {:.2f}mts\npromedio de peso del equipo: {:.2f}kg\njugadores que superen el promedio de peso del equipo: {}\njugadores que superen el promedio de altura del equipo: {}".format(nombre_jugador_joven, Peso_jugador_alto, promedio_altura, promedio_peso, jugadores_mas_peso, jugadores_mas_altos))


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()