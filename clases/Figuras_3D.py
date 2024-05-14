#Derechos reservados para Jesús Benjamín Morales Hernández.
import math
def limpiar():
    print("")
def piramide_poligonal(n_lado, lado, altura):
    apo = round((math.sqrt((lado**2)-((lado/2)**2))),4)
    
    apo_cu = round((apo**2),4)
    al_cu = altura**2
    
    b = lado/2
    b_cu = b**2
    lado_cu = lado**2
    apo_triangulo = round(math.sqrt((apo**2)+(altura**2)),4)
    
    perimetro_base = lado * n_lado
    area_base = perimetro_base * apo
    total_base = area_base/2
    xd = round((lado * apo_triangulo),4)
    xdd = round((xd/2),4)
    area_lateral = round((n_lado * xdd),4)
    area_total = area_lateral + total_base
    
    resultados = print(f'''
    Apotema (a’):
    A² = C² - B²
    (a’)² = {lado}² - {b}²
    a’ = √{lado_cu} - {b_cu}
    a’ = {apo} u
    
    Apotema (Ap):
    C² = A² + B²
    (Ap)² = {apo}² + {altura}²
    Ap = √{apo_cu} + {al_cu} 
    Ap = {apo_triangulo} u
    
    Área de la piramide poligonal:
    A_lateral = N * (b * Ap)/2
    A_lateral = {n_lado} * ({lado} * {apo_triangulo}) / 2
    A_lateral = {n_lado} * ({xd}/2)
    A_lateral = {n_lado} * {xdd}
    A_lateral = {area_lateral} u²
        
    A_base = (P * a’)/2
    A_base = ({perimetro_base} * {apo})/2
    A_base = ({area_base}) / 2
    A_base = {total_base} u²
    
    A_total = A_lateral + A_base
    A_total = {area_lateral} u² + {total_base} u²
    A_total = {area_total} u²
    ''')
    return resultados
def ortoedro(lado_a, lado_b, lado_c):
    area = 2*(lado_a*lado_b+lado_a*lado_c+lado_b*lado_c)
    volumen = lado_a*lado_b*lado_c
    #variables
    a = lado_a*lado_b
    b = lado_a*lado_c
    c = lado_b*lado_c
    suma = a+b+c
    resultados = print(f'''
    
    A = 2 * (A*B+A*C+B*C)
    A = 2 * (({lado_a} u * {lado_b}) u + ({lado_a} u * {lado_c}) u + ({lado_b} u * {lado_c} u))
    A = 2 * (({a}) u + ({b}) u + ({c}) u)
    A = 2 * ({suma} u)
    A = {area} u²
    
    V = A * B * C
    V = {lado_a} u * {lado_b} u * {lado_c} u
    V = {volumen} u³
    ''')
    return resultados
def sacar_apotema_altura_y_base(altura, alrura_interna):
    apotema = math.sqrt((altura**2)+(alrura_interna**2))
    return apotema
def piramide_penta(n_lados, lado, altura):
    apo = round((math.sqrt((lado**2)-((lado/2)**2))),4)
    b = lado/2
    b_cu = b**2
    lado_cu = lado**2
    perimetro_base = n_lados * lado
    a_la = perimetro_base * altura
    area_bases = round((perimetro_base * apo),4)
    una_base = round((area_bases/2),4)
    volumen = round((una_base * altura),4)
    area_total = round((a_la+area_bases),4)
    resultados = print(f'''
    Apotema:
    A² = C² - B²
    (a’)² = {lado}² - {b}²
    a’ = √{lado_cu} u - {b_cu} u
    a’ = {apo} u
    
    Área del prisma Poligonal:
    A_lateral = P_base * h
    A_lateral = {perimetro_base} u * {altura} u
    A_lateral = {a_la} u²
    
    A_bases = 2 * (P * a’)/2
    A_bases = 2 * ({perimetro_base} * {apo})/2 = {perimetro_base} * {apo}
    A_bases = {area_bases} u²
    
    Área total
    A_total = A_lateral + A_bases
    A_total = {a_la} u² + {area_bases} u²
    A_total = {area_total} u²
    
    Volumen del prisma poligonal:
    V = ((A_base * h)/2) * h = ((P * a’)/2) * h
    V = (({perimetro_base} u * {apo} u )/2) * {altura} u
    V = (({area_bases} u² )/2) * {altura} u
    V = {una_base} u² * {altura} u
    V = {volumen} u³
    
    ''')
    return resultados
def piramide_keops(altura, base, base2):
    apo = round((math.sqrt(altura**2 + base2**2)),4)
    al_cu = altura**2
    ba_cu = base2**2
    triangulo_1 = base * apo
    cara = (base * apo)/2
    area_lat = cara * 4
    area_base = base**2
    area_tot = area_lat + area_base
    volumen_uno = area_base * altura
    v = volumen_uno / 3
    resultados = print(f'''
    Apotema:
    C² = A² + B²
    (a’)² = {altura}² + {base2}²
    a’ = √{al_cu} u + {ba_cu} u
    a' = {apo} u
    
    Área de la piramide de Keops:
    A_lateral = N_caras * (b*a‘)/2
    A_lateral = 4 * ({base} u * {apo} u )/2
    A_lateral = 4 * ({triangulo_1} u )/2
    A_lateral = 4 * ({cara} u )
    A_lateral = {area_lat} u²
    
    A_base = b²
    A_base = {base}²
    A_base = {area_base} u²
    
    A_total = A_lateral + A_base
    A_total = {area_lat} u² +  {area_base} u²
    A_total = {area_tot} u²
    
    Volumen:
    V = (A_base * h)/3
    V = ({area_base} * {altura}) / 3
    V = ({volumen_uno}) / 3
    V = {v} u³
    ''')
    return resultados
