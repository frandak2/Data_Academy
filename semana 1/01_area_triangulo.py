
import math
import os

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


def area_triangulo(base, altura):
    area_general = (base * altura) / 2

    area_isosceles = base*math.sqrt((lado_isosceles**2)-((base**2)/4))/2

    area_equilatero = (math.sqrt(3)/4) * (base ** 2)

    lado_isosceles = math.sqrt(16*(area_general**2)+(base**4))/(2*base)     

    if area_general == area_isosceles:
        tipo = "Isosceles"
    elif area_general == area_equilatero:
        tipo = "Equilatero"
    else:
        tipo = "Escaleno"

    return print(f"El Triangulo es de tipo {tipo}, y tiene un area de {area_general}")

def main():
    continuar = True
    while continuar:
        print("tipos y areas en los triangulos")
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
            
        area_triangulo(base, altura)

        pregunta = input('Continuar? [Y/N] ').lower()
        
        if pregunta == 'y':
            screen_clear()
        else:
            continuar = False              


if __name__ == '__main__':
    main()