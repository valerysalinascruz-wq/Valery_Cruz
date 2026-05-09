import sys

#limpia cada valor individual de la cadena
def limpiar_valor(valor):

    valor = valor.strip()
    caracteres_validos = "0123456789.-" #los caracteres validos son:numeros,punto decimal,negativos
    resultado = "" #se guarda el numero limpio

    for char in valor:
        if char in caracteres_validos: #verifica si el valor es valido
            resultado += char #si es valido se lo agrega a resultado

    return resultado

#procesa la cadena que se ingreso
def procesar_linea(linea):

    linea = linea.strip()

    if linea == "": #si la cadena es vacia
        return 0

    valores = linea.split(',') #divide la cadena con comas
    suma = 0  

    for v in valores: #recorre cada valor cuando los separa la coma

        limpio = limpiar_valor(v)

        if limpio == "": #si esta vacio depues de limpiar
            continue #continua con el siguiente valor

        try:
            numero = float(limpio)
            suma += int(numero)  # truncar
        except ValueError: #si ocurre un error al limpiarlo
            continue 

    return suma


def main():
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)

#Verifica que el archivo este ejecutando 
#Ejecuta la funcion principal
if __name__ == "__main__":
    main()