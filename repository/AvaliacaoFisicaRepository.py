from model.AvaliacaoFisica import AvaliacaoFisica
from model.MedidasCorporais import MedidasCorporais
from datetime import datetime
from decimal import Decimal

def _get_db_connection():
    """Importa get_db_connection do app para evitar dependência circular."""
    from app import get_db_connection
    return get_db_connection()

class AvaliacaoFisicaRepository:
    
    def criar_avaliacao_db(self, avaliacao, dados_adicionais=None):
        conexao = _get_db_connection()
        
        if conexao is None:
            return (False, "Erro ao conectar ao banco de dados")
        
        try:
            cursor = conexao.cursor()
            
            dados = avaliacao.to_dict()
            if dados_adicionais:
                dados.update(dados_adicionais)
            medidas = avaliacao.getMedidasCorporais()
            
            colunas = []
            valores_placeholder = []
            valores = []
            
            if dados.get('aluno_id'):
                colunas.append('aluno_id')
                valores_placeholder.append('%s')
                valores.append(dados['aluno_id'])
            
            if 'profissional_nome' in dados and dados['profissional_nome']:
                colunas.append('profissional_nome')
                valores_placeholder.append('%s')
                valores.append(dados['profissional_nome'])
            
            if medidas:
                if medidas.getPeso() is not None:
                    colunas.append('peso')
                    valores_placeholder.append('%s')
                    valores.append(medidas.getPeso())
                
                if medidas.getAltura() is not None:
                    colunas.append('altura')
                    valores_placeholder.append('%s')
                    valores.append(medidas.getAltura())
            
            campos_composicao = [
                'percentual_gordura', 'peso_osso', 'peso_residual', 
                'peso_muscular', 'peso_gordura', 'imc', 'classificacao_imc'
            ]
            
            for campo in campos_composicao:
                if campo in dados and dados[campo] is not None:
                    colunas.append(campo)
                    valores_placeholder.append('%s')
                    valores.append(dados[campo])
            
            if medidas:
                campos_circunferencias = [
                    'torax', 'braco_direito_contraido', 'braco_esquerdo_contraido',
                    'braco_direito_relaxado', 'braco_esquerdo_relaxado', 'abdomen',
                    'cintura', 'quadril', 'antebraco_direito', 'antebraco_esquerdo',
                    'coxa_direita', 'coxa_esquerda', 'panturrilha_direita',
                    'panturrilha_esquerda', 'escapular'
                ]
                
                for campo in campos_circunferencias:
                    if campo in dados and dados[campo] is not None:
                        colunas.append(campo)
                        valores_placeholder.append('%s')
                        valores.append(dados[campo])
            
            if dados.get('observacoes'):
                colunas.append('observacoes')
                valores_placeholder.append('%s')
                valores.append(dados['observacoes'])
            
            if 'completa' in dados:
                colunas.append('completa')
                valores_placeholder.append('%s')
                valores.append(dados['completa'])
            
            if not colunas:
                return (False, "Nenhum dado válido para inserir")
            
            sql = f"INSERT INTO Avaliacao ({', '.join(colunas)}) VALUES ({', '.join(valores_placeholder)})"
            
            cursor.execute(sql, valores)
            conexao.commit()
            
            return (True, "Avaliação criada com sucesso")
            
        except Exception as e:
            conexao.rollback()
            return (False, f"Erro ao criar avaliação: {str(e)}")
        
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
    
    def buscar_avaliacoes_por_aluno_db(self, aluno_id):
        conexao = _get_db_connection()
        
        if conexao is None:
            return (False, "Erro ao conectar ao banco de dados")
        
        try:
            cursor = conexao.cursor()
            
            sql = """
                SELECT a.*, al.nome as aluno_nome 
                FROM Avaliacao a
                LEFT JOIN Aluno al ON a.aluno_id = al.id
                WHERE a.aluno_id = %s 
                ORDER BY a.data_avaliacao DESC
            """
            
            cursor.execute(sql, (aluno_id,))
            resultados_tuplas = cursor.fetchall()
            
            if not resultados_tuplas:
                return (True, [], [])
            
            colunas = [desc[0] for desc in cursor.description]
            
            avaliacoes = []
            dados_adicionais_list = []
            for tupla in resultados_tuplas:
                resultado_dict = {}
                for i, valor in enumerate(tupla):
                    resultado_dict[colunas[i]] = valor
                
                def _convert_decimal(value):
                    if value is None:
                        return None
                    if isinstance(value, Decimal):
                        return float(value)
                    return value
                
                dados_adicionais = {
                    'imc': _convert_decimal(resultado_dict.get('imc')),
                    'classificacao_imc': resultado_dict.get('classificacao_imc'),
                    'percentual_gordura': _convert_decimal(resultado_dict.get('percentual_gordura')),
                    'peso_gordura': _convert_decimal(resultado_dict.get('peso_gordura')),
                    'peso_muscular': _convert_decimal(resultado_dict.get('peso_muscular')),
                    'peso_osso': _convert_decimal(resultado_dict.get('peso_osso')),
                    'peso_residual': _convert_decimal(resultado_dict.get('peso_residual')),
                    'torax': _convert_decimal(resultado_dict.get('torax')),
                    'braco_direito_contraido': _convert_decimal(resultado_dict.get('braco_direito_contraido')),
                    'braco_esquerdo_contraido': _convert_decimal(resultado_dict.get('braco_esquerdo_contraido')),
                    'braco_direito_relaxado': _convert_decimal(resultado_dict.get('braco_direito_relaxado')),
                    'braco_esquerdo_relaxado': _convert_decimal(resultado_dict.get('braco_esquerdo_relaxado')),
                    'abdomen': _convert_decimal(resultado_dict.get('abdomen')),
                    'coxa_direita': _convert_decimal(resultado_dict.get('coxa_direita')),
                    'coxa_esquerda': _convert_decimal(resultado_dict.get('coxa_esquerda')),
                    'antebraco_direito': _convert_decimal(resultado_dict.get('antebraco_direito')),
                    'antebraco_esquerdo': _convert_decimal(resultado_dict.get('antebraco_esquerdo')),
                    'panturrilha_direita': _convert_decimal(resultado_dict.get('panturrilha_direita')),
                    'panturrilha_esquerda': _convert_decimal(resultado_dict.get('panturrilha_esquerda')),
                    'escapular': _convert_decimal(resultado_dict.get('escapular')),
                    'profissional_nome': resultado_dict.get('profissional_nome'),
                    'aluno_nome': resultado_dict.get('aluno_nome')
                }
                dados_adicionais_list.append(dados_adicionais)
                
                medidas = MedidasCorporais(
                    id=resultado_dict.get('id'),
                    peso=resultado_dict.get('peso'),
                    altura=resultado_dict.get('altura'),
                    cintura=resultado_dict.get('cintura'),
                    quadril=resultado_dict.get('quadril'),
                    braco=resultado_dict.get('braco_direito_contraido') or resultado_dict.get('braco'),
                    coxa=resultado_dict.get('coxa_direita') or resultado_dict.get('coxa')
                )
                
                data_avaliacao = resultado_dict.get('data_avaliacao')
                if isinstance(data_avaliacao, str):
                    try:
                        data_avaliacao = datetime.fromisoformat(data_avaliacao.replace('Z', '+00:00'))
                    except:
                        pass
                
                avaliacao = AvaliacaoFisica(
                    id=resultado_dict.get('id'),
                    aluno=resultado_dict.get('aluno_id'),
                    dataAvaliacao=data_avaliacao,
                    observacoes=resultado_dict.get('observacoes'),
                    completa=resultado_dict.get('completa', False),
                    medidasCorporais=medidas
                )
                
                avaliacoes.append(avaliacao)
            
            return (True, avaliacoes, dados_adicionais_list)
            
        except Exception as e:
            return (False, f"Erro ao buscar avaliações: {str(e)}")
        
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
    
    def atualizar_avaliacao_db(self, avaliacao):
        if not avaliacao.getId():
            return (False, "ID da avaliação é obrigatório para atualização")
        
        conexao = _get_db_connection()
        if conexao is None:
            return (False, "Erro ao conectar ao banco de dados")
        
        try:
            cursor = conexao.cursor()
            dados = avaliacao.to_dict()
            medidas = avaliacao.getMedidasCorporais()
            
            set_clauses = []
            valores = []
            
            if dados.get('aluno_id'):
                set_clauses.append('aluno_id = %s')
                valores.append(dados['aluno_id'])
            
            if medidas:
                if medidas.getPeso() is not None:
                    set_clauses.append('peso = %s')
                    valores.append(medidas.getPeso())
                
                if medidas.getAltura() is not None:
                    set_clauses.append('altura = %s')
                    valores.append(medidas.getAltura())
            
            if dados.get('observacoes') is not None:
                set_clauses.append('observacoes = %s')
                valores.append(dados['observacoes'])
            
            if 'completa' in dados:
                set_clauses.append('completa = %s')
                valores.append(dados['completa'])
            
            if not set_clauses:
                return (False, "Nenhum campo para atualizar")
            
            valores.append(avaliacao.getId())
            
            sql = f"UPDATE Avaliacao SET {', '.join(set_clauses)} WHERE id = %s"
            cursor.execute(sql, valores)
            conexao.commit()
            
            return (True, "Avaliação atualizada com sucesso")
            
        except Exception as e:
            conexao.rollback()
            return (False, f"Erro ao atualizar avaliação: {str(e)}")
        
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
    
    def excluir_avaliacao_db(self, avaliacao_id):
        conexao = _get_db_connection()
        if conexao is None:
            return (False, "Erro ao conectar ao banco de dados")
        
        try:
            cursor = conexao.cursor()
            sql = "DELETE FROM Avaliacao WHERE id = %s"
            cursor.execute(sql, (avaliacao_id,))
            conexao.commit()
            
            if cursor.rowcount == 0:
                return (False, "Avaliação não encontrada")
            
            return (True, "Avaliação excluída com sucesso")
            
        except Exception as e:
            conexao.rollback()
            return (False, f"Erro ao excluir avaliação: {str(e)}")
        
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
