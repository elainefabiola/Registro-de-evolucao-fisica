/* ============================================
   RELATORIO.JS - JavaScript da Página de Relatórios
   ============================================ */

// Aguarda o carregamento do DOM
document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
        searchForm.addEventListener('submit', handleSearchSubmit);
    }
});

/**
 * Manipula o envio do formulário de busca.
 */
async function handleSearchSubmit(e) {
    e.preventDefault();
    
    const alunoId = document.getElementById('aluno_id_search').value;
    
    if (!alunoId) {
        showAlert('Digite o ID do aluno', 'error');
        return;
    }

    showLoading(true);
    const container = document.getElementById('avaliacoes-container');
    container.innerHTML = '';

    try {
        const response = await fetch(`/api/aluno/${alunoId}/avaliacoes`);
        const result = await response.json();

        if (result.sucesso) {
            if (result.avaliacoes && result.avaliacoes.length > 0) {
                container.innerHTML = '';
                result.avaliacoes.forEach((avaliacao, index) => {
                    container.appendChild(createAvaliacaoCard(avaliacao, index));
                });
                showAlert(`Encontradas ${result.avaliacoes.length} avaliação(ões)`, 'success');
            } else {
                container.innerHTML = `
                    <div class="empty-state">
                        <div class="empty-state-icon"></div>
                        <h3>Nenhuma avaliação encontrada</h3>
                        <p>Não há avaliações registradas para este aluno</p>
                    </div>
                `;
            }
        } else {
            showAlert('Erro: ' + result.mensagem, 'error');
        }
    } catch (error) {
        showAlert('Erro ao buscar avaliações: ' + error.message, 'error');
    } finally {
        showLoading(false);
    }
}

/**
 * Cria um card de avaliação para exibição.
 * 
 * @param {Object} avaliacao - Dados da avaliação
 * @param {number} index - Índice da avaliação
 * @returns {HTMLElement} Elemento do card criado
 */
function createAvaliacaoCard(avaliacao, index) {
    const card = document.createElement('div');
    card.className = 'avaliacao-card';

    const dataAvaliacao = new Date(avaliacao.data_avaliacao).toLocaleDateString('pt-BR');
    const imcClass = getIMCClass(avaliacao.classificacao_imc);
    
    // Formata IMC para exibição (2 casas decimais)
    let imcFormatado = null;
    if (avaliacao.imc !== null && avaliacao.imc !== undefined && avaliacao.imc !== '') {
        try {
            const imcNum = typeof avaliacao.imc === 'number' ? avaliacao.imc : parseFloat(avaliacao.imc);
            if (!isNaN(imcNum)) {
                imcFormatado = imcNum.toFixed(2);
            }
        } catch (e) {
            console.error('Erro ao formatar IMC:', e);
        }
    }

    card.innerHTML = `
        <div class="avaliacao-header">
            <div>
                <h3>Avaliação #${avaliacao.id || index + 1}</h3>
                ${avaliacao.aluno_nome ? `
                    <div style="margin-top: 5px; color: #6c757d; font-size: 14px; font-weight: 600;">
                        ${avaliacao.aluno_nome}
                    </div>
                ` : ''}
                ${avaliacao.profissional_nome ? `
                    <div style="margin-top: 3px; color: #6c757d; font-size: 12px;">
                        Profissional: ${avaliacao.profissional_nome}
                    </div>
                ` : ''}
            </div>
            <span class="avaliacao-date">${dataAvaliacao}</span>
        </div>
        
        ${imcFormatado ? `
            <div class="imc-section">
                <div class="imc-value">
                    <div class="imc-value-label">Índice de Massa Corporal</div>
                    <div class="imc-value-number">${imcFormatado}</div>
                </div>
                ${avaliacao.classificacao_imc ? `
                    <div class="imc-classificacao">
                        ${avaliacao.classificacao_imc}
                    </div>
                ` : ''}
            </div>
        ` : ''}
        
        <div class="avaliacao-grid">
            ${avaliacao.peso ? `
                <div class="avaliacao-item">
                    <label>Peso</label>
                    <value>${avaliacao.peso} kg</value>
                </div>
            ` : ''}
            
            ${avaliacao.altura ? `
                <div class="avaliacao-item">
                    <label>Altura</label>
                    <value>${avaliacao.altura} m</value>
                </div>
            ` : ''}
            
            ${avaliacao.percentual_gordura ? `
                <div class="avaliacao-item">
                    <label>% Gordura</label>
                    <value>${avaliacao.percentual_gordura}%</value>
                </div>
            ` : ''}
            
            ${avaliacao.peso_gordura ? `
                <div class="avaliacao-item">
                    <label>Peso Gordura</label>
                    <value>${avaliacao.peso_gordura} kg</value>
                </div>
            ` : ''}
            
            ${avaliacao.peso_muscular ? `
                <div class="avaliacao-item">
                    <label>Peso Muscular</label>
                    <value>${avaliacao.peso_muscular} kg</value>
                </div>
            ` : ''}
            
            ${avaliacao.cintura ? `
                <div class="avaliacao-item">
                    <label>Cintura</label>
                    <value>${avaliacao.cintura} cm</value>
                </div>
            ` : ''}
            
            ${avaliacao.quadril ? `
                <div class="avaliacao-item">
                    <label>Quadril</label>
                    <value>${avaliacao.quadril} cm</value>
                </div>
            ` : ''}
        </div>
        
        ${avaliacao.observacoes ? `
            <div class="observacoes-section">
                <h4>Observações</h4>
                <p>${avaliacao.observacoes}</p>
            </div>
        ` : ''}
        
        ${avaliacao.completa !== undefined ? `
            <div style="margin-top: 15px;">
                <span style="padding: 5px 12px; background: #e9e9e9; color: #333; border: 1px solid #999; font-size: 12px; font-weight: normal;">
                    ${avaliacao.completa ? 'Completa' : 'Em andamento'}
                </span>
            </div>
        ` : ''}
        
        <div class="card-actions">
            <button class="export-button" onclick="exportarAvaliacao(this)" title="Exportar avaliação detalhada">
                Exportar Avaliação
            </button>
        </div>
    `;

    // Armazena os dados da avaliação para exportação
    card.dataset.avaliacaoData = JSON.stringify(avaliacao);

    return card;
}

