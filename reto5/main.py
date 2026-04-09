import argparse
import sys

def es_valor_nulo(valor):
    if valor is None:
        return True
    if isinstance(valor,str) and valor.strip() == "":
        return True
    return False

def es_numerico(valor):
    try:
        float(str(valor).replace(',','').strip())
        return True
    except:
        return False

def es_fecha(valor):
    v = str(valor).strip()
    if len(v) >= 10 and v[4] == '-' and v[7] == '-':
        try:
            y, m, d = map(int, v[:10].split('-'))
            return 1900 <= y <= 2100 and 1 <= m <= 12 and 1 <= d <= 31
        except:
            pass
    return False

def es_booleano(valor):
    return str(valor).strip().lower()in[
        'true', 'false', 'yes', 'no', 'si', '1', '0', 't', 'f'
    ] 
    