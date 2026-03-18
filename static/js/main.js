document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navLinks.forEach(nav => nav.classList.remove('active'));
            this.classList.add('active');
        });
    });

    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            const userId = document.getElementById('user_id').value;
            const documentType = document.getElementById('document_type').value;
            const file = document.getElementById('file').files[0];

            if (!userId || !documentType || !file) {
                alert('Please fill out all fields and upload a document.');
                event.preventDefault();
            }
        });
    }

    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    smoothScrollLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
});
