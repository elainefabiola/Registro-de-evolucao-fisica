# Diagrama de Classes - Módulo Registro de Evolução Física (Arquitetura MVC)

## Diagrama de Classes - Arquitetura MVC

```mermaid
classDiagram
    %% ===== DADOS (MODEL) =====
    %% Aqui ficam as informações que o sistema guarda
    
    %% Estilo para classe Aluno (cor vermelha - não implementada)
    classDef alunoClass fill:#ff6b6b,stroke:#d63031,stroke-width:2px,color:#fff
    
    class AvaliacaoFisica {
        -int id
        -int aluno_id
        -Date dataAvaliacao
        -String observacoes
        -boolean completa
        -MedidasCorporais medidasCorporais
        +getId() int
        +getAluno() int
        +getDataAvaliacao() Date
        +getObservacoes() String
        +isCompleta() boolean
        +getMedidasCorporais() MedidasCorporais
        +setId(id)
        +setAluno(aluno_id)
        +setDataAvaliacao(data)
        +setObservacoes(obs)
        +setCompleta(completa)
        +setMedidasCorporais(medidas)
        +to_dict() dict
        +from_dict(dados)$ AvaliacaoFisica
    }

    class Aluno {
        %% Classe não implementada - apenas aluno_id é usado
    }
    

    class MedidasCorporais {
        -int id
        -float peso
        -float altura
        -float cintura
        -float quadril
        -float braco
        -float coxa
        +getId() int
        +getPeso() float
        +getAltura() float
        +getCintura() float
        +getQuadril() float
        +getBraco() float
        +getCoxa() float
        +setId(id)
        +setPeso(peso)
        +setAltura(altura)
        +setCintura(cintura)
        +setQuadril(quadril)
        +setBraco(braco)
        +setCoxa(coxa)
        +to_dict() dict
    }

    class Relatorio {
        -int id
        -int nomeAluno
        -Date dataGeracao
        +getId() int
        +getNomeAluno() int
        +getDataGeracao() Date
        +setId(id)
        +setNomeAluno(aluno_id)
        +setDataGeracao(data)
        +to_dict() dict
    }

    %% ===== LÓGICA DE NEGÓCIO (SERVICES) =====
    %% Aqui ficam os cálculos e validações
    
    class CalculadoraIMC {
        +calcularIMC(peso, altura) float
        +classificarIMC(imc) String
        +calcular_peso_gordura(peso, percentual_gordura) float
        +calcular_percentual_gordura(peso, altura, imc) float
    }

    class ValidadorDados {
        +validarPeso(peso) tuple
        +validarAltura(altura) tuple
        +validarMedidas(medidas) tuple
        +validarFormatoNumerico(valor) tuple
        +validarFaixaValores(valor, min, max) tuple
        -_validar_percentual_gordura(percentual) tuple
        -_validar_circunferencia(valor, nome_campo) tuple
        -_validar_observacoes(observacoes) tuple
    }

    %% ===== CONTROLE (CONTROLLER) =====
    %% Aqui ficam as operações principais
    
    class SistemaController {
        -CalculadoraIMC calculadoraIMC
        -ValidadorDados validadorDados
        -AvaliacaoFisicaRepository repository
        -boolean sistemaInicializado
        -String usuarioLogado
        +criarAvaliacao(dados_json) dict
        +buscarAvaliacao(dados) dict
        +atualizarAvaliacao(dados) dict
        +excluirAvaliacao(dados) dict
        +gerarRelatorio(dados) dict
        +inicializarSistema() boolean
        +autenticarUsuario(usuario, senha) boolean
        +validarPermissoes(acao) boolean
        +getCalculadoraIMC() CalculadoraIMC
        +getValidadorDados() ValidadorDados
        +isSistemaInicializado() boolean
        +getUsuarioLogado() String
    }

    %% ===== PERSISTÊNCIA (REPOSITORY) =====
    %% Aqui ficam as operações de banco de dados
    
    class AvaliacaoFisicaRepository {
        +criar_avaliacao_db(avaliacao, dados_adicionais) tuple
        +buscar_avaliacoes_por_aluno_db(aluno_id) tuple
        +atualizar_avaliacao_db(avaliacao) tuple
        +excluir_avaliacao_db(avaliacao_id) tuple
    }

    %% ===== INTERFACE (VIEW) =====
    %% Aqui ficam as telas que o usuário vê
    
    class TelaAvaliacao {
        -SistemaController controller
        -boolean formularioVisivel
        -String mensagemAtual
        +submeterAvaliacao(dados_avaliacao) dict
        +getController() SistemaController
        +isFormularioVisivel() boolean
        +getMensagemAtual() String
    }

    class TelaRelatorio {
        -SistemaController controller
        -boolean relatorioCarregado
        -String formatoAtual
        +getController() SistemaController
        +isRelatorioCarregado() boolean
        +getFormatoAtual() String
    }

    class TelaPrincipal {
        -SistemaController controller
        -boolean menuAberto
        -String telaAtual
        +getController() SistemaController
        +isMenuAberto() boolean
        +getTelaAtual() String
    }

    %% ===== RELACIONAMENTOS MVC COM CARDINALIDADES =====
    
    %% Relacionamentos de COMPOSIÇÃO (Composição - forte dependência)
    %% Uma AvaliacaoFisica É COMPOSTA POR MedidasCorporais
    AvaliacaoFisica "1" *-- "1" MedidasCorporais : "composição<br/>(tem-um)"
    
    %% Relacionamentos de AGREGAÇÃO (Agregação - dependência média)
    %% Services podem existir independentemente do Controller
    SistemaController "1" o-- "1" CalculadoraIMC : "agregação<br/>(usa)"
    SistemaController "1" o-- "1" ValidadorDados : "agregação<br/>(usa)"
    SistemaController "1" o-- "1" AvaliacaoFisicaRepository : "agregação<br/>(usa)"
    
    %% Relacionamentos de ASSOCIAÇÃO (Associação - relacionamento fraco)
    %% Relatorio pode existir independentemente de AvaliacaoFisica
    AvaliacaoFisica "1" --> "0..*" Relatorio : "associação<br/>(gera)"
    
    %% Relacionamentos Aluno (Agregação)
    %% NOTA: Aluno não é implementado - apenas aluno_id (int) é usado
    %% AvaliacaoFisica armazena apenas aluno_id (int), não objeto Aluno
    AvaliacaoFisica "1" ..> "0..1" Aluno : "dependência<br/>(referencia por ID)"
    Relatorio "1" ..> "0..1" Aluno : "dependência<br/>(referencia por ID)"
    
    %% Relacionamentos Controller -> Model (Associações)
    %% Controller gerencia mas não possui os modelos
    SistemaController "1" --> "0..*" AvaliacaoFisica : "associação<br/>(gerencia)"
    SistemaController "1" --> "0..*" MedidasCorporais : "associação<br/>(manipula)"
    SistemaController "1" --> "0..*" Relatorio : "associação<br/>(gerencia)"
    
    %% Relacionamentos Controller -> Repository (Agregação)
    %% Controller usa Repository para persistência
    SistemaController "1" o-- "1" AvaliacaoFisicaRepository : "agregação<br/>(usa)"
    
    %% Relacionamentos Repository -> Model (Associações)
    %% Repository trabalha com modelos para persistência
    AvaliacaoFisicaRepository "1" --> "0..*" AvaliacaoFisica : "associação<br/>(persiste)"
    AvaliacaoFisicaRepository "1" --> "0..*" MedidasCorporais : "associação<br/>(persiste)"
    
    %% Relacionamentos View -> Controller (Associações)
    %% Views dependem do Controller para funcionar
    TelaAvaliacao "1" --> "1" SistemaController : "associação<br/>(comunica)"
    TelaRelatorio "1" --> "1" SistemaController : "associação<br/>(comunica)"
    TelaPrincipal "1" --> "1" SistemaController : "associação<br/>(comunica)"
    
    %% Relacionamentos Service -> Model (Dependências)
    %% Services dependem temporariamente dos modelos
    CalculadoraIMC "1" ..> "0..*" MedidasCorporais : "dependência<br/>(calcula)"
    ValidadorDados "1" ..> "0..*" MedidasCorporais : "dependência<br/>(valida)"

    %% Notas explicativas
    note for Aluno "Classe não implementada<br/>Apenas aluno_id (int) é usado<br/>Informações vêm do banco de dados"
    
    note for AvaliacaoFisica "Armazena informações<br/>básicas da avaliação<br/>Composição com MedidasCorporais"
    
    note for MedidasCorporais "Guarda todas as<br/>medidas do corpo<br/>Composta por AvaliacaoFisica"
    
    note for CalculadoraIMC "Faz os cálculos<br/>matemáticos: IMC,<br/>classificação IMC,<br/>percentual de gordura,<br/>peso de gordura"
    
    note for SistemaController "Controla todo o<br/>sistema MVC<br/>Coordena operações"
    
    note for AvaliacaoFisicaRepository "Gerencia persistência<br/>no banco MySQL<br/>Repository Pattern"
```

