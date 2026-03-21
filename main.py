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
    '''
    # Leer y descartar encabezado de entrada
    '''
    print("ciudad,temperatura_celsius,clasificacion")
    primera_linea = True
    '''
    
    # Imprimir encabezado de salida

        
        # Saltar encabezado

        # Saltar lineas vacias

        
        # Separar campos

        
        # Validar unidad

        # Convertir temperatura

             # Ignorar si no es numero
        
        # Convertir a Celsius

        
        # Clasificar y imprimir
 
'''

if __name__ == "__main__":
    main()
print(convertir_a_Cel(50,'F'))
print(clasf_temp(10)) 