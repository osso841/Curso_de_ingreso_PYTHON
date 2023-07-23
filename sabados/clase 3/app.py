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
Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante 
que deberá abandonar la casa más famosa del mundo.

Los participantes en la placa son: Giovanni, Gianni y Facundo. Fausto no fue nominado y Marina no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:
1 Nombre del votante
2 Edad del votante (debe ser mayor a 13)
3 Género del votante (Masculino, Femenino, Otro)
4 El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
5 No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
6 El promedio de edad de las votantes de género Femenino 
7 Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
8 Nombre del votante más joven qué votó a Gianni.
9 Nombre de cada participante y porcentaje de los votos qué recibió.
10 El nombre del participante que debe dejar la casa (El que tiene más votos)

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
        #declaracion de variables
        continuar_Carga = True #5

        acumulador_edad_f = 0 #6
        contador_edad_f = 0 #6

        contador_votantes_edad_giovanni_facundo = 0 #7

        primer_votante_joven_voto_gianni = True #8
        votante_mas_joven_voto_gianni = None #8

        contador_votos_giovanni = 0 #9
        contador_votos_gianni = 0 #9
        contador_votos_facundo = 0 #9

        participante_sale_casa = None #10

        while continuar_Carga:
            #entrada de nombre
            nombre_votante = prompt(title="datos votantes", prompt="ingrese el nombre")

            #entrada de apellido
            while True:
                edad_votante = prompt(title = "datos votantes", prompt="ingrese la edad")
                edad_votante = int(edad_votante)
                if edad_votante >= 13:
                    break
                alert(title="dato incorrecto", message="ingrese una edad correcta")

            #entrada de genero
            while True:
                genero_votante = prompt(title = "datos votantes", prompt="ingrese genero:\n(F) Femenino\n(M) Masculino\n(O) Otros")
                match genero_votante:
                    case "M":
                        genero_votante = "Masculino"
                        break
                    case "F":
                        genero_votante = "Femenino"
                        break
                    case "O":
                        genero_votante = "Otros"
                        break

                alert(title="dato incorrecto", message="ingrese nuevamente")
            
            #carga de voto del votante
            while True:
                voto_negativo = prompt(title="voto negativo", prompt="a quien desea sacar de la casa: Giovanni, Gianni o Facundo")
                match voto_negativo:
                    case "Giovanni":
                        contador_votos_giovanni += 1
                        break
                    case "Gianni":
                        contador_votos_gianni += 1
                        break
                    case "facundo":
                        contador_votos_facundo += 1
                        break
                alert(title="voto incorrecto", message="ingrese nuevamente el nombre de quien desea sacar de la casa mas famosa del mundo")
            
            #promedio de edad de los votantes femeninos
            if genero_votante == "Femenino":
                acumulador_edad_f = edad_votante 
                contador_edad_f += 1

            # Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo
            if genero_votante == "Masculino" and edad_votante >= 25 and edad_votante <= 40 and (voto_negativo =="Giovanni" or voto_negativo == "Facundo"):
                contador_votantes_edad_giovanni_facundo += 1 #mostrar en salida
                
            #votante mas joven que voto a gianni
            if primer_votante_joven_voto_gianni or (voto_negativo == "Gianni" and edad_votante < votante_mas_joven_voto_gianni):
                votante_mas_joven_voto_gianni = nombre_votante #mostrar en salida
                primer_votante_joven_voto_gianni = False

            #solicitud de continuacion de carga
            continuar_Carga = question(title="carga de votantes", message="desea continuar con la carga?")
        #--------------- FIN DE CARGA DE DATOS ------------------

        promedio_edad_f = acumulador_edad_f / edad_votante * 100 #promedio de edad votante femenino mostrar en salida

        # Nombre de cada participante y porcentaje de los votos qué recibió.
        votos_totales = contador_votos_facundo + contador_votos_gianni + contador_votos_giovanni
        #mostrar en salida
        porcentaje_votos_giovanni = contador_votos_giovanni / votos_totales * 100
        porcentaje_votos_gianni = contador_votos_gianni / votos_totales * 100
        porcentaje_votos_facundo = contador_votos_facundo / votos_totales * 100

        #mostrar en salida
        if porcentaje_votos_facundo > porcentaje_votos_gianni:
            if porcentaje_votos_facundo > porcentaje_votos_giovanni:
                participante_sale_casa = "facundo sale de la casa"
            else:
                participante_sale_casa = "giovanni sale de la casa"
        elif porcentaje_votos_gianni > porcentaje_votos_giovanni:
            participante_sale_casa = "gianni sale de la casa"
        else:
            participante_sale_casa = "aun no sale nadie de la casa"
 

        #salida:
        alert(title="datos totales", message="promedio de edad de genero femenino: {0}\ncantidad de votantes masculinos entre 25 y 40 años que votaron a giovanni y facundo: {1}\nnombre del votante mas joven que voto a gianni: {2}\nnombre de cada participante y porcentaje de votos:\n   Facundo: %{3}\n  Gianni: %{4}\n   Giovanni: %{5}\nPARTICIPANTE QUE SALE DE LA CASA: {6}".format(promedio_edad_f, contador_votantes_edad_giovanni_facundo, votante_mas_joven_voto_gianni, porcentaje_votos_facundo, porcentaje_votos_gianni, porcentaje_votos_giovanni, participante_sale_casa))







if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
