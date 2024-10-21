/* static/admin/js/custom.js */
document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll('.card');
    cards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            card.style.backgroundColor = '#e0f7fa';  // Light blue on hover
        });
        card.addEventListener('mouseout', function() {
            card.style.backgroundColor = 'white';  // Back to white
        });
    });
});
