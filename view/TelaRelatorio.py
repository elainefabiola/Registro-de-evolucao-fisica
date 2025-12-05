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
    
