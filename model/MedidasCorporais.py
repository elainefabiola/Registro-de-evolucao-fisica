class MedidasCorporais:
    
    def __init__(self, id=None, peso=None, altura=None, cintura=None, 
                 quadril=None, braco=None, coxa=None):
        self._id = id
        self._peso = peso
        self._altura = altura
        self._cintura = cintura
        self._quadril = quadril
        self._braco = braco
        self._coxa = coxa
    
    def getId(self):
        return self._id
    
    def getPeso(self):
        return self._peso
    
    def getAltura(self):
        return self._altura
    
    def getCintura(self):
        return self._cintura
    
    def getQuadril(self):
        return self._quadril
    
    def getBraco(self):
        return self._braco
    
    def getCoxa(self):
        return self._coxa
    
    def setId(self, id):
        self._id = id
    
    def setPeso(self, peso):
        self._peso = peso
    
    def setAltura(self, altura):
        self._altura = altura
    
    def setCintura(self, cintura):
        self._cintura = cintura
    
    def setQuadril(self, quadril):
        self._quadril = quadril
    
    def setBraco(self, braco):
        self._braco = braco
    
    def setCoxa(self, coxa):
        self._coxa = coxa
    
    def to_dict(self):
        return {
            'id': self._id,
            'peso': self._peso,
            'altura': self._altura,
            'cintura': self._cintura,
            'quadril': self._quadril,
            'braco': self._braco,
            'coxa': self._coxa
        }
