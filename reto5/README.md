#Perfilador de Datasets

Herramienta en Python que analiza archivos CSV y genera un reporte de calidas de datos por cada columna.
Permite identificar rapidamente tipos de datos,valores nulos, valores unicos y obtener vista general 
del dataset antes de analizarlo.

##Requisitos

-Python 3.8+

##Instalacion 

-Clonar el repositorio
git clone <https://github.com/valerysalinascruz-wq/Valery_Cruz.git>
cd reto5

-Crear ambiente virtual
py -m venv .venv

-Activar ambiente virtual
#Windows
source .ven/Scripts/activate
#Linux
pip install -r requirements.txt

-Instalar dependencias 
pip install -r requirements.txt

##Uso
python main.py --input <archivo_entrada.csc> --output <archivo_salida.csv>
#Ejemplo
python main.py --input data/ventas.csc --output outputs/perfil.csv

#Formato de salida
El perfil generado contiene las siguientes columnas:

Columna	          Descripcion
nombre_columna	  Nombre de la columna
tipo_inferido	  Tipo detectado (numerico, texto, fecha, booleano)
total_registros	  Total de filas
valores_nulos	  Cantidad de valores vacios
porcentaje_nulos  Porcentaje de valores nulos
valores_unicos	  Cantidad de valores distintos
porcentaje_unicos Porcentaje de unicidad
ejemplo_valor	  Primer valor no nulo


##Ejemplo de entrada
Archivo: data/ventas.csv
fecha,producto,cantidad,precio,vendedor 
2026-01-01,Laptop,2,15000.00,Ana 
2026-01-02,Mouse,10,250.00,Bob 
2026-01-03,Teclado,,800.00,Ana 
2026-01-04,Monitor,3,,Carlos 
2026-01-05,Laptop,1,15000.00,

##Ejemplo de salida
Archivo generado: outputs/perfil_ventas.csv
nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos ejemplo_valor 
fecha,fecha,5,0,0.00,5,100.00,2026-01-01 
producto,texto,5,0,0.00,4,80.00,Laptop 
cantidad,numerico,5,1,20.00,4,80.00,2 
precio,numerico,5,1,20.00,3,60.00,15000.00 
vendedor,texto,5,1,20.00,3,60.00,Ana

##Autos 
Valery Cruz Salinas -Abril 2026


