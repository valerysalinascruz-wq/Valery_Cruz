#Sistema de Inventario Modular

##Descripcion 
Sistema que detecta productos con stock bajo y genera un reporte a partir de un archivo csv

##Estructura
-models: contiene la clase Producto
-utils: contiene validaciones y funciones de lectura/escritura
-data: archivo de netrada(inventario.csv)
-outputs: archivo de salisa(reporte_inventario.csv)
-main.py: archivo principal

##Ejecutar 
python main.py

##Entrada
Archivo CSV con formato:
sku,nombre,categoria,precio,stock,stock_minimo

##Salida
Archivo CSV con productos que necesitan reorden:
sku,nombre,categoria,stock_actual,atock_minimo,unidades_faltantes,_valor_inventario

##Notas
-Se ignora registros invalidos
-No hay productos duplicados 
-Se ordena por unidades faltantes(de mayor a menor)