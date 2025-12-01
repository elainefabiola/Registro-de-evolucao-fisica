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
    
    def exibirFormulario(self):
        self._formularioVisivel = True
        self._mensagemAtual = "Formulário de avaliação exibido"
        return {
            'formulario_visivel': True,
            'mensagem': self._mensagemAtual
        }
    
    def exibirDados(self, dados):
        self._mensagemAtual = "Dados da avaliação exibidos"
        return {
            'dados': dados,
            'mensagem': self._mensagemAtual
        }
    
    def exibirMensagem(self, mensagem):
        self._mensagemAtual = mensagem
        return {
            'mensagem': self._mensagemAtual
        }
    
    def ocultarFormulario(self):
        self._formularioVisivel = False
        self._mensagemAtual = "Formulário ocultado"
        return {
            'formulario_visivel': False,
            'mensagem': self._mensagemAtual
        }
    
    def limparCampos(self):
        self._mensagemAtual = "Campos limpos"
        return {
            'mensagem': self._mensagemAtual
        }
    
    def submeterAvaliacao(self, dados_avaliacao):
        resultado = self._controller.criarAvaliacao(dados_avaliacao)
        
        if resultado.get('sucesso'):
            self._mensagemAtual = resultado.get('mensagem', 'Avaliação criada com sucesso')
        else:
            self._mensagemAtual = resultado.get('mensagem', 'Erro ao criar avaliação')
        
        return resultado
