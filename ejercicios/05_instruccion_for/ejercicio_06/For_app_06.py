import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #declaracion
        contador = 0
        #entrada
        numero = prompt(title = "entrada", prompt="ingrese un valor")
        #parseo de variable
        numero = int(numero)
        #calculo de numeros pares
        for i in range(0, numero, 1):
            if i % 2 == 0:
                contador += 1
        #mensaje y salida
        mensaje = "hay {0} numeros pares en el rango de valores desde 0 hasta {1}".format(contador, numero)
        alert(title="resultado", message=mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()