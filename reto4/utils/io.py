def leer_inventario(ruta) :
    productos = []

    with open(ruta, "r", encoding= "utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            return productos
        
        encabezados = lineas[0].strip().split(",")

        for linea in lineas[1:]:
            linea = linea.strip()
            if not linea:
                continue

            valores = linea.split(",")

            if len(valores) == len(encabezados):
                producto = dict(zip(encabezados,valores))
                productos.append(producto)
    
    return productos

def escribir_reporte(productos, ruta):
    with open(ruta, "w", encoding="utf-8") as archivo:

        archivo.write("sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario\n")

        for p in productos:
            linea = f"{p.sku},{p.nombre},{p.categoria},{p.stock},{p.stock_minimo},{p.unidades_faltantes()},{p.valor_inventario():.2f}"
            archivo.write(linea + "\n")