/**
 * Exporta uma avaliação para impressão/PDF.
 * 
 * @param {HTMLElement} button - Botão que acionou a exportação
 */
function exportarAvaliacao(button) {
    // Encontra o card pai do botão
    const card = button.closest('.avaliacao-card');
    
    if (!card || !card.dataset.avaliacaoData) {
        showAlert('Erro ao encontrar dados da avaliação', 'error');
        return;
    }

    const avaliacao = JSON.parse(card.dataset.avaliacaoData);
    
    // Formata a data
    const dataAvaliacao = new Date(avaliacao.data_avaliacao).toLocaleDateString('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });

    // Cria o conteúdo HTML formatado para exportação
    const htmlContent = createExportHTML(avaliacao, dataAvaliacao);

    // Abre uma nova janela com o conteúdo formatado
    const printWindow = window.open('', '_blank');
    printWindow.document.write(htmlContent);
    printWindow.document.close();
    
    // Aguarda o carregamento e então abre o diálogo de impressão
    printWindow.onload = function() {
        setTimeout(() => {
            printWindow.print();
        }, 250);
    };
}

/**
 * Cria o HTML formatado para exportação.
 * 
 * @param {Object} avaliacao - Dados da avaliação
 * @param {string} dataAvaliacao - Data formatada
 * @returns {string} HTML completo para exportação
 */
function createExportHTML(avaliacao, dataAvaliacao) {
    return `
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Avaliação Física - ${avaliacao.aluno_nome || 'Aluno'}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, Helvetica, sans-serif;
            padding: 40px;
            background: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border: 1px solid #ddd;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 2px solid #333;
        }
        .header h1 {
            color: #333;
            font-size: 24px;
            margin-bottom: 8px;
            font-weight: normal;
        }
        .header h2 {
            color: #666;
            font-size: 18px;
            font-weight: normal;
        }
        .info-section {
            margin-bottom: 25px;
        }
        .info-section h3 {
            color: #333;
            font-size: 16px;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid #ddd;
            font-weight: normal;
        }
        .info-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin-bottom: 15px;
        }
        .info-item {
            background: #f9f9f9;
            padding: 12px;
            border: 1px solid #ddd;
        }
        .info-item label {
            font-size: 11px;
            color: #666;
            display: block;
            margin-bottom: 3px;
            text-transform: uppercase;
            font-weight: normal;
        }
        .info-item value {
            font-size: 16px;
            font-weight: normal;
            color: #333;
        }
        .imc-section {
            background: #f5f5f5;
            color: #333;
            padding: 20px;
            border: 1px solid #ddd;
            text-align: center;
            margin-bottom: 25px;
        }
        .imc-value {
            font-size: 36px;
            font-weight: normal;
            margin-bottom: 8px;
        }
        .imc-classificacao {
            font-size: 16px;
            font-weight: normal;
            margin-top: 8px;
        }
        .observacoes {
            background: #e9e9e9;
            border-left: 3px solid #999;
            padding: 15px;
            margin-top: 15px;
        }
        .observacoes h4 {
            color: #333;
            margin-bottom: 8px;
            font-weight: normal;
        }
        .observacoes p {
            color: #333;
            line-height: 1.5;
            font-size: 13px;
        }
        .footer {
            margin-top: 30px;
            padding-top: 15px;
            border-top: 1px solid #ddd;
            text-align: center;
            color: #666;
            font-size: 11px;
        }
        @media print {
            body {
                background: white;
                padding: 0;
            }
            .container {
                border: none;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Avaliação Física</h1>
            <h2>${avaliacao.aluno_nome || 'Aluno não identificado'}</h2>
            <p style="margin-top: 10px; color: #6c757d;">Data da Avaliação: ${dataAvaliacao}</p>
            ${avaliacao.profissional_nome ? `<p style="color: #6c757d;">Profissional: ${avaliacao.profissional_nome}</p>` : ''}
        </div>

        ${avaliacao.imc ? `
        <div class="imc-section">
            <div style="font-size: 12px; color: #666; margin-bottom: 8px;">Índice de Massa Corporal</div>
            <div class="imc-value">${parseFloat(avaliacao.imc).toFixed(2)}</div>
            ${avaliacao.classificacao_imc ? `<div class="imc-classificacao">${avaliacao.classificacao_imc}</div>` : ''}
        </div>
        ` : ''}

        <div class="info-section">
            <h3>Medidas Corporais</h3>
            <div class="info-grid">
                ${avaliacao.peso ? `
                <div class="info-item">
                    <label>Peso</label>
                    <value>${avaliacao.peso} kg</value>
                </div>
                ` : ''}
                ${avaliacao.altura ? `
                <div class="info-item">
                    <label>Altura</label>
                    <value>${avaliacao.altura} m</value>
                </div>
                ` : ''}
                ${avaliacao.cintura ? `
                <div class="info-item">
                    <label>Cintura</label>
                    <value>${avaliacao.cintura} cm</value>
                </div>
                ` : ''}
                ${avaliacao.quadril ? `
                <div class="info-item">
                    <label>Quadril</label>
                    <value>${avaliacao.quadril} cm</value>
                </div>
                ` : ''}
            </div>
        </div>

        <div class="info-section">
            <h3>Composição Corporal</h3>
            <div class="info-grid">
                ${avaliacao.percentual_gordura ? `
                <div class="info-item">
                    <label>Percentual de Gordura</label>
                    <value>${avaliacao.percentual_gordura}%</value>
                </div>
                ` : ''}
                ${avaliacao.peso_gordura ? `
                <div class="info-item">
                    <label>Peso de Gordura</label>
                    <value>${avaliacao.peso_gordura} kg</value>
                </div>
                ` : ''}
                ${avaliacao.peso_muscular ? `
                <div class="info-item">
                    <label>Peso Muscular</label>
                    <value>${avaliacao.peso_muscular} kg</value>
                </div>
                ` : ''}
                ${avaliacao.peso_osso ? `
                <div class="info-item">
                    <label>Peso Ósseo</label>
                    <value>${avaliacao.peso_osso} kg</value>
                </div>
                ` : ''}
                ${avaliacao.peso_residual ? `
                <div class="info-item">
                    <label>Peso Residual</label>
                    <value>${avaliacao.peso_residual} kg</value>
                </div>
                ` : ''}
            </div>
        </div>

        ${(avaliacao.torax || avaliacao.braco_direito_contraido || avaliacao.braco_esquerdo_contraido || avaliacao.abdomen || avaliacao.coxa_direita || avaliacao.coxa_esquerda) ? `
        <div class="info-section">
            <h3>Circunferências Corporais</h3>
            <div class="info-grid">
                ${avaliacao.torax ? `
                <div class="info-item">
                    <label>Tórax</label>
                    <value>${avaliacao.torax} cm</value>
                </div>
                ` : ''}
                ${avaliacao.braco_direito_contraido ? `
                <div class="info-item">
                    <label>Braço Direito Contraído</label>
                    <value>${avaliacao.braco_direito_contraido} cm</value>
                </div>
                ` : ''}
                ${avaliacao.braco_esquerdo_contraido ? `
                <div class="info-item">
                    <label>Braço Esquerdo Contraído</label>
                    <value>${avaliacao.braco_esquerdo_contraido} cm</value>
                </div>
                ` : ''}
                ${avaliacao.abdomen ? `
                <div class="info-item">
                    <label>Abdômen</label>
                    <value>${avaliacao.abdomen} cm</value>
                </div>
                ` : ''}
                ${avaliacao.coxa_direita ? `
                <div class="info-item">
                    <label>Coxa Direita</label>
                    <value>${avaliacao.coxa_direita} cm</value>
                </div>
                ` : ''}
                ${avaliacao.coxa_esquerda ? `
                <div class="info-item">
                    <label>Coxa Esquerda</label>
                    <value>${avaliacao.coxa_esquerda} cm</value>
                </div>
                ` : ''}
            </div>
        </div>
        ` : ''}

        ${avaliacao.observacoes ? `
        <div class="observacoes">
            <h4>Observações</h4>
            <p>${avaliacao.observacoes}</p>
        </div>
        ` : ''}

        <div class="footer">
            <p>Documento gerado em ${new Date().toLocaleString('pt-BR')}</p>
            <p>Registro de Evolução Física - Sistema de Avaliação</p>
        </div>
    </div>
</body>
</html>
    `;
}

/**
 * Retorna a classe CSS para classificação do IMC.
 * 
 * @param {string} classificacao - Classificação do IMC
 * @returns {string} Classe CSS
 */
function getIMCClass(classificacao) {
    if (!classificacao) return '';
    if (classificacao.includes('normal')) return 'imc-normal';
    if (classificacao.includes('Acima') || classificacao.includes('Abaixo')) return 'imc-alto';
    if (classificacao.includes('Obesidade')) return 'imc-obesidade';
    return '';
}

