from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

from controller.SistemaController import SistemaController

DB_CONFIG = {
    "host": "212.1.208.51",
    "port": 3306,
    "user": "u592878919_ufscar",
    "password": "",
    "database": "u592878919_ufscar",
    "ssl_disabled": True
}

def get_db_connection():
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

app = Flask(__name__)

controller = SistemaController()

controller.inicializarSistema()

@app.route('/api/avaliacao', methods=['POST'])
def registrar_avaliacao():
    try:
        dados_json = request.json
        
        if dados_json is None:
            return jsonify({
                'sucesso': False,
                'mensagem': 'Nenhum dado foi enviado. Envie um JSON válido.'
            }), 400
        
        resultado = controller.criarAvaliacao(dados_json)
        
        if resultado['sucesso']:
            return jsonify(resultado), 201
        else:
            return jsonify(resultado), 400
        
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro inesperado: {str(e)}'
        }), 500

@app.route('/api/aluno/<int:aluno_id>/avaliacoes', methods=['GET'])
def obter_avaliacoes_aluno(aluno_id):
    try:
        resultado = controller.buscarAvaliacao({'aluno_id': aluno_id})
        
        if resultado['sucesso']:
            return jsonify(resultado), 200
        else:
            return jsonify(resultado), 400
        
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro inesperado: {str(e)}'
        }), 500

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/avaliacao', methods=['GET'])
def avaliacao():
    return render_template('avaliacao.html')

@app.route('/relatorio', methods=['GET'])
def relatorio():
    return render_template('relatorio.html')

@app.route('/api', methods=['GET'])
def api_info():
    return jsonify({
        'mensagem': 'API de Registro de Evolução Física está funcionando!',
        'rotas_disponiveis': {
            'POST /api/avaliacao': 'Registra uma nova avaliação física',
            'GET /api/aluno/<id>/avaliacoes': 'Busca histórico de avaliações de um aluno'
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
