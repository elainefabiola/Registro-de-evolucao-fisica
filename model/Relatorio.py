from datetime import datetime

class Relatorio:
    
    def __init__(self, id=None, nomeAluno=None, dataGeracao=None):
        self._id = id
        self._nomeAluno = nomeAluno
        self._dataGeracao = dataGeracao if dataGeracao else datetime.now()
    
    def getId(self):
        return self._id
    
    def getNomeAluno(self):
        return self._nomeAluno
    
    def getDataGeracao(self):
        return self._dataGeracao
    
    def setId(self, id):
        self._id = id
    
    def setNomeAluno(self, aluno_id):
        self._nomeAluno = aluno_id
    
    def setDataGeracao(self, data):
        self._dataGeracao = data
    
    def to_dict(self):
        return {
            'id': self._id,
            'nomeAluno': self._nomeAluno,
            'dataGeracao': self._dataGeracao.isoformat() if isinstance(self._dataGeracao, datetime) else self._dataGeracao
        }
