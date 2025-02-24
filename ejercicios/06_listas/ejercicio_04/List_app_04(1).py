import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'MÍNIMO' se analizará el vector lista_datos a efectos de determinar cuál es el número 
más chico allí contenido el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="MÍNIMO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        numero_minimo = None
        bandera_primer_numero = True

        for elemento in self.lista_datos:
            if bandera_primer_numero or elemento < numero_minimo:
                numero_minimo = elemento
                bandera_primer_numero = False
        
        alert(title="MINIMO", message="el menor numero de la lista es: {0}".format(numero_minimo))
            
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()