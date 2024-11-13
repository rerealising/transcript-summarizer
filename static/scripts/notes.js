// Search func for filtering documents by title

function filterDocuments() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const documentItems = document.querySelectorAll('.document-item');
    
    documentItems.forEach(item => {
        const title = item.querySelector('.document-info h2').textContent.toLowerCase();
        if (title.includes(searchInput)) {
            item.style.display = 'flex';
        } else {
            item.style.display = 'none';
        }
    });
}