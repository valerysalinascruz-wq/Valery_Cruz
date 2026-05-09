# Analizador de Ventas

Programa en Python que lee un archivo CSV desde la entrada estándar (stdin), agrupa las transacciones por producto y genera un reporte consolidado ordenado por ingreso total.

---

## ¿Cómo funciona?

- Lee un CSV con columnas `fecha,producto,cantidad,precio_unitario` desde stdin
- Salta la primera línea (encabezado)
- Agrupa todas las transacciones del mismo producto
- Calcula por cada producto:
  - **Unidades vendidas**: suma de todas las cantidades
  - **Ingreso total**: suma de (cantidad × precio) por transacción
  - **Precio promedio**: ingreso total / unidades vendidas
- Ordena el reporte de mayor a menor ingreso total
- Ignora líneas con datos inválidos
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
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00
2026-01-04,Teclado,5,800.00
2026-01-05,Mouse,8,250.00
```

**Salida:**
```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
Teclado,5,4000.00,800.00
```

> Las transacciones de Laptop se consolidan: 2+1=3 unidades, (2×15000)+(1×14500)=44500.00

---

## Casos manejados

| Caso | Comportamiento |
|------|----------------|
| Mismo producto en varias líneas | Se agrupa y acumula |
| Cantidad no numérica | Línea ignorada |
| Precio no numérico | Línea ignorada |
| Menos de 4 columnas | Línea ignorada |
| Línea vacía | Ignorada |

---

## Autor

**Valery Cruz Salinas**  
Programación para Ciencia de Datos — IPN  
Semestre Febrero-Julio 2026