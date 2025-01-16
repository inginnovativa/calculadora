def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
    
def main():
    print("Calculadora Básica")
    print("Suma de 3 y 5:", suma(3, 5))
    print("Resta de 10 y 4:", resta(10, 4))

if __name__ == "__main__":
    main()