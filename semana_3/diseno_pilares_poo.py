# diseno_pilares_poo.py
# OBJETIVO SEMANA 3: Aplicar Encapsulamiento, Herencia y Polimorfismo.
# NOTA: EL CÓDIGO FALLARÁ SI SE INTENTA ASIGNAR UN MONTO NEGATIVO EN EL MAIN.

class TransaccionBase:
    """
    Clase Padre/Base que contiene la estructura y lógica común 
    a todas las transacciones. Aplica Encapsulamiento.
    """
    
    def __init__(self, cliente_id, monto):
        # ATRIBUTOS PRIVADOS: Se usa el guion bajo (_) para indicar que solo se acceden vía Getters/Setters.
        self._cliente_id = cliente_id.strip()
        self._monto = 0  
        
        # 💡 Uso del setter para aplicar validación inicial al asignar el monto.
        self.monto = monto 
        
    # --- GETTER Y SETTER PARA CONTROL DE ACCESO (Encapsulamiento) ---
    
    @property
    def monto(self):
        """Getter: Permite leer el valor del atributo privado _monto."""
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto):
        """Setter: Controla cómo se asigna el valor, aplicando validación."""
        if nuevo_monto < 0:
            # 🚨 Levantamiento de Excepción (raise): Es inherente al diseño POO proteger el dato.
            # El programa principal (ejecutar_demostracion) debe manejar esta excepción.
            raise ValueError("El monto de la transacción no puede ser negativo. Dato inválido.") 
        self._monto = nuevo_monto

    def obtener_info_base(self):
        """Método base que retorna información común."""
        return f"ID Cliente: {self._cliente_id}, Monto: ${self.monto:,.2f}"

    def calcular_impacto(self):
        """Método Polimórfico: Debe ser sobrescrito por las clases hijas."""
        raise NotImplementedError("El método 'calcular_impacto' debe ser implementado por la clase hija.")


# --- CLASES HIJAS: Reutilización y Comportamiento Único ---

class TransaccionCredito(TransaccionBase):
    """Clase Hija: Hereda la estructura y aplica lógica específica de Crédito."""
    
    def __init__(self, cliente_id, monto, tasa_interes):
        # 🤝 Herencia: Llama al constructor del padre.
        super().__init__(cliente_id, monto)
        self.tasa_interes = tasa_interes

    # 🟣 Polimorfismo: Sobreescribe el método del padre.
    def calcular_impacto(self):
        """Calcula el impacto económico del crédito (ej. el interés generado)."""
        interes_generado = self.monto * (self.tasa_interes / 100)
        return f"Interés Generado: ${interes_generado:,.2f}"

    def obtener_info_base(self):
        # Polimorfismo: Extiende la información del padre.
        info_padre = super().obtener_info_base()
        return f"[CRÉDITO] {info_padre}"


class TransaccionDebito(TransaccionBase):
    """Clase Hija: Hereda la estructura y aplica lógica específica de Débito."""
    COMISION_FIJA = 2500

    # 🟣 Polimorfismo: Sobreescribe el método del padre.
    def calcular_impacto(self):
        """Calcula el impacto económico del débito (ej. la comisión fija)."""
        return f"Comisión Cobrada: ${self.COMISION_FIJA:,.2f}"

    def obtener_info_base(self):
        # Polimorfismo: Extiende la información del padre.
        info_padre = super().obtener_info_base()
        return f"[DÉBITO] {info_padre}"


# --- FUNCIÓN DE EJECUCIÓN Y DEMOSTRACIÓN ---

def ejecutar_demostracion():
    print("--- Demostración de Pilares POO (Semana 3) ---")

    # 🤝 HERENCIA Y ENCAPSULAMIENTO: Creamos objetos válidos
    credito_perez = TransaccionCredito("C009", 1000000, 5.0)
    debito_lopez = TransaccionDebito("C010", 50000, 0)
    
    print("\n" + "=" * 50)
    print("Demostración de Control de Acceso (Encapsulamiento):")
    # Prueba de lectura segura (Getter)
    print(f"Monto (Acceso por Getter): ${credito_perez.monto:,.2f}") 
    print("=" * 50)

    # 🟣 POLIMORFISMO: Recorremos los objetos de forma genérica.
    transacciones = [credito_perez, debito_lopez]

    print("\nDemostración de Polimorfismo y Herencia:")
    for t in transacciones:
        info = t.obtener_info_base() 
        impacto = t.calcular_impacto() 
        
        print(info)
        print(f"  |-> Impacto Único: {impacto}")
        
    print("\n--- PRUEBA DE FALLO CONTROLADO (JUSTIFICACIÓN SEMANA 4) ---")
    # 💥 ESTA LÍNEA PROVOCARÁ UN FALLO (ValueError) Y DETENDRÁ EL PROGRAMA.
    # El código debe fallar aquí para justificar la necesidad de TRY-EXCEPT.
    print("Intentando crear objeto con monto negativo...")
    credito_fallido = TransaccionCredito("C011", -500, 10.0) 
    print("Esta línea nunca debería imprimirse si el Setter funcionó.")
    

# Punto de entrada del programa.
if __name__ == "__main__":
    ejecutar_demostracion()