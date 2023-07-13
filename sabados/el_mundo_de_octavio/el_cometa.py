import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

'''
La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

COMETA: 

AB = Diámetro mayor (se debe calcular)
DC = diámetro menor (se ingresa por prompt)
BD y BC = lados menores (se ingresa por prompt)
AD y AC = lados mayores (se ingresa por prompt)

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia.
La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="El Cometa 🪁", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.label_diametro_menor = customtkinter.CTkLabel(master=self, text="Diametro Menor DC")
        self.label_diametro_menor.grid(row=1, column=0, padx=20, pady=10)

        self.txt_diametro_menor= customtkinter.CTkEntry(master=self)
        self.txt_diametro_menor.grid(row=1, column=1)
        
        self.label_lados_menores = customtkinter.CTkLabel(master=self, text="Lados Menores BD y BC")
        self.label_lados_menores.grid(row=2, column=0, padx=20, pady=10)

        self.txt_lados_menores = customtkinter.CTkEntry(master=self)
        self.txt_lados_menores.grid(row=2, column=1)

        self.label_lados_mayores = customtkinter.CTkLabel(master=self, text="Lados Mayores AD y AC")
        self.label_lados_mayores.grid(row=3, column=0, padx=20, pady=10)

        self.txt_lados_mayores = customtkinter.CTkEntry(master=self)
        self.txt_lados_mayores.grid(row=3, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #adicional cola cometa
        ADICIONAL_COLA_COMETA = 10 
        CANTIDAD_COMETAS = 10

        #Entrada
        diametro_menor = self.txt_diametro_menor.get()
        lados_menores = self.txt_lados_menores.get()
        lados_mayores = self.txt_lados_mayores.get()

        #parseo de variables de entrada
        diametro_menor = int(diametro_menor)
        lados_mayores = int(lados_mayores)
        lados_menores = int(lados_menores)

        #calculo perimetro
        perimetro_cometa = (lados_menores + lados_mayores) * 2

        #calculo de varillas entrecruce superior
        #considerando diametro menor / 2 y lado bd y parte superior de varilla , se obtiene un triangulo rectangulo.

        #Calculo varilla vertical
        varilla_vertical_superior = math.sqrt(pow(diametro_menor / 2, 2) + pow(lados_menores, 2))
        varilla_vertical_inferior = math.sqrt(pow(diametro_menor / 2, 2) + pow(lados_mayores, 2))

        varilla_vertical = varilla_vertical_inferior + varilla_vertical_superior

        #cantidad total de varilla
        cantidad_varillas_cometa_total = perimetro_cometa + varilla_vertical + diametro_menor

        #calculo del area de cometa

        area_cometa_superior = diametro_menor * varilla_vertical_superior / 2
        area_cometa_inferior = diametro_menor * varilla_vertical_inferior / 2

        superficie_cometa = area_cometa_inferior + area_cometa_superior

        # calculo de la cola del cometa
        superficie_cola_cometa =  superficie_cometa * (1 + ADICIONAL_COLA_COMETA / 100)

        # calculo de varillas para 10 cometas
        varilla_total_por_cantidad = cantidad_varillas_cometa_total * CANTIDAD_COMETAS # salida Alert

        # calculo de papel para 10 cometas
        papel_por_cantidad = (superficie_cola_cometa + superficie_cometa) * CANTIDAD_COMETAS # salida Alert

        mensaje = "para la fabricacion de {0:.2f} cometas en masa se debe contar con:\n {1:.2f} cm2 de papel de alta resistencia y\n {2:.2f} cm de varillas de platico".format(CANTIDAD_COMETAS, papel_por_cantidad, varilla_total_por_cantidad)

        #salida
        alert(title="materiales", message=mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()