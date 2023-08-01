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
        numeros_negativos = []
        numeros_positivos = []
        contador_ceros = 0 #mostrar alert
        suma_negativos = 0 #mostrar alert
        suma_positivos = 0 #mostrar alert

        primer_numero_minimo_negativos = True
        primer_numero_maximo_positivos = True
        maximo_positivos = None
        minimo_negativos = None

        promedio_numero_negativos = 0

        while True:
            #entrada
            numero = prompt(title="entrada", prompt="ingrese un numero")

            #escape por boton cancel
            if numero is None:
                break

            #parseo de valores de entrada
            numero = int(numero)

            #a. llenado de listas para realizar la suma de los negativos y positivos respectivamente
            if numero < 0:
                numeros_negativos.append(numero)
            elif numero > 0:
                numeros_positivos.append(numero)
            else:
                contador_ceros +=1

            # f. El minimo de los negativos
            if primer_numero_minimo_negativos or numero < minimo_negativos:
                if numero < 0:
                    minimo_negativos = numero # mostrar alert
                    primer_numero_minimo_negativos = False
            if primer_numero_maximo_positivos or numero > maximo_positivos:
                if numero > 0:
                    maximo_positivos = numero # mostrar alert
                    primer_numero_maximo_positivos = False

        ############ FIN BUCLE ###############

        # a. La suma acumulada de los negativos ---
        for elemento in numeros_negativos:
            suma_negativos += elemento

        # b. La suma acumulada de los positivos ---
        for elemento in numeros_positivos:
            suma_positivos += elemento

        # c. Cantidad de números positivos ingresados ---
        cantidad_numeros_positivos = len(numeros_positivos) #mostrar alert
        # d. Cantidad de números negativos ingresados ---
        cantidad_numeros_negativos = len(numeros_negativos) #mostrar alert

        # h. El promedio de los negativos ---
        if cantidad_numeros_negativos != 0:
            promedio_numero_negativos = suma_negativos / cantidad_numeros_negativos
        

        #mensaje lista salida
        mensaje_resultados = "suma acumulada negativos: {}\nsuma acumulada positivos: {}\ncantidad de numeros positivos: {}\ncantidad de numeros negativos: {}\ncantidad de ceros: {}\nel minimo de los negativos: {}\nel maximo de los positivos: {}\nel promedio de los negativos: {}".format(suma_negativos, suma_positivos, cantidad_numeros_positivos, cantidad_numeros_negativos, contador_ceros, minimo_negativos, maximo_positivos, promedio_numero_negativos)

        alert(title="output", message=mensaje_resultados)

    def btn_mostrar_estadisticas_on_click(self):
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
