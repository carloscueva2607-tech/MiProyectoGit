
def mostrar_menu():
    """Muestra las opciones de la calculadora."""
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")


def leer_opcion():
    """Solicita la opción al usuario."""
    return int(input("Elige una opción: "))


def leer_numero(mensaje):
    """Solicita un número al usuario."""
    return float(input(mensaje))


def calcular_suma(num1, num2):
    """Suma dos números."""
    return num1 + num2


def calcular_resta(num1, num2):
    """Resta dos números."""
    return num1 - num2


def calcular_multiplicacion(num1, num2):
    """Multiplica dos números."""
    return num1 * num2


def calcular_division(num1, num2):
    """Divide dos números evitando dividir entre cero."""
    if num2 == 0:
        print("No se puede dividir entre cero")
        return None
    return num1 / num2


def calcular_potencia(base, exponente):
    """Calcula una potencia."""
    return base ** exponente


def calcular_raiz_cuadrada(numero):
    """Calcula la raíz cuadrada de un número no negativo."""
    if numero < 0:
        print("No se puede calcular la raíz cuadrada de un número negativo")
        return None
    return numero ** 0.5


def ejecutar_calculadora():
    """Controla el funcionamiento de la calculadora."""
    operaciones = {
        1: ("Suma", calcular_suma, 2),
        2: ("Resta", calcular_resta, 2),
        3: ("Multiplicación", calcular_multiplicacion, 2),
        4: ("División", calcular_division, 2),
        5: ("Potencia", calcular_potencia, 2),
        6: ("Raíz cuadrada", calcular_raiz_cuadrada, 1)
    }

    opcion_usuario = 0

    while opcion_usuario != 7:
        mostrar_menu()
        opcion_usuario = leer_opcion()

        if opcion_usuario == 7:
            print("Programa finalizado")

        elif opcion_usuario not in operaciones:
            print("Opción no válida")

        else:
            nombre_operacion, funcion, cantidad_numeros = operaciones[opcion_usuario]

            if cantidad_numeros == 1:
                numero = leer_numero("Ingrese el número: ")
                resultado = funcion(numero)
            else:
                num1 = leer_numero("Ingrese el primer número o la base: ")
                num2 = leer_numero("Ingrese el segundo número o el exponente: ")
                resultado = funcion(num1, num2)

            if resultado is not None:
                print(nombre_operacion + " - Resultado:", resultado)


ejecutar_calculadora()