## Arquitetura MVC - Descrição das Camadas

### **CAMADA MODEL (MODELOS + SERVIÇOS + REPOSITÓRIOS)**

### 🗂️ **DADOS (Model)**
São como "gavetas" onde guardamos as informações:
- **AvaliacaoFisica**: Guarda informações básicas (aluno_id, data, observações, completa). Tem composição 1:1 com MedidasCorporais.
- **MedidasCorporais**: Guarda todas as medidas do corpo (peso, altura, cintura, quadril, braco, coxa). É composta por AvaliacaoFisica.
- **Relatorio**: Guarda informações dos relatórios gerados (id, nomeAluno como ID, dataGeracao).
- **Aluno**: Classe não implementada - apenas aluno_id (int) é usado. Informações completas vêm do banco de dados.

### ⚙️ **LÓGICA DE NEGÓCIO (Services)**
São como "calculadoras inteligentes" que fazem os cálculos:

- **CalculadoraIMC**: 
  - Calcula o IMC (Índice de Massa Corporal)
  - Classifica o IMC em categorias da OMS
  - Calcula percentual de gordura (fórmula Deurenberg simplificada: (1.20 * imc) - 5.4)
  - Calcula peso de gordura

- **ValidadorDados**: 
  - Valida peso (20-180 kg)
  - Valida altura (1.00-2.50 m)
  - Valida medidas completas
  - Valida formato numérico
  - Valida faixa de valores
  - Métodos privados para validações internas (percentual gordura, circunferências, observações)

