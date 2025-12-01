-- ============================================
-- SETUP_DATABASE.SQL - Script para phpMyAdmin
-- ============================================
-- Este script cria a estrutura completa do banco de dados
-- para a aplicação de Registro de Evolução Física.
--
-- INSTRUÇÕES:
-- 1. Abra o phpMyAdmin no seu navegador
-- 2. Selecione o banco de dados (ex: sql10808130)
-- 3. Vá na aba "SQL"
-- 4. Cole todo o conteúdo deste arquivo
-- 5. Clique em "Executar"
--
-- ============================================

-- Remove as tabelas se elas já existirem (CUIDADO: isso apaga todos os dados!)
-- Descomente as linhas abaixo apenas se quiser recriar as tabelas do zero
-- DROP TABLE IF EXISTS Avaliacao;
-- DROP TABLE IF EXISTS Aluno;

-- ============================================
-- CRIAÇÃO DA TABELA: Aluno
-- ============================================
-- Esta tabela armazena informações básicas dos alunos.
-- É uma tabela simples para facilitar os testes da aplicação.

CREATE TABLE IF NOT EXISTS Aluno (
    -- ID único do aluno (auto-incremento)
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Nome completo do aluno
    nome VARCHAR(255) NOT NULL COMMENT 'Nome completo do aluno',
    
    -- Data de nascimento (opcional)
    data_nascimento DATE COMMENT 'Data de nascimento do aluno',
    
    -- Gênero (opcional)
    genero VARCHAR(20) COMMENT 'Gênero: Masculino, Feminino, Outro',
    
    -- Email (opcional)
    email VARCHAR(255) COMMENT 'Email de contato',
    
    -- Telefone (opcional)
    telefone VARCHAR(20) COMMENT 'Telefone de contato',
    
    -- Data de cadastro
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Data de cadastro no sistema',
    
    -- Status (ativo/inativo)
    ativo BOOLEAN DEFAULT TRUE COMMENT 'Indica se o aluno está ativo no sistema',
    
    -- Índice para buscas por nome
    INDEX idx_nome (nome)
    
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- INSERÇÃO DE DADOS DE TESTE: Aluno
-- ============================================
-- Inserindo alguns alunos de exemplo para testar a aplicação

INSERT INTO Aluno (nome, data_nascimento, genero, email, telefone, ativo) VALUES
('João Silva', '1990-05-15', 'Masculino', 'joao.silva@email.com', '(11) 98765-4321', TRUE),
('Maria Santos', '1992-08-22', 'Feminino', 'maria.santos@email.com', '(11) 97654-3210', TRUE),
('Pedro Oliveira', '1988-03-10', 'Masculino', 'pedro.oliveira@email.com', '(11) 96543-2109', TRUE),
('Ana Costa', '1995-11-30', 'Feminino', 'ana.costa@email.com', '(11) 95432-1098', TRUE),
('Carlos Souza', '1985-07-18', 'Masculino', 'carlos.souza@email.com', '(11) 94321-0987', TRUE),
('Juliana Ferreira', '1993-01-25', 'Feminino', 'juliana.ferreira@email.com', '(11) 93210-9876', TRUE),
('Roberto Lima', '1991-09-12', 'Masculino', 'roberto.lima@email.com', '(11) 92109-8765', TRUE),
('Fernanda Alves', '1994-06-08', 'Feminino', 'fernanda.alves@email.com', '(11) 91098-7654', TRUE);

-- ============================================
-- CRIAÇÃO DA TABELA: Avaliacao
-- ============================================
-- Esta tabela armazena todas as informações de uma avaliação física.
-- É uma tabela UNIFICADA que combina:
-- - Dados de AvaliacaoFisica (data, observações, etc.)
-- - Dados de MedidasCorporais (peso, altura, circunferências, etc.)
-- - Dados de Composição Corporal (percentual de gordura, etc.)

CREATE TABLE IF NOT EXISTS Avaliacao (
    -- ID único da avaliação (auto-incremento)
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- ID do aluno (apenas um número inteiro, sem tabela de Aluno)
    aluno_id INT NOT NULL,
    
    -- Data e hora da avaliação (será preenchida automaticamente)
    data_avaliacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Nome do profissional que registrou
    profissional_nome VARCHAR(255),
    
    -- ============================================
    -- COMPOSIÇÃO CORPORAL
    -- ============================================
    peso DECIMAL(5,2) COMMENT 'Peso em kg (20-180 kg)',
    altura DECIMAL(3,2) COMMENT 'Altura em metros (1.00-2.50 m)',
    percentual_gordura DECIMAL(5,2) COMMENT 'Percentual de gordura % (3-70%)',
    peso_osso DECIMAL(5,2) COMMENT 'Peso ósseo em kg',
    peso_residual DECIMAL(5,2) COMMENT 'Peso residual em kg',
    peso_muscular DECIMAL(5,2) COMMENT 'Peso muscular em kg',
    peso_gordura DECIMAL(5,2) COMMENT 'Peso de gordura calculado em kg',
    
    -- IMC calculado automaticamente
    imc DECIMAL(5,2) COMMENT 'Índice de Massa Corporal',
    classificacao_imc VARCHAR(50) COMMENT 'Classificação do IMC',
    
    -- ============================================
    -- CIRCUNFERÊNCIAS CORPORAIS (todas em centímetros)
    -- ============================================
    torax DECIMAL(6,2) COMMENT 'Tórax em cm',
    braco_direito_contraido DECIMAL(6,2) COMMENT 'Braço direito contraído em cm',
    braco_esquerdo_contraido DECIMAL(6,2) COMMENT 'Braço esquerdo contraído em cm',
    braco_direito_relaxado DECIMAL(6,2) COMMENT 'Braço direito relaxado em cm',
    braco_esquerdo_relaxado DECIMAL(6,2) COMMENT 'Braço esquerdo relaxado em cm',
    abdomen DECIMAL(6,2) COMMENT 'Abdômen em cm',
    cintura DECIMAL(6,2) COMMENT 'Cintura em cm',
    quadril DECIMAL(6,2) COMMENT 'Quadril em cm',
    antebraco_direito DECIMAL(6,2) COMMENT 'Antebraço direito em cm',
    antebraco_esquerdo DECIMAL(6,2) COMMENT 'Antebraço esquerdo em cm',
    coxa_direita DECIMAL(6,2) COMMENT 'Coxa direita em cm',
    coxa_esquerda DECIMAL(6,2) COMMENT 'Coxa esquerda em cm',
    panturrilha_direita DECIMAL(6,2) COMMENT 'Panturrilha direita em cm',
    panturrilha_esquerda DECIMAL(6,2) COMMENT 'Panturrilha esquerda em cm',
    escapular DECIMAL(6,2) COMMENT 'Escapular em cm',
    
    -- ============================================
    -- OBSERVAÇÕES
    -- ============================================
    observacoes TEXT COMMENT 'Campo de texto livre (até 1000 caracteres)',
    
    -- Status da avaliação (completa ou parcial)
    completa BOOLEAN DEFAULT FALSE COMMENT 'Indica se a avaliação está completa',
    
    -- ============================================
    -- ÍNDICES (para melhorar performance)
    -- ============================================
    INDEX idx_aluno_id (aluno_id) COMMENT 'Índice para buscas por aluno',
    INDEX idx_data_avaliacao (data_avaliacao) COMMENT 'Índice para ordenação por data'
    
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- INSERÇÃO DE DADOS DE TESTE: Avaliacao
-- ============================================
-- Inserindo 20 avaliações de exemplo com todos os campos preenchidos para testar a aplicação

INSERT INTO Avaliacao (
    aluno_id, peso, altura, percentual_gordura, peso_osso, peso_residual, 
    peso_muscular, peso_gordura, imc, classificacao_imc, profissional_nome,
    torax, braco_direito_contraido, braco_esquerdo_contraido, 
    braco_direito_relaxado, braco_esquerdo_relaxado, abdomen, cintura, 
    quadril, antebraco_direito, antebraco_esquerdo, coxa_direita, 
    coxa_esquerda, panturrilha_direita, panturrilha_esquerda, escapular,
    observacoes, completa
) VALUES
-- Avaliação 1 - Aluno 1 (João Silva)
(1, 75.5, 1.80, 15.0, 5.2, 3.5, 50.0, 11.3, 23.30, 'Peso normal', 'Prof. João Silva',
 95.0, 35.5, 35.0, 32.5, 32.0, 85.0, 80.0, 95.0, 28.5, 28.0, 55.0, 54.5, 38.0, 37.5, 20.0,
 'Aluno em boa forma física. Manter treino atual. Progresso consistente nos últimos meses.', TRUE),

-- Avaliação 2 - Aluno 1 (João Silva) - Segunda avaliação
(1, 74.2, 1.80, 14.5, 5.1, 3.4, 50.5, 10.8, 22.87, 'Peso normal', 'Prof. João Silva',
 94.5, 35.8, 35.3, 32.8, 32.3, 84.0, 79.0, 94.5, 28.8, 28.3, 55.5, 55.0, 38.2, 37.8, 20.2,
 'Pequena redução de peso. Continuar evoluindo. Ganho de massa muscular observado.', TRUE),

-- Avaliação 3 - Aluno 2 (Maria Santos)
(2, 65.0, 1.65, 22.0, 4.5, 3.0, 42.0, 14.3, 23.88, 'Peso normal', 'Prof. Maria Santos',
 88.0, 28.0, 27.5, 26.0, 25.5, 75.0, 70.0, 92.0, 24.0, 23.5, 48.0, 47.5, 33.0, 32.5, 18.0,
 'Boa evolução. Aumentar carga nos treinos. Melhora significativa na composição corporal.', TRUE),

-- Avaliação 4 - Aluno 2 (Maria Santos) - Segunda avaliação
(2, 63.5, 1.65, 20.5, 4.4, 2.9, 43.0, 13.0, 23.33, 'Peso normal', 'Prof. Maria Santos',
 87.5, 28.5, 28.0, 26.5, 26.0, 74.0, 69.0, 91.0, 24.5, 24.0, 48.5, 48.0, 33.5, 33.0, 18.2,
 'Excelente progresso. Redução de gordura corporal e aumento de massa magra.', TRUE),

-- Avaliação 5 - Aluno 3 (Pedro Oliveira)
(3, 85.0, 1.75, 18.0, 6.0, 4.0, 60.0, 15.3, 27.76, 'Acima do peso', 'Prof. Pedro Oliveira',
 102.0, 38.0, 37.5, 35.0, 34.5, 95.0, 90.0, 105.0, 30.0, 29.5, 62.0, 61.5, 42.0, 41.5, 22.0,
 'Necessário ajustar dieta e aumentar exercícios aeróbicos. Foco em redução de peso.', TRUE),

-- Avaliação 6 - Aluno 3 (Pedro Oliveira) - Segunda avaliação
(3, 82.5, 1.75, 16.5, 5.9, 3.9, 60.5, 13.6, 26.94, 'Acima do peso', 'Prof. Pedro Oliveira',
 100.5, 38.5, 38.0, 35.5, 35.0, 93.0, 88.0, 103.0, 30.5, 30.0, 62.5, 62.0, 42.5, 42.0, 22.2,
 'Boa evolução. Redução de 2.5kg. Continuar com dieta e treino aeróbico.', TRUE),

-- Avaliação 7 - Aluno 4 (Ana Costa)
(4, 58.5, 1.60, 20.0, 4.0, 2.7, 40.0, 11.7, 22.85, 'Peso normal', 'Prof. Ana Costa',
 82.0, 26.0, 25.5, 24.0, 23.5, 72.0, 68.0, 88.0, 22.0, 21.5, 45.0, 44.5, 31.0, 30.5, 17.0,
 'Excelente progresso. Manter rotina. Aluna muito dedicada aos treinos.', TRUE),

-- Avaliação 8 - Aluno 4 (Ana Costa) - Segunda avaliação
(4, 57.8, 1.60, 19.0, 3.9, 2.6, 40.5, 11.0, 22.58, 'Peso normal', 'Prof. Ana Costa',
 81.5, 26.5, 26.0, 24.5, 24.0, 71.0, 67.0, 87.0, 22.5, 22.0, 45.5, 45.0, 31.5, 31.0, 17.2,
 'Melhora contínua. Redução de gordura e ganho de massa muscular. Parabéns!', TRUE),

-- Avaliação 9 - Aluno 5 (Carlos Souza)
(5, 92.0, 1.82, 20.0, 6.5, 4.3, 64.0, 18.4, 27.75, 'Acima do peso', 'Prof. Carlos Souza',
 108.0, 40.0, 39.5, 37.0, 36.5, 100.0, 95.0, 110.0, 32.0, 31.5, 65.0, 64.5, 44.0, 43.5, 24.0,
 'Aluno iniciante. Necessário acompanhamento nutricional. Foco em perda de peso inicial.', TRUE),

-- Avaliação 10 - Aluno 5 (Carlos Souza) - Segunda avaliação
(5, 89.5, 1.82, 18.5, 6.4, 4.2, 65.0, 16.6, 27.00, 'Acima do peso', 'Prof. Carlos Souza',
 106.5, 40.5, 40.0, 37.5, 37.0, 98.0, 93.0, 108.0, 32.5, 32.0, 65.5, 65.0, 44.5, 44.0, 24.2,
 'Bom progresso. Redução de 2.5kg. Continuar com dieta e treino.', TRUE),

-- Avaliação 11 - Aluno 6 (Juliana Ferreira)
(6, 62.0, 1.68, 21.5, 4.3, 2.8, 42.0, 13.3, 21.97, 'Peso normal', 'Prof. Juliana Ferreira',
 86.0, 27.5, 27.0, 25.5, 25.0, 76.0, 72.0, 90.0, 23.5, 23.0, 47.0, 46.5, 32.5, 32.0, 18.5,
 'Aluna dedicada. Boa evolução física. Manter intensidade dos treinos.', TRUE),

-- Avaliação 12 - Aluno 6 (Juliana Ferreira) - Segunda avaliação
(6, 61.2, 1.68, 20.0, 4.2, 2.7, 42.5, 12.2, 21.70, 'Peso normal', 'Prof. Juliana Ferreira',
 85.5, 28.0, 27.5, 26.0, 25.5, 75.0, 71.0, 89.0, 24.0, 23.5, 47.5, 47.0, 33.0, 32.5, 18.7,
 'Excelente evolução. Redução de gordura e melhora na composição corporal.', TRUE),

-- Avaliação 13 - Aluno 7 (Roberto Lima)
(7, 78.0, 1.78, 16.0, 5.5, 3.7, 55.0, 12.5, 24.61, 'Peso normal', 'Prof. Roberto Lima',
 98.0, 36.0, 35.5, 33.0, 32.5, 88.0, 83.0, 98.0, 29.0, 28.5, 56.0, 55.5, 39.0, 38.5, 21.0,
 'Aluno em boa forma. Manter treino atual. Foco em hipertrofia.', TRUE),

-- Avaliação 14 - Aluno 7 (Roberto Lima) - Segunda avaliação
(7, 79.5, 1.78, 15.5, 5.6, 3.8, 56.0, 12.3, 25.08, 'Peso normal', 'Prof. Roberto Lima',
 99.0, 36.5, 36.0, 33.5, 33.0, 89.0, 84.0, 99.0, 29.5, 29.0, 56.5, 56.0, 39.5, 39.0, 21.2,
 'Ganho de massa muscular. Excelente progresso. Continuar evoluindo.', TRUE),

-- Avaliação 15 - Aluno 8 (Fernanda Alves)
(8, 59.5, 1.63, 19.5, 4.1, 2.7, 41.0, 11.6, 22.40, 'Peso normal', 'Prof. Fernanda Alves',
 84.0, 26.5, 26.0, 24.5, 24.0, 73.0, 69.0, 89.0, 23.0, 22.5, 46.0, 45.5, 32.0, 31.5, 17.5,
 'Aluna iniciante. Boa adaptação aos treinos. Manter frequência.', TRUE),

-- Avaliação 16 - Aluno 8 (Fernanda Alves) - Segunda avaliação
(8, 58.8, 1.63, 18.5, 4.0, 2.6, 41.5, 10.9, 22.12, 'Peso normal', 'Prof. Fernanda Alves',
 83.5, 27.0, 26.5, 25.0, 24.5, 72.0, 68.0, 88.0, 23.5, 23.0, 46.5, 46.0, 32.5, 32.0, 17.7,
 'Boa evolução. Redução de gordura e melhora na força. Parabéns!', TRUE),

-- Avaliação 17 - Aluno 1 (João Silva) - Terceira avaliação
(1, 73.0, 1.80, 14.0, 5.0, 3.3, 51.0, 10.2, 22.53, 'Peso normal', 'Prof. João Silva',
 94.0, 36.0, 35.5, 33.0, 32.5, 83.0, 78.0, 94.0, 29.0, 28.5, 56.0, 55.5, 38.5, 38.0, 20.5,
 'Evolução constante. Melhora na composição corporal. Aluno muito comprometido.', TRUE),

-- Avaliação 18 - Aluno 2 (Maria Santos) - Terceira avaliação
(2, 62.5, 1.65, 19.5, 4.3, 2.8, 43.5, 12.2, 22.96, 'Peso normal', 'Prof. Maria Santos',
 87.0, 29.0, 28.5, 27.0, 26.5, 73.0, 68.0, 90.0, 25.0, 24.5, 49.0, 48.5, 34.0, 33.5, 18.5,
 'Excelente progresso. Ganho de massa muscular e redução de gordura. Continue assim!', TRUE),

-- Avaliação 19 - Aluno 3 (Pedro Oliveira) - Terceira avaliação
(3, 80.0, 1.75, 15.5, 5.8, 3.8, 61.0, 12.4, 26.12, 'Acima do peso', 'Prof. Pedro Oliveira',
 99.0, 39.0, 38.5, 36.0, 35.5, 91.0, 86.0, 102.0, 31.0, 30.5, 63.0, 62.5, 43.0, 42.5, 22.5,
 'Boa evolução. Redução de 5kg no total. Continuar com dieta e treino.', TRUE),

-- Avaliação 20 - Aluno 4 (Ana Costa) - Terceira avaliação
(4, 57.0, 1.60, 18.5, 3.8, 2.5, 41.0, 10.5, 22.27, 'Peso normal', 'Prof. Ana Costa',
 81.0, 27.0, 26.5, 25.0, 24.5, 70.0, 66.0, 86.0, 23.0, 22.5, 46.0, 45.5, 32.0, 31.5, 17.5,
 'Evolução excepcional. Redução de gordura e ganho de massa magra. Aluna exemplar!', TRUE);

-- ============================================
-- VERIFICAÇÃO
-- ============================================
-- Execute as queries abaixo para verificar se as tabelas foram criadas:

-- Ver todas as tabelas:
-- SHOW TABLES;

-- Ver a estrutura da tabela Aluno:
-- DESCRIBE Aluno;

-- Ver a estrutura da tabela Avaliacao:
-- DESCRIBE Avaliacao;

-- Ver todos os alunos cadastrados:
-- SELECT * FROM Aluno;

-- Ver todas as avaliações:
-- SELECT * FROM Avaliacao;

-- Ver avaliações com nome do aluno (usando JOIN):
-- SELECT a.id, al.nome, a.data_avaliacao, a.peso, a.altura, a.imc, a.classificacao_imc
-- FROM Avaliacao a
-- INNER JOIN Aluno al ON a.aluno_id = al.id
-- ORDER BY a.data_avaliacao DESC;

