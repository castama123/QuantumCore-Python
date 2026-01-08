import json

class Transaccion:
    """Clase simple que simula el objeto POO a guardar."""
    def __init__(self, cliente_id: str, tipo: str, monto: float):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        # Método para imprimir el objeto de forma legible
        return f"Transacción [{self.tipo}] - ID: {self.cliente_id}, Monto: ${self.monto:,.2f}"

    def aplicar_regla(self):
        """Método de ejemplo para demostrar que es un objeto funcional."""
        if self.monto > 500000:
            return "APROBADO para auditoría de alto valor."
        return "APROBADO estándar."

# --- PROCESO DE SERIALIZACIÓN (OBJETO A JSON) ---

def serializar_objeto(obj_transaccion: Transaccion) -> str:
    """Convierte el objeto POO a una cadena de texto JSON."""
    
    print("\n--- INICIANDO SERIALIZACIÓN (POO -> JSON) ---")
    
    # 1. Objeto a Diccionario (Extracción de atributos)
    # El diccionario es el formato intermedio que JSON entiende.
    datos_diccionario = {
        "cliente_id": obj_transaccion.cliente_id,
        "tipo": obj_transaccion.tipo,
        "monto": obj_transaccion.monto
    }
    print(f"Paso 1: Objeto convertido a Diccionario: {datos_diccionario}")
    
    # 2. Diccionario a Cadena JSON
    cadena_json_final = json.dumps(datos_diccionario, indent=4) 
    print("Paso 2: Diccionario convertido a Cadena JSON (Lista para guardar o enviar).")
    
    return cadena_json_final

# --- PROCESO DE DESERIALIZACIÓN (JSON A OBJETO) ---

def deserializar_json(cadena_json: str) -> Transaccion:
    """Convierte la cadena de texto JSON de vuelta a un objeto POO."""
    
    print("\n--- INICIANDO DESERIALIZACIÓN (JSON -> POO) ---")
    
    # 3. Cadena JSON a Diccionario
    diccionario_recuperado = json.loads(cadena_json)
    print(f"Paso 3: Cadena JSON convertida a Diccionario: {diccionario_recuperado}")
    
    # 4. Reconstrucción del Objeto POO (Instanciación)
    # Usamos las claves del Diccionario para llamar al constructor
    objeto_recuperado = Transaccion(
        cliente_id=diccionario_recuperado["cliente_id"],
        tipo=diccionario_recuperado["tipo"],
        monto=diccionario_recuperado["monto"]
    )
    print("Paso 4: Objeto POO reconstruido exitosamente.")
    
    return objeto_recuperado

# --- FUNCIÓN DE PRUEBA Y VERIFICACIÓN ---

if __name__ == "__main__":
    # A. Objeto original en memoria
    transaccion_original = Transaccion("C987", "CREDITO", 750000.50)
    print(f"1. Objeto Inicial: {transaccion_original}")
    print(f"   Lógica inicial: {transaccion_original.aplicar_regla()}")
    
    # B. Serialización
    json_resultante = serializar_objeto(transaccion_original)
    
    print("\n--- RESULTADO DE LA SERIALIZACIÓN ---")
    print(json_resultante)
    print("-------------------------------------")
    
    # C. Deserialización
    transaccion_recuperada = deserializar_json(json_resultante)
    
    # D. Verificación: Asegurarse de que el objeto recuperado es funcional
    print("\n--- VERIFICACIÓN DEL OBJETO RECUPERADO ---")
    print(f"Objeto Final: {transaccion_recuperada}")
    print(f"El objeto final es funcional: {transaccion_recuperada.aplicar_regla()}")
    
    # Prueba de que la serialización/deserialización fue exitosa
    if transaccion_original.cliente_id == transaccion_recuperada.cliente_id and \
       transaccion_original.monto == transaccion_recuperada.monto:
        print("\n✅ Verificación Final: Los datos se conservaron y el objeto fue reconstruido correctamente.")
    else:
        print("\n❌ Verificación Fallida: Los datos del objeto original y el recuperado no coinciden.")