import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt). 
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
        # declaracion de variables
        suma_numeros = 0
        contador = 0

        while True:
            #entrada de numero
            numero = prompt(title="entrada", prompt="ingrese numero")

            #escape por boton cancel
            if numero is None:
                break

            #verificar si el numero que ingresa es un valor numerico aceptado
            if not numero.isdigit():
                alert(title="error", message="no se ha ingresado un numero, vuelva a intentarlo")
                continue

            #parseo de variable
            numero = int(numero)

            #suma de numeros ingresados
            suma_numeros += numero

            #contador para el promedio
            contador += 1

        
        if contador != 0:
            #calculo de promedio
            promedio = suma_numeros / contador

            #salida (solo si se cumple la condicion)
            self.txt_suma_acumulada.delete(first_index=0, last_index="end")
            self.txt_suma_acumulada.insert(index=0, string=suma_numeros)
            self.txt_promedio.delete(first_index=0, last_index="end")
            self.txt_promedio.insert(index=0, string=promedio)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
