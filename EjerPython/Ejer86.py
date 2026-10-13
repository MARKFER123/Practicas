class AnalizadorParesImpares:
    def __init__(self):
        self.pares = 0
        self.impares = 0

    def procesar(self):
        print("Ejercicio 86: Pares e Impares")
        for i in range(1, 11):
            n = int(input("Ingresa el numero: "))
            if n % 2 == 0:
                self.pares += 1
            else:
                self.impares += 1
        print("Pares:", self.pares)
        print("Impares:", self.impares)

if __name__ == "__main__":
    app = AnalizadorParesImpares()
    app.procesar()