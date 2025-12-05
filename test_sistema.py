import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from service.ValidadorDados import ValidadorDados
from service.CalculadoraIMC import CalculadoraIMC


class TestValidadorDados(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorDados()

    def test_AC1_RegistrarTodasCircunferencias(self):
        circunferencias = {
            'torax': 95.0,
            'braco_direito_contraido': 35.5,
            'braco_esquerdo_contraido': 35.0,
            'braco_direito_relaxado': 32.5,
            'braco_esquerdo_relaxado': 32.0,
            'abdomen': 85.0,
            'cintura': 80.0,
            'quadril': 95.0,
            'antebraco_direito': 28.5,
            'antebraco_esquerdo': 28.0,
            'coxa_direita': 55.0,
            'coxa_esquerda': 54.5,
            'panturrilha_direita': 38.0,
            'panturrilha_esquerda': 37.5,
            'escapular': 20.0
        }
        for campo, valor in circunferencias.items():
            valido, erro = self.validador._validar_circunferencia(valor, campo)
            self.assertTrue(valido)
            self.assertIsNone(erro)

    def test_AC2_ValoresNumericosPositivosComDuasCasasDecimais(self):
        for valor in [30.00, 35.50, 40.99, 28.5, 33.0]:
            valido, erro = self.validador._validar_circunferencia(valor, "torax")
            self.assertTrue(valido, f"Valor {valor} deveria ser válido")
        
        valido, erro = self.validador._validar_circunferencia(-30.0, "torax")
        self.assertFalse(valido)
        self.assertIn("positivo", erro.lower())

    def test_AC7_ValidacaoPercentualGordura(self):
        for valor_valido in [3.0, 70.0]:
            valido, erro = self.validador._validar_percentual_gordura(valor_valido)
            self.assertTrue(valido, f"Percentual {valor_valido}% deveria ser válido")
        
        casos_invalidos = [(2.5, "3%"), (75.0, "70%")]
        for valor_invalido, mensagem_esperada in casos_invalidos:
            valido, erro = self.validador._validar_percentual_gordura(valor_invalido)
            self.assertFalse(valido, f"Percentual {valor_invalido}% deveria ser inválido")
            self.assertIn(mensagem_esperada, erro)

    def test_AC8_ValidacaoPeso(self):
        for peso_valido in [20.0, 180.0]:
            valido, erro = self.validador.validarPeso(peso_valido)
            self.assertTrue(valido, f"Peso {peso_valido}kg deveria ser válido")
        
        casos_invalidos = [(19.0, "20 kg"), (185.0, "180 kg")]
        for peso_invalido, mensagem_esperada in casos_invalidos:
            valido, erro = self.validador.validarPeso(peso_invalido)
            self.assertFalse(valido, f"Peso {peso_invalido}kg deveria ser inválido")
            self.assertIn(mensagem_esperada, erro)

    def test_AC9_ValidacaoAltura(self):
        for altura_valida in [1.00, 2.50]:
            valido, erro = self.validador.validarAltura(altura_valida)
            self.assertTrue(valido, f"Altura {altura_valida}m deveria ser válida")
        
        casos_invalidos = [(0.95, "1.00 m"), (2.60, "2.50 m")]
        for altura_invalida, mensagem_esperada in casos_invalidos:
            valido, erro = self.validador.validarAltura(altura_invalida)
            self.assertFalse(valido, f"Altura {altura_invalida}m deveria ser inválida")
            self.assertIn(mensagem_esperada, erro)

    def test_AC10_AC11_CampoObservacoesComLimite(self):
        valido, erro = self.validador._validar_observacoes("A" * 1000)
        self.assertTrue(valido, "Observação com 1000 caracteres deveria ser válida")
        
        valido, erro = self.validador._validar_observacoes("A" * 1001)
        self.assertFalse(valido, "Observação com 1001 caracteres deveria ser inválida")
        self.assertIn("1000 caracteres", erro)

    def test_ValidarMedidasCompletas(self):
        medidas = {
            'peso': 75.0,
            'altura': 1.80,
            'percentual_gordura': 15.0,
            'torax': 95.0,
            'cintura': 80.0,
            'quadril': 95.0,
            'observacoes': 'Teste de medidas'
        }
        valido, erro = self.validador.validarMedidas(medidas)
        self.assertTrue(valido)
        self.assertIsNone(erro)

    def test_ValidarMedidasInvalidas(self):
        medidas = {'peso': 250.0, 'altura': 1.80}
        valido, erro = self.validador.validarMedidas(medidas)
        self.assertFalse(valido)
        self.assertIn("180 kg", erro)

    def test_ValidarFormatoNumerico(self):
        valido, erro = self.validador.validarFormatoNumerico(75.5)
        self.assertTrue(valido, "Número deveria ser válido")
        
        for valor_invalido in ["abc", None]:
            valido, erro = self.validador.validarFormatoNumerico(valor_invalido)
            self.assertFalse(valido, f"Valor {valor_invalido} deveria ser inválido")

    def test_ValidarFaixaValores(self):
        valido, erro = self.validador.validarFaixaValores(50, 0, 100)
        self.assertTrue(valido, "Valor 50 dentro da faixa deveria ser válido")
        
        casos_invalidos = [(-10, "mínimo 0"), (150, "máximo 100")]
        for valor_invalido, mensagem_esperada in casos_invalidos:
            valido, erro = self.validador.validarFaixaValores(valor_invalido, 0, 100)
            self.assertFalse(valido, f"Valor {valor_invalido} fora da faixa deveria ser inválido")
            self.assertIn(mensagem_esperada, erro)


class TestCalculadoraIMC(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculadoraIMC()

    def test_AC5_CalculoAutomaticoPesoGordura(self):
        peso_gordura = self.calculadora.calcular_peso_gordura(75.5, 15.0)
        self.assertIsNotNone(peso_gordura)
        self.assertAlmostEqual(peso_gordura, 11.32, places=2)

    def test_AC26_CalculoAutomaticoIMC(self):
        imc = self.calculadora.calcularIMC(75.5, 1.80)
        self.assertIsNotNone(imc)
        self.assertAlmostEqual(imc, 23.30, places=2)

    def test_AC27_IMCDuasCasasDecimais(self):
        imc = self.calculadora.calcularIMC(75.567, 1.803)
        self.assertIsNotNone(imc)
        partes_decimais = str(imc).split('.')
        if len(partes_decimais) > 1:
            self.assertLessEqual(len(partes_decimais[1]), 2, "IMC deve ter no máximo 2 casas decimais")

    def test_AC28_ClassificacaoIMC(self):
        classificacoes = [
            (16.5, "Muito abaixo do peso"),
            (18.0, "Abaixo do peso"),
            (22.0, "Peso normal"),
            (27.0, "Acima do peso"),
            (32.0, "Obesidade I"),
            (37.0, "Obesidade II"),
            (42.0, "Obesidade III")
        ]
        for imc, classificacao_esperada in classificacoes:
            classificacao = self.calculadora.classificarIMC(imc)
            self.assertIsNotNone(classificacao)
            self.assertIn(classificacao_esperada.lower(), classificacao.lower())

    def test_CalcularIMCValoresInvalidos(self):
        casos_invalidos = [
            (None, 1.80, "Peso None"),
            (75.0, None, "Altura None"),
            (0, 1.80, "Peso zero"),
            (75.0, 0, "Altura zero"),
            (-75.0, 1.80, "Peso negativo")
        ]
        for peso, altura, descricao in casos_invalidos:
            resultado = self.calculadora.calcularIMC(peso, altura)
            self.assertIsNone(resultado, f"IMC com {descricao} deveria retornar None")

    def test_ClassificarIMCNulo(self):
        self.assertIsNone(self.calculadora.classificarIMC(None))

    def test_CalcularPesoGorduraValoresInvalidos(self):
        casos_invalidos = [
            (None, 15.0, "Peso None"),
            (75.0, None, "Percentual None"),
            (0, 15.0, "Peso zero"),
            (75.0, -5.0, "Percentual negativo")
        ]
        for peso, percentual, descricao in casos_invalidos:
            resultado = self.calculadora.calcular_peso_gordura(peso, percentual)
            self.assertIsNone(resultado, f"Peso gordura com {descricao} deveria retornar None")

    def test_CalcularPercentualGordura(self):
        percentual = self.calculadora.calcular_percentual_gordura(75.0, 1.80)
        self.assertIsNotNone(percentual)
        self.assertGreaterEqual(percentual, 3.0)
        self.assertLessEqual(percentual, 70.0)

    def test_CalcularPercentualGorduraValoresInvalidos(self):
        casos_invalidos = [
            (None, 1.80, "Peso None"),
            (75.0, None, "Altura None"),
            (0, 1.80, "Peso zero")
        ]
        for peso, altura, descricao in casos_invalidos:
            resultado = self.calculadora.calcular_percentual_gordura(peso, altura)
            self.assertIsNone(resultado, f"Percentual gordura com {descricao} deveria retornar None")


if __name__ == "__main__":
    unittest.main(verbosity=2)
