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


    def btn_mostrar_on_click(self):
        #declaracion constante numeros primos
        COINCIDENCIA_NUMERO_PRIMO = 2

        #entrada de variables
        numero = prompt(title="numero primo", prompt="ingrese un valor")

        #parseo
        numero = int(numero)
        contador = 0

        #calculo de numeros primos
        for i in range(1, numero + 1, 1):
            if numero % i == 0:
                contador += 1

        #mesaje de salida prom
        if contador == COINCIDENCIA_NUMERO_PRIMO:
            mensaje = "es primo"
        else:
            mensaje = "no es primo"

        alert(title="numeros primos", message=mensaje)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()