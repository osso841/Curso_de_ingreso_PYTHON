import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

# DIVISIBLE POR 1 Y POR SI MISMO
    def btn_mostrar_on_click(self):
        #declaracion de constantes y variables
        DIVISIBLE_DOS_VECES = 2 #para que sea primo
        numero_ingresado = prompt(title="numero", prompt="INGRESE NUMERO: ")
        numero_ingresado = int(numero_ingresado)
        contador_numeros_divisibles = 0 #contador de la cantidad de veces que es divisible el numero

        for i in range(1, numero_ingresado + 1, 1):

            if numero_ingresado % i == 0:
                contador_numeros_divisibles += 1
            
        if contador_numeros_divisibles == DIVISIBLE_DOS_VECES:
            mensaje = "es primo"
        else:
            mensaje = "no es primo"

        alert(title="resultado", message=mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()