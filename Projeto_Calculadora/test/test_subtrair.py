from Calculadora.calculadora import Calculadora

class TestSubtrair:
    def test_subtrair_dois_numeros(self):
        input1 = 20
        input2 = 10
        esperado = 10

        teste_subtrair = Calculadora(input1, input2)
        resultado = teste_subtrair.subtrairDoisNumeros()

        assert resultado == esperado

