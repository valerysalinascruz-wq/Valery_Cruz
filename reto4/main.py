from models.producto import Producto 
from utils.validators import validar_producto 
from utils.io import leer_inventario, escribir_reporte 

ARCHIVO_ENTRADA = "data/inventario.csv"
ARCHIVO_SALIDA = "outputs/reporte_inventario.csv"

def crear_productos(datos):
    productos = []

    for d in datos:
        valido, error = validar_producto(
            d.get("sku"),
            d.get("nombre"),
            d.get("categoria"),
            d.get("precio"),
            d.get("stock"),
            d.get("stock_minimo"),
        ) 

        if not valido:
            continue

        p = Producto(
            d["sku"],
            d["nombre"],
            d["categoria"],
            float(d["precio"]),
            int(d["stock"]),
            int(d["stock_minimo"]),
        )
        productos.append(p)

    return productos 

def filtrar_reorden(productos):
    return [p for p in productos if p.necesita_reorden()]

def ordenar(productos):
    return sorted(productos, key=lambda p: p.unidades_faltantes(),reverse=True)

def main():

    datos = leer_inventario(ARCHIVO_ENTRADA)

    productos = crear_productos(datos)

    reorden = filtrar_reorden(productos)

    reorden = ordenar(reorden)

    for p in reorden:
        print(p)

    escribir_reporte(reorden, ARCHIVO_SALIDA)

if __name__ == "__main__":
  main()