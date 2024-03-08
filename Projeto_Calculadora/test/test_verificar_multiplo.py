from Calculadora.calculadora import Calculadora

class TestVerificarMultiplo:
    def test_verificar_se_um_numero_e_multiplo_de_cinco(self):
        input1 = 20
        input2 = 10
        esperado = True

        verificar_multiplo = Calculadora(input1, input2)
        resultado = verificar_multiplo.verificarMultiploDeCinco()

        assert resultado == esperado

