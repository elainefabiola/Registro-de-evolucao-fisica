from controller.SistemaController import SistemaController

class TelaPrincipal:
    
    def __init__(self, controller=None):
        self._controller = controller if controller else SistemaController()
        self._menuAberto = False
        self._telaAtual = "principal"
    
    def getController(self):
        return self._controller
    
    def isMenuAberto(self):
        return self._menuAberto
    
    def getTelaAtual(self):
        return self._telaAtual
    
    def exibirMenu(self):
        self._menuAberto = True
        return {
            'menu_aberto': True,
            'opcoes': ['Avaliação', 'Relatório', 'Sair']
        }
    
    def exibirDashboard(self):
        self._telaAtual = "dashboard"
        return {
            'tela': 'dashboard',
            'dados': {
                'sistema_inicializado': self._controller.isSistemaInicializado(),
                'usuario_logado': self._controller.getUsuarioLogado()
            }
        }
    
    def exibirLogin(self):
        self._telaAtual = "login"
        return {
            'tela': 'login',
            'mensagem': 'Tela de login'
        }
    
    def exibirNavegacao(self):
        return {
            'navegacao': {
                'tela_atual': self._telaAtual,
                'menu_aberto': self._menuAberto
            }
        }
    
    def fecharMenu(self):
        self._menuAberto = False
        return {
            'menu_aberto': False
        }
    
    def trocarTela(self, novaTela):
        self._telaAtual = novaTela
        return {
            'tela_atual': self._telaAtual,
            'mensagem': f'Tela alterada para: {novaTela}'
        }
    
    def inicializar(self):
        sucesso = self._controller.inicializarSistema()
        if sucesso:
            return self.exibirDashboard()
        else:
            return {
                'sucesso': False,
                'mensagem': 'Erro ao inicializar sistema'
            }
    
    def fazerLogin(self, usuario, senha=None):
        sucesso = self._controller.autenticarUsuario(usuario, senha)
        if sucesso:
            self._telaAtual = "dashboard"
            return {
                'sucesso': True,
                'mensagem': 'Login realizado com sucesso',
                'tela': self._telaAtual
            }
        else:
            return {
                'sucesso': False,
                'mensagem': 'Erro ao fazer login'
            }
