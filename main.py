from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Dividir dos números")
        print("5. Suma avanzada (N números)")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", sumar(a, b))
        elif opcion == '2':
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", restar(a, b))
        elif opcion == '3':
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", multiplicar(a, b))
        elif opcion == '4':
            a = float(input("Dividendo: "))
            b = float(input("Divisor: "))
            try:
                print("Resultado:", dividir(a, b))
            except ZeroDivisionError:
                print("Error: No se puede dividir entre cero.")
        elif opcion == '5':
            numeros = input("Ingresa los números separados por espacios: ").split()
            numeros = [float(num) for num in numeros]
            print("Resultado:", suma_avanzada(numeros))
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
