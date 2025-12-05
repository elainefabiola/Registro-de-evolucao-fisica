from model.MedidasCorporais import MedidasCorporais
from datetime import datetime

class AvaliacaoFisica:
    
    def __init__(self, id=None, aluno=None, dataAvaliacao=None, 
                 observacoes=None, completa=False, medidasCorporais=None):
        self._id = id
        self._aluno = aluno
        self._dataAvaliacao = dataAvaliacao if dataAvaliacao else datetime.now()
        self._observacoes = observacoes
        self._completa = completa
        self._medidasCorporais = medidasCorporais if medidasCorporais else MedidasCorporais()
    
    def getId(self):
        return self._id
    
    def getAluno(self):
        return self._aluno
    
    def getDataAvaliacao(self):
        return self._dataAvaliacao
    
    def getObservacoes(self):
        return self._observacoes
    
    def isCompleta(self):
        return self._completa
    
    def getMedidasCorporais(self):
        return self._medidasCorporais
    
    def setId(self, id):
        self._id = id
    
    def setAluno(self, aluno_id):
        self._aluno = aluno_id
    
    def setDataAvaliacao(self, data):
        self._dataAvaliacao = data
    
    def setObservacoes(self, obs):
        self._observacoes = obs
    
    def setCompleta(self, completa):
        self._completa = completa
    
    def setMedidasCorporais(self, medidas):
        if isinstance(medidas, MedidasCorporais):
            self._medidasCorporais = medidas
        else:
            self._medidasCorporais = MedidasCorporais(**medidas)
    
    def to_dict(self):
        return {
            'id': self._id,
            'aluno_id': self._aluno if isinstance(self._aluno, (int, str)) else None,
            'data_avaliacao': self._dataAvaliacao.isoformat() if isinstance(self._dataAvaliacao, datetime) else self._dataAvaliacao,
            'observacoes': self._observacoes,
            'completa': self._completa,
            'medidas_corporais': self._medidasCorporais.to_dict() if self._medidasCorporais else None
        }
    
    @classmethod
    def from_dict(cls, dados):
        medidas_dict = {}
        campos_medidas = ['peso', 'altura', 'cintura', 'quadril', 'braco', 'coxa']
        for campo in campos_medidas:
            if campo in dados:
                medidas_dict[campo] = dados.pop(campo)
        
        medidas = MedidasCorporais(**medidas_dict) if medidas_dict else None
        
        avaliacao = cls(
            id=dados.get('id'),
            aluno=dados.get('aluno_id'),
            dataAvaliacao=dados.get('data_avaliacao'),
            observacoes=dados.get('observacoes'),
            completa=dados.get('completa', False),
            medidasCorporais=medidas
        )
        
        return avaliacao
