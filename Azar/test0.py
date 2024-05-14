import random
import time
import keyword

ronda = 0
numeros_puntos = []
def verificar_arreglo(list):
    for num in range(4, 11):
        if num != 7 and num not in list:
            return False
    return True
def cuenta_regresiva():
    print
    for i in range(3, 0, -1):
        print(" ", i)
        time.sleep(1)
    if i == 1:
        print("Tirando Dados!")
        time.sleep(1)
def comproba_num(lista_numeros, suma):
    if suma == 7:
        print("HAZ PERDIDO!!")
        return False
    elif suma not in lista_numeros:
        lista_numeros.append(suma)
    else:
        print("Número repetido:", suma)
    return True

numero_lanzamientos = 0

while True:
    cuenta_regresiva()
    dado1 = random.randint(1, 6)
    time.sleep(1)
    print("Dado uno es: ", dado1)
    time.sleep(0.7)
    dado2 = random.randint(1, 6)
    time.sleep(1)
    print("Dado dos es: ", dado2)
    suma_dados = dado1 + dado2
    numero_lanzamientos += 1

    if numero_lanzamientos == 1:
        if suma_dados == 7 or suma_dados == 11:
            print(f'''
    HAZ GANADO!!!
    
    N° lanzamiento: {numero_lanzamientos}
    N° Primer Dado: {dado1}
    N° Segundo Dado: {dado2}
    
    ''')
            break
        elif suma_dados == 2 or suma_dados == 3 or suma_dados == 12:
            print(f'''
    HAZ PERDIDO, TIRO CRAPS!!!
    
    N° lanzamiento: {numero_lanzamientos}
    N° Primer Dado: {dado1}
    N° Segundo Dado: {dado2}
    
    ''')
            break
        else:
            print(f'''
    Suma de puntos: {suma_dados}
    Comenzando siguiente ronda...
    
    ''')
        time.sleep(1.5)
    else:
        if verificar_arreglo(numeros_puntos):
            print(f'''
    Haz GANADO!!!
    
    Obtuviste los Números para ganar (4, 5, 6, 8, 9, 10)
    totales obtenidos: {numeros_puntos}
    
                ''')
        elif suma_dados == 7:
             print(f'''
     HAZ PERDIDO!
    
     Causa: no alcanzaste los numeros necesarios
     y haz saca una puntuacion de : {suma_dados}, antes de obtener los N° requeridos
     primer Dado: {dado1}
     Segundo Dado: {dado2}
    
     Números obtenidos: {numeros_puntos}
     ''')
             break
        elif suma_dados in numeros_puntos:
            print(f'''
    suma de ambos dados: {suma_dados}
    
    ''')
        else:
            print(f'''
    Suma de puntos: {suma_dados}
    Comenzando siguiente ronda!

    
    ''')
            time.sleep(1.5)
            if not comproba_num(numeros_puntos, suma_dados):
                break
