document.addEventListener('DOMContentLoaded', function() {
    // Function to check if an element is in the viewport
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // Function to handle the scroll event and apply the 'in-view' class
    function handleScroll() {
        const elements = document.querySelectorAll('.aboutPage-header h1, .aboutPage-header p, .aboutPage-content h2, .aboutPage-content p');
        elements.forEach((element) => {
            if (isInViewport(element)) {
                element.classList.add('in-view');
            }
        });
    }

    // Apply the 'in-view' class to elements already in the viewport on page load
    handleScroll();

    // Listen for scroll events and apply the 'in-view' class when elements enter the viewport
    window.addEventListener('scroll', handleScroll);
});