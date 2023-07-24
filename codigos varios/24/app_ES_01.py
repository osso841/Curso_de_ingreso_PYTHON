import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: oscar
apellido: alonso
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        # palabra = prompt("mostrar", "ingrese una palabra")

        # for letra in palabra:
        #     if letra == "a":
        #         print("la palabra tiene a")
        # #ord() devuelve el codigo ascii de cada uno de los simbolos

        # listas
        # numero = 3

        # mi_lista = ['H', 'o', 'l', 'a', 'a', 5, 234,'%', True, numero, 3.4, 'aaa']  #lista declarada 
        # lista_vacia = []                          #lista vacia

        # for elemento in mi_lista:
        #     if str(elemento).isalpha():           #isalpha() devuelve true si el elemento de la lista es [a-z] o [A-Z]
        #             lista_vacia.append(elemento)          #el append es para adicionar a una nueva lista?

        # print(lista_vacia)

        # print(mi_lista[3])

        # palabra = "pepe"
        # print(palabra[4])

        # for elemento in mi_lista:
        #     if elemento == 'a':
        #         mi_lista.remove('a')              #sacar / eliminar elementos de una lista
                

        # # print(mi_lista)

        # numero = 3

        # mi_lista = ['H', 'o', 'l', 'a', 'a', 5, 234,'%', True, numero, 3.4, 'aaa']
        # lista_vacia = []

        # for i in range(0, len(mi_lista), 1):        # len(mi_lista) metodo que devuelve un entero que representa la cantidad de elemento de una lista a partir de 1
        #     print(mi_lista[i])
        pass        











if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
