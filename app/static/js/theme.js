const toggle = document.getElementById('theme-toggle');
const html = document.documentElement;

const savedTheme = localStorage.getItem('chessi_theme') || 'light';
html.setAttribute('data-theme', savedTheme);
toggle.textContent = savedTheme === 'dark' ? '☀️' : '🌙';

toggle.addEventListener('click', () => {
    const current = html.getAttribute('data-theme');
    const newTheme = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('chessi_theme', newTheme);
    toggle.textContent = newTheme === 'dark' ? '☀️' : '🌙';
});