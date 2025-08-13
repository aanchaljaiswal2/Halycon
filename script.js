// Smooth scroll for navigation links
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const sectionId = this.getAttribute('href').substring(1);
        const section = document.getElementById(sectionId);
        section.scrollIntoView({ behavior: 'smooth' });
    });
});

// Dynamic greeting message based on time
window.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('header p');
    const hour = new Date().getHours();
    let greeting = 'Welcome!';

    if (hour < 12) {
        greeting = 'Good Morning!';
    } else if (hour < 18) {
        greeting = 'Good Afternoon!';
    } else {
        greeting = 'Good Evening!';
    }

    header.innerText = `${greeting} I'm John Doe, Software Engineer.`;
});
