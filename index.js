document.addEventListener('DOMContentLoaded', function() {
    // Flip card functionality
    document.querySelectorAll('.med-card').forEach(card => {
        card.addEventListener('click', (event) => {
            if (event.target.classList.contains('add-to-cart') || event.target.classList.contains('order-now')) {
                return;
            }
            const cardInner = card.querySelector('.med-card-inner');
            if (cardInner.style.transform === 'rotateY(180deg)') {
                cardInner.style.transform = 'rotateY(0deg)';
            } else {
                cardInner.style.transform = 'rotateY(180deg)';
            }
        });
    });

    // Carousel functionality
    const carouselImages = document.querySelectorAll('.carousel img');
    let currentImageIndex = 0;

    function showNextImage() {
        // Hide current image
        carouselImages[currentImageIndex].classList.remove('visible');
        // Calculate index of next image
        currentImageIndex = (currentImageIndex + 1) % carouselImages.length;
        // Display next image
        carouselImages[currentImageIndex].classList.add('visible');
    }

    // Initial call to display the first image
    carouselImages[currentImageIndex].classList.add('visible');

    // Set interval to change images every 3 seconds
    setInterval(showNextImage, 3000);
});
