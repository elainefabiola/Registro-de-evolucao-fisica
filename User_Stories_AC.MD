US10: Registro de circunferências corporais 
Como   instrutor da academia.
Quero registrar circunferências corporais mensalmente (tórax, braços, abdômen, cintura, coxas, panturrilhas).
Para acompanhar a evolução das minhas medidas ao longo do tempo.
Critérios de aceitação:
AC1 - O sistema deve permitir o registro das seguintes circunferências em centímetros: tórax, braço direito contraído, braço esquerdo contraído, braço direito relaxado, braço esquerdo relaxado, abdômen, cintura, quadril, antebraço direito, antebraço esquerdo, coxa direita, coxa esquerda, panturrilha direita, panturrilha esquerda e escapular.
AC2 - O sistema deve aceitar apenas valores numéricos positivos com até 2 casas decimais para cada medida.
AC3 - O sistema deve permitir salvar o registro mesmo que nem todas as medidas estejam preenchidas (campos opcionais).
US13: Registro de peso, altura e percentual de gordura
Como  instrutor da academia.
Quero registrar peso, altura e percentual de gordura (bioimpedância) do aluno periodicamente.
Para monitorar a composição corporal e saúde geral.
Critérios de aceitação:
AC4 - O sistema deve exibir campos para registro de: peso (kg), altura (m), percentual de gordura (%), peso ósseo (kg), peso residual (kg), peso muscular (kg) e calcular automaticamente o peso de gordura (kg).
AC5 - O sistema deve calcular automaticamente o "Peso Gordura" em kg a partir do peso total e percentual de gordura informados.
AC6 - O sistema deve classificar automaticamente o percentual de gordura segundo faixas por idade e gênero (ex: mulheres 36-45 anos: Excelente, Bom, Acima da média, Média, Abaixo da média, Ruim, Muito ruim).
AC7   - O sistema deve validar que o percentual de gordura esteja entre 3% e 70%.
AC8  - O sistema deve validar que o peso esteja entre 20 kg e 180 kg.
AC9   - O sistema deve validar que a altura esteja entre 1,00 m e 2,50 m.

US17: Adição de observações na avaliação física
Como   instrutor da academia.
Quero adicionar observações e anotações em cada avaliação física.
Para registrar informações importantes sobre meu progresso, dificuldades ou mudanças na rotina.
Critérios de aceitação:
AC10 - O sistema deve exibir um campo de texto livre na seção de observações de cada avaliação física.
AC11 - O sistema deve permitir até 1000 caracteres de texto no campo de observações.
AC12- O sistema deve permitir formatação básica de texto aceita texto simples.
AC13 - O sistema deve permitir que profissionais registrem: percepções técnicas, recomendações, ajustes necessários no treino e pontos de atenção.
AC14- O sistema deve permitir salvar a avaliação física sem observações (campo opcional).
AC15 - O sistema deve exibir as observações nos relatórios de evolução organizadas cronologicamente por data da avaliação.

US15: Visualização do histórico de avaliações físicas
Como  instrutor e aluno  da academia..
Quero visualizar um histórico completo de todas as minhas avaliações físicas com datas e resultados.
Para ter uma visão de longo prazo da minha evolução e manter a motivação.
Critérios de aceitação:
AC16 - O sistema deve exibir uma lista cronológica de todas as avaliações físicas do aluno, ordenadas da mais recente para a mais antiga.
AC17  - O sistema deve exibir para cada avaliação na lista: data, profissional responsável, peso, IMC e status (completa/parcial).
AC18 - O sistema deve permitir que o aluno clique em uma avaliação específica para visualizar todos os detalhes registrados (circunferências, composição corporal, observações).
AC19 - O sistema deve exibir a mensagem "Nenhuma avaliação registrada" com botão "Solicitar Avaliação" quando o aluno não possuir avaliações.


US12: Registro de múltiplas medidas em uma sessão
Como instrutor da academia.
Quero registrar múltiplas medidas de circunferência de um aluno em uma única sessão.
Para realizar uma avaliação física completa e documentada.
Critérios de aceitação:
AC20 - O sistema deve permitir que profissionais autenticados acessem o perfil de qualquer aluno e criem uma nova avaliação física completa.
AC21 - O sistema deve exibir todos os campos de medidas (circunferências e composição corporal) em um único formulário.
AC22 - O sistema deve permitir navegação rápida entre os campos através das teclas Tab ou Enter.
AC23 - O sistema deve salvar todos os dados inseridos em um único registro com a mesma data e hora quando o profissional clicar em "Salvar Avaliação".
AC24 - O sistema deve solicitar confirmação para salvar como rascunho ou descartar os dados caso o profissional saia da tela sem salvar.
AC25 - O sistema deve identificar no histórico do aluno cada avaliação com a data e o nome do profissional que a registrou.

US14: Visualização do IMC calculado
Como instrutor e aluno  da academia..
Quero visualizar meu IMC calculado automaticamente com a classificação correspondente.
Para entender em qual faixa de peso estou e definir metas realistas.
Critérios de aceitação:
AC26 - O sistema deve calcular automaticamente o IMC usando a fórmula: IMC = Peso (kg) / (Altura (m))² quando peso e altura estiverem registrados.
AC27- O sistema deve exibir o valor do IMC com 2 casas decimais.
AC28 - O sistema deve exibir a classificação correspondente ao IMC calculado: Muito abaixo do peso (< 17), Abaixo do peso (17,1 a 18,49), Peso normal (18,5 a 24,99), Acima do peso (25 a 29,99), Obesidade I (30 a 34,99), Obesidade II - Severa (35 a 39,99), Obesidade III - Mórbida (≥ 40).
AC29 - O sistema deve destacar visualmente (com cor ou negrito) a faixa de classificação em que o aluno se encontra.
AC30- O sistema deve exibir a mensagem "Registre seu peso e altura para calcular o IMC" quando não houver dados suficientes.

US16: Geração de relatórios de evolução física
Como instrutor.
Quero gerar relatórios completos de evolução física do aluno com gráficos e comparações temporais.
Para apresentar resultados e ajustar o planejamento de treinos.
Critérios de aceitação:
AC31 - O sistema deve disponibilizar a opção "Gerar Relatório de Evolução" para profissionais autenticados no perfil de alunos com histórico de avaliações.
AC32 - O sistema deve permitir exportar o relatório em formato PDF com layout profissional incluindo logo da academia.
AC33 - O sistema deve exibir alerta "Necessário pelo menos 2 avaliações para gerar relatório de evolução" quando o aluno tiver menos de 2 avaliações registradas.

