from Calculadora.calculadora import Calculadora

class TestReturnAtributosConta:
    def test_return_atributos_da_conta(self):
        input1 = 10
        input2 = 20
        esperado = 10, 20

        return_atributos = Calculadora(input1, input2)
        resultado = return_atributos.imprimirAtributosOperaçãoNumerica()

        assert resultado == esperado
