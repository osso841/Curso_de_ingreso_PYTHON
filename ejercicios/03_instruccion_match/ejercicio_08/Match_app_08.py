import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el botón 
‘Informar’ indicar mediante alert si en el destino hace frío o calor la mayoría 
de las estaciones del año.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        #entrada
        destinos = self.combobox_destino.get()

        #proceso
        match destinos:
            case "Bariloche" | "Ushuaia":
                mensaje = "hace frio la mayoria de las estaciones del año"
            case "Mar del plata" | "Cataratas":
                mensaje = "hace calor la mayoria de las estaciones del año"
        
        #salida
        alert(title=destinos, message=mensaje)
    

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()