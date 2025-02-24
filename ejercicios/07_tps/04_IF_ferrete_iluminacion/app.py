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
        # declaraciones constantes
        DESCUENTO_SEIS_UNIDADES = 50
        IMPORTE_FINAL_CON_DESCUENTO_ADICIONAL = 4000
        DESCUENTO_ADICIONAL = 5
        COSTO_LAMPARAS = 800

        # contantes Marcas
        ARGENTINALUZ = "ArgentinaLuz"
        FELIPELAMPARAS = "FelipeLamparas"

        # declaraciones
        descuento = 0
    
        # entrada
        marca = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()
        
        # parseo de variables
        cantidad_int = int(cantidad)

        #cantidad de lamparas para el descuento adicional
        cantidad_lamparas_descuento_adicional = IMPORTE_FINAL_CON_DESCUENTO_ADICIONAL / (1 - DESCUENTO_SEIS_UNIDADES /100) / COSTO_LAMPARAS

        if cantidad_int >= 6:         # descuento Mayorista
            descuento = DESCUENTO_SEIS_UNIDADES
            if cantidad_int >= cantidad_lamparas_descuento_adicional: # calculo descuento adicional por cantidad
                descuento += DESCUENTO_ADICIONAL
        elif marca == FELIPELAMPARAS: # calculo descuentos "FelipeLamparas"
            if cantidad_int == 3:
                descuento = 10
            elif cantidad_int == 4:
                descuento = 25
            elif cantidad_int == 5:
                descuento = 30
        elif marca == ARGENTINALUZ:   # calculo descuentos "ArgentinaLuz"
            if cantidad_int == 3:
                descuento = 15
            elif cantidad_int == 4:
                descuento = 25
            elif cantidad_int == 5:
                descuento = 40
        else:                        # calculo descuentos estandar
            if cantidad_int == 3:
                descuento = 5
            elif cantidad_int == 4:
                descuento = 20
            elif cantidad_int == 5:
                descuento = 30

        costo_total_con_descuento = cantidad_int * COSTO_LAMPARAS * (1 - descuento / 100) #info Dialog alert
        costo_total_sin_descuento = cantidad_int * COSTO_LAMPARAS #info Dialog alert

        # salida
        alert(title="costo total", message=" valor de lampara c/u = ${0} \n cantidad = {1} \n descuento aplicado = %{2}. \n total sin descuento: ${3}. \n total con descuento: ${4:.0f}. \n marca = {5}".format(COSTO_LAMPARAS, cantidad_int, descuento, costo_total_sin_descuento, costo_total_con_descuento, marca))
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()