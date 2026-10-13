class AnalizadorMinMax:
    def __init__(self):
        self.numeros = []

    def procesar(self):
        print("Ejercicio 87: Mayor y Menor")
        for i in range(1, 11):
            n = int(input("Ingresa el numero: "))
            self.numeros.append(n)

        print("Mayor:", max(self.numeros))
        print("Menor:", min(self.numeros))


if __name__ == "__main__":
    app = AnalizadorMinMax()
    app.procesar()