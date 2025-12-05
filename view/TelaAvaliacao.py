from controller.SistemaController import SistemaController

class TelaAvaliacao:
    
    def __init__(self, controller=None):
        self._controller = controller if controller else SistemaController()
        self._formularioVisivel = False
        self._mensagemAtual = ""
    
    def getController(self):
        return self._controller
    
    def isFormularioVisivel(self):
        return self._formularioVisivel
    
    def getMensagemAtual(self):
        return self._mensagemAtual
    
    
    def submeterAvaliacao(self, dados_avaliacao):
        resultado = self._controller.criarAvaliacao(dados_avaliacao)
        
        if resultado.get('sucesso'):
            self._mensagemAtual = resultado.get('mensagem', 'Avaliação criada com sucesso')
        else:
            self._mensagemAtual = resultado.get('mensagem', 'Erro ao criar avaliação')
        
        return resultado
