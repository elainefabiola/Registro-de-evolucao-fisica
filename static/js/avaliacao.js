/* ============================================
   AVALIACAO.JS - JavaScript da Página de Avaliação
   ============================================ */

// Aguarda o carregamento do DOM
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('avaliacaoForm');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});

/**
 * Manipula o envio do formulário de avaliação.
 */
async function handleFormSubmit(e) {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const data = {};
    formData.forEach((value, key) => {
        if (value) {
            // Converte strings numéricas para números
            if (!isNaN(value) && value !== '') {
                data[key] = parseFloat(value);
            } else if (key === 'completa') {
                data[key] = value === 'true';
            } else {
                data[key] = value;
            }
        }
    });

    showLoading(true);

    try {
        const response = await fetch('/api/avaliacao', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.sucesso) {
            showAlert('Avaliação criada com sucesso!', 'success');
            setTimeout(() => {
                window.location.href = '/relatorio?aluno_id=' + data.aluno_id;
            }, 2000);
        } else {
            showAlert('Erro: ' + result.mensagem, 'error');
        }
    } catch (error) {
        showAlert('Erro ao salvar avaliação: ' + error.message, 'error');
    } finally {
        showLoading(false);
    }
}

/**
 * Limpa todos os campos do formulário.
 */
function limparFormulario() {
    if (confirm('Deseja limpar todos os campos?')) {
        document.getElementById('avaliacaoForm').reset();
    }
}

