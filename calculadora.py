class Calculadora:
    def __init__(self):
        # Lista flexible de valores
        self._valores = []
        self._historial = []

    # --- MÉTODOS DE CONFIGURACIÓN ---
    def set_valores(self, valores):
        # Validamos que todos sean números
        if all(isinstance(v, (int, float)) for v in valores):
            self._valores = valores
        else:
            raise ValueError("Todos los valores deben ser números")

    # --- OPERACIONES ---
    def sumar(self):
        resultado = sum(self._valores)
        self._registrar_operacion('+', resultado)
        return resultado

    def restar(self):
        if not self._valores:
            return 0
        resultado = self._valores[0]
        for v in self._valores[1:]:
            resultado -= v
        self._registrar_operacion('-', resultado)
        return resultado

    def multiplicar(self):
        resultado = 1
        for v in self._valores:
            resultado *= v
        self._registrar_operacion('*', resultado)
        return resultado

    def dividir(self):
        if not self._valores:
            return 0
        resultado = self._valores[0]
        try:
            for v in self._valores[1:]:
                if v == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero")
                resultado /= v
            self._registrar_operacion('/', resultado)
            return resultado
        except ZeroDivisionError as e:
            print(e)
            return None

    def potencia(self):
        if len(self._valores) != 2:
            raise ValueError("La operación de potencia requiere exactamente 2 valores")
        base, exponente = self._valores
        resultado = base ** exponente
        self._registrar_operacion('^', resultado)
        return resultado

    # --- REGISTRO DE OPERACIONES ---
    def _registrar_operacion(self, operador, resultado):
        expresion = f" {operador} ".join(map(str, self._valores))
        self._historial.append({
            'operacion': f"{expresion}",
            'resultado': resultado
        })

    # --- MOSTRAR HISTORIAL ---
    def ver_historial(self):
        if not self._historial:
            print("No hay operaciones en el historial")
            return
        print("\n--- Historial de Operaciones ---")
        for i, operacion in enumerate(self._historial, 1):
            print(f"{i}. {operacion['operacion']} = {operacion['resultado']}")
