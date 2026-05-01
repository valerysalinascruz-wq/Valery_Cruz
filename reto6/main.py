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

#validar_empleado

#validar_factura

#validador universal

#procesamiento por lotes
