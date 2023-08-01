import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón Comenzar ingreso, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        #declaracion de constantes
        ENTRADA_DE_NUMEROS = 5
        contador_numeros = 0
        acumulador_suma = 0

        while contador_numeros < ENTRADA_DE_NUMEROS:
            #entrada con validacion
            numero = prompt(title="entrada", prompt="ingrese un numero: ")
            while numero is None or numero.isdigit():
                numero = prompt(title="entrada", prompt="ingrese nuevamente un numero")
            numero = int(numero)

            #acumulador y contador
            acumulador_suma += numero
            contador_numeros += 1

            promedio = acumulador_suma / contador_numeros

            self.txt_suma_acumulada.delete(first_index=0, last_index="end")
            self.txt_suma_acumulada.insert(index=0, string=acumulador_suma)
            self.txt_promedio.delete(first_index=0, last_index="end")
            self.txt_promedio.insert(index=0, string=promedio)

            



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
