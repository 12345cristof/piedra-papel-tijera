import random
import getpass

ultima_estadistica = None

def menu():
    while True:
        print("1. Jugar")
        print("2. Ver reglas")
        print("3. Ver estadísticas de la última partida")
        print("4. Salir")
        op = input("Elige opción: ")
        if op == "1":
            jugar()
        elif op == "2":
            reglas()
        elif op == "3":
            mostrar_estadisticas()
        elif op == "4":
            print("Game over")
            break
        else:
            print("No entiendo esa opción")

def mostrar_estadisticas():
    global ultima_estadistica
    if ultima_estadistica is None:
        print("No hay estadísticas de partidas jugadas todavía.")
        return
    
    print("Estadísticas de la última partida")
    print("Jugadores:", ultima_estadistica['jugador1'], "vs", ultima_estadistica['jugador2'])
    print("Partidas jugadas:", ultima_estadistica['total_partidas'])
    print(ultima_estadistica['jugador1'], "ganó", ultima_estadistica['gana1'], "veces")
    print(ultima_estadistica['jugador2'], "ganó", ultima_estadistica['gana2'], "veces")
    print("Empates:", ultima_estadistica['empates'])

def reglas():
    print("Piedra gana a tijera")
    print("Tijera gana a papel")
    print("Papel gana a piedra")
    input("Enter para volver")

def jugar():
    while True:
        print("1. Contra PC")
        print("2. Dos jugadores")
        print("3. Volver")
        op = input("Elige: ")
        if op == "1":
            jugar_pc()
        elif op == "2":
            jugar_2()
        elif op == "3":
            break
        else:
            print("Opción inválida")

def pedir_partidas():
    resp = input("Cuántas partidas quieres? : ")
    if resp.isdigit():
        return int(resp)
    else:
        return -1

def partida(j1, j2, ocultar=False):
    while True:
        if ocultar:
            e1 = getpass.getpass(j1 + " elige piedra, papel o tijera: ").lower()
            e2 = getpass.getpass(j2 + " elige piedra, papel o tijera: ").lower()
        else:
            e1 = input(j1 + " elige piedra, papel o tijera: ").lower()
            e2 = random.choice(["piedra", "papel", "tijera"])
            print(j2, "eligió", e2)

        if e1 not in ["piedra", "papel", "tijera"] or e2 not in ["piedra", "papel", "tijera"]:
            print("Opción no válida, vuelve a intentar")
            continue

        if e1 == e2:
            print("Empate")
            return "empate", "empate", e1, e2
        if (e1 == "piedra" and e2 == "tijera") or (e1 == "papel" and e2 == "piedra") or (e1 == "tijera" and e2 == "papel"):
            print("Gana", j1)
            return "gana", "pierde", e1, e2
        else:
            print("Gana", j2)
            return "pierde", "gana", e1, e2

def jugar_pc():
    global ultima_estadistica
    nombre = input("Tu nombre: ")
    partidas = pedir_partidas()
    g = e = p = 0
    cont = 0
    while partidas == -1 or cont < partidas:
        cont += 1
        print("Partida", cont)
        r1, r2, elec1, elec2 = partida(nombre, "Computadora")
        
        if r1 == "gana":
            print(nombre, "ganó con", elec1, "contra", elec2)
            g += 1
        elif r1 == "empate":
            print("Empate, ambos eligieron", elec1)
            e += 1
        else:
            print("Computadora ganó con", elec2, "contra", elec1)
            p += 1
        
        if partidas == -1:
            seguir = input("Otra partida? (si/no): ").lower()
            if seguir != "si":
                break
    
    ultima_estadistica = {
        'jugador1': nombre,
        'jugador2': 'Computadora',
        'gana1': g,
        'gana2': p,
        'empates': e,
        'total_partidas': cont
    }
    
    print("Resultados: Ganaste", g, ", Perdiste", p, ", Empataste", e)

def jugar_2():
    global ultima_estadistica
    j1 = input("Nombre de jugador 1: ")
    j2 = input("Nombre de jugador 2: ")
    partidas = pedir_partidas()
    e1 = e2 = emp = 0
    cont = 0
    while partidas == -1 or cont < partidas:
        cont += 1
        print("Partida", cont)
        r1, r2, elec1, elec2 = partida(j1, j2, ocultar=True)
        
        if r1 == "gana":
            print(j1, "ganó con", elec1, "contra", elec2)
            e1 += 1
        elif r1 == "empate":
            print("Empate, ambos eligieron", elec1)
            emp += 1
        else:
            print(j2, "ganó con", elec2, "contra", elec1)
            e2 += 1
            break

    ultima_estadistica = {
        'jugador1': j1,
        'jugador2': j2,
        'gana1': e1,
        'gana2': e2,
        'empates': emp,
        'total_partidas': cont
    }
    
    print("Resultados:", j1, "ganó", e1, ",", j2, "ganó", e2, ", empates", emp)

menu()

