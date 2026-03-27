import sys


def main():
    primera = True
    for linea in sys.stdin:
        linea=linea.strip()
        if not linea:
            continue
        if primera:
            primera=False
            continue
        partes =linea.split(",")


        if len(partes)<4:
            continue

        partes = partes[:4]
        fecha =partes[0]
        producto=partes[1]

        try:
            cantidad=int(partes[2])
            precio=float(partes[3])
        except:
            continue

        print(producto, cantidad,precio)

# Saltar encabezado


# Saltar lineas vacias

# Parsear linea

# Convertir cantidad y precio (con manejo de errores)

# Crear entrada si no existe

# Acumular

# Calcular precio promedio


# Ordenar por ingreso descendente


# Imprimir salida


if __name__ == "__main__":
    main()