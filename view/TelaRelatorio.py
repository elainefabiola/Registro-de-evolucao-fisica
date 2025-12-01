from controller.SistemaController import SistemaController

class TelaRelatorio:
    
    def __init__(self, controller=None):
        self._controller = controller if controller else SistemaController()
        self._relatorioCarregado = False
        self._formatoAtual = "json"
    
    def getController(self):
        return self._controller
    
    def isRelatorioCarregado(self):
        return self._relatorioCarregado
    
    def getFormatoAtual(self):
        return self._formatoAtual
    
    def exibirRelatorio(self, dados_relatorio):
        self._relatorioCarregado = True
        return {
            'relatorio_carregado': True,
            'dados': dados_relatorio
        }
    
    def exportarRelatorio(self, dados_relatorio, formato=None):
        formato_export = formato if formato else self._formatoAtual
        
        if formato_export.lower() == 'pdf':
            resultado = self._controller.exportarPDF(dados_relatorio)
        else:
            resultado = {
                'sucesso': True,
                'mensagem': f'Relatório exportado em formato {formato_export}',
                'dados': dados_relatorio
            }
        
        return resultado
    
    def gerarRelatorioAluno(self, aluno_id):
        resultado = self._controller.gerarRelatorio({'aluno_id': aluno_id})
        
        if resultado.get('sucesso'):
            self._relatorioCarregado = True
            return self.exibirRelatorio(resultado.get('relatorio', {}))
        else:
            return resultado
