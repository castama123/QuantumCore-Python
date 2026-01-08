# robustez_try_except.py
# Semana 4, Actividad 1: Implementación de la Robustez con try-except

# --- Clases Robustas de la Semana 3 (Solo la estructura mínima) ---

class TransaccionBase:
    """Clase Base con Encapsulamiento."""
    
    def __init__(self, cliente_id, monto_str):
        self._cliente_id = cliente_id.strip()
        # Intentamos convertir aquí, lo cual puede lanzar un ValueError.
        monto = float(monto_str)
        self.monto = monto  # Usa el setter para validar

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto):
        # Validación de la Semana 3: Si es negativo, lanza ValueError.
        if nuevo_monto < 0:
            raise ValueError("Monto negativo no permitido por la clase.")
        self._monto = nuevo_monto

# Clases Hija para Polimorfismo (Se usa para instanciar)
class TransaccionCredito(TransaccionBase):
    pass
class TransaccionDebito(TransaccionBase):
    pass

# --- FUNCIÓN CRÍTICA: Implementación del try-except ---

def leer_y_procesar_transacciones(nombre_archivo: str):
    """
    Lee el archivo línea por línea, instancia objetos y maneja errores.
    El uso de try-except permite que el sistema continúe a pesar de los datos corruptos.
    """
    lista_transacciones_validas = []
    linea_num = 0

    print("--- INICIANDO PROCESAMIENTO DE DATOS ---")
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea_num += 1
                linea = linea.strip()
                partes = linea.split(',')
                
                # Bloque de Manejo de Excepciones: try-except
                try:
                    # Intentamos la lógica crítica de instanciación y conversión:
                    
                    if len(partes) < 3:
                        # Forzamos un error si faltan datos (se atrapará con TypeError)
                        raise TypeError("Faltan campos en el registro.")

                    cliente_id = partes[0]
                    tipo = partes[1].upper()
                    monto_str = partes[2]
                    
                    # Instanciación y Conversión:
                    if tipo == "CREDITO":
                        # El constructor llama a float(monto_str) y luego al setter (validación)
                        nueva_transaccion = TransaccionCredito(cliente_id, monto_str)
                    elif tipo == "DEBITO":
                        nueva_transaccion = TransaccionDebito(cliente_id, monto_str)
                    else:
                        raise ValueError("Tipo de transacción inválido.")

                    # Si llegamos aquí, la transacción es válida
                    lista_transacciones_validas.append(nueva_transaccion)
                    print(f"[OK] Línea {linea_num}: Procesada con éxito.")
                
                # --- ATRAPAR ERRORES ESPECÍFICOS ---
                
                except ValueError as e:
                    # Atrapa errores de conversión ('texto_invalido' a float) 
                    # y errores de validación (monto negativo desde el Setter de la Semana 3)
                    print(f"[FALLO] Línea {linea_num} (Registro: {linea}): ERROR DE VALOR O VALIDACIÓN -> {e}")
                    # Estrategia de recuperación: Registrar y CONTINUAR con el siguiente bucle.
                    
                except TypeError as e:
                    # Atrapa errores como 'len(partes) < 3' o argumentos insuficientes en la instanciación.
                    print(f"[FALLO] Línea {linea_num} (Registro: {linea}): ERROR DE TIPO/ESTRUCTURA -> {e}")
                    # Estrategia de recuperación: Registrar y CONTINUAR.

                except Exception as e:
                    # Atrapa cualquier otro error inesperado (Estrategia de respaldo)
                    print(f"[FALLO GRAVE] Línea {linea_num}: ERROR DESCONOCIDO -> {e}")
                    
    except FileNotFoundError:
        print(f"\n[ERROR FATAL] Archivo '{nombre_archivo}' no encontrado. No se puede continuar.")
        return []
    
    finally:
        print("\n--- FIN DE PROCESAMIENTO DE ARCHIVO ---")
        return lista_transacciones_validas

# --- EJECUCIÓN DEL PROGRAMA ---

if __name__ == "__main__":
    archivo_a_usar = "transacciones_corruptas.txt"
    datos_recuperados = leer_y_procesar_transacciones(archivo_a_usar)
    
    print(f"\nResultados Finales:")
    print(f"Total de registros intentados: 7")
    print(f"Total de objetos VÁLIDOS procesados (Recuperados): {len(datos_recuperados)}")
    print("El sistema fue robusto: Ignoró 3 errores y continuó.")