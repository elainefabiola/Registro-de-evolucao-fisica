import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from controller.SistemaController import SistemaController
from model.AvaliacaoFisica import AvaliacaoFisica
from model.MedidasCorporais import MedidasCorporais
from service.ValidadorDados import ValidadorDados
from service.CalculadoraIMC import CalculadoraIMC


class TestSistemaRegistroEvolucaoFisica(unittest.TestCase):
    
    def setUp(self):
        self.controller = SistemaController()
        self.controller.inicializarSistema()
        self.controller.autenticarUsuario("Prof. Joao Silva")
        
        self.validador = ValidadorDados()
        self.calculadora = CalculadoraIMC()
        
        self.dados_avaliacao_completa = {
            'aluno_id': 1,
            'peso': 75.5,
            'altura': 1.80,
            'percentual_gordura': 15.0,
            'peso_osso': 5.2,
            'peso_residual': 3.5,
            'peso_muscular': 50.0,
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
            'escapular': 20.0,
            'observacoes': 'Avaliacao fisica completa. Aluno apresenta boa evolucao.',
            'profissional_nome': 'Prof. Joao Silva',
            'completa': True
        }
        
        self.dados_avaliacao_parcial = {
            'aluno_id': 2,
            'peso': 68.0,
            'altura': 1.65,
            'torax': 88.0,
            'cintura': 75.0,
            'quadril': 92.0
        }
    
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
        valores_validos = [30.00, 35.50, 40.99, 28.5, 33.0]
        for valor in valores_validos:
            valido, erro = self.validador._validar_circunferencia(valor, "torax")
            self.assertTrue(valido)
        
        valor_negativo = -30.0
        valido, erro = self.validador._validar_circunferencia(valor_negativo, "torax")
        self.assertFalse(valido)
        self.assertIn("positivo", erro.lower())
    
    def test_AC3_CamposOpcionaisCircunferencias(self):
        dados_parciais = {
            'aluno_id': 1,
            'peso': 70.0,
            'altura': 1.75,
            'torax': 90.0,
            'cintura': 78.0
        }
        
        resultado = self.controller.criarAvaliacao(dados_parciais)
        
        self.assertTrue(resultado['sucesso'])
        self.assertIn("sucesso", resultado['mensagem'].lower())
    
    def test_AC4_CamposComposicaoCorporal(self):
        dados = {
            'aluno_id': 1,
            'peso': 75.5,
            'altura': 1.80,
            'percentual_gordura': 15.0,
            'peso_osso': 5.2,
            'peso_residual': 3.5,
            'peso_muscular': 50.0
        }
        
        resultado = self.controller.criarAvaliacao(dados)
        
        self.assertTrue(resultado['sucesso'])
    
    def test_AC5_CalculoAutomaticoPesoGordura(self):
        peso = 75.5
        percentual_gordura = 15.0
        
        peso_gordura = self.calculadora.calcular_peso_gordura(peso, percentual_gordura)
        
        peso_gordura_esperado = 75.5 * 0.15
        self.assertIsNotNone(peso_gordura)
        self.assertAlmostEqual(peso_gordura, peso_gordura_esperado, places=2)
    
    def test_AC7_ValidacaoPercentualGordura(self):
        valido, erro = self.validador._validar_percentual_gordura(3.0)
        self.assertTrue(valido)
        
        valido, erro = self.validador._validar_percentual_gordura(70.0)
        self.assertTrue(valido)
        
        valido, erro = self.validador._validar_percentual_gordura(2.5)
        self.assertFalse(valido)
        self.assertIn("3%", erro)
        
        valido, erro = self.validador._validar_percentual_gordura(75.0)
        self.assertFalse(valido)
        self.assertIn("70%", erro)
    
    def test_AC8_ValidacaoPeso(self):
        valido, erro = self.validador.validarPeso(20.0)
        self.assertTrue(valido)
        
        valido, erro = self.validador.validarPeso(180.0)
        self.assertTrue(valido)
        
        valido, erro = self.validador.validarPeso(19.0)
        self.assertFalse(valido)
        self.assertIn("20 kg", erro)
        
        valido, erro = self.validador.validarPeso(185.0)
        self.assertFalse(valido)
        self.assertIn("180 kg", erro)
    
    def test_AC9_ValidacaoAltura(self):
        valido, erro = self.validador.validarAltura(1.00)
        self.assertTrue(valido)
        
        valido, erro = self.validador.validarAltura(2.50)
        self.assertTrue(valido)
        
        valido, erro = self.validador.validarAltura(0.95)
        self.assertFalse(valido)
        self.assertIn("1.00 m", erro)
        
        valido, erro = self.validador.validarAltura(2.60)
        self.assertFalse(valido)
        self.assertIn("2.50 m", erro)
    
    def test_AC10_AC11_CampoObservacoesComLimite(self):
        observacao_valida = "A" * 1000
        valido, erro = self.validador._validar_observacoes(observacao_valida)
        self.assertTrue(valido)
        
        observacao_invalida = "A" * 1001
        valido, erro = self.validador._validar_observacoes(observacao_invalida)
        self.assertFalse(valido)
        self.assertIn("1000 caracteres", erro)
    
    def test_AC14_ObservacoesOpcionais(self):
        dados_sem_obs = {
            'aluno_id': 1,
            'peso': 70.0,
            'altura': 1.75
        }
        
        resultado = self.controller.criarAvaliacao(dados_sem_obs)
        
        self.assertTrue(resultado['sucesso'])
    
    def test_AC16_ListaCronologicaAvaliacoes(self):
        aluno_id = 1
        
        dados1 = {'aluno_id': aluno_id, 'peso': 70.0, 'altura': 1.75}
        self.controller.criarAvaliacao(dados1)
        
        dados2 = {'aluno_id': aluno_id, 'peso': 68.0, 'altura': 1.75}
        self.controller.criarAvaliacao(dados2)
        
        resultado = self.controller.buscarAvaliacao({'aluno_id': aluno_id})
        
        self.assertTrue(resultado['sucesso'])
        self.assertIn('avaliacoes', resultado)
        self.assertGreater(len(resultado['avaliacoes']), 0)
    
    def test_AC19_MensagemSemAvaliacoes(self):
        resultado = self.controller.buscarAvaliacao({'aluno_id': 99999})
        
        self.assertTrue(resultado['sucesso'])
        self.assertIn('avaliacoes', resultado)
        self.assertEqual(len(resultado['avaliacoes']), 0)
    
    def test_AC21_FormularioCompletoUnicaSessao(self):
        resultado = self.controller.criarAvaliacao(self.dados_avaliacao_completa)
        
        self.assertTrue(resultado['sucesso'])
        self.assertIn("criada", resultado['mensagem'].lower())
    
    def test_AC23_SalvarTodosDadosUnicoRegistro(self):
        resultado = self.controller.criarAvaliacao(self.dados_avaliacao_completa)
        
        self.assertTrue(resultado['sucesso'])
        
        busca = self.controller.buscarAvaliacao({'aluno_id': self.dados_avaliacao_completa['aluno_id']})
        self.assertTrue(busca['sucesso'])
        self.assertGreater(len(busca['avaliacoes']), 0)
    
    def test_AC26_CalculoAutomaticoIMC(self):
        peso = 75.5
        altura = 1.80
        
        imc = self.calculadora.calcularIMC(peso, altura)
        
        imc_esperado = peso / (altura ** 2)
        
        self.assertIsNotNone(imc)
        self.assertAlmostEqual(imc, imc_esperado, places=2)
    
    def test_AC27_IMCDuasCasasDecimais(self):
        imc = self.calculadora.calcularIMC(75.567, 1.803)
        
        self.assertIsNotNone(imc)
        imc_str = str(imc)
        if '.' in imc_str:
            casas_decimais = len(imc_str.split('.')[1])
            self.assertLessEqual(casas_decimais, 2)
    
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
    
    def test_AC31_GerarRelatorioEvolucao(self):
        aluno_id = 1
        self.controller.criarAvaliacao({'aluno_id': aluno_id, 'peso': 75.0, 'altura': 1.80})
        self.controller.criarAvaliacao({'aluno_id': aluno_id, 'peso': 73.0, 'altura': 1.80})
        
        resultado = self.controller.gerarRelatorio({'aluno_id': aluno_id})
        
        self.assertTrue(resultado['sucesso'])
        self.assertIn('relatorio', resultado)
        self.assertIn('avaliacoes', resultado)
    
    def test_AC33_AlertaMinimoAvaliacoes(self):
        resultado = self.controller.gerarRelatorio({'aluno_id': 99999})
        
        self.assertIsNotNone(resultado)
    
    def test_FacadeEncapsulaSubsistemas(self):
        self.assertIsNotNone(self.controller._validadorDados)
        self.assertIsNotNone(self.controller._calculadoraIMC)
        self.assertIsNotNone(self.controller._repository)
        
        self.assertIsInstance(self.controller._validadorDados, ValidadorDados)
        self.assertIsInstance(self.controller._calculadoraIMC, CalculadoraIMC)
    
    def test_CriacaoAvaliacaoCompletaIntegracao(self):
        resultado = self.controller.criarAvaliacao(self.dados_avaliacao_completa)
        
        self.assertTrue(resultado['sucesso'])
        self.assertIsInstance(resultado, dict)
        self.assertIn('mensagem', resultado)
    
    def test_FluxoCompletoAvaliacaoHistorico(self):
        aluno_id = 1
        
        dados = {'aluno_id': aluno_id, 'peso': 75.0, 'altura': 1.80}
        resultado_criacao = self.controller.criarAvaliacao(dados)
        self.assertTrue(resultado_criacao['sucesso'])
        
        resultado_busca = self.controller.buscarAvaliacao({'aluno_id': aluno_id})
        self.assertTrue(resultado_busca['sucesso'])
        self.assertGreater(len(resultado_busca['avaliacoes']), 0)
    
    def test_ValidacaoIntegradaNoController(self):
        dados_invalidos = {
            'aluno_id': 1,
            'peso': 250.0,
            'altura': 1.75
        }
        
        resultado = self.controller.criarAvaliacao(dados_invalidos)
        
        self.assertFalse(resultado['sucesso'])
        self.assertIn('180 kg', resultado['mensagem'])


if __name__ == "__main__":
    unittest.main(verbosity=2)
