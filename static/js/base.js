/* ============================================
   BASE.JS - Funções JavaScript Base
   ============================================ */

/**
 * Exibe uma mensagem de alerta na tela.
 * 
 * @param {string} message - Mensagem a ser exibida
 * @param {string} type - Tipo do alerta ('success' ou 'error')
 */
function showAlert(message, type = 'success') {
    const alertContainer = document.getElementById('alert-container');
    if (!alertContainer) return;
    
    const alert = document.createElement('div');
    alert.className = `alert ${type} show`;
    alert.textContent = message;
    alertContainer.appendChild(alert);
    
    setTimeout(() => {
        alert.remove();
    }, 5000);
}

/**
 * Mostra ou esconde o indicador de carregamento.
 * 
 * @param {boolean} show - true para mostrar, false para esconder
 */
function showLoading(show = true) {
    const loading = document.querySelector('.loading');
    if (loading) {
        loading.classList.toggle('show', show);
    }
}

