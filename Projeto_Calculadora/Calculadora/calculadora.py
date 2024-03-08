
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def imprimirAtributosOperaçãoNumerica(self):
        return self.numero1, self.numero2

    def somarDoisNumeros(self):
        return self.numero1 + self.numero2

    def multiplicarDoisNumeros(self):
        return self.numero1 * self.numero2

    def dividirDoisNumeros(self):
        return self.numero1 / self.numero2

    def subtrairDoisNumeros(self):
        return self.numero1 - self.numero2

#% retorna o resto da divisão do primeiro número pelo segundo
    def verificarMultiploDeCinco(self):
        if self.numero1 % 5 == 0:
            return True
        return False

