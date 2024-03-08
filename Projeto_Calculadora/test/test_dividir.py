from Calculadora.calculadora import Calculadora

class TestDividir:
    def test_dividir_dois_numeros(self):
        input1 = 20
        input2 = 10
        esperado = 2

        teste_dividir = Calculadora(input1, input2)
        resultado = teste_dividir.dividirDoisNumeros()

        assert resultado == esperado
