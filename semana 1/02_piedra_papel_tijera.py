import os

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
   

def piedra_papel_tijera(input_P1, input_P2):
    if (input_P1 == input_P2):
        return print('Se ha producido un empate !!!')
    elif ((input_P1 == "piedra" and input_P2 == "tijera") or 
          (input_P1 == "papel" and input_P2 == "piedra") or 
          (input_P1 == "tijera" and input_P2 == "papel")):
          return print('Gana el Jugador 1  !!!')
    else:
        return print('Gana el Jugador 2 !!!')

def main():
    continuar = True
    while continuar:
        print("piedra, papel o tijera")
        rounds = []
        for i in range(2):
            print(f'Jugador {i+1}, seleccione una opcion: ')
            print('Piedra')
            print('Papel')
            print('Tijera\n')
            jugada=input()
            rounds.append(jugada)
        piedra_papel_tijera(rounds[0], rounds[1])
        pregunta = input('Otra ronda? [Y/N] ').lower()
    
        if pregunta == 'y':
            screen_clear()
        else:
            continuar = False


if __name__ == "__main__":
    main()