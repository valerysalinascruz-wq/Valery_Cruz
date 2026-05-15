import math

def validar_sku(sku) :
    if not sku or not str(sku).strip() :
        return False
    return True

def validar_precio(precio) :
    try:
        precio = float(precio)
        return precio >= 0 and math.isfinite(precio)
    except:
        return False

def validar_stock(stock):
    try:
        stock = int(stock)
        return stock >= 0
    except:
        return False

def validar_producto(sku,nombre,categoria,precio,stock,stock_minimo) :
    if not validar_sku(sku):
        return False,"SKU invalido" 
    if not nombre or not str(nombre).strip():
        return False,"Nombre invalido"
    if not validar_precio(precio):
        return False,"Precio invalido"
    if not validar_stock(stock):
        return False,"Stock invalido"
    if not validar_stock(stock_minimo):
        return False,"Stock minimo invalido"
    return True,None