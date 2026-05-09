# Calculadora de Sumas

Programa en Python que lee líneas desde la entrada estándar (stdin), procesa valores separados por comas y muestra la suma de cada línea.

---

## ¿Cómo funciona?

- Lee líneas desde stdin hasta encontrar el fin del archivo (EOF)
- Separa cada línea por comas
- Limpia caracteres inválidos de cada valor
- Trunca los decimales a entero (no redondea)
- Imprime la suma de cada línea

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
1,2,3
10

1.9,2.1,3.7
1a2,3b,4
-5,10,3
  5 , 10 , 15  
```

**Salida:**
```
6
10
0
6
19
8
30
```

---

## Reglas de procesamiento

| Caso | Ejemplo | Salida |
|------|---------|--------|
| Suma básica | `1,2,3` | `6` |
| Un solo valor | `10` | `10` |
| Línea vacía | `` | `0` |
| Truncar decimales | `1.9,2.1,3.7` | `6` |
| Caracteres basura | `1a2,3b,4` | `19` |
| Números negativos | `-5,10,3` | `8` |
| Espacios extra | `  5 , 10 , 15  ` | `30` |

---

## Autor

**Valery Cruz Salinas**  
Programación para Ciencia de Datos — IPN  
Semestre Febrero-Julio 2026