# Clasificador de Temperaturas

Programa en Python que lee un archivo CSV desde la entrada estándar (stdin), convierte temperaturas de Fahrenheit a Celsius, clasifica cada ciudad según su clima y genera un reporte estandarizado.

---

## ¿Cómo funciona?

- Lee un CSV con columnas `ciudad,temperatura,unidad` desde stdin
- Salta la primera línea (encabezado)
- Convierte temperaturas en Fahrenheit a Celsius
- Clasifica cada temperatura según la siguiente tabla:

| Temperatura (°C) | Clasificación |
|------------------|---------------|
| Menor a 0        | Congelante    |
| 0 a 15           | Frio          |
| 16 a 25          | Templado      |
| 26 a 35          | Calido        |
| Mayor a 35       | Extremo       |

- Ignora líneas con datos inválidos (temperatura no numérica, unidad distinta de C o F, columnas faltantes)
- Imprime el resultado en formato CSV a stdout

---

## Instrucciones de uso

### Windows (CMD)
```cmd
type entrada.txt | python main.py
```

### Windows (PowerShell)
```powershell
Get-Content entrada.txt | python main.py
```

### Linux / Mac
```bash
python main.py < entrada.txt
```

### Guardar la salida en un archivo
```bash
# Linux/Mac
python main.py < entrada.txt > salida.txt

# Windows CMD
type entrada.txt | python main.py > salida.txt
```

### Entrada manual (para pruebas)
```bash
python main.py
# Escribe líneas manualmente
# Presiona Ctrl+D (Linux/Mac) o Ctrl+Z (Windows) para terminar
```

---

## Ejemplo

**Entrada:**
```
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
Moscu,-10,C
Miami,95,F
Cancun,30,C
Chicago,14,F
Error,abc,C
```

**Salida:**
```
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
Moscu,-10.0,Congelante
Miami,35.0,Calido
Cancun,30.0,Calido
Chicago,-10.0,Congelante
```

> La línea con "Error" no aparece porque la temperatura no es un número válido.

---

## Casos manejados

| Caso | Comportamiento |
|------|----------------|
| Temperatura en Fahrenheit | Se convierte a Celsius |
| Temperatura negativa | Se clasifica como Congelante |
| Unidad en minúsculas (`c`, `f`) | Se acepta correctamente |
| Espacios extra | Se ignoran con `.strip()` |
| Temperatura no numérica | Línea ignorada |
| Unidad inválida (ej. `X`) | Línea ignorada |
| Línea vacía | Ignorada |
| Menos de 3 columnas | Línea ignorada |

---

## Autor

**Valery Cruz Salinas**  
Programación para Ciencia de Datos — IPN  
Semestre Febrero-Julio 2026