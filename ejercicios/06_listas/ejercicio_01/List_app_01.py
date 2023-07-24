import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre y apellido: oscar alonso
Al presionar el botón  'Mostrar', se deberán mostrar los números 
almacenados en el vector lista_datos utilizando Dialog Alert para informar cada elemento.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]


    def btn_mostrar_on_click(self):
        # for elemento in self.lista_datos:
        #     alert(title="salida", message=elemento)
        
        numero = prompt("ingreso", "ingrese un numero")

        bandera_coma = False
        primer_digito = True

        if numero.isdigit():
            numero = int(numero)
        else:
            for digito in numero:
                if digito < '0' or digito > '9' or :
                    "fuera del rango del numero"
                    pass
                else:
                    if digito == '-' and primer_digito == True:
                        primer_digito = False
                    else:
                        if digito == '-' and primer_digito == False:
                            #no es un numero
                            pass
                        if digito == '.' and bandera_coma == False:
                            bandera_coma = True
                        else:
                            if digito == '.' and bandera_coma == True:
                                #no es un numero
                                pass



                primer_digito = False
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()