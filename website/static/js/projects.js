// Function to switch between tabs
function openTab(evt, tabName) {
    var i, tabcontent, tablinks;

    // Hide all tab contents
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove active class from all tab links
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab and add an active class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Function to open the modal
function openModal(projectId) {
    document.getElementById('modal-' + projectId).style.display = "block";
}

// Function to close the modal
function closeModal(projectId) {
    document.getElementById('modal-' + projectId).style.display = "none";
}

// Close the modal if the user clicks anywhere outside of the modal
window.onclick = function(event) {
    if (event.target.classList.contains('project-modal')) {
        event.target.style.display = "none";
    }
}
