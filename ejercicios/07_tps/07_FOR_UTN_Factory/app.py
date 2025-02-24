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
        acumulador_edad_f = 0 #c
        contador_edades_f = 0 #c e
        acumulador_edad_m = 0 #c
        contador_edades_m = 0 #c e
        acumulador_edad_nb = 0 #c
        contador_edades_nb = 0 #c e
        contador_tecnologia_py = 0 #d
        contador_tecnologia_js = 0 #d
        contador_tecnologia_net = 0 #d
        tecnologia_con_mas_postulantes = None #d



        #calculo general de postulantes
        for i in range(1, CANTIDAD_DE_POSTULANTES + 1, 1):

            #entrada nombre 
            nombre_postulante = prompt(title="dato postulante", prompt="ingrese nombre:")

            #entrada edad (mayor de edad) y validacion
            edad_postulante = prompt(title="dato postulante", prompt="ingrese edad:")
            while int(edad_postulante) < 18:
                edad_postulante = prompt(title="dato postulante", prompt="Dato invalido, ingresar nuevamente la edad:")
            edad_postulante = int(edad_postulante)


            #entrada genero (F-M-NB)
            genero = prompt(title="dato postulante", prompt="ingrese su genero. femenino(F), Masculino(M), No Binario (NB)")
            while not(genero == "F" or genero == "M" or genero == "NB"):
                genero = prompt(title="dato postulante", prompt="ingrese nuevamente su genero. femenino(F), Masculino(M), No Binario (NB)")


            #entrada tecnologia de desarrollo (PYTHON - JS - ASP.NET)
            tecnologia_postulante = prompt(title="dato postulante", prompt="ingrese lenguaje de desarrollo: PYTHON - JS - ASP.NET")
            while not(tecnologia_postulante == "PYTHON" or tecnologia_postulante == "JS" or tecnologia_postulante == "ASP.NET"):
                tecnologia_postulante = prompt(title="dato postulante", prompt="ingrese nuevamente el lenguaje de desarrollo: PYTHON - JS - ASP.NET")
  
                
            #entrada puesto (Jr - Ssr - Sr)
            puesto_postulante = prompt(title="puesto del postulante", prompt="seleccione su puesto Jr - Ssr - Sr")
            while not(puesto_postulante == "Jr" or puesto_postulante == "Ssr" or puesto_postulante == "Sr"):
                puesto_postulante = prompt(title="puesto del postulante", prompt="seleccione nuevamente su puesto Jr - Ssr - Sr")



            # Nombre del postulante Jr con menor edad.
            if primer_postulante_js or edad_postulante < edad_minima_postulante_js and puesto_postulante == "Jr":
                edad_minima_postulante_js = edad_postulante
                nombre_postulante_js = nombre_postulante
                primer_postulante_js = False

            # Promedio de edades por género.
            match genero:
                case "F":
                    acumulador_edad_f += edad_postulante
                    contador_edades_f += 1
                case "M":
                    acumulador_edad_m += edad_postulante
                    contador_edades_m += 1   
                case "NB":
                    acumulador_edad_nb += edad_postulante
                    contador_edades_nb += 1
                    # Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
                    if (tecnologia_postulante == "ASP.NET" or tecnologia_postulante == "JS") and (edad_postulante >= 25 and edad_postulante <= 40) and puesto_postulante =="Ssr":
                        contador_postulante_nb += 1

            # Tecnologia con mas postulantes.
            match tecnologia_postulante:
                case "PYTHON":
                    contador_tecnologia_py += 1
                case "JS":
                    contador_tecnologia_js += 1
                case "ASP.NET":
                    contador_tecnologia_net += 1

        #fin de bucle


        #calculo de promedio de edades por genero
        if contador_edades_f != 0:
            promedio_edades_f = acumulador_edad_f / contador_edades_f
        else:
            promedio_edades_f = "no hay postulantes femeninos"

        if contador_edades_m != 0:
            promedio_edades_m = acumulador_edad_m / contador_edades_m
        else:
            promedio_edades_m = "no hay postulantes masculinos"

        if contador_edades_nb != 0:
            promedio_edades_nb = acumulador_edad_nb / contador_edades_nb
        else:
            promedio_edades_nb = "no hay postulantes no binarios"

        # calculo tecnologia con mas postulantes
        if contador_tecnologia_js > contador_tecnologia_net and contador_tecnologia_js > contador_tecnologia_py:
            tecnologia_con_mas_postulantes = "JS"
        elif contador_tecnologia_py > contador_tecnologia_js and contador_tecnologia_py > contador_tecnologia_net:
            tecnologia_con_mas_postulantes = "PYTHON"
        elif contador_tecnologia_net > contador_tecnologia_js and contador_tecnologia_net > contador_tecnologia_py:
            tecnologia_con_mas_postulantes = "ASP.NET"
        else:
            tecnologia_con_mas_postulantes = "no hay una tecnologia con mas postulantes"

        # Porcentaje de postulantes de cada genero.

        porcentaje_postulantes_f = contador_edades_f / CANTIDAD_DE_POSTULANTES * 100
        porcentaje_postulantes_m = contador_edades_m  / CANTIDAD_DE_POSTULANTES * 100
        porcentaje_postulantes_nb = contador_edades_nb / CANTIDAD_DE_POSTULANTES * 100

        print("PUNTO A: Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.{0}".format(contador_postulante_nb))
        print("PUNTO B: Nombre del postulante Jr con menor edad. {0}".format(nombre_postulante_js))
        print("PUNTO C: Promedio de edades por género: \n Femenino: {0} postulantes\nMasculino: {1} postulantes\nNo Binario: {2} postulantes".format(promedio_edades_f, promedio_edades_m, promedio_edades_nb))
        print("PUNTO D: Tecnologia con mas postulantes (solo hay una). {0}".format(tecnologia_con_mas_postulantes))
        print("PUNTO E: Porcentaje de postulantes de cada genero.\nFemenino: %{0} postulantes\nMasculino: %{1} postulantes\nNo Binario %{2} postulante.".format(porcentaje_postulantes_f, porcentaje_postulantes_m, porcentaje_postulantes_nb))


        
        
       





        lista = [3, 4, 7, 8, 9]

        for elemento in lista:
            # elemento te devuelve la variable dentro de la lista
            pass


        for i in range(0, len(lista), 1):
            # i es la posicion de cada elemento
            pass








if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()