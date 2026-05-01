import re 
from typing import Dict,List
from datetime import datetime

Depa_validos = [ 'VEN', 'ADM', 'TEC', 'LOG', 'RHH']
Series_validas = [ 'A', 'B', 'C', 'D', 'E']

def sugerir_correccion(codigo: str) -> str:
    sugerido = codigo.upper()

    if codigo != sugerido:
        return sugerido
    
    return "Sin sugerencia"

def validar_fecha_real(anio: int, mes: int, dia: int ) -> bool:
    try:
        datetime(anio, mes, dia)
        return True
    except ValueError:
        return False

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

        if 2020 <= int(anio) <= 2030 and validar_fecha_real(int(anio), int(mes), int(dia)):
            resultado["fecha"] = f"{anio}-{mes}-{dia}"
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
        dept, num = match.groups()

        if dept in Depa_validos and not num.sttartswith('0'):
            resultado["valido"] = True
            resultado["departamento"] = dept
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
        serie ,numero = match.groups()

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
        resultado["sugerencia"] = sugerir_correccion(codigo)
        return resultado
    
    resultado["valido"] = res["valido"]
    resultado["detalles"] = {k: v for k,v in res.items() if k != "valido" }

    if not resultado["valido"]:
        resultado["sugerencia"] = sugerir_correccion(codigo)

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

    
def exportar_resultados(reporte: Dict, archivo:str) -> None:
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write("codigo,tipo,valido,sugerencia\n")

        for r in reporte["detalle"]:
            fila= f"{r['codigo']},{r['tipo']},{r['valido']},{r.get('sugerencia','')}\n"

    print(f"Archivo exportado: {archivo}")

def mostrar_resultado(resultado: Dict) -> None:
    estado = "OK" if resultado["valido"] else "ERROR"
    print(f"{estado} {resultado['codigo']:<30} | Tipo: {resultado['tipo']:<12}")

    if resultado["valido"] and resultado["detalles"]:
        detalles = ", ".join(f"{k}: {v}" for k,v in resultado["detalles"].items() if v)
        print(f"    -> {detalles}")

    if not resultado["valido"] and resultado["sugerencia"]:
        print(f"    ->Sugerencia: {resultado['sugerencia']}")

def mostrar_reporte(reporte: Dict) -> None:
    print("=" * 60)
    print("REPORTE DE VALIDACION")
    print("=" * 60)

    print(f"\nTotal: {reporte['total']}")
    print(f"Validos: {reporte['validos']}")
    print(f"Invalidos: {reporte['invalidos']}")

    print("\nPor tipo:")
    for tipo, stats in reporte["por_tipo"].items():
        if stats["total"] > 0:
            print(f"{tipo}: {stats['validos']}/{stats['total']}")

    print("=" * 60)

if __name__ == "__main__":
    CODIGOS_PRUEBA = [
        "TEC-0001-MX",
        "ALI-9999-US",
        "ROB-1234-CA",
        "tec-0001-MX",
        "TEC-001-MX",
        "TECH-0001-MX",

        "ENV-2024-03-15-001234",
        "ENV-2025-12-01-999999",
        "ENV-2019-03-15-001234",
        "ENV-2024-13-15-001234",
        "ENV-2024-03-32-001234",

        "EMP-VEN-1234",
        "EMP-TEC-9999",
        "EMP-ADM-1000",
        "EMP-VEN-0123",
        "EMP-XXX-1234",
        "EMP-VEN-123",

        "FAC-A-123456",
        "FAC-E-000001",
        "FAC-B-999999",
        "FAC-F-123456",
        "FAC-A-12345",
        "FAC-a-123456",

        "XXX-1234",
        "RANDOM-CODE"
    ]

    reporte = procesar_lote(CODIGOS_PRUEBA)
    mostrar_reporte(reporte)