// Get the nav links and menu icons
var navLinks = document.getElementById("navLinks");
var openMenuIcon = document.querySelector(".fa-bars");  // Mobile menu (hamburger) icon
var closeMenuIcon = document.querySelector(".fa-times");  // Close icon

// Show the mobile menu (when hamburger is clicked)
function showMenu() {
    navLinks.classList.add("show"); // Slide the nav into view
    navLinks.style.right = "0"; // Ensure it slides in from the right
    closeMenuIcon.style.display = "block"; // Show close icon
    openMenuIcon.style.display = "none"; // Hide hamburger icon
}

// Hide the mobile menu (when close icon is clicked)
function hideMenu() {
    navLinks.classList.remove("show"); // Hide the nav
    navLinks.style.right = "-100%";  // Slide it off the screen to the right
    closeMenuIcon.style.display = "none"; // Hide close icon
    openMenuIcon.style.display = "block"; // Show hamburger icon again
}

// Event listeners to handle clicks on hamburger and close icons
openMenuIcon.addEventListener("click", showMenu);  // Handle hamburger menu click
closeMenuIcon.addEventListener("click", hideMenu);  // Handle close icon click

// Function to toggle dropdown menus in mobile view
function applyMobileDropdowns() {
    document.querySelectorAll(".nav-links ul li").forEach(function (li) {
        li.addEventListener("touchstart", function (e) {
            e.preventDefault(); // Prevent default touch behavior
            const dropdownMenu = li.querySelector(".dropdown-menu");
            const isVisible = dropdownMenu && dropdownMenu.classList.contains("show");

            // Hide all dropdowns first
            document.querySelectorAll(".dropdown-menu").forEach(function (menu) {
                menu.classList.remove("show");
            });

            // Toggle the clicked dropdown
            if (!isVisible && dropdownMenu) {
                dropdownMenu.classList.add("show");
            }
        });
    });

    // Handle sub-dropdown menus the same way
    document.querySelectorAll(".dropdown-menu ul li").forEach(function (li) {
        li.addEventListener("touchstart", function (e) {
            e.preventDefault(); // Prevent default touch behavior
            const subDropdownMenu = li.querySelector(".dropdown-menu-1");
            const isVisible = subDropdownMenu && subDropdownMenu.classList.contains("show");

            // Hide all sub-dropdowns first
            document.querySelectorAll(".dropdown-menu-1").forEach(function (menu) {
                menu.classList.remove("show");
            });

            // Toggle the clicked sub-dropdown
            if (!isVisible && subDropdownMenu) {
                subDropdownMenu.classList.add("show");
            }
        });
    });
}

// **Function to toggle dropdowns on hover for desktop view**
function applyDesktopDropdowns() {
    document.querySelectorAll(".nav-links ul li").forEach(function (li) {
        li.addEventListener("mouseover", function () {
            const dropdownMenu = li.querySelector(".dropdown-menu");
            if (dropdownMenu) {
                dropdownMenu.classList.add("show");
            }
        });

        li.addEventListener("mouseleave", function () {
            const dropdownMenu = li.querySelector(".dropdown-menu");
            if (dropdownMenu) {
                dropdownMenu.classList.remove("show");
            }
        });
    });

    document.querySelectorAll(".dropdown-menu ul li").forEach(function (li) {
        li.addEventListener("mouseover", function () {
            const subDropdownMenu = li.querySelector(".dropdown-menu-1");
            if (subDropdownMenu) {
                subDropdownMenu.classList.add("show");
            }
        });

        li.addEventListener("mouseleave", function () {
            const subDropdownMenu = li.querySelector(".dropdown-menu-1");
            if (subDropdownMenu) {
                subDropdownMenu.classList.remove("show");
            }
        });
    });
}

// **Function to handle different behaviors for mobile and desktop**
function handleResponsiveMenu() {
    if (window.innerWidth <= 768) {
        // Mobile view behavior
        applyMobileDropdowns();
    } else {
        // Desktop view behavior
        applyDesktopDropdowns();
    }
}

// Call the function on page load
document.addEventListener("DOMContentLoaded", handleResponsiveMenu);

// Reapply the function when window is resized
window.addEventListener("resize", handleResponsiveMenu);

// Function to prevent dropdowns from overflowing off the screen
function preventOverflow() {
    const dropdowns = document.querySelectorAll('.dropdown-menu, .dropdown-menu-1');

    dropdowns.forEach(dropdown => {
        const rect = dropdown.getBoundingClientRect();
        const isOverflowing = rect.right > window.innerWidth;

        if (isOverflowing) {
            dropdown.classList.add('is-overflowing');
        } else {
            dropdown.classList.remove('is-overflowing');
        }
    });
}

// Check for overflow on window resize and on page load
window.addEventListener('resize', preventOverflow);
document.addEventListener('DOMContentLoaded', preventOverflow);

// **Scroll-based functionality**
document.addEventListener('scroll', function () {
    const aboutSection = document.querySelector('.about-section');
    const linkItems = document.querySelectorAll('.link-item');

    const triggerPoint = window.innerHeight * 0.7; // Adjust as necessary

    // Check if About Section is in view
    if (aboutSection && aboutSection.getBoundingClientRect().top < triggerPoint) {
        aboutSection.classList.add('scrolled');
    }

    // Check if individual link items are in view
    linkItems.forEach(item => {
        if (item.getBoundingClientRect().top < triggerPoint) {
            item.classList.add('scrolled');
        }
    });
});

// Function to handle scrolling to specific sections
function smoothScroll(target) {
    document.querySelector(target).scrollIntoView({
        behavior: 'smooth'
    });
}

// Add smooth scroll behavior to navigation links
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', function (e) {
        const target = this.getAttribute('href');
        if (target.startsWith("#")) {
            e.preventDefault();
            smoothScroll(target);
        }
    });
});