### 🎮 **CONTROLE (Controller)**
É como um "gerente geral" que coordena tudo:

- **SistemaController**: 
  - Controla todo o sistema - avaliações, relatórios, autenticação
  - Coordena operações entre Services, Models e Repository
  - Implementa padrão Facade
  - Gerencia estado do sistema (inicialização, usuário logado)
  - Métodos principais: criarAvaliacao, buscarAvaliacao, atualizarAvaliacao, excluirAvaliacao, gerarRelatorio

### 💾 **PERSISTÊNCIA (Repository)**
Gerencia acesso ao banco de dados:

- **AvaliacaoFisicaRepository**: 
  - Implementa padrão Repository Pattern
  - Separa lógica de persistência do modelo de domínio
  - Operações CRUD: criar, buscar, atualizar, excluir avaliações
  - Converte objetos para/do banco de dados
  - Usa função `get_db_connection()` do `app.py` (importação local para evitar dependência circular)

### 🖥️ **INTERFACE (View)**
São as telas que o usuário vê e usa:

- **TelaAvaliacao**: 
  - Tela para preencher dados da avaliação
  - Submete avaliação através do controller
  - Gerencia estado básico (formulário visível, mensagem atual)
  - **Nota**: Métodos de exibição foram removidos (lógica está no frontend)

- **TelaRelatorio**: 
  - Tela para ver relatórios
  - Gerencia estado básico (relatório carregado, formato atual)
  - **Nota**: Métodos de exibição e exportação foram removidos (lógica está no frontend)

- **TelaPrincipal**: 
  - Tela principal com menu, dashboard e navegação
  - Gerencia estado básico (menu aberto, tela atual)
  - **Nota**: Métodos de exibição e navegação foram removidos (lógica está no frontend)

## Como Funciona na Prática?

