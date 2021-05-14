import random
import os
from art import logo

cartas_mano_casa = []
cartas_mano_jugador = []

def dar_cartas(carta1, carta_final):
  cartas_casa = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  cartas_jugador =  [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  for i in range (carta1,carta_final):
    cartas_mano_casa.append(random.choice(cartas_casa))
    cartas_mano_jugador.append(random.choice(cartas_jugador))
    cartas_casa.remove(cartas_mano_casa[-1])
    cartas_jugador.remove(cartas_mano_jugador[-1])

def suma(cartas):
    return sum(cartas)

def quien_gana():
  if suma(cartas_mano_jugador) > suma(cartas_mano_casa):
    print(f"Tu mano final {cartas_mano_jugador}. Sumaste {suma(cartas_mano_jugador)}")
    print(f"La mano de la casa {cartas_mano_casa}. Sumo {suma(cartas_mano_casa)}")
    print("Felicitaciones, GANASTE.")
  elif suma(cartas_mano_jugador) < suma(cartas_mano_casa):
    print(f"Tu mano final {cartas_mano_jugador}. Sumaste {suma(cartas_mano_jugador)}")
    print(f"La mano de la casa {cartas_mano_casa}. Sumo {suma(cartas_mano_casa)}")
    print("Lo siento, PERDISTE.")
  
def pasarse_21(suma_jugador, suma_casa):
  if suma_jugador > 21:
    print(f"Tu mano final {cartas_mano_jugador}. Sumaste {suma(cartas_mano_jugador)}")
    print(f"La mano de la casa {cartas_mano_casa}. Sumo {suma(cartas_mano_casa)}")
    print("Lo siento, te pasaste.")
  elif suma_casa > 21:
    print(f"Tu mano final {cartas_mano_jugador}. Sumaste {suma(cartas_mano_jugador)}")
    print(f"La mano de la casa {cartas_mano_casa}. Sumo {suma(cartas_mano_casa)}")
    print("Felicidades, ganaste.")
  else:
     quien_gana()

def logo_clear():
  os.system('cls')
  print(logo)

logo_clear()
jugar = input("¿Queres jugar blackjack?(si/no) : ").lower() 
while jugar == "si":
  if jugar == "no":
    logo_clear()  
  elif jugar == "si":
    logo_clear()
    dar_cartas(0,2)
    print(f"Tus cartas son {cartas_mano_jugador}. Sumas {suma(cartas_mano_jugador)}")
    print(f"La primer carta de la casa es {cartas_mano_casa[0]}\n")

  pedir_carta = input("¿Queres una carta mas?(si/no): ").lower() 
  logo_clear()
  if pedir_carta == "no":
    quien_gana()
  elif pedir_carta == "si":
    dar_cartas(0,1)
    pasarse_21(suma(cartas_mano_jugador), suma(cartas_mano_casa))
  cartas_mano_jugador = []
  cartas_mano_casa = []
  input("\nPresiona cualquier tecla para continuar...")
  logo_clear()
  jugar = input("¿Queres jugar blackjack?(si/no) : ").lower() 
print("Vuelve cuando quieras jugar, ¡Te estare esperando!")
input("")
