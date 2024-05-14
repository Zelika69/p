# Un jugador tira dos dados. Cada dado tiene 6 caras.Las caras contienen números de el 1 al 6. 
# Una vez que los dados se han detenido, se calcula la suma de los puntos en las dos caras superiores. 
# Si la suma es 7 u 11 en el primer lanzamiento, el jugador gana. Si la suma es 2 ,3 o 12 en el primer 
# tiro (llamado "craps"), el jugador pierde es decir la casa gana. 
# Si la suma es 4,5,6,8,9 o 10 en el primer lanzamiento, está suma se convierte en el punto de el jugador. 
# Para ganar debes continuar tirando los dados hasta que "hagas un punto". 
# El jugador pierde si saca un 7 antes de hacer el punto.
import random
import time

numeros_puntos = [] 
def cuenta_regresiva():
    for i in range(3, 0, -1):
        print("El juego comienza en ", i)
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
    numero_lanzamientos =+ 1
    
    if numero_lanzamientos == 1 and suma_dados == (7 or 11):
        print(f'''
              
    HAZ GANADO!!!
    
    N° lanzamiento: {numero_lanzamientos}
    N° Primer Dado: {dado1}
    N° Segundo Dado: {dado2}
    
    ''')
    elif numero_lanzamientos == 1 and suma_dados == (2 or 3 or 12):
        print(f'''
              
    HAZ PERDIDO, TIRO CRAPS!!!
    
    N° lanzamiento: {numero_lanzamientos}
    N° Primer Dado: {dado1}
    N° Segundo Dado: {dado2}
    
    ''')
    elif suma_dados == (4 or 5 or 6 or 7 or 8 or 9 or 10):
        while len(numeros_puntos) < 6:
            if not comproba_num(numeros_puntos, suma_dados):
                break
    