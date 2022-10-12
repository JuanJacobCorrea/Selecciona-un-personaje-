import os

#Ejercicio que pretende ser un menú con algo de navegabilidad, como siempre escucho sus comentarios y/o consejo sobre buenas practicas, legibilidad etc...

PERSONAJES = 1
SALIR = 2

def Personajes():
        
    MAGO = 1
    GUERRERO = 2
    SENTAURO = 3
    GOLEM = 4
    GRIFO = 5
    NINFA = 6
    VAMPIRO = 7
    VOLBER = 8 

    continuar = True
    while continuar:
        os.system("clear")
        print(f"""
            PERSONAJES:

        {MAGO}) MAGO
        {GUERRERO}) Guerrero
        {SENTAURO}) Sentauro
        {GOLEM}) Golem
        {NINFA}) Ninfa
        {VAMPIRO}) Vampiro
        {VOLBER}) Volver
        """) 

        opc = input("Escoja su pesonaje: ")

        if opc == MAGO:
            print(""" 
                MAGO
            Fuerza + 5
            velozidad + 15
            Inteligencia + 10
            """)
            input("Oprima cualquier tecla para continuar")

        elif opc == GUERRERO:
            print(""" 
                GUERRERO
            Fuerza + 15
            velozidad + 10
            Inteligencia + 5
            """)
            input("Oprima cualquier tecla para continuar")

        elif opc == SENTAURO:
            print(""" 
                SENTAURO
            Fuerza + 5
            velozidad + 20
            Inteligencia + 5
            """)
            input("Oprima cualquier tecla para continuar")

        elif opc == GOLEM:
            print(""" 
                GOLEM
            Fuerza + 20
            velozidad + 5
            Inteligencia + 5
            """)
            input("Oprima cualquier tecla para continuar")

        elif opc == NINFA:
            print(""" 
                NINFA
            Fuerza + 5
            velozidad + 5
            Inteligencia + 20
            """)
            input("Oprima cualquier tecla para continuar")

        elif opc == VAMPIRO:
            print(""" 
                VAMPIRO
            Fuerza + 10
            velozidad + 10
            Inteligencia + 10
            """)
            input("Oprima cualquier tecla para continuar")

        elif opc == VOLBER:
            continuar = False

        else:
            print("!Opcion invalida¡")
            input("Oprima cualquier tecla para continuar")
       
def main():
    continuar = True
    while continuar:
        os.system("clear")
        print(f"""
        ==========================    
        |         D & D          |
        ==========================

        {PERSONAJES}) Personajes
        {SALIR}) Salir
        """)
        opc = int(input("Elija una opcion: "))

        if opc == PERSONAJES:
            Personajes()
        
        elif opc == SALIR:
            continuar = False
        
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()