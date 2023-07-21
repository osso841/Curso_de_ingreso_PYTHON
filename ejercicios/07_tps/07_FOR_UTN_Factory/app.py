'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        # declaracion de constantes
        CANTIDAD_DE_POSTULANTES = 2


        #declaracion de variables
        contador_postulante_nb = 0 #a
        primer_postulante_js = True #b
        edad_minima_postulante_js = None #b
        nombre_postulante_js = None #b
        contador_edad_f = 0 #c
        acumulador_f = 0 #c e
        contador_edad_m = 0 #c
        acumulador_m = 0 #c e
        contador_edad_nb = 0 #c
        acumulador_nb = 0 #c e
        acumulador_tecnologia_py = 0 #d
        acumulador_tecnologia_js = 0 #d
        acumulador_tecnologia_net = 0 #d
        tecnologia_con_mas_postulantes = None #d



        #calculo general de postulantes
        for i in range(1, CANTIDAD_DE_POSTULANTES + 1, 1):
            #mensaje prompt
            title_prompt: "dato postulante {0} de {1}".format(i, CANTIDAD_DE_POSTULANTES)

            #entrada nombre 
            nombre_postulante = prompt(title=title_prompt, prompt="ingrese nombre:")

            #entrada edad (mayor de edad) y validacion
            while True:
                edad_postulante = prompt(title=title_prompt, prompt="ingrese edad:")
                edad_postulante = int(edad_postulante)
                # escape
                if edad_postulante >= 18:
                    break
                alert(title="dato invalido", message="dato invalido, ingresar nuevamente")


            #entrada genero (F-M-NB)
            while True:
                genero = prompt(title=title_prompt, prompt="ingrese su genero. femenino(F), Masculino(M), No Binario (NB)")
                match genero:
                    case "F" | "M" | "NB":
                        break



            #entrada tecnologia de desarrollo (PYTHON - JS - ASP.NET)
            while True:
                tecnologia_postulante = prompt(title=title_prompt, prompt="ingrese lenguaje de desarrollo: PHYTON - JS - ASP.NET")
                match tecnologia_postulante:
                    case "PHYTON" | "JS" | "ASP.NET":
                        break
                

            #entrada puesto (Jr - Ssr - Sr)
            while True:
                puesto_postulante = prompt(title=title_prompt, prompt="seleccione su puesto Js - Ssr - Sr")
                match puesto_postulante:
                    case "Js" | "Ssr" | "Sr":
                        break

            # Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
            postulante_nb = genero == "NB" and tecnologia_postulante == "ASP.NET" and edad_postulante >= 25 and edad_postulante <= 40 and puesto_postulante =="Ssr"
            if postulante_nb:
                contador_postulante_nb += 1

            # Nombre del postulante Jr con menor edad.
            if primer_postulante_js or (edad_postulante < edad_minima_postulante_js) and puesto_postulante == "Js":
                edad_minima_postulante_js = edad_postulante
                nombre_postulante_js = nombre_postulante
                primer_postulante_js = False

            # Promedio de edades por género.
            match genero:
                case "F":
                    contador_edad_f += edad_postulante
                    acumulador_f += 1
                case "M":
                    contador_edad_m += edad_postulante
                    acumulador_m += 1   
                case "NB":
                    contador_edad_nb += edad_postulante
                    acumulador_nb += 1

            # Tecnologia con mas postulantes.
            match tecnologia_postulante:
                case "PHYTON":
                    acumulador_tecnologia_py += 1
                case "JS":
                    acumulador_tecnologia_js += 1
                case "ASP.NET":
                    acumulador_tecnologia_net += 1
        #fin de bucle


        #calculo de promedio de edades por genero
        promedio_edades_f = contador_edad_f / acumulador_f
        promedio_edades_m = contador_edad_m / acumulador_m
        promedio_edades_nb = contador_edad_nb / acumulador_nb

        # calculo tecnologia con mas postulantes
        if (acumulador_tecnologia_py > acumulador_tecnologia_js):
            if(acumulador_tecnologia_py > acumulador_tecnologia_net):
                tecnologia_con_mas_postulantes = "PYTHON"
            else:
                tecnologia_con_mas_postulantes = "ASP.NET"
        elif acumulador_tecnologia_js > acumulador_tecnologia_net:
            tecnologia_con_mas_postulantes = "JS"

        # Porcentaje de postulantes de cada genero.

        promedio_postulantes_f = acumulador_f / CANTIDAD_DE_POSTULANTES * 100
        promedio_postulantes_m = acumulador_m  / CANTIDAD_DE_POSTULANTES * 100
        promedio_postulantes_nb = acumulador_nb / CANTIDAD_DE_POSTULANTES * 100



        
        
       



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
