import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (V)Poste Quebracho Fino de 2.2 mts
    (F)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        #entrada
        largo = self.txt_largo.get()
        ancho = self.txt_ancho.get()

        #parseo de variables
        largo_float = float(largo)
        ancho_float = float(ancho)


        # A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
        #calculo de perimetro
        perimetro_total = (largo_float + ancho_float)*2

        #calculo area total en m2
        area_total = largo_float * ancho_float

        print("El area total sera de: {0} m2, y el perimetro total sera de {1} m.".format(area_total, perimetro_total)) 

        # B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).

        poste_quebracho_grueso = 4
        poste_quebracho_grueso_largo = largo_float // 250 
        poste_quebracho_grueso_ancho = ancho_float // 250 
        
        cantidad_postes_quebracho_grueso = poste_quebracho_grueso + (poste_quebracho_grueso_largo + poste_quebracho_grueso_ancho) * 2

        print ("la cantidad de postes de quebracho a utilizar es: {0}.".format(cantidad_postes_quebracho_grueso))

        # C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en ese lugar no se encuentra el poste grueso).

        #calculo de espacio disponible
        largo_disponible = largo_float - (poste_quebracho_grueso_largo - poste_quebracho_grueso / 2) * 2.4
        ancho_disponible = ancho_float - (poste_quebracho_grueso_ancho - poste_quebracho_grueso / 2) * 2.4

        #cantidad de postes a utilizar
        poste_quebracho_fino_largo = largo_disponible // 12
        poste_quebracho_fino_ancho = ancho_disponible // 12

        cantidad_postes_quebracho_fino = (poste_quebracho_fino_largo + poste_quebracho_fino_ancho) * 2

        print("la cantidad de postes de quebracho fino utilizado es {0}".format(cantidad_postes_quebracho_fino))

        # D. Informar la cantidad de varillas (van cada 2 mts lineales).

        largo_disponible_total = largo_disponible - poste_quebracho_fino_largo * 2.2
        ancho_disponible_total = ancho_disponible - poste_quebracho_fino_ancho * 2.2

        cantidad_varillas_largo = largo_disponible_total // 2
        cantidad_varillas_ancho = ancho_disponible_total // 2

        cantidad_varillas_total = (cantidad_varillas_ancho + cantidad_varillas_largo) * 2

        print("la cantidad de varillas a utilizar son: {0}".format(cantidad_varillas_total))

        # E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos

        Cantidad_alambre = perimetro_total * 7

        print("la cantidad de alambre a utilizar es {0}m".format(Cantidad_alambre))


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
