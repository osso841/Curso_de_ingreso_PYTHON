import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        # declaracion constantes marcas
        ARGENTINALUZ = "ArgentinaLuz"
        FELIPELAMPARAS = "FelipeLamparas"

        #declaracion constantes
        DESCUENTO_SEIS_UNIDADES = 50
        DESCUENTO_ADICIONAL = 5
        COSTO_LAMPARAS = 800
        IMPORTE_FINAL_DESCUENTO= 4000

        #declaracion
        descuento = 0
        costo_lampara_actualizado = 10000 # precio actualizado

        #entrada
        marca = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()

        #parseo de variables
        cantidad_int = int(cantidad)

        # calculo inflacionario y actualizacion de montos de descuento
        importe_final_descuento_actualizado = costo_lampara_actualizado * IMPORTE_FINAL_DESCUENTO / COSTO_LAMPARAS

        #cantidad bombillas para descuento adicional
        cantidad_lamparas_descuento = importe_final_descuento_actualizado / (1 - DESCUENTO_SEIS_UNIDADES / 100) / costo_lampara_actualizado

        if cantidad_int >= 6:           #descuento por 6 o mas uniadades
            descuento = DESCUENTO_SEIS_UNIDADES
            if cantidad_int >= cantidad_lamparas_descuento: #maximo descuento
                descuento = float(descuento)
                descuento = DESCUENTO_SEIS_UNIDADES * (1 + DESCUENTO_ADICIONAL / 100)
                print(descuento)
        elif cantidad_int == 5: #descuento por 5 unidades
            descuento = 30
            if marca == ARGENTINALUZ:
                descuento = 40
        elif cantidad_int == 4: #descuento por 4 unidades
            descuento = 20         
            if marca == ARGENTINALUZ or marca == FELIPELAMPARAS:
                descuento = 25
        elif cantidad_int == 3:             #descuento por 3 unidades
            descuento = 5
            if marca == ARGENTINALUZ:
                descuento = 15
            elif marca == FELIPELAMPARAS:
                descuento = 10
                

        #valores salida dialog alert
        valor_total_sin_descuento = cantidad_int * costo_lampara_actualizado
        valor_total_con_descuento = cantidad_int * costo_lampara_actualizado * (1 - descuento / 100)

        mensaje = "cantidad de lamparas {0}. \n descuento aplicado: %{1}, \n valor sin descuento: ${2} \n valor con descuento ${3:.0F}. \n marca: {4}".format(cantidad_int, descuento, valor_total_sin_descuento, valor_total_con_descuento, marca)
        
        alert(title="salida", message=mensaje)
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()