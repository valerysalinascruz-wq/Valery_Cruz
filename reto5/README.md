# Perfilador de Datasets

Herramienta en Python que analiza cualquier archivo CSV y genera un reporte de calidad de datos automáticamente.

---

## Descripcion

El programa lee cualquier CSV, analiza cada columna y genera un perfil con información sobre tipos de datos, valores nulos, valores únicos y ejemplos. El resultado se guarda en un nuevo archivo CSV.

---

## Requisitos

- Python 3.8 o superior
- No requiere dependencias externas

---

## Instalacion

### 1. Clonar el repositorio
```bash
git clone https://github.com/valerysalinascruz-wq/Valery_Cruz.git
cd Valery_Cruz
```

### 2. Crear ambiente virtual

**Windows (CMD/PowerShell):**
```cmd
python -m venv .venv
```

**Linux/Mac:**
```bash
python3 -m venv .venv
```

### 3. Activar ambiente virtual

**Windows (CMD):**
```cmd
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## Uso

### Windows (CMD/PowerShell)
```cmd
python main.py --input data/ventas.csv --output outputs/perfil_ventas.csv
```

### Linux/Mac
```bash
python3 main.py --input data/ventas.csv --output outputs/perfil_ventas.csv
```

### Forma corta
```bash
python main.py -i data/ventas.csv -o outputs/perfil_ventas.csv
```

### Ejemplos con los archivos de prueba
```bash
python main.py -i data/ventas.csv -o outputs/perfil_ventas.csv
python main.py -i data/empleados.csv -o outputs/perfil_empleados.csv
python main.py -i data/sensores.csv -o outputs/perfil_sensores.csv
```

---

## Estructura del Proyecto

```
reto-semana-05/
├── main.py               # Programa principal
├── requirements.txt      # Dependencias
├── README.md             # Documentacion
├── .gitignore            # Archivos a ignorar
├── data/                 # CSVs de prueba
│   ├── ventas.csv
│   ├── empleados.csv
│   └── sensores.csv
└── outputs/              # Perfiles generados
```

---

## Formato de Entrada

Cualquier archivo CSV con:
- Primera fila como encabezados
- Separador: coma (`,`)
- Codificación: UTF-8

---

## Formato de Salida

El perfil generado contiene una fila por columna del CSV original:

| Columna | Descripcion |
|---------|-------------|
| `nombre_columna` | Nombre de la columna |
| `tipo_inferido` | Tipo detectado: `numerico`, `texto`, `fecha`, `booleano` |
| `total_registros` | Total de filas |
| `valores_nulos` | Cantidad de valores vacios |
| `porcentaje_nulos` | Porcentaje de nulos (2 decimales) |
| `valores_unicos` | Cantidad de valores distintos |
| `porcentaje_unicos` | Porcentaje de unicidad (2 decimales) |
| `ejemplo_valor` | Primer valor no nulo encontrado |

### Ejemplo de salida:
```
nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
fecha,fecha,5,0,0.00,5,100.00,2026-01-01
producto,texto,5,0,0.00,4,80.00,Laptop
cantidad,numerico,5,1,20.00,4,80.00,2
precio,numerico,5,1,20.00,3,60.00,15000.00
vendedor,texto,5,1,20.00,3,60.00,Ana
```

---

## Autor

**Valery Cruz Salinas**  
Programación para Ciencia de Datos — IPN  
Semestre Febrero-Julio 2026