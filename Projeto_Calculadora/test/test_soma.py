from Calculadora.calculadora import Calculadora

class TestSoma:
    def test_soma_dois_numeros(self):
        input1 = 10
        input2 = 20
        esperado = 30

        teste_soma = Calculadora(input1, input2)
        resultado = teste_soma.somarDoisNumeros()

        assert resultado == esperado