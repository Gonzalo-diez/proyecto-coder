// Función para ocultar el contenedor de carga
function hideLoading() {
    var loadingContainer = document.getElementById('loading');
    loadingContainer.classList.add('hide');
}

setTimeout(hideLoading, 5000);