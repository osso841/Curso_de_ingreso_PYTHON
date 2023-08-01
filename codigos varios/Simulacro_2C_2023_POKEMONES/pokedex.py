# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones. TODO
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Fuego)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)
    3
    
    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    6
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario
    , si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos. ---
    #! 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Psiquico.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        # self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        # self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        # self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_4 = customtkinter.CTkButton(master=self, text="Informe 4", command=self.btn_mostrar_informe_4)
        self.btn_informe_4.grid(row=7, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_5 = customtkinter.CTkButton(master=self, text="Informe 5", command=self.btn_mostrar_informe_5)
        self.btn_informe_5.grid(row=8, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_6 = customtkinter.CTkButton(master=self, text="Informe 6", command=self.btn_mostrar_informe_6)
        self.btn_informe_6.grid(row=9, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_7 = customtkinter.CTkButton(master=self, text="Informe 7", command=self.btn_mostrar_informe_7)
        self.btn_informe_7.grid(row=10, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_8 = customtkinter.CTkButton(master=self, text="Informe 8", command=self.btn_mostrar_informe_8)
        self.btn_informe_8.grid(row=11, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_9 = customtkinter.CTkButton(master=self, text="Informe 9", command=self.btn_mostrar_informe_9)
        self.btn_informe_9.grid(row=12, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_10 = customtkinter.CTkButton(master=self, text="Informe 10", command=self.btn_mostrar_informe_10)
        self.btn_informe_10.grid(row=13, pady=11, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones =["Squirtle", "Psyduck", "Cloyster", "Charmander", "Drowzee", "Gyarados", "Squirtle", "Mewtwo", "Charizard", "Magikarp"]
        self.lista_poder_pokemones = [90, 150, 150, 95, 70, 90, 150, 80, 50, 103]
        self.lista_tipo_pokemones = ["agua", "psíquico", "agua", "fuego", "psíquico", "agua", "agua", "psíquico", "fuego", "agua"]

    def btn_mostrar_todos_on_click(self): #Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal)
        for i in range(0, len(self.lista_nombre_pokemones), 1):
            nombre = self.lista_nombre_pokemones[i]
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            print(f"posicion {i}. pokemon: {nombre:15}. tipo: {tipo:10}. poder: {poder:5}.")
    

    def btn_mostrar_informe_1(self): #Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
        contador_pokemons_fuego_10_extra = 0

        for i in range(0, len(self.lista_tipo_pokemones), 1):
            if self.lista_tipo_pokemones[i] == "fuego" and self.lista_poder_pokemones[i] * 1.1 > 100:
                contador_pokemons_fuego_10_extra += 1
        print(f"Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos: {contador_pokemons_fuego_10_extra}\n")


    def btn_mostrar_informe_2(self): #Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
        contador_pokemon_psiquico_poder_rango = 0

        for i in range(0, len(self.lista_nombre_pokemones), 1):
            if self.lista_tipo_pokemones[i] == "psíquico" and self.lista_poder_pokemones[i] * 0.85 >= 100 and self.lista_poder_pokemones[i] * 0.85 <=150:
                contador_pokemon_psiquico_poder_rango += 1
        print(f"Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos: {contador_pokemon_psiquico_poder_rango}\n")
    

    def btn_mostrar_informe_3(self): #Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
        bandera_primera_entrada = True
        poder_alto_pokemon_fuego = None
        nombre_poder_alto_pokemon_fuego = None

        for i in range(0, len(self.lista_nombre_pokemones), 1):
            if bandera_primera_entrada or self.lista_poder_pokemones[i] > poder_alto_pokemon_fuego and self.lista_tipo_pokemones[i] == "agua":
                poder_alto_pokemon_fuego = self.lista_poder_pokemones[i]
                nombre_poder_alto_pokemon_fuego = self.lista_nombre_pokemones[i]
                bandera_primera_entrada = False
        print(f"Nombre y Poder del pokemon de tipo Agua con el poder mas alto:\nnombre: {nombre_poder_alto_pokemon_fuego}. Poder: {poder_alto_pokemon_fuego}")


    def btn_mostrar_informe_4(self): # Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
        bandera_primera_entrada = True
        poder_bajo_pokemon_psiquico = None
        nombre_poder_bajo_pokemon_psiquico = None

        for i in range(0, len(self.lista_nombre_pokemones), 1):
            if bandera_primera_entrada or self.lista_poder_pokemones[i] < poder_bajo_pokemon_psiquico and self.lista_tipo_pokemones[i] == "psíquico":
                poder_bajo_pokemon_psiquico = self.lista_poder_pokemones[i]
                nombre_poder_bajo_pokemon_psiquico = self.lista_nombre_pokemones[i]
                bandera_primera_entrada = False
        print(f"# Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.\nnombre: {nombre_poder_bajo_pokemon_psiquico}. Poder: {poder_bajo_pokemon_psiquico}")


    def btn_mostrar_informe_5(self): #Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
        contador_pokemones_agua_nivel_alto = 0

        for i in range(0, len(self.lista_nombre_pokemones), 1):
            if self.lista_tipo_pokemones[i] == "agua" and self.lista_poder_pokemones[i] >= 100:
                contador_pokemones_agua_nivel_alto += 1
        if len(self.lista_tipo_pokemones) != 0:
            porcentaje_pokemones_agua_nivel_alto = contador_pokemones_agua_nivel_alto / len(self.lista_tipo_pokemones) * 100

        print(f"Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados): %{porcentaje_pokemones_agua_nivel_alto}")


    def btn_mostrar_informe_6(self): #Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
        contador_pokemones_psiquico_menor_150 = 0

        for i in range(0, len(self.lista_nombre_pokemones), 1):
            if self.lista_tipo_pokemones[i] == "psíquico" and self.lista_poder_pokemones[i] <= 150:
                contador_pokemones_psiquico_menor_150 += 1

        if len(self.lista_tipo_pokemones) != 0:
            porcentaje_pokemon_psiquico_menor_150 = contador_pokemones_psiquico_menor_150 / len(self.lista_tipo_pokemones) * 100

        print(f"Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados): %{porcentaje_pokemon_psiquico_menor_150}")

    def btn_mostrar_informe_7(self): #tipo de los pokemones del tipo que mas pokemones posea.
        contador_pokemones_fuego = 0
        contador_pokemones_psiquico = 0
        contador_pokemones_agua = 0
        mensaje_tipo_pokemon_mas_cargado = ""

        for tipo in self.lista_tipo_pokemones:
            match tipo:
                case "fuego":
                    contador_pokemones_fuego += 1
                case "psíquico":
                    contador_pokemones_psiquico += 1
                case "agua":
                    contador_pokemones_agua += 1
                
        if contador_pokemones_fuego > contador_pokemones_psiquico and contador_pokemones_fuego > contador_pokemones_agua:
            mensaje_tipo_pokemon_mas_cargado = "fuego"
        elif contador_pokemones_agua > contador_pokemones_fuego and contador_pokemones_agua > contador_pokemones_psiquico:
            mensaje_tipo_pokemon_mas_cargado = "agua"
        elif contador_pokemones_psiquico > contador_pokemones_agua and contador_pokemones_psiquico > contador_pokemones_fuego:
            mensaje_tipo_pokemon_mas_cargado = "psíquico"
        else:
            mensaje_tipo_pokemon_mas_cargado = "no hay un tipo de pokemon predominante"

        print(f"tipo de los pokemones del tipo que mas pokemones posea: {mensaje_tipo_pokemon_mas_cargado}")


    def btn_mostrar_informe_8(self): # tipo de los pokemones del tipo que menos pokemones posea. 
        contador_pokemones_fuego = 0
        contador_pokemones_psiquico = 0
        contador_pokemones_agua = 0
        mensaje_tipo_pokemon_menos_cargado = ""

        for tipo in self.lista_tipo_pokemones:
            match tipo:
                case "fuego":
                    contador_pokemones_fuego += 1
                case "psíquico":
                    contador_pokemones_psiquico += 1
                case "agua":
                    contador_pokemones_agua += 1

        if contador_pokemones_fuego < contador_pokemones_psiquico and contador_pokemones_fuego < contador_pokemones_agua:
            mensaje_tipo_pokemon_menos_cargado = "fuego"
        elif contador_pokemones_agua < contador_pokemones_fuego and contador_pokemones_agua < contador_pokemones_psiquico:
            mensaje_tipo_pokemon_menos_cargado = "agua"
        elif contador_pokemones_psiquico < contador_pokemones_agua and contador_pokemones_psiquico < contador_pokemones_fuego:
            mensaje_tipo_pokemon_menos_cargado = "psíquico"
        else:
            mensaje_tipo_pokemon_menos_cargado = "no hay un tipo de pokemon predominante"

        print(f"tipo de los pokemones del tipo que mas pokemones posea: {mensaje_tipo_pokemon_menos_cargado}")
    
    def btn_mostrar_informe_9(self): #Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
        acumulador_poder = 0
        lista_pokemones_encima_promedio = []

        if len(self.lista_poder_pokemones):

            for poder in self.lista_poder_pokemones:
                acumulador_poder += poder

            promedio_poder = acumulador_poder / len(self.lista_poder_pokemones)

            for i in range(0, len(self.lista_tipo_pokemones), 1):
                if self.lista_poder_pokemones[i] > promedio_poder:
                    lista_pokemones_encima_promedio.append(self.lista_nombre_pokemones[i])

            print("lista de pokemones cuyo poder de pelea este por encime del promedio")
            for i in range(0, len(lista_pokemones_encima_promedio), 1):
                pokemon = lista_pokemones_encima_promedio[i]
                print(f"posicion: {i:3} pokemon: {pokemon}")

    def btn_mostrar_informe_10(self): #el promedio de poder de todos los pokemones de tipo Psiquico.
        acumulador_poder_psiquico = 0
        contador_psiquico = 0

        for i in range(0, len(self.lista_poder_pokemones), 1):
            if self.lista_tipo_pokemones[i] == "psíquico":
                acumulador_poder_psiquico += self.lista_poder_pokemones[i]
                contador_psiquico += 1

        if contador_psiquico != 0:
            promedio_poder_psiquico = acumulador_poder_psiquico / contador_psiquico

            print(f"el promedio de poder de todos los pokemones de tipo Psiquico. {promedio_poder_psiquico}")

    def btn_cargar_pokedex_on_click(self):

        nombre_pokemon = prompt(title="carga datos", prompt="ingrese nombre de pokemon encontrado")

        tipo_pokemon = prompt(title="carga datos", prompt="ingrese el tipo de pokemon")
        while not(tipo_pokemon == "agua" or tipo_pokemon == "psiquico" or tipo_pokemon == "fuego"):
            tipo_pokemon = prompt(title="carga datos", prompt="ingrese nuevamente el tipo de pokemon")


        poder_ataque = prompt(title="carga datos", prompt="ingrese el ataque del pokemon")
        while int(poder_ataque) <= 50 or int(poder_ataque) >= 200:
            poder_ataque = prompt(title="carga datos", prompt="ingrese nuevamente el ataque del pokemon")
        poder_ataque = int(poder_ataque)

        self.lista_nombre_pokemones.append(nombre_pokemon)
        self.lista_tipo_pokemones.append(tipo_pokemon)
        self.lista_poder_pokemones.append(poder_ataque)

        
            
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()