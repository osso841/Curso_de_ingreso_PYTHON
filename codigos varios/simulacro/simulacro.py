import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
La Cueva De Fausto:
Se pide un programa que agrega los ingresos y egresos de dinero en dos divisas, dólares y pesos

A)  Al presionar el botón 'Agregar' se debera cargar el dinero (Positivo si es un ingreso, negativo si es un egreso),
el cual podra ser ingresado en ARS o en USD.

    El tipo de cambio indicado mediante una lista desplegable.

* Flotantes Distintos de 0

Los ingresos/egresos se guardaran en la "self.lista_transacciones" en ARS.

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar las transacciones en USD, en ARS y su posicion en la lista (por terminal)

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar 
    0- Cantidad de dinero (en ARS) y posicion (indice) de la transaccion de mayor valor---
    1- Cantidad de dinero (en ARS) y posicion (indice) de la transaccion de menor valor---
    2- Promedio de dinero ingresado (mostrarlo en ARS) ---
    3- Promedio de dinero egresado (mostrarlo en USD) ---
    4- Informar las transacciones que superan el promedio total (en ARS)---
    5- Informar las transacciones que NO superan el promedio total (en USD) ---
    6- Informar la cantidad de Transacciones que superan el promedio total
    7- Informar la cantidad de transacciones que NO superan el promedio total
    8- Indicar Si hubo mas ingresos o egresos
    9- Indicar Si hubo ganancia o perdida


