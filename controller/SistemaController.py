from service.ValidadorDados import ValidadorDados
from service.CalculadoraIMC import CalculadoraIMC
from model.AvaliacaoFisica import AvaliacaoFisica
from model.MedidasCorporais import MedidasCorporais
from model.Relatorio import Relatorio
from repository.AvaliacaoFisicaRepository import AvaliacaoFisicaRepository

class SistemaController:
    
    def __init__(self):
        self._calculadoraIMC = CalculadoraIMC()
        self._validadorDados = ValidadorDados()
        self._sistemaInicializado = False
        self._usuarioLogado = None
        self._repository = AvaliacaoFisicaRepository()
    
    def getCalculadoraIMC(self):
        return self._calculadoraIMC
    
    def getValidadorDados(self):
        return self._validadorDados
    
    def isSistemaInicializado(self):
        return self._sistemaInicializado
    
    def getUsuarioLogado(self):
        return self._usuarioLogado
    
    def inicializarSistema(self):
        try:
            self._sistemaInicializado = True
            return True
        except Exception as e:
            print(f"Erro ao inicializar sistema: {e}")
            return False
    
    def autenticarUsuario(self, usuario, senha=None):
        if usuario:
            self._usuarioLogado = usuario
            return True
        return False
    
    def validarPermissoes(self, acao):
        return self._sistemaInicializado and self._usuarioLogado is not None
    
    def coordenarOperacoes(self, operacao, dados=None):
        if not self.validarPermissoes(operacao):
            return {
                'sucesso': False,
                'mensagem': 'Permissão negada'
            }
        
        if operacao == 'criarAvaliacao':
            return self.criarAvaliacao(dados)
        elif operacao == 'buscarAvaliacao':
            return self.buscarAvaliacao(dados)
        elif operacao == 'atualizarAvaliacao':
            return self.atualizarAvaliacao(dados)
        elif operacao == 'excluirAvaliacao':
            return self.excluirAvaliacao(dados)
        elif operacao == 'gerarRelatorio':
            return self.gerarRelatorio(dados)
        else:
            return {
                'sucesso': False,
                'mensagem': f'Operação {operacao} não reconhecida'
            }
    
    def criarAvaliacao(self, dados_json):
        if 'aluno_id' not in dados_json or dados_json['aluno_id'] is None:
            return {
                'sucesso': False,
                'mensagem': 'aluno_id é obrigatório'
            }
        
        if 'peso' in dados_json:
            valido, erro = self._validadorDados.validarPeso(dados_json['peso'])
            if not valido:
                return {'sucesso': False, 'mensagem': f'Erro na validação: {erro}'}
        
        if 'altura' in dados_json:
            valido, erro = self._validadorDados.validarAltura(dados_json['altura'])
            if not valido:
                return {'sucesso': False, 'mensagem': f'Erro na validação: {erro}'}
        
        medidas = MedidasCorporais(
            peso=dados_json.get('peso'),
            altura=dados_json.get('altura'),
            cintura=dados_json.get('cintura'),
            quadril=dados_json.get('quadril'),
            braco=dados_json.get('braco_direito_contraido') or dados_json.get('braco'),
            coxa=dados_json.get('coxa_direita') or dados_json.get('coxa')
        )
        
        imc = None
        if 'peso' in dados_json and 'altura' in dados_json:
            imc = self._calculadoraIMC.calcularIMC(
                dados_json['peso'],
                dados_json['altura']
            )
            if imc is not None:
                dados_json['imc'] = imc
                classificacao = self._calculadoraIMC.classificarIMC(imc)
                if classificacao:
                    dados_json['classificacao_imc'] = classificacao
        
        if 'peso' in dados_json and 'altura' in dados_json:
            percentual_gordura = self._calculadoraIMC.calcular_percentual_gordura(
                dados_json['peso'],
                dados_json['altura'],
                imc
            )
            if percentual_gordura is not None:
                dados_json['percentual_gordura'] = percentual_gordura
        
        if 'peso' in dados_json and 'percentual_gordura' in dados_json:
            peso_gordura = self._calculadoraIMC.calcular_peso_gordura(
                dados_json['peso'],
                dados_json['percentual_gordura']
            )
            if peso_gordura is not None:
                dados_json['peso_gordura'] = peso_gordura
        
        avaliacao = AvaliacaoFisica(
            aluno=dados_json.get('aluno_id'),
            observacoes=dados_json.get('observacoes'),
            completa=dados_json.get('completa', False),
            medidasCorporais=medidas
        )
        
        sucesso, mensagem = self._repository.criar_avaliacao_db(avaliacao, dados_json)
        
        if sucesso:
            return {'sucesso': True, 'mensagem': mensagem}
        else:
            return {'sucesso': False, 'mensagem': mensagem}
    
    def buscarAvaliacao(self, dados):
        aluno_id = dados.get('aluno_id') if isinstance(dados, dict) else dados
        
        if aluno_id is None:
            return {
                'sucesso': False,
                'mensagem': 'aluno_id é obrigatório'
            }
        
        resultado_busca = self._repository.buscar_avaliacoes_por_aluno_db(aluno_id)
        
        if len(resultado_busca) == 2:
            sucesso, resultado = resultado_busca
            dados_adicionais_list = []
        else:
            sucesso, resultado, dados_adicionais_list = resultado_busca
        
        if sucesso:
            if len(resultado) == 0:
                return {
                    'sucesso': True,
                    'mensagem': 'Nenhuma avaliação encontrada',
                    'avaliacoes': []
                }
            
            avaliacoes_dict = []
            for i, av in enumerate(resultado):
                av_dict = av.to_dict()
                if i < len(dados_adicionais_list):
                    av_dict.update(dados_adicionais_list[i])
                if av.getMedidasCorporais():
                    medidas_dict = av.getMedidasCorporais().to_dict()
                    av_dict.update(medidas_dict)
                avaliacoes_dict.append(av_dict)
            
            return {
                'sucesso': True,
                'mensagem': f'Encontradas {len(resultado)} avaliação(ões)',
                'avaliacoes': avaliacoes_dict
            }
        else:
            return {
                'sucesso': False,
                'mensagem': resultado
            }
    
    def atualizarAvaliacao(self, dados):
        if 'id' not in dados:
            return {
                'sucesso': False,
                'mensagem': 'ID da avaliação é obrigatório'
            }
        
        avaliacao = AvaliacaoFisica.from_dict(dados)
        avaliacao.setId(dados['id'])
        
        sucesso, mensagem = self._repository.atualizar_avaliacao_db(avaliacao)
        
        if sucesso:
            return {'sucesso': True, 'mensagem': mensagem}
        else:
            return {'sucesso': False, 'mensagem': mensagem}
    
    def excluirAvaliacao(self, dados):
        avaliacao_id = dados if isinstance(dados, int) else dados.get('id')
        
        if avaliacao_id is None:
            return {
                'sucesso': False,
                'mensagem': 'ID da avaliação é obrigatório'
            }
        
        sucesso, mensagem = self._repository.excluir_avaliacao_db(avaliacao_id)
        
        if sucesso:
            return {'sucesso': True, 'mensagem': mensagem}
        else:
            return {'sucesso': False, 'mensagem': mensagem}
    
    def gerarRelatorio(self, dados):
        aluno_id = dados.get('aluno_id') if isinstance(dados, dict) else dados
        
        if aluno_id is None:
            return {
                'sucesso': False,
                'mensagem': 'aluno_id é obrigatório'
            }
        
        resultado_busca = self._repository.buscar_avaliacoes_por_aluno_db(aluno_id)
        
        if len(resultado_busca) == 2:
            sucesso, avaliacoes = resultado_busca
            dados_adicionais_list = []
        else:
            sucesso, avaliacoes, dados_adicionais_list = resultado_busca
        
        if not sucesso:
            return {
                'sucesso': False,
                'mensagem': 'Erro ao buscar avaliações'
            }
        
        relatorio = Relatorio(
            nomeAluno=aluno_id,
            dataGeracao=None
        )
        
        avaliacoes_dict = []
        for i, av in enumerate(avaliacoes):
            av_dict = av.to_dict()
            if i < len(dados_adicionais_list):
                av_dict.update(dados_adicionais_list[i])
            if av.getMedidasCorporais():
                medidas_dict = av.getMedidasCorporais().to_dict()
                av_dict.update(medidas_dict)
            avaliacoes_dict.append(av_dict)
        
        return {
            'sucesso': True,
            'mensagem': 'Relatório gerado com sucesso',
            'relatorio': relatorio.to_dict(),
            'avaliacoes': avaliacoes_dict
        }
    
    def exportarPDF(self, relatorio_dados):
        return {
            'sucesso': True,
            'mensagem': 'Exportação para PDF não implementada',
            'dados': relatorio_dados
        }
    
    def registrar_nova_avaliacao(self, dados_json):
        return self.criarAvaliacao(dados_json)
    
    def obter_historico_aluno(self, aluno_id):
        return self.buscarAvaliacao({'aluno_id': aluno_id})
