def clasificar_nota(nota):
    if 95 <= nota <= 100:
        return "Excelente"
    elif 85 <= nota <= 94:
        return "Notable"
    elif 75 <= nota <= 84:
        return "Buena"
    elif 70 <= nota <= 74:
        return "Regular"
    else:
        return "N/A"  

nombre = input("Ingresa tu nombre: ")
materia = input("Ingresa el nombre de la materia: ")
nota = int(input("Ingresa la nota: "))

mensaje = clasificar_nota(nota)
print(f"\n datos")
print(f"Nombre: {nombre}")
print(f"Materia: {materia}")
print(f"La calificación es: {clasificar_nota(nota)}")

