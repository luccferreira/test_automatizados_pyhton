from Calculadora.calculadora import Calculadora

class TestMultiplicar:
    def test_multiplicar_dois_numeros(self):
        input1 = 10
        input2 = 20
        esperado = 200

        teste_multiplicar = Calculadora(input1, input2)
        resultado = teste_multiplicar.multiplicarDoisNumeros()

        assert resultado == esperado

        