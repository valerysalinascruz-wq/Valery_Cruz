# Sistema de Inventario Modular

Sistema en Python que lee un inventario desde un archivo CSV, identifica productos que necesitan reorden y genera un reporte consolidado.

---

## Descripcion

El sistema lee el archivo `data/inventario.csv`, valida cada registro, filtra los productos con stock menor al mínimo requerido y genera el archivo `outputs/reporte_inventario.csv` ordenado por unidades faltantes de mayor a menor.

---

## Estructura del Proyecto

```
reto-semana-04/
├── main.py                  # Punto de entrada del sistema
├── README.md                # Documentacion
├── .gitignore               # Archivos a ignorar
├── models/
│   ├── __init__.py
│   └── producto.py          # Clase Producto con sus metodos
├── utils/
│   ├── __init__.py
│   ├── io.py                # Funciones de lectura y escritura de archivos
│   └── validators.py        # Funciones de validacion de datos
├── data/
│   └── inventario.csv       # Archivo de entrada con el inventario
└── outputs/
    └── reporte_inventario.csv  # Reporte generado por el sistema
```

---

## Como Ejecutar

### Windows (CMD)
```cmd
python main.py
```

### Windows (PowerShell)
```powershell
python main.py
```

### Linux / Mac
```bash
python3 main.py
```

> El programa debe ejecutarse desde la raíz del proyecto para que las rutas de `data/` y `outputs/` funcionen correctamente.

### Guardar la salida en un archivo de log
```bash
# Linux/Mac
python3 main.py > log.txt

# Windows CMD
python main.py > log.txt
```

---

## Entrada

### Archivo: `data/inventario.csv`

Formato CSV con las siguientes columnas:

| Columna | Tipo | Descripcion |
|---------|------|-------------|
| `sku` | texto | Identificador unico del producto |
| `nombre` | texto | Nombre del producto |
| `categoria` | texto | Categoria del producto |
| `precio` | decimal | Precio unitario |
| `stock` | entero | Cantidad actual en inventario |
| `stock_minimo` | entero | Nivel minimo antes de reordenar |

### Ejemplo:
```csv
sku,nombre,categoria,precio,stock,stock_minimo
SKU100,Laptop Dell,Electronica,20000.00,2,10
SKU101,Mouse Gamer,Accesorios,500.00,15,10
SKU102,Teclado RGB,Accesorios,1200.00,0,5
```

### Lineas ignoradas automaticamente:
- Precio no numerico (ej. `N/A`, `pendiente`)
- Stock no numerico (ej. `abc`, `null`)
- Stock minimo no numerico (ej. `???`)
- Menos de 6 columnas
- Mas de 6 columnas

---

## Salida

### Archivo: `outputs/reporte_inventario.csv`

Contiene solo los productos con `stock < stock_minimo`, ordenados por unidades faltantes de mayor a menor.

| Columna | Descripcion |
|---------|-------------|
| `sku` | SKU del producto |
| `nombre` | Nombre del producto |
| `categoria` | Categoria |
| `stock_actual` | Stock actual |
| `stock_minimo` | Stock minimo requerido |
| `unidades_faltantes` | `stock_minimo - stock_actual` |
| `valor_inventario` | `precio × stock_actual` (2 decimales) |

### Ejemplo:
```csv
sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario
SKU100,Laptop Dell,Electronica,2,10,8,40000.00
SKU104,Audifonos Pro,Audio,1,8,7,1500.00
SKU102,Teclado RGB,Accesorios,0,5,5,0.00
```

---

## Autor

**Valery Cruz Salinas**  
Programación para Ciencia de Datos — IPN  
Semestre Febrero-Julio 2026