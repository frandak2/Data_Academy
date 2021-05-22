import os
import math

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def rangos_cambiantes(superior, inferior, comparacion):
    mensajeExito = f' {inferior} < {comparacion} < {superior}'
    mensajeFalla = f'{comparacion} esta fuera de rango o los limites estan invertidos'
    return mensajeExito if comparacion > inferior and comparacion < superior else mensajeFalla


def main():
    continuar = True
    while continuar:
        print("rangos cambiantes")
        superior = float(input("Ingrese el limite superior: "))
        inferior = float(input("Ingrese el limite inferior: "))
        comparacion = float(input("Ingrese el numero de comparacion: "))

        print(rangos_cambiantes(superior, inferior, comparacion))

        pregunta = input('Desea probar otro rango? [Y/N]: ').lower()
    
        if pregunta == 'y':
            screen_clear()
        else:
            continuar = False    


if __name__ == '__main__':
    main()
