import sys

def limpiar_valor(valor):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no validos
    - Retorna el numero limpio como string
    """
    
    valor = valor.strip()
    caracteres_validos = "0123456789.-"
    resultado = ""

    for char in valor:
        if char in caracteres_validos:
            resultado += char

    return resultado


def procesar_linea(linea):
    """
    Procesa una linea completa:
    - Separa por comas
    - Limpia cada valor
    - Trunca a entero
    - Suma todos
    - Retorna el resultado
    """

    linea = linea.strip()

    if linea == "":
        return 0

    valores = linea.split(',')
    suma = 0

    for v in valores:

        limpio = limpiar_valor(v)

        if limpio == "":
            continue

        try:
            numero = float(limpio)
            suma += int(numero)  # truncar
        except ValueError:
            continue

    return suma


def main():
    """
    Lee de stdin linea por linea
    Procesa cada linea
    Imprime el resultado
    Pedira las dos cadenas
    """
    lacadena=input("Ingresa la cadena: ")
    resultadosuma = procesar_linea(lacadena)

    print("Resultado de la suma de la cadena: ",resultadosuma)

    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)


if __name__ == "__main__":
    main()