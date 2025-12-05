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
    
