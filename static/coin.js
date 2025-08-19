// coin.js
document.addEventListener('DOMContentLoaded', function() {
    const coin = document.getElementById('coin');
    const choiceButtons = document.querySelectorAll('.choice-btn');
    const darkModeToggle = document.getElementById('darkModeToggle');
    
    // Dark mode functionality
    function initDarkMode() {
        const isDarkMode = localStorage.getItem('darkMode') === 'true';
        document.body.classList.toggle('dark-mode', isDarkMode);
        updateDarkModeIcon(isDarkMode);
    }
    
    function updateDarkModeIcon(isDark) {
        if (darkModeToggle) {
            const icon = darkModeToggle.querySelector('i');
            icon.className = isDark ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
        }
    }
    
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            const isDarkMode = document.body.classList.toggle('dark-mode');
            localStorage.setItem('darkMode', isDarkMode);
            updateDarkModeIcon(isDarkMode);
        });
    }
    
    // Initialize dark mode
    initDarkMode();
    
    // Coin animation
    if (coin && choiceButtons) {
        choiceButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Add flipping animation
                coin.classList.add('flipping');
                
                // Remove animation class after animation completes
                setTimeout(() => {
                    coin.classList.remove('flipping');
                }, 1200);
            });
        });
    }
});