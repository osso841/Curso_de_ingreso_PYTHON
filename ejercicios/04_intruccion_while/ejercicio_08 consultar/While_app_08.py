import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        #declaracion de variables
        acumulador_suma_positivos = 0
        acumulador_producto_negativos = 1
        
        while True:
            numero = prompt(title="numero", prompt="ingrese numero")
            if numero is None or numero == 0 :
                break

            numero  = int(numero)
            if numero > 0:
                acumulador_suma_positivos += numero
            else:
                acumulador_producto_negativos *= numero
        
        self.txt_producto.delete(first_index=0, last_index="end")
        self.txt_producto.insert(index=0, string=acumulador_producto_negativos)
        self.txt_suma_acumulada.delete(first_index=0, last_index="end")
        self.txt_suma_acumulada.insert(index=0, string=acumulador_suma_positivos)
        


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
