import sys
'''
    """Convierte Fahrenheit a Celsius."""
'''
def convertir_a_Cel(valor,unidad):
    if unidad == 'F':
        return (valor - 32) * 5 / 9
    return valor

'''
    """Clasifica la temperatura."""
'''
def clasf_temp(temp):
    if temp < 0 :
        return "Congelante"
    elif temp <= 15:
        return "Frio"
    elif temp <= 25:
        return "Templado"
    elif temp <= 35:
        return "Calido"
    else:
        return "Extremo"
     
def main():

    
    # Encabezado
    
    print("ciudad,temperatura_celsius,clasificacion")
    primera_linea = True
    for linea in sys.stdin:
        linea = linea.strip()

    #saltar encabezado    
        if primera_linea:
            primera_linea = False
            continue

    # Saltar lineas vacias
        if not linea:
            continue
        datos = linea.split(',')

    # Validad que tenga 3 columnas
        if len(datos) != 3:
            continue
        ciudad = datos[0].strip()
        unidad = datos[2].strip().upper()

    # Validar unidad
        if unidad not in ['C', 'F']:
            continue

    # Convertir temperatura
        try:
            temp = float(datos[1])
        except ValueError:
            continue 
        
    # Convertir a Celsius
        temp_cel = convertir_a_Cel(temp,unidad)

    # Clasificar y imprimir
        estado_de_cli= clasf_temp(temp_cel)
        print(f"{ciudad},{temp_cel:.1f},{estado_de_cli}")
 

if __name__ == "__main__":
    main()
