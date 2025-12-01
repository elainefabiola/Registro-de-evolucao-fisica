# 📊 Registro de Evolução Física

Sistema web para registro e acompanhamento de avaliações físicas em academias e centros esportivos.

**Desenvolvido por:** Elaine Faiola Soares  
**Orientadora:** Profa. Dra. Luciana Zaina

---

## 📋 Descrição

O módulo de Registro de Evolução Física fornece uma interface integrada ao sistema de Gestão de Academias e Atividades Esportivas, permitindo:

- ✅ Registro completo de avaliações físicas (peso, altura, circunferências, composição corporal)
- ✅ Cálculo automático de IMC com classificação
- ✅ Validação automática de dados
- ✅ Geração e exportação de relatórios detalhados
- ✅ Histórico completo de avaliações por aluno

---

## 🔧 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.10+** (recomendado Python 3.11 ou superior)
- **pip** (gerenciador de pacotes Python)
- **Conexão com a internet** (para acesso ao banco de dados remoto)

### Verificar versão do Python

```bash
python3 --version
```

---

## 🚀 Instalação e Execução

### 1. Clone ou acesse o projeto

```bash
cd /caminho/para/RegistroEFep/RegistroEF
```

### 2. Instale as dependências

**Opção A - Com ambiente virtual (recomendado):**

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

**Opção B - Instalação direta (sistemas Debian/Ubuntu):**

```bash
pip3 install --break-system-packages -r requirements.txt
```

> ⚠️ **Nota:** Em sistemas Debian/Ubuntu mais recentes, pode ser necessário usar a flag `--break-system-packages` ou criar um ambiente virtual.

### 3. Execute a aplicação

```bash
python3 app.py
```

### 4. Acesse no navegador

A aplicação estará disponível em:

- **Local:** http://127.0.0.1:5000
- **Rede:** http://SEU_IP:5000

---

## 📦 Dependências

As dependências estão listadas no arquivo `requirements.txt`:

| Pacote | Versão | Descrição |
|--------|--------|-----------|
| Flask | 3.0.0 | Framework web |
| mysql-connector-python | 8.2.0 | Conector MySQL |

---

## 🗄️ Banco de Dados

O sistema utiliza um banco de dados MySQL remoto já configurado. A conexão está definida no arquivo `app.py`.

### Estrutura do Banco

O banco contém duas tabelas principais:

- **Aluno:** Dados cadastrais dos alunos
- **Avaliacao:** Registros das avaliações físicas

### Configuração Local (Opcional)

Se desejar usar um banco de dados local:

1. Instale o MySQL Server
2. Execute o script `setup_database.sql` no phpMyAdmin ou MySQL CLI
3. Atualize as credenciais em `app.py`:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "seu_usuario",
    "password": "sua_senha",
    "database": "nome_do_banco"
}
```

---

## 🌐 Rotas Disponíveis

### Páginas Web

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/avaliacao` | GET | Formulário de avaliação |
| `/relatorio` | GET | Página de relatórios |

### API REST

| Rota | Método | Descrição |
|------|--------|-----------|
| `/api` | GET | Informações da API |
| `/api/avaliacao` | POST | Registrar nova avaliação |
| `/api/aluno/<id>/avaliacoes` | GET | Buscar avaliações do aluno |

### Exemplo de Requisição POST

```json
POST /api/avaliacao
Content-Type: application/json

{
    "aluno_id": 1,
    "peso": 75.5,
    "altura": 1.80,
    "percentual_gordura": 15.0,
    "torax": 95.0,
    "abdomen": 85.0,
    "cintura": 80.0,
    "quadril": 95.0,
    "observacoes": "Avaliação inicial"
}
```

---

## 📁 Estrutura do Projeto

```
RegistroEF/
├── app.py                    # Aplicação principal Flask
├── requirements.txt          # Dependências do projeto
├── setup_database.sql        # Script de criação do banco
├── README.md                 # Este arquivo
│
├── controller/
│   └── SistemaController.py  # Controlador principal
│
├── model/
│   ├── AvaliacaoFisica.py    # Modelo de avaliação
│   ├── MedidasCorporais.py   # Modelo de medidas
│   └── Relatorio.py          # Modelo de relatório
│
├── repository/
│   └── AvaliacaoFisicaRepository.py  # Repositório de dados
│
├── service/
│   ├── CalculadoraIMC.py     # Serviço de cálculo de IMC
│   └── ValidadorDados.py     # Serviço de validação
│
├── view/
│   ├── TelaAvaliacao.py      # View de avaliação
│   ├── TelaPrincipal.py      # View principal
│   └── TelaRelatorio.py      # View de relatório
│
├── templates/
│   ├── base.html             # Template base
│   ├── index.html            # Página inicial
│   ├── avaliacao.html        # Formulário de avaliação
│   └── relatorio.html        # Página de relatórios
│
└── static/
    ├── css/                  # Estilos CSS
    ├── js/                   # Scripts JavaScript
    └── images/               # Imagens
```

---

## 🛠️ Solução de Problemas

### Erro: "No module named 'mysql'"

Instale o conector MySQL:

```bash
pip3 install mysql-connector-python
```

### Erro: "externally-managed-environment"

Use ambiente virtual ou adicione a flag:

```bash
pip3 install --break-system-packages -r requirements.txt
```

### Erro: "python3-venv não está instalado"

Instale o pacote venv:

```bash
# Ubuntu/Debian
sudo apt install python3-venv

# Ou para Python 3.13
sudo apt install python3.13-venv
```

### Erro de conexão com banco de dados

Verifique:
- Conexão com a internet
- Credenciais em `app.py`
- Se o serviço MySQL está ativo

---

## 📝 Licença

Este projeto foi desenvolvido para fins acadêmicos.


