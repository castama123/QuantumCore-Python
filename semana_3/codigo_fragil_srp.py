# codigo_fragil_srp.py
# CLASE MONOLÍTICA QUE VIOLA EL PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
# Tarea: Identificar y proponer la división de responsabilidades.

class GestorTransaccionPrincipal:
    
    def __init__(self, monto: float, cliente_activo: bool, tipo: str):
        self.monto = monto
        self.cliente_activo = cliente_activo
        self.tipo = tipo
        self.resultado_riesgo = ""
        self.puntuacion = 0

    def procesar_y_validar_y_reportar(self):
        """
        MÉTODO PROBLEMÁTICO: Contiene las tres responsabilidades que violan el SRP:
        1. Validación de Precondiciones
        2. Lógica de Negocio (Puntuación)
        3. Formateo de Salida
        """
        
        # 1. VALIDACIÓN DE PRECONDICIONES (Responsabilidad de una clase Validadora)
        if self.monto <= 0:
            self.resultado_riesgo = "RECHAZADO: Monto inválido."
            print(f"[LOG] Fallo en validación: {self.resultado_riesgo}")
            return False

        if not self.cliente_activo:
            self.resultado_riesgo = "RECHAZADO: Cliente inactivo."
            print(f"[LOG] Fallo en validación: {self.resultado_riesgo}")
            return False

        # 2. PROCESAMIENTO DE LÓGICA DE NEGOCIO (Responsabilidad del Motor de Cálculo)
        if self.tipo == "CREDITO" and self.monto > 500000:
            self.puntuacion = 80
            mensaje_logica = "APROBADO: Crédito de alto valor."
        elif self.tipo == "DEBITO":
            self.puntuacion = 100
            mensaje_logica = "APROBADO: Débito estándar."
        else:
            self.puntuacion = 50
            mensaje_logica = "APROBADO: Riesgo bajo."
            
        self.resultado_riesgo = mensaje_logica

        # 3. REPORTE/SALIDA (Responsabilidad de un Formateador)
        reporte = (
            f"--- REPORTE OFICIAL ---\n"
            f"Tipo: {self.tipo}\n"
            f"Estado: {self.resultado_riesgo}\n"
            f"Puntuación final: {self.puntuacion}\n"
        )
        print(reporte)
        return True

def ejecutar_prueba_srp():
    # Caso 1: Aprobado estándar
    trans_ok = GestorTransaccionPrincipal(monto=100000, cliente_activo=True, tipo="DEBITO")
    trans_ok.procesar_y_validar_y_reportar()

if __name__ == "__main__":
    ejecutar_prueba_srp()