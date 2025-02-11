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


nota = int(input("Ingresa la nota: "))
print(f"La calificación es: {clasificar_nota(nota)}")
