import sys


def main():
    productos={}
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

        producto=partes[1]

        try:
            cantidad=int(partes[2])
            precio=float(partes[3])
        except:
            continue

        if producto not in productos:
            productos[producto]={
                "unidades": 0,
                "ingreso": 0.0
            }

        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

        for prod in productos:
            unidades = productos[prod]["unidades"]
            ingreso = productos[prod]["ingreso"]

            if unidades > 0:
                productos[prod]["promedio"] = ingreso / unidades
            else:
                productos["promedio"] = 0

        lista = list(productos.items())

        ordenados = sorted(
            lista,
            key=lambda x: x[1]["ingreso"],
            reverse=True
        )

        print(productos)


# Saltar encabezado


# Saltar lineas vacias

# Parsear linea

# Convertir cantidad y precio (con manejo de errores)

# Crear entrada si no existe

# Acumular


# Imprimir salida


if __name__ == "__main__":
    main()