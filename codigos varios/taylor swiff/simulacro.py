import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

# Se nos ha solicitado desarrollar una aplicación para llevar REGISTRO de las entradas vendidas en el Estadio River Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de comprar cada entrada:

# Nombre del comprador
# Edad (no menor a 16)
# Género (Masculino, Femenino, Otro)
# Tipo de entrada (General, Campo delantero, Platea)
# Medio de pago (Crédito, Efectivo, Débito) 
# Precio de la entrada (Se debe calcular)

# Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, el medio de pago y su precio correspondiente.

# Lista de precios: 
# General: $16000
# Campo: $25000
# Platea: $30000

# Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 


# Al finalizar la venta de entradas, los organizadores quieren obtener la siguiente información:

# Cantidad total de dinero recaudado por las ventas de entradas.
# Cantidad de entradas vendidas para cada tipo.
# Promedio de edad de las personas que compraron ubicación en Platea.
# Nombre de la persona de mayor edad que compró una entrada de platea.
# Porcentaje de entradas vendidas de tipo "general"
# Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
# Tipo de entradas más vendidas




class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        # Lista de nombres
        self.nombres = [
        "Juan", "María", "Luis", "Ana", "Carlos", "Jose", "Pedro", "Sofía", "Miguel", "Valentina",
        "Andrés", "Lucía", "Fernando", "Gabriela", "Diego", "Martina", "Jorge", "Camila", "Ricardo", "Isabella",
        "José", "Paula", "Manuel", "Alejandra", "Santiago", "Daniela", "Gustavo", "Carolina", "Emilio", "Antonella",
        "Pablo", "Valeria", "Eduardo", "Florencia", "Alberto", "Agustina", "Raul", "Rocio", "Javier", "Marina",
        "Sebastian", "Catalina", "Rafael", "Carmen", "Rodrigo", "Elena", "Oscar", "Pilar", "Hugo", "Juana",
        "Guillermo", "Natalia", "Francisco", "Constanza", "Hector", "Adriana", "Victor", "Anita", "Lorenzo", "Estela",
        "Enrique", "Diana", "Fabian", "Patricia", "Felipe", "Claudia", "Camilo", "Teresa", "Samuel", "Rosa",
        "Joaquin", "Monica", "Lucas", "Ines", "Omar", "Gloria", "Mariano", "Silvia", "Nicolas", "Alicia",
        "Federico", "Olga", "Arturo", "Amparo", "Julio", "Elsa", "Alfredo", "Beatriz", "Elias", "Rita",
        "Benjamin", "Margarita", "Agustin", "Dolores", "Dario", "Lourdes", "Gerardo", "Manuela", "Feliciano", "Marta"
        ]

        # Lista de edades (mayores o iguales a 16)
        self.edades = [
        25, 33, 20, 29, 50, 40, 22, 28, 35, 18,
        26, 21, 30, 32, 19, 27, 24, 38, 31, 23,
        29, 17, 28, 34, 20, 25, 22, 33, 40, 16,
        19, 37, 24, 28, 31, 21, 33, 18, 29, 26,
        35, 20, 23, 39, 30, 27, 22, 36, 28, 32,
        31, 19, 24, 20, 25, 33, 40, 27, 21, 39,
        29, 22, 36, 30, 19, 25, 21, 38, 34, 17,
        32, 18, 23, 27, 22, 40, 36, 29, 20, 33,
        31, 35, 24, 19, 28, 30, 26, 37, 33, 21,
        25, 29, 16, 38, 40, 50, 27, 30, 32, 24
        ]

        # Lista de géneros (Masculino, Femenino u Otro)
        self.generos = [
        "Masculino", "Femenino", "Masculino", "Femenino", "Otro", "Masculino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino"
        ]

        # Lista de tipo de entrada (General, Campo delantero, Platea)
        self.tipo_entrada = [
        "General", "Campo delantero", "Platea", "General", "Platea", "General", "General", "Platea", "Campo delantero", "General",
        "Campo delantero", "Platea", "General", "General", "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "General", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero"
        ]

        # Lista de medio de pago (Credito, Debito, Efectivo)
        self.medio_pago = [
        "Credito", "Debito", "Efectivo", "Credito", "Efectivo", "Debito", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito"
        ]

        # Lista de precios correspondientes a cada tipo de entrada
        self.precios = [16000, 30000, 25000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000
    ]
        
    def btn_mostrar_on_click(self):
        acumulador_total_dinero_recaudado = 0  #salida consola
        contador_general = 0 #salida consola
        contador_campo = 0 #salida consola
        contador_platea = 0 #salida consola
        acumulador_edad_platea = 0
        #declaracion de variables
        costo_entrada = 0
        bandera_edad_primera_persona = True
        nombre_persona_mayor_edad = None
        persona_mayor_platea = None
        contador_entradas_vendidas_general = 0
        
        nombre = prompt(title="registro", prompt="ingrese nombre del comprador:")

        edad = prompt(title="registro", prompt="ingrese edad del comprador:")
        while int(edad) < 16:
            edad = prompt(title="registro", prompt="ingrese nuevamente edad del comprador:")
        edad = int(edad)

        genero = prompt(title="registro", prompt="ingrese genero del comprador:")
        while not(genero == "Masculino" or genero == "Femenino" or genero == "Otro"):
            genero = prompt(title="registro", prompt="ingrese nuevamente genero del comprador:")

        tipo_de_entrada = prompt(title="registro", prompt="ingrese tipo de entrada:")
        while not(tipo_de_entrada == "General" or tipo_de_entrada == "Campo delantero" or tipo_de_entrada == "Platea"):
            tipo_de_entrada = prompt(title="registro", prompt="ingrese nuevamente tipo de entrada:")

        medio_de_pago = prompt(title="registro", prompt="ingrese el medio de pago:")
        while not(medio_de_pago == "Credito" or medio_de_pago == "Efectivo" or medio_de_pago == "Debito"):
            medio_de_pago = prompt(title="registro", prompt="ingrese nuevamente el medio de pago:")

        match tipo_de_entrada:
            case "Campo delantero":
                costo_entrada = 25000
            case "General":
                costo_entrada = 16000
            case _:
                costo_entrada = 30000

        self.nombres.append(nombre)
        self.edades.append(edad)
        self.generos.append(genero)
        self.tipo_entrada.append(tipo_de_entrada)
        self.medio_pago.append(medio_de_pago)
        self.precios.append(costo_entrada)

        for i in range(0, len(self.nombres), 1):
            if self.medio_pago[i] == "Credito":
                acumulador_total_dinero_recaudado = self.precios[i] * 0.8
            elif self.medio_pago[i] == "Debito":
                acumulador_total_dinero_recaudado = self.precios[i] * 0.85
            else:
                acumulador_total_dinero_recaudado = self.precios[i]

        for tipo in self.tipo_entrada:
            if tipo == "Campo delantero":
                contador_campo += 1
            elif tipo == "General":
                contador_general += 1
            else:
                contador_platea += 1

        for i in range(0, len(self.nombres), 1):
            if self.tipo_entrada == "Platea":
                acumulador_edad_platea += self.edades[i]
                if bandera_edad_primera_persona or self.edades[i] > persona_mayor_platea:
                    persona_mayor_platea = self.edades[i]
                    nombre_persona_mayor_edad = self.nombres[i]
                    bandera_edad_primera_persona = False


        promedio_edad_platea = acumulador_edad_platea / contador_platea # salida consola TODO division por cero

        porcentaje_entradas_vendidas_general = contador_general / len(self.tipo_entrada) * 100 #salida consola TODO division por cero


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
