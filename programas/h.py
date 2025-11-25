def palabras_unicas(archivo1, archivo2, salida):
    # Leer ambos archivos
    with open(archivo1, "r", encoding="utf-8") as f1:
        texto1 = f1.read().lower()

    with open(archivo2, "r", encoding="utf-8") as f2:
        texto2 = f2.read().lower()

    # Separar palabras
    palabras1 = texto1.split()
    palabras2 = texto2.split()

    # Unir y eliminar duplicados
    unicas = sorted(set(palabras1 + palabras2))

    # Guardar en archivo de salida
    with open(salida, "w", encoding="utf-8") as f_out:
        f_out.write(" ".join(unicas))


# Ejemplo de uso:
palabras_unicas("../diccionarios/dic_fran", "../diccionarios/dic_fran2", "../diccionarios/dic_fran")