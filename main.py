import sys

def limpiar_valor(valor):
    
    valor = valor.strip()
    caracteres_validos = "0123456789.-"
    resultado = ""

    for char in valor:
        if char in caracteres_validos:
            resultado += char

    return resultado


def procesar_linea(linea):

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

    while True:
        try:
            print(f"Imprima Ctrl Z para salir\n")
            pedircad = input("Ingrese la cadena SEPARANDO con comas los valores: \n")
        except EOFError:
            break

        if pedircad == '':
            break

        resultadosuma = procesar_linea(pedircad)
        print(f"Resultado de la suma de la cadena: \n",resultadosuma)


if __name__ == "__main__":
    main()