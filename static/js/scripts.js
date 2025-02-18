document.addEventListener('DOMContentLoaded', () => {
    // Exibir/ocultar formulário de comentários
    const commentForms = document.querySelectorAll('.comment-form');
    commentForms.forEach(form => {
        form.style.display = 'none'; // Oculta todos os formulários inicialmente
    });

    document.querySelectorAll('.topic').forEach((topic, index) => {
        topic.addEventListener('click', () => {
            const form = commentForms[index];
            if (form.style.display === 'none') {
                form.style.display = 'flex';
            } else {
                form.style.display = 'none';
            }
        });
    });
});