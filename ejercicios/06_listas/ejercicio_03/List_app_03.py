import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'MÁXIMO' se analizará el vector lista_datos a efectos de determinar cuál es el número 
más grande allí contenido el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="MÁXIMO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]
        #                   0,1, 2,3,4 ,5, 6 ,7

    def btn_calcular_on_click(self):
        valor_maximo = None
        carga_primer_valor = True
        # i : 0, 1, 2, 3, 4, 5, 6, 7
        for i in range(0, len(self.lista_datos), 1):
            if carga_primer_valor or valor_maximo < self.lista_datos[i]:
                valor_maximo = self.lista_datos[i]
                carga_primer_valor = False

        alert(title="numero maximo", message= valor_maximo)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()