1. **Usuário** acessa o sistema através da **TelaPrincipal**
2. **TelaPrincipal** comunica com o **SistemaController** para autenticação
3. **SistemaController** valida permissões e coordena acesso
4. **SistemaController** busca dados do aluno no banco via **AvaliacaoFisicaRepository** (aluno_id é usado, classe Aluno não implementada)
5. **Usuário** preenche dados na **TelaAvaliacao**
6. **TelaAvaliacao** envia dados para o **SistemaController**
7. **SistemaController** pede para o **ValidadorDados** verificar se está tudo certo
8. **SistemaController** pede para o **CalculadoraIMC** calcular o IMC e percentual de gordura
9. **SistemaController** cria objetos **AvaliacaoFisica** e **MedidasCorporais**
10. **SistemaController** salva os dados via **AvaliacaoFisicaRepository** no banco MySQL
11. **SistemaController** avisa a **TelaAvaliacao** que deu tudo certo
12. **TelaRelatorio** solicita relatório ao **SistemaController**
13. **SistemaController** busca avaliações via **AvaliacaoFisicaRepository**
14. **SistemaController** gera **Relatorio** baseado nos dados salvos
15. **TelaRelatorio** exibe relatório formatado

## 📊 Tabela de Relacionamentos de Classes e Cardinalidades

### **Resumo Completo dos Relacionamentos**

| Classe Origem | Relacionamento | Classe Destino | Cardinalidade | Tipo | Descrição |
|---------------|----------------|----------------|---------------|------|-----------|
| **AvaliacaoFisica** | `*--` | **MedidasCorporais** | 1:1 | COMPOSIÇÃO | Uma avaliação É COMPOSTA POR uma medida corporal |
| **AvaliacaoFisica** | `..>` | **Aluno** | 1:0..1 | DEPENDÊNCIA | Uma avaliação referencia aluno por ID (classe não implementada) |
| **AvaliacaoFisica** | `-->` | **Relatorio** | 1:N | ASSOCIAÇÃO | Uma avaliação GERA zero ou muitos relatórios |
| **Relatorio** | `..>` | **Aluno** | 1:0..1 | DEPENDÊNCIA | Um relatório referencia aluno por ID (classe não implementada) |
| **SistemaController** | `o--` | **CalculadoraIMC** | 1:1 | AGREGAÇÃO | Um controller USA uma calculadora |
| **SistemaController** | `o--` | **ValidadorDados** | 1:1 | AGREGAÇÃO | Um controller USA um validador |
| **SistemaController** | `o--` | **AvaliacaoFisicaRepository** | 1:1 | AGREGAÇÃO | Um controller USA um repositório |
| **SistemaController** | `-->` | **AvaliacaoFisica** | 1:N | ASSOCIAÇÃO | Um controller GERENCIA zero ou muitas avaliações |
| **SistemaController** | `-->` | **MedidasCorporais** | 1:N | ASSOCIAÇÃO | Um controller MANIPULA zero ou muitas medidas |
| **SistemaController** | `-->` | **Relatorio** | 1:N | ASSOCIAÇÃO | Um controller GERENCIA zero ou muitos relatórios |
| **AvaliacaoFisicaRepository** | `-->` | **AvaliacaoFisica** | 1:N | ASSOCIAÇÃO | Um repositório PERSISTE zero ou muitas avaliações |
| **AvaliacaoFisicaRepository** | `-->` | **MedidasCorporais** | 1:N | ASSOCIAÇÃO | Um repositório PERSISTE zero ou muitas medidas |
| **TelaAvaliacao** | `-->` | **SistemaController** | 1:1 | ASSOCIAÇÃO | Uma tela COMUNICA com um controller |
| **TelaRelatorio** | `-->` | **SistemaController** | 1:1 | ASSOCIAÇÃO | Uma tela COMUNICA com um controller |
| **TelaPrincipal** | `-->` | **SistemaController** | 1:1 | ASSOCIAÇÃO | Uma tela COMUNICA com um controller |
| **CalculadoraIMC** | `..>` | **MedidasCorporais** | 1:N | DEPENDÊNCIA | Uma calculadora CALCULA zero ou muitas medidas |
| **ValidadorDados** | `..>` | **MedidasCorporais** | 1:N | DEPENDÊNCIA | Um validador VALIDA zero ou muitas medidas |

## Métodos Principais por Classe

### **AvaliacaoFisica**
- Getters: `getId()`, `getAluno()`, `getDataAvaliacao()`, `getObservacoes()`, `isCompleta()`, `getMedidasCorporais()`
- Setters: `setId()`, `setAluno()`, `setDataAvaliacao()`, `setObservacoes()`, `setCompleta()`, `setMedidasCorporais()`
- Auxiliares: `to_dict()`, `from_dict()` (classmethod)

