const menuButton = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');
const copyEmailButton = document.querySelector('#copyEmail');

if (menuButton && navLinks) {
    menuButton.addEventListener('click', () => {
        const isOpen = navLinks.classList.toggle('open');
        menuButton.setAttribute('aria-expanded', String(isOpen));
    });

    navLinks.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('open');
            menuButton.setAttribute('aria-expanded', 'false');
        });
    });
}

if (copyEmailButton) {
    copyEmailButton.addEventListener('click', async () => {
        const email = 'alex@example.com';

        try {
            await navigator.clipboard.writeText(email);
            copyEmailButton.textContent = 'Email Copied';
        } catch (error) {
            copyEmailButton.textContent = email;
        }

        setTimeout(() => {
            copyEmailButton.textContent = 'Copy Email';
        }, 1800);
    });
}
