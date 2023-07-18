import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        #declaracion de variable de escape
        continuar = True
        #declaracion variables
        suma_negativos = 0
        suma_positivos = 0
        cantidad_negativos = 0
        cantidad_positivos = 0
        cantidad_ceros = 0

        while continuar:
            #entrada de numeros
            numero = prompt(title="numero", prompt="ingrese un numero")
            numero = int(numero)

            #proceso verificacion de numeros
            if numero > 0:
                suma_positivos += numero
                cantidad_positivos += 1
            elif numero < 0:
                suma_negativos += numero
                cantidad_negativos += 1
            else:
                cantidad_ceros += 1

            #consulta continuar cargando numeros usuario
            continuar = question(title="cargar numeros", message="ingresar otro numero?")

        #calculo diferencia entre la "CANTIDAD" de numeros positivos y negativos
        diferencia_numeros_positivos_negativos = suma_positivos + suma_negativos

        #mensaje salida
        mensaje_ingreso_numeros = "el usuario ingreso:\n{0} numeros positivos\n{1} numeros negativos\n{2} ceros".format(cantidad_positivos, cantidad_negativos, cantidad_ceros)
        mensaje_calculos = "\nsuma numeros negativos {0}\nsuma numeros positivos {1}\ndiferencia: {2}".format(suma_negativos, suma_positivos, diferencia_numeros_positivos_negativos)

        #salida
        alert(title="datos", message=mensaje_ingreso_numeros + mensaje_calculos)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