### **MedidasCorporais**
- Getters: `getId()`, `getPeso()`, `getAltura()`, `getCintura()`, `getQuadril()`, `getBraco()`, `getCoxa()`
- Setters: `setId()`, `setPeso()`, `setAltura()`, `setCintura()`, `setQuadril()`, `setBraco()`, `setCoxa()`
- Auxiliares: `to_dict()`

### **Relatorio**
- Getters: `getId()`, `getNomeAluno()`, `getDataGeracao()`
- Setters: `setId()`, `setNomeAluno()`, `setDataGeracao()`
- Auxiliares: `to_dict()`

### **CalculadoraIMC**
- Cálculos: `calcularIMC()`, `classificarIMC()`, `calcular_peso_gordura()`, `calcular_percentual_gordura()`

### **ValidadorDados**
- Validações públicas: `validarPeso()`, `validarAltura()`, `validarMedidas()`, `validarFormatoNumerico()`, `validarFaixaValores()`
- Validações privadas: `_validar_percentual_gordura()`, `_validar_circunferencia()`, `_validar_observacoes()`

### **SistemaController**
- CRUD Avaliações: `criarAvaliacao()`, `buscarAvaliacao()`, `atualizarAvaliacao()`, `excluirAvaliacao()`
- Relatórios: `gerarRelatorio()`
- Sistema: `inicializarSistema()`, `autenticarUsuario()`, `validarPermissoes()`
- Getters: `getCalculadoraIMC()`, `getValidadorDados()`, `isSistemaInicializado()`, `getUsuarioLogado()`

### **AvaliacaoFisicaRepository**
- CRUD: `criar_avaliacao_db()`, `buscar_avaliacoes_por_aluno_db()`, `atualizar_avaliacao_db()`, `excluir_avaliacao_db()`

### **TelaAvaliacao**
- Integração: `submeterAvaliacao()`
- Getters: `getController()`, `isFormularioVisivel()`, `getMensagemAtual()`

### **TelaRelatorio**
- Getters: `getController()`, `isRelatorioCarregado()`, `getFormatoAtual()`

### **TelaPrincipal**
- Getters: `getController()`, `isMenuAberto()`, `getTelaAtual()`

## Observações Importantes

1. **Classe Aluno**: Não é implementada. Apenas `aluno_id` (int) é usado. Informações completas do aluno vêm do banco de dados via JOIN.

2. **Composição**: `AvaliacaoFisica` tem composição 1:1 com `MedidasCorporais` - uma avaliação É COMPOSTA POR medidas corporais.

3. **Repository Pattern**: `AvaliacaoFisicaRepository` separa lógica de persistência do modelo de domínio.

4. **Facade Pattern**: `SistemaController` atua como Facade, simplificando a interface complexa do sistema.

5. **Encapsulamento**: Todos os atributos são privados (prefixo `_`). Acesso via getters e setters.

6. **Métodos Auxiliares**: Classes Model têm métodos `to_dict()` e `from_dict()` para serialização.

7. **Cálculos no Backend**: IMC e percentual de gordura são calculados no backend, não no frontend. O percentual de gordura usa a fórmula simplificada de Deurenberg: (1.20 * imc) - 5.4, com limites entre 3% e 70%.

8. **Simplificações Realizadas**: 
    - **ValidadorDados**: Removidos métodos duplicados (aliases em snake_case). Mantidos apenas métodos em camelCase.
    - **SistemaController**: Removidos métodos não utilizados (`coordenarOperacoes()`, `exportarPDF()`, `registrar_nova_avaliacao()`, `obter_historico_aluno()`).
    - **AvaliacaoFisica**: Removido método duplicado `getNomeAluno()`. Mantido apenas `getAluno()` e `setAluno()`.
    - **Views**: Removidos métodos não utilizados das classes TelaAvaliacao, TelaPrincipal e TelaRelatorio (lógica de interface está no frontend).

9. **Validações**: ValidadorDados tem métodos privados para validações internas (prefixo `_`).

10. **Conexão com Banco de Dados**: A função `get_db_connection()` está centralizada no arquivo `app.py`. O `AvaliacaoFisicaRepository` importa essa função localmente para evitar dependência circular.

11. **Código Simplificado**: O código foi simplificado para facilitar o aprendizado de estudantes, removendo duplicações e métodos não utilizados, mantendo todas as funcionalidades principais.
