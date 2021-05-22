import os

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def conversor(tipo, cantidad):
    MILE=1.609344
    
    if tipo == 1:
        km = cantidad * MILE
        print(f"{cantidad} Millas = {km} Kilometros")

    else:
        print("en progreso")
        miles = cantidad / MILE
        print(f"{cantidad} Kilometros = {miles} Millas")

def main():
    continuar = True
    while continuar:
        print("conversor de area")
        print("Seleccione el tipo de conversion:")
        print("[1] de Milla a Km")
        print("[2] de Km a Milla")
        tipo = int(input())
        cantidad = float(input("Ingrese la cantidad de a convertir: "))
        conversor(tipo, cantidad)

        pregunta = input('Desea hacer otra conversion? [Y/N]: ').lower()
    
        if pregunta == 'y':
            screen_clear()
        else:
            continuar = False

if __name__ == '__main__':
    main()