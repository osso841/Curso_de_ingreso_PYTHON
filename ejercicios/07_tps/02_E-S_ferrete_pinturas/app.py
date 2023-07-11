import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	Para el departamento de Pinturas:
	A.	Al ingresar una temperatura en Fahrenheit debemos mostrar la temperatura en Centígrados con un mensaje concatenado 
        (0 °F − 32) × 5/9 = -17,78 °C

    B.	Al ingresar una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        (0 °C × 9/5) + 32 = 32 °F

    
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Temperatura °C")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_temperatura_c = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_c.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Temperatura °F")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_temperatura_f = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_f.grid(row=1, column=1)
       
        self.btn_convertir_c_f = customtkinter.CTkButton(master=self, text="Convertir °C a °F", command=self.btn_convertir_c_f_on_click)
        self.btn_convertir_c_f.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_convertir_f_c = customtkinter.CTkButton(master=self, text="Convertir °F a °C", command=self.btn_convertir_f_c_on_click)
        self.btn_convertir_f_c.grid(row=4, pady=10, columnspan=2, sticky="nsew")
    
    def btn_convertir_c_f_on_click(self):
        # B. Al ingresar una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        # (0 °C × 9/5) + 32 = 32 °F
        # entrada
        temperatura_c = self.txt_temperatura_c.get()

        # parseo de valor de entrada
        temperatura_c_float = float(temperatura_c)

        # calculo de temperatura en grados fahrenheit
        temperatura_f = (temperatura_c_float * 9 / 5) + 32

        alert(title="conversion c a f", message="({0}°C x 9/5) + 32 = {1}°F".format(temperatura_c_float, temperatura_f))


    def btn_convertir_f_c_on_click(self):
        # A.	Al ingresar una temperatura en Fahrenheit debemos mostrar la temperatura en Centígrados con un mensaje concatenado 
        # (0 °F − 32) × 5/9 = -17,78 °C

        # entrada
        temperatura_f = self.txt_temperatura_f.get()

        # parseo de variables
        temperatura_f_float = float(temperatura_f)
        
        # calculo de temperatura en grados celcius
        temperatura_c = (temperatura_f_float - 32) * 5 / 9

        alert(title="conversion f a c" ,message="({0}°F - 32) x 5/9 = {1:.2f} °C".format(temperatura_f_float, temperatura_c))
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()