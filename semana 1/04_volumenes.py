import os
import math

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def calcular_volumen(altura, radio):
    
    area_base = math.pi * radio**2
    volumen_A = math.pi * (radio**2) * altura    
    volumen_B = area_base * altura   

    volumenes = {
        'A': volumen_A,
        'B': volumen_B,
    }
    
    return volumenes
    


def main():
    continuar = True
    while continuar:
        print("calculo de volumen")
        print("Seleccione el metodo a utilizar:")
        print("[1] π * r²")
        print("[2] A * h")
        metodo = int(input())

        r = float(input('Ingrese el Radio de la Base: '))
        h = float(input('Ingrese la altura del cilndro: '))
        
        if metodo == 1:
            volumen = calcular_volumen(h, r)['A']
            print('Él volumen del cilindro es de', volumen)
        elif metodo == 2:
            volumen = calcular_volumen(h, r)['B']
            print('Él volumen del cilindro es de', volumen)
        else:
            print('Opcion incorrecta')

        pregunta = input('Desea hacer otro calculo? [Y/N]: ').lower()
    
        if pregunta == 'y':
            screen_clear()
        else:
            continuar = False    


if __name__ == '__main__':
    main()
