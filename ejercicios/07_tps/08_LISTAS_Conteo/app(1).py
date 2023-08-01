import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos ---
    b. La suma acumulada de los positivos ---
    c. Cantidad de números positivos ingresados ---
    d. Cantidad de números negativos ingresados ---
    e. Cantidad de ceros ---
    f. El minimo de los negativos ---
    g. El maximo de los positivos ---
    h. El promedio de los negativos ---

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):

        while True:
            #entrada de datos
            numero = prompt(title="entrada", prompt="ingrese un numero:")
            #escape por boton cancel
            if numero is None:
                break
            numero = int(numero)
            self.lista.append(numero)

 


        
    def btn_mostrar_estadisticas_on_click(self):
        #declaracion de variables
        suma_negativos = 0
        suma_positivos = 0
        contador_numeros_negativos = 0
        contador_numeros_positivos = 0
        contador_ceros = 0
        bandera_primer_negativo = True
        bandera_primer_positivo = True
        minimo_negativo = "no hay elementos negativos"
        maximo_positivo = "no hay elementos positivos"

        for elemento in self.lista:
            if elemento < 0:
                suma_negativos += elemento #salida alert
                contador_numeros_negativos += 1 #salida alert

                if bandera_primer_negativo or elemento < minimo_negativo:
                    minimo_negativo = elemento #salida alert
                    bandera_primer_negativo = False
            elif elemento > 0:
                suma_positivos += elemento #salida alert
                contador_numeros_positivos += 1 #salida alert

                if bandera_primer_positivo or elemento > maximo_positivo:
                    maximo_positivo = elemento #salida alert
                    bandera_primer_positivo = False
            else:
                contador_ceros += 1

        if contador_numeros_negativos != 0:
            promedio_negativos = suma_negativos / contador_numeros_negativos
        else:
            promedio_negativos = "no hay numero negativos"

        mensaje = "La suma acumulada de los negativos: {0}\nLa suma acumulada de los positivos: {1}\nCantidad de números positivos ingresados: {2}\nCantidad de números negativos ingresados: {3}\nCantidad de ceros: {4}\nEl minimo de los negativos: {5}\nEl maximo de los positivos: {6}\nEl promedio de los negativos: {7}".format(suma_negativos, suma_positivos, contador_numeros_positivos, contador_numeros_negativos, contador_ceros, minimo_negativo, maximo_positivo, promedio_negativos)
        
        alert(title="salida", message=mensaje)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
