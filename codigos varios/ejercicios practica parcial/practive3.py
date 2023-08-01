import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


# Ejercicio de parcial 3: 

# En una carga indefinida de datos (hasta que el usuario quiera) se desea llevar a cabo el registro diario de una granja de minería en Bitcoin y Ethereum.
# Se requieren los siguientes datos:
# Nombre de la criptomoneda (VALIDAR EL INGRESO solo de BTC o ETH).
# Cantidad de BTC o ETH minado ese día - Número positivo.
# Cotización diaria en USD - Número positivo inclusive 0.
# INFORMAR
# A) Nombre y cantidad de la criptomoneda más minada.
# B) Nombre de la criptomoneda que mayor cotización tuvo.
# C) Cantidad total de ingreso bruto en USD de cada criptomoneda.
# D) Sabiendo que el coste de electricidad para:

# BTC es de un 7% y para ETH es un 4% calcular el ingreso total neto en USD.

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        porcentaje_costo_electrico_btc = 7
        porcentaje_costo_electrico_eth = 4
        acumulador_btc = 0
        acumulador_eth = 0
        continuar_carga = True
 

        #cotizacion de las cripto con validacion
        cotizacion_bitcoin = prompt(title= "datos cotizacion", prompt="ingrese cotizacion de bitcoin en USD")
        while float(cotizacion_bitcoin) < 0:
            cotizacion_bitcoin = prompt(title= "datos cotizacion", prompt="ingrese nuevamente la cotizacion de bitcoin USD")

        cotizacion_ethereum = prompt(title= "datos cotizacion", prompt="ingrese cotizacion de ethereum en USD")
        while float(cotizacion_ethereum) < 0:
            cotizacion_bitcoin = prompt(title= "datos cotizacion", prompt="ingrese nuevamente la cotizacion de ethereum USD")

        while continuar_carga:

            #entrada nombre cripto con validacion
            nombre_cripto = prompt(title="datos graja", prompt="ingrese el nombre de la cripto: BITCOIN (BTC), ETHEREUM (ETH)")
            while not(nombre_cripto == "BTC" or nombre_cripto == "ETH"):
                nombre_cripto = prompt(title="datos graja", prompt="ingrese nuevamente el nombre de la cripto: BITCOIN (BTC), ETHEREUM (ETH)")

            #entrada cantidad minado con validacion
            cantidad_minado_diario = prompt(title="datos granja", prompt="ingrese la cantidad minada")
            while float(cantidad_minado_diario) < 0:
                cantidad_minado_diario = prompt(title="datos granja", prompt="ingrese nuevamente la cantidad minada:")
            cantidad_minado_diario = float(cantidad_minado_diario)

            continuar_carga = question(title="continuar", message="desea continuar con la carga?")

            #acumulador cripto mas minado
            if nombre_cripto == "BTC":
                acumulador_btc += cantidad_minado_diario
            else:
                acumulador_eth += cantidad_minado_diario

        #cripto mas minada
        if acumulador_btc > acumulador_eth:
            cripto_mas_minada = "Bitcoin"
        elif acumulador_btc < acumulador_eth:
            cripto_mas_minada = "Ethereum"
        else:
            cripto_mas_minada = "misma cantidad"
            
        #nombre cripto mayor cotizacion
        total_USD_bitcoin = acumulador_btc * cotizacion_bitcoin
        total_USD_ethereum = acumulador_eth * cotizacion_ethereum

        if cotizacion_bitcoin > cotizacion_ethereum:
            cripto_mas_cotizada = cotizacion_bitcoin
        else:
            cripto_mas_cotizada = cotizacion_ethereum

        total_USD_bitcoin_neto = total_USD_bitcoin * (1 - porcentaje_costo_electrico_btc / 100)
        total_USD_ethereum_neto = total_USD_ethereum * (1 - porcentaje_costo_electrico_eth / 100)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()