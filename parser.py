def interpretar_expresion(expresion):
    operadores = ['+', '-', '*', '/', '^']
    for operador in operadores:
        if operador in expresion:
            partes = expresion.split(operador)
            try:
                valores = [float(p.strip()) for p in partes]
                return valores, operador
            except ValueError:
                return None
    return None
