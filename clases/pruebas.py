import math

# Datos
lado_base = 6
altura = 15

# 1. Área de la base
A_base = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * lado_base**2

# 2. Apotema lateral
s = math.sqrt(altura**2 + (lado_base / (2 * math.tan(math.pi / 5)))**2)

# 3. Área lateral
P_base = 5 * lado_base  # Perímetro de la base
A_lateral = (1/2) * P_base * s
at = A_lateral + A_base

print(A_base, A_lateral, s, at)