# transaccion_poo_v1.py
# OBJETIVO SEMANA 2: Transición de PE a POO - Clases, Objetos y Constructor.

class Transaccion:
    """
    CLASE (MOLDE): Representa una única transacción con sus datos y lógica.
    Resuelve la dispersión de datos del código PE.
    """
    
    # 1. CONSTRUCTOR (__init__): Encapsula los datos dispersos como atributos
    def __init__(self, cliente_id, tipo, monto_str):
        # ATRIBUTOS: Los datos ahora están organizados dentro del objeto (self).
        self.cliente_id = cliente_id.strip()
        self.tipo = tipo.strip()
        
        # Manejo simple de conversión de monto (se mejorará en la Semana 4)
        try:
            self.monto = int(monto_str.strip())
        except ValueError:
            self.monto = 0 # Valor por defecto si no es un número
        
        # Un atributo que almacenará el resultado de la lógica
        self.es_credito = (self.tipo.upper() == "CREDITO")

    # 2. MÉTODO: Reemplaza una función externa de PE (Comportamiento)
    def obtener_informacion_concisa(self):
        """Devuelve una cadena de texto con la información principal de la transacción."""
        estado = "Crédito" if self.es_credito else "Débito"
        return f"[{estado}] ID: {self.cliente_id} | Monto: ${self.monto:,.2f}"

    # Nuevo Método de Lógica (Simula una de las funciones de la Semana 1)
    def verificar_monto_alto(self, umbral):
        """Verifica si el monto de ESTA transacción supera un umbral dado."""
        # La lógica usa el dato encapsulado (self.monto)
        return self.monto > umbral


# --- Funciones de Orquestación POO ---
# NOTA: Estas funciones ahora crean OBJETOS en lugar de Diccionarios.

def leer_y_almacenar_objetos(transacciones: str) -> list:
    """Lee el archivo de texto y retorna una Lista de OBJETOS Transaccion."""
    lista_objetos = []
    
    try:
        with open(transacciones, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')
                
                if len(partes) == 3:
                    # **PUNTO CLAVE:** Instanciación del Objeto
                    nuevo_objeto = Transaccion(
                        cliente_id=partes[0], 
                        tipo=partes[1], 
                        monto_str=partes[2]
                    )
                    lista_objetos.append(nuevo_objeto)
    
    except FileNotFoundError:
        print("\n[ERROR FATAL]: Archivo de datos no encontrado. Asegúrese de que 'transacciones.txt' existe.")
        return []
        
    return lista_objetos


def ejecutar_refactorizacion():
    """
    Función principal que demuestra la organización POO.
    """
    NOMBRE_ARCHIVO = "transacciones.txt"
    UMBRAL_ALTO = 30000

    print("\n--- INICIO PROCESAMIENTO POO (Semana 2) ---")
    
    # 1. Lectura y creación de Objetos
    datos_objetos = leer_y_almacenar_objetos(NOMBRE_ARCHIVO)
    
    if not datos_objetos:
        return
        
    print(f"Total de objetos Transaccion cargados: {len(datos_objetos)}")
    print("-" * 40)
    
    # 2. Demostración de Métodos y Atributos (Interacción con Objetos)
    monto_alto_encontrado = 0
    
    for obj_transaccion in datos_objetos:
        # Uso del Método para obtener información (Comportamiento)
        info = obj_transaccion.obtener_informacion_concisa()
        
        # Uso del Método para aplicar lógica interna
        if obj_transaccion.verificar_monto_alto(UMBRAL_ALTO):
            monto_alto_encontrado += 1
            print(f"ALTO: {info}")
        else:
            print(f"Bajo: {info}")

    print("-" * 40)
    print(f"Resultado: {monto_alto_encontrado} transacciones superan el umbral de ${UMBRAL_ALTO:,.2f}.")
    print("\nDiseño POO exitoso: Datos y Lógica agrupados en Clases.")


# Punto de entrada del programa.
if __name__ == "__main__":
    ejecutar_refactorizacion()