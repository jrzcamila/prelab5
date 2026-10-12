paquetes = ["Apuntes: ", "Guía de ejercicios: ", "Material de consulta: "]
paquetes_aceptados = 0
total_paginas = 0
precio_pagina = 2

def calcular_subtotal(total_paginas, precio_pagina):
    return total_paginas * precio_pagina

for i in range(len(paquetes)):
    try:
        paginas = int(input(paquetes[i]))
        
        if paginas >= 1 and paginas <= 50:
            paquetes_aceptados += 1
            total_paginas += paginas
        else:
            print("Número fuera del rango permitido.")
            continue
            
    except ValueError:
        print("Valor inválido.")
        continue

subtotal = calcular_subtotal(total_paginas, precio_pagina)

if total_paginas > 100:
    descuento = subtotal * 0.10
    total_pagar = subtotal - descuento
else:
    descuento = 0
    total_pagar = subtotal

print(f"Paquetes aceptados: {paquetes_aceptados}")
print(f"Total de páginas: {total_paginas}")
print(f"El subtotal es: {subtotal}")
print(f"Descuento aplicado: {descuento}")
print(f"Total a pagar: {total_pagar}")