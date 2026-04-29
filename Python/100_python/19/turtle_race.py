from turtle import Turtle as T, Screen as S
from random import randint as r

t1 = T("turtle") 
t2 = T("turtle")
t3 = T("turtle")
t4 = T("turtle")
t5 = T("turtle")
t6 = T("turtle")
s = S()

COLORES = ["red", "orange", "yellow", "green", "blue", "purple"]
LISTADO_TORTUGAS = [t1, t2, t3, t4, t5, t6]
posiciones = [-240, -240, -240, -240, -240, -240]
s.setup(500, 500)

def dibujar_meta():
    t1.hideturtle()
    t1.penup()
    t1.goto(200, -150)
    t1.pendown()
    t1.goto(200, 200)
    t1.penup()
    t1.home()
    t1.showturtle()

def set_colores(tortugas):
    for i, tortuga in enumerate(tortugas):
        tortuga.color(COLORES[i])

def colocar_tortugas(tortugas):
    posicion = -100
    for tortuga in tortugas:
        tortuga.penup()
        tortuga.goto(-240, posicion)
        posicion += 50

def avance_aleatorio(tortugas):
    for i, tortuga in enumerate(tortugas):
        avance = r(10, 20)
        tortuga.fd(avance)
        actualizar_posicion(i, avance)

def actualizar_posicion(posicion, avance):
    posiciones[posicion] += avance

def hay_ganador(posiciones):
    for i, posicion in enumerate(posiciones):
        if posicion >= 200:
            return True, i
    return False, None

def main():
    dibujar_meta()
    set_colores(LISTADO_TORTUGAS)
    colocar_tortugas(LISTADO_TORTUGAS)
    user_bet = s.textinput("Make your bet", "Wich turtle will win the race? Enter a color: ")
    def revisar_apuesta(guess, turtle):
        return guess.lower() == turtle.lower()
    while True:
        ganador, posicion = hay_ganador(posiciones) 
        if ganador:
            tortuga_ganadora = COLORES[posicion]
            print(f"The winer is: {tortuga_ganadora}")
            if revisar_apuesta(user_bet, tortuga_ganadora):
                print("You win!")
            else: 
                print("You lost!")
            break
        else:
            avance_aleatorio(LISTADO_TORTUGAS)
    s.exitonclick()

main()
