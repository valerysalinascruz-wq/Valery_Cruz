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
def validar_factura(codigo: str) -> Dict:
    resultado ={
        "valido": False,
        "serie": None,
        "numero": None
    }

    patron = r'^FAC-([A-Z])-(/d{6})$'
    match = re.match(patron, codigo)

    if match:
        serie = match.group(1)
        numero = match.group(2)

        if serie in Series_validas:
            resultado["valido"] = True
            resultado["serie"] = serie
            resultado["numero"] = numero

    return resultado 

#validador universal
def validar_codigo(codigo: str) -> Dict:
    resultado ={
        "codigo": codigo,
        "tipo": "desconocido",
        "valido": False,
        "detalles": {}
    }
    if codigo.startswith("ENV"):
        resultado["tipo"] = "envio"
        res = validar_envio(codigo)

    elif codigo.startswith("EMP"):
        resultado["tipo"] = "empleado"
        res = validar_empleado(codigo)

    elif codigo.startswith("FAC"):
        resultado["tipo"] = "factura"
        res = validar_factura(codigo)

    elif re.match(r'^[A-Z]{3}-',codigo):
        resultado["tipo"] = "producto"
        res = validar_producto(codigo)

    else:
        return resultado
    
    resultado["valido"] = res["valido"]
    resultado["detalles"] = {k: v for k,v in res.items() if k != "valido" and v is not None}

    return resultado
    

#procesamiento por lotes
def procesar_lotes(codigos: List[str]) -> Dict:
    resultado = {
        "total": len(codigos),
        "validos": 0,
        "invalidos": 0,
        "por_tipo":{
            "producto": {"total": 0, "validos": 0},
            "envio": {"total": 0, "validos": 0},
            "empleado": {"total": 0, "validos": 0},
            "fatura": {"total": 0, "validos": 0},
            "desconocido": {"total": 0, "validos": 0}
        },
        "detalle": []
    }

    for codigo in codigos:
        res = validar_codigo(codigo)
        resultado["detalles"].append(res)

        tipo = res["tipo"]
        resultado["por_tipo"][tipo]["total"] += 1

        if res["valido"]:
            resultado["validos"] += 1
            resultado["por_tipo"][tipo]["validos"] += 1
        else:
            resultado["invalidos"] += 1

    return resultado
