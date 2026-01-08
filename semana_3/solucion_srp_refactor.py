# solucion_srp_refactor.py
# SOLUCIÓN DE DISEÑO: Aplicación del Principio de Responsabilidad Única (SRP)

# ----------------------------------------------------------------------
# 1. CLASE/MÓDULO: VALIDADOR (Única Responsabilidad: Verificar Reglas)
# ----------------------------------------------------------------------
class ValidadorDatos:
    """Responsabilidad Única: Asegurar que los datos de entrada cumplan las precondiciones."""
    
    @staticmethod
    def validar(transaccion) -> bool:
        """Devuelve True si los datos básicos de la transacción son válidos."""
        if transaccion.monto <= 0:
            print("[VALIDACIÓN] Monto inválido. Rechazado.")
            return False
        if not transaccion.cliente_activo:
            print("[VALIDACIÓN] Cliente inactivo. Rechazado.")
            return False
        return True

# ----------------------------------------------------------------------
# 2. CLASE/MÓDULO: MOTOR DE LÓGICA DE NEGOCIO (Única Responsabilidad: Cálculo)
# ----------------------------------------------------------------------
class MotorCalculoRiesgo:
    """Responsabilidad Única: Aplicar las reglas de negocio y calcular la puntuación."""
    
    @staticmethod
    def calcular(transaccion):
        """Calcula la puntuación de riesgo y devuelve el resultado y el mensaje."""
        puntuacion = 50 
        
        if transaccion.tipo == "CREDITO" and transaccion.monto > 500000:
            puntuacion = 80
            mensaje = "APROBADO: Crédito de alto valor."
        elif transaccion.tipo == "DEBITO":
            puntuacion = 100
            mensaje = "APROBADO: Débito estándar."
        else:
            mensaje = "APROBADO: Riesgo bajo."
            
        return puntuacion, mensaje

# ----------------------------------------------------------------------
# 3. CLASE/MÓDULO: FORMATEADOR DE REPORTE (Única Responsabilidad: Salida)
# ----------------------------------------------------------------------
class FormateadorReporte:
    """Responsabilidad Única: Dar formato a la salida de la información (ej. Texto, JSON)."""
    
    @staticmethod
    def generar_reporte_texto(transaccion, puntuacion, estado):
        return (
            f"\n--- REPORTE OFICIAL (SRP) ---\n"
            f"Tipo: {transaccion.tipo}\n"
            f"Estado: {estado}\n"
            f"Puntuación final: {puntuacion}\n"
        )

# ----------------------------------------------------------------------
# 4. CLASE PRINCIPAL REFACTORIZADA (Gestor, solo coordina las responsabilidades)
# ----------------------------------------------------------------------
class Transaccion:
    """
    Clase Principal: Simplificada para manejar solo sus atributos, usando 
    otros módulos (Validador, Motor) para el comportamiento.
    """
    def __init__(self, monto: float, cliente_activo: bool, tipo: str):
        self.monto = monto
        self.cliente_activo = cliente_activo
        self.tipo = tipo

    def procesar(self):
        # 1. Coordina la Validación
        if not ValidadorDatos.validar(self):
            return "Falló la Validación"

        # 2. Coordina el Cálculo
        puntuacion, estado = MotorCalculoRiesgo.calcular(self)

        # 3. Coordina el Reporte
        reporte = FormateadorReporte.generar_reporte_texto(self, puntuacion, estado)
        print(reporte)
        return "Procesamiento Exitoso"


# --- EJECUCIÓN DE PRUEBA Y DEMOSTRACIÓN DEL SRP ---
def ejecutar_prueba_refactor():
    print("--- DEMOSTRACIÓN DE SRP (Semana 3) ---")
    
    # Caso 1: Aprobado estándar
    trans_ok = Transaccion(monto=100000, cliente_activo=True, tipo="DEBITO")
    trans_ok.procesar()
    
    # Caso 2: Rechazado (monto cero)
    print("\n" + "="*30)
    trans_fail = Transaccion(monto=0, cliente_activo=True, tipo="CREDITO")
    trans_fail.procesar()
    
    # 💡 BENEFICIO CLAVE: Si se cambia el formato del reporte (FormateadorReporte), 
    # la lógica de cálculo (MotorCalculoRiesgo) no necesita ser modificada.

if __name__ == "__main__":
    ejecutar_prueba_refactor()