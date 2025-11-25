from calculadora import Calculadora
from parser import interpretar_expresion

def main():
    calc = Calculadora()
    print("\nCalculadora avanzada con POO. Escribe 'salir' para terminar o 'historial' para ver operaciones.\n")

    while True:
        entrada = input("Ingresa la operación (ejemplo 5+5+10 o 2^3): ")

        if entrada.strip().lower() == "salir":
            print("Hasta pronto")
            break

        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue

        resultado = interpretar_expresion(entrada)
        if not resultado:
            print("Expresión inválida. Usa el formato correcto.\n")
            continue

        valores, operador = resultado
        calc.set_valores(valores)

        if operador == '+':
            print("Resultado:", calc.sumar())
        elif operador == '-':
            print("Resultado:", calc.restar())
        elif operador == '*':
            print("Resultado:", calc.multiplicar())
        elif operador == '/':
            print("Resultado:", calc.dividir())
        elif operador == '^':
            try:
                print("Resultado:", calc.potencia())
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()
