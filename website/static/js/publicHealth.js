document.addEventListener("DOMContentLoaded", function() {
    // COLLAPSIBLE SECTIONS
    var coll = document.getElementsByClassName("collapsible");
    for (var i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    }

    // MODAL FUNCTIONALITY
    var modals = document.querySelectorAll(".modal");
    var modalButtons = document.querySelectorAll(".open-modal");
    var closeButtons = document.querySelectorAll(".close");

    modalButtons.forEach(function(btn) {
        btn.onclick = function() {
            var targetModal = document.getElementById(this.getAttribute('data-modal'));
            targetModal.style.display = "block";
        };
    });

    closeButtons.forEach(function(closeBtn) {
        closeBtn.onclick = function() {
            this.closest(".modal").style.display = "none";
        };
    });

    window.onclick = function(event) {
        modals.forEach(function(modal) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        });
    };

    // Prevent overflow for collapsible content
    function preventOverflow() {
        const contentSections = document.querySelectorAll('.content');
        contentSections.forEach(content => {
            if (content.scrollHeight > window.innerHeight) {
                content.style.overflowY = "auto";
            }
        });
    }

    window.addEventListener('resize', preventOverflow);
    preventOverflow();  // Ensure it's called when the page loads
});