def cono(radio, altura):       
    generatriz = round((math.sqrt(radio**2 + altura**2)), 4) 
    altu_cu = altura**2
    radi_cu = radio**2
    pi = round((math.pi), 4)
    area_l = round((math.pi*radio*generatriz),4)
    area_b = round((math.pi*radio**2),4)
    area = area_l + area_b
    v_1 = round((math.pi * radio**2 * altura),4)
    volumen = round((v_1 / 3),4)
    
    resultados = print(f'''
    Generatriz:
    C² = A² + B²
    g² = {altura}² + {radio}²
    g = √{altu_cu} u + {radi_cu} u
    g = {generatriz} u
    
    Área de un cono
    A_lateral = π * r * g
    A_lateral = {pi} * {radio} u * {generatriz} u
    A_lateral = {area_l} u²
    
    A_base = π * r²
    A_base = {pi}  * {radio}² u
    A_base = {area_b} u²
    
    A_total = A_lateral + A_base
    A_total = {area_l} u² + {area_b} u²
    A_total = {area} u²
    
    Volumen de un cono
    
    V = (π * r² * h)/3
    V = (π * {radio}² u * {altura} u )/3
    V = ({v_1} u ) / 3
    V = {volumen} u³
    ''')
    return resultados
def esfera(radio):
    pi = round((math.pi),4)
    area = round((4 * math.pi * radio**2),4)
    volumen = round(((4/3)*math.pi*radio**3),4)
    Resultados = print(f'''
                       
    El área de la esfera es:
    
    A = 4 * π * r²
    A = 4 * {pi} * {radio}² = {area} u²
    A = {area} u²
    
    El volumen de la esfera es:
    
    V = (4/3) * π * r³
    V = (4/3) * {pi} * {radio}³ u = {volumen} u³
    V = {volumen} u³
    ''')
    return Resultados
def cilindro(radio, altura):
    pi = round((math.pi),4)
    a_late = round((2*math.pi*radio*altura), 4)
    a_base = round((math.pi*radio**2),4)
    are_1 = a_base * 2
    area_to = a_late + are_1
    volumen = round((math.pi * radio**2 * altura),4)
    
    resultados = print(f'''
    
    Area del cilindro:
    
    A_lateral = 2 * π * r * h
    A_lateral = 2 * {pi} * {radio} u * {altura} u
    A_lateral = {a_late} u²
    
    A_bases = 2 * (π * r²)
    A_bases = 2 * {pi} * {radio}² u
    A_bases = 2 * ({a_base} u)
    A_bases = {are_1} u²
    
    A_total = A_lateral + A_bases
    A_total = {a_late} u² + {are_1} u²
    A_total = {area_to} u²
    
    Volumen del cilindro
    
    V = π * r² * h
    V = {pi} * {radio}² u * {altura} u
    V = {volumen} u³
    ''')
    return resultados

while True:
    opcion = int(input(f'''
    Secciones del programa

    Áreas de figuras 3D
        
    1) Ortoedro.
    2) Prisma poligonal
    3) Piramide de Keops.
    4) Piramide poligonal        
    6) Calcular el volumen de una esfera.
    7) Calcular el volumen de un cono.
    8) Propiedades de una cilindro.
    
Opcion a realizar: '''))
    limpiar()
    
    if  opcion == 1:
        lado_a = float(input("Lado A: "))
        lado_b = float(input("lado B: "))
        lado_c = float(input("Lado C: "))
        resultados = ortoedro(lado_a, lado_b, lado_c)
        limpiar()
        
    elif opcion == 2:
        n_lados = int(input("Ingrese el número de lados de la base del poligino: "))
        lado = float(input("Ingrese la medida de uno de los lados de la base: "))
        altura = float(input("Altura: "))
        resultados = piramide_penta(n_lados, lado, altura)
        limpiar()
        
    elif opcion == 3:
        altura = float(input("Ingresar la altura: "))
        base = float(input("Ingresar la longitud de la base: "))
        base2 = base*0.5
        area = piramide_keops(altura, base, base2)
        limpiar()
        
    elif opcion == 4:
        n_lado = float(input("Lados totales de la base: "))
        lado = float(input("Medida de los lados del poligono: "))
        altura = float(input("Altura: "))
        resultados = piramide_poligonal(n_lado, lado, altura)
        limpiar()
        
    elif opcion == 6:
        radio = float(input("Radio de la esfera: "))
        resultados = esfera(radio)
        limpiar()
        
    elif opcion == 7:
        radio = float(input("Radio del cono: "))
        altura = float(input("Altura del cono: "))
        resultados = cono(radio, altura)
        limpiar()
        
    elif opcion == 8:
        radio = float(input("Radio:"))
        altura = float(input("Altura:"))
        resultados = cilindro(radio, altura)
        limpiar()
        
    input(" Enter para continuar...")