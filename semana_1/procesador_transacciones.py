# procesador_transacciones.py
# OBJETIVO SEMANA 1: Demostrar Programación Estructurada (PE) Limpia
# y dominio de Listas, Diccionarios y Manejo de Archivos.

def leer_y_almacenar_datos(transacciones: str) -> list:
    """
    FUNCIÓN 1: Lee datos desde un archivo de texto y los almacena en una
    Lista de Diccionarios.
    
    NOTA: Si el archivo no existe, esta función provocará un error de
    tiempo de ejecución (FileNotFoundError), el cual es esperado en PE básica.
    """
    lista_transacciones = []
    
    # Uso de la función OPEN() directamente.
    with open(transacciones, 'r') as archivo:
        for linea in archivo:
            # Separar y limpiar la línea
            partes = linea.strip().split(',')
            
            if len(partes) == 3:
                # Conversión a Diccionario y a tipo numérico para el monto.
                try:
                    monto_numerico = int(partes[2].strip())
                except ValueError:
                    # Si el monto no es un número válido, lo ponemos en cero.
                    monto_numerico = 0 
                
                transaccion_dict = {
                    'cliente_id': partes[0].strip(),
                    'tipo': partes[1].strip(),
                    'monto': monto_numerico
                }
                lista_transacciones.append(transaccion_dict)
    
    return lista_transacciones

def calcular_monto_total(lista_transacciones: list) -> int:
    """
    FUNCIÓN 2: Calcula la suma total de los montos usando un bucle FOR.
    Demuestra la habilidad de Iteración.
    """
    monto_total = 0
    # Iteración sobre la Lista de Diccionarios
    for transaccion in lista_transacciones:
        monto_total += transaccion['monto']
    return monto_total

def filtrar_por_tipo(lista_transacciones: list, tipo_filtro: str) -> list:
    """
    FUNCIÓN 3: Filtra las transacciones y devuelve una nueva lista con solo el tipo.
    Demuestra la habilidad de Selección (IF) dentro de la Iteración.
    """
    transacciones_filtradas = []
    
    for transaccion in lista_transacciones:
        # Uso de IF (Selección)
        if transaccion['tipo'].upper() == tipo_filtro.upper():
            transacciones_filtradas.append(transaccion)
            
    return transacciones_filtradas

def ejecutar_sistema():
    """
    FUNCIÓN PRINCIPAL: Orquesta todas las operaciones (modularidad de la PE).
    """
    NOMBRE_ARCHIVO = "transacciones.txt"
    
    print("\n--- INICIO PROCESAMIENTO PE LIMPIO ---")
    
    # 1. Lectura y almacenamiento (Si el archivo no existe, el programa FALLA)
    datos_cargados = leer_y_almacenar_datos(NOMBRE_ARCHIVO)
    
    print(f"Total de registros cargados: {len(datos_cargados)}")
    
    # 2. Cálculo del total
    total = calcular_monto_total(datos_cargados)
    print(f"\nMonto Total de todas las transacciones: ${total:,.2f}")
    
    # 3. Filtrado
    TIPO_BUSCADO = "CREDITO"
    transacciones_credito = filtrar_por_tipo(datos_cargados, TIPO_BUSCADO)
    
    print(f"\n--- Resultado del Filtrado ---")
    print(f"Transacciones de {TIPO_BUSCADO} encontradas: {len(transacciones_credito)}")
    for t in transacciones_credito:
        print(f"  > Cliente {t['cliente_id']} / Monto: ${t['monto']:,.2f}")
        
    print("\n--- FIN PROCESAMIENTO ---")


# Punto de entrada (main) del programa.
if __name__ == "__main__":
    ejecutar_sistema()