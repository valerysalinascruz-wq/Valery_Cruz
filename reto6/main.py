import re 
from typing import Dict,List

Depa_validos = [ 'VEN', 'ADM', 'TEC', 'LOG', 'RHH']
Series_validas = [ 'A', 'B', 'C', 'D', 'E']

#validar producto 
def validar_producto(codigo: str) -> Dict:
    resultado ={
        "valido": False,
        "categoria": None,
        "numero": None,
        "pais": None
    }
    patron = r'^([A-Z]{3})-(/d{4})-([A-Z]{2})$'
    match = re.match(patron, codigo)

    if match:
        resultado["valido"] = True
        resultado["categoria"] = match.group(1)
        resultado["numero"] = match.group(2)
        resultado["pais"]= match.group(3)

    return resultado

#validar envio 
def validar_envio(codigo: str) -> Dict:
    resultado = {
        "valido": False,
        "fehca": None,
        "secuencial": None
    }

    patron= r'^ENV-(/d{4})-(/d{2})-(/d{2})-(/d{6})$'
    match =re.match(patron, codigo)

    if match:
        anio=int(match.group(1))
        mes=int(match.group(2))
        dia=int(match.group(3))
        sec=match.group(4)

        if 2020 <= anio <= 2030 and 1 <= mes <= 12 and 1 <= dia <= 31:
            resultado["valido"] = True
            resultado["fecha"] = f"{anio}-{mes:02d}-{dia:02d}"
            resultado["secuencial"]= sec

    return resultado

#validar_empleado
def validar_empleado(codigo: str) -> Dict:
    resultado = {
        "valido":False,
        "departamento": None,
        "numero": None
    }

    patron = r'^EMP-([A-Z]{3})-(/d{4})$'
    match = re.match(patron, codigo)

    if match:
        depto = match.group(1)
        num = match.group(2)

        if depto in Depa_validos and not num.sttartswith('0'):
            resultado["valido"] = True
            resultado["departamento"] = depto
            resultado["numero"] =  num 

    return resultado

#validar_factura

#validador universal

#procesamiento por lotes