1 ARS son 0,0018484 USD
1 USD son 541 ARS
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("SIMULACRO EXAMEN INGRESO")

        self.txt_dinero = customtkinter.CTkEntry(master=self, placeholder_text="DINERO")
        self.txt_dinero.grid(row=1, padx=20, pady=20)

        self.combobox_divisa = customtkinter.CTkComboBox(master=self, values=["ARS", "USD"])
        self.combobox_divisa.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_transacciones = []
        

    def btn_agregar_on_click(self):
        # declaracion de constantes
        PESO_A_DOLAR : 541

        entrada_salida_divisa = self.txt_dinero.get()
        entrada_salida_divisa = float(entrada_salida_divisa)

        tipo_divisa = self.combobox_divisa.get()

        if entrada_salida_divisa != 0:
            if tipo_divisa == "ARS":
                self.lista_transacciones.append(entrada_salida_divisa)
                alert(title="validacion", message="carga exitosa")
            else:
                entrada_salida_divisa *= PESO_A_DOLAR
                self.lista_transacciones.append(entrada_salida_divisa)
                alert(title="validacion", message="carga exitosa")
        else:
            alert(title="validacion", message="entrada fuera de rango. ingrese otro valor")


    def btn_mostrar_on_click(self):
        # B) Al presionar el boton mostrar se deberan listar las transacciones en USD, en ARS y su posicion en la lista (por terminal)
        for i in range(0, len(self.lista_transacciones), 1):
            if self.lista_transacciones[i] < 0:
                print("pos {0}. salida de dinero: {1}".format(i+1, self.lista_transacciones[i]))
            else:
                print("pos {0}. entrada de dinero: {1}".format(i+1, self.lista_transacciones[i]))


    def btn_informar_on_click(self):
        # Tener en cuenta que pueden no haber ingresos o egresos
        # declaracion de constantes y variables
        PESO_A_DOLAR = 0.0018484
        bandera_transaccion_mayor_menor_valor = True
        transaccion_mayor_valor = None
        indice_transaccion_mayor_valor = None
        transaccion_menor_valor = None
        indice_transaccion_menor_valor = None
        total_dinero_ingresado = 0
        contador_dinero_ingresado = 0
        total_dinero_egresado_USD = 0
        contador_dinero_egresado = 0
        promedio_total_transacciones = 0
        msg_elemento_encima_promedio = ""
        msg_elemento_debajo_promedio_USD = ""
        contador_transacciones_superen_promedio = 0
        contador_transacciones_no_superen_promedio = 0 
        ganancia_perdida = 0

        for i in range(0, len(self.lista_transacciones),1):
            if bandera_transaccion_mayor_menor_valor or self.lista_transacciones[i] > transaccion_mayor_valor: # REVISAR el ingreso no puede ser negativo
                transaccion_mayor_valor = self.lista_transacciones[i] # 0, mostrar salida
                indice_transaccion_mayor_valor = i # 0, mostrar salida
                
            if bandera_transaccion_mayor_menor_valor or self.lista_transacciones[i] < transaccion_menor_valor: # REVISAR el egreso no puede ser positivo
                transaccion_menor_valor = self.lista_transacciones[i] # 1, mostrar salida
                indice_transaccion_menor_valor = i # 1, mostrar salida
                bandera_transaccion_mayor_menor_valor = False

            if self.lista_transacciones[i] > 0:
                total_dinero_ingresado += self.lista_transacciones[i]
                contador_dinero_ingresado += 1
            else:
                total_dinero_egresado_USD += self.lista_transacciones[i] * PESO_A_DOLAR
                contador_dinero_egresado += 1

            ganancia_perdida += self.lista_transacciones[i]

        if contador_dinero_ingresado != 0:
            promedio_dinero_ingresado = total_dinero_ingresado / contador_dinero_ingresado # 2, mostrar salida
        else:
            promedio_dinero_ingresado = "no se han realizado transacciones de ingreso"

        if contador_dinero_egresado != 0:
            promedio_dinero_egresado_USD = total_dinero_egresado_USD / contador_dinero_egresado # 3, mostrar salida
        else:
            promedio_dinero_egresado_USD = "no se han realizado transacciones de egreso"

        if (contador_dinero_egresado + contador_dinero_ingresado) != 0:
            promedio_total_transacciones = (total_dinero_egresado_USD / PESO_A_DOLAR + total_dinero_ingresado) / (contador_dinero_egresado + contador_dinero_ingresado)

            for elemento in self.lista_transacciones:
                if  elemento > promedio_total_transacciones:
                    msg_elemento_encima_promedio += "    {0} ARS supera el promedio de transacciones\n".format(elemento) # 4, mostrar salida
                    contador_transacciones_superen_promedio += 1 # 6, mostrar salida

                if elemento < promedio_total_transacciones:
                    elemento *= PESO_A_DOLAR
                    msg_elemento_debajo_promedio_USD += "    {0} USD. NO supera el promedio de transacciones\n".format(elemento) # 5, mostrar salida
                    contador_transacciones_no_superen_promedio += 1 # 7, mostrar salida

        else:
            promedio_total_transacciones = "no se han realizado transacciones de ingreso ni de egreso"
            msg_elemento_encima_promedio = "no se han realizado transacciones de ingreso ni de egreso"
            msg_elemento_debajo_promedio_USD = "no se han realizado transacciones de ingreso ni de egreso"

        if contador_dinero_ingresado > contador_dinero_egresado:
            msg_mayor_transaccion = "hubo mas ingresos que egresos en esta cuenta" # 8 mostrar salida
        elif contador_dinero_egresado < contador_dinero_egresado:
            msg_mayor_transaccion = "hubo mas egresos que ingresos en esta cuenta" # 8 mostrar salida
        else:
            msg_mayor_transaccion = "hubo la misma cantidad de ingresos que de egresos en esta cuenta" # 8 mostrar salida

        if ganancia_perdida > 0:
            msg_ganancia_perdida = f"TU GANANCIA ES DE ${ganancia_perdida}" # 9 mostrar salida
        elif ganancia_perdida < 0:
            msg_ganancia_perdida = f"TU PERDIDA ES DE ${ganancia_perdida}" # 9 mostrar salida
        else:
            msg_ganancia_perdida = "TU CUENTA ESTA EN 0" # 9 mostrar salida
        
        print(f"transaccion mayor valor: {transaccion_mayor_valor}. indice transaccion mayor valor: {indice_transaccion_mayor_valor}\ntransaccion_menor_valor: {transaccion_menor_valor}. indice transaccion menor valor: {indice_transaccion_menor_valor}\npromedio dinero ingresado: {promedio_dinero_ingresado}\npromedio dinero egresado en USD: {promedio_dinero_egresado_USD}\nentradas que supera el promedio de transacciones:\n{msg_elemento_encima_promedio}\nentradas que no superan el promedio de transacciones:\n{msg_elemento_debajo_promedio_USD}\ncantidad transacciones que superan el promedio: {contador_transacciones_superen_promedio}\ncantidad transacciones que no superan el promedio: {contador_transacciones_no_superen_promedio}\ntransaccion mas realizada en esta cuenta: {msg_mayor_transaccion}\nEstado de cuenta: {msg_ganancia_perdida}\n\n")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
