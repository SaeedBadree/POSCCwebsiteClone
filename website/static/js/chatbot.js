// FAQ Toggle Function
function toggleAnswer(element) {
    const answer = element.querySelector('.answer');
    if (answer.style.display === 'block') {
        answer.style.display = 'none';
    } else {
        answer.style.display = 'block';
    }
}

// Chatbot Functionality
function sendMessage() {
    const inputField = document.getElementById('user-input');
    const userInput = inputField.value.trim();

    if (userInput === "") return;

    // Add the user's message to the chat
    const chatContent = document.getElementById('chat-content');
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'chat-message user';
    userMessageDiv.textContent = userInput;
    chatContent.appendChild(userMessageDiv);

    // Scroll to the bottom of the chat content
    chatContent.scrollTop = chatContent.scrollHeight;

    // Send the user's message to the server
    fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Add the bot's response to the chat
        const botMessageDiv = document.createElement('div');
        botMessageDiv.className = 'chat-message bot';
        botMessageDiv.textContent = data.response;
        chatContent.appendChild(botMessageDiv);

        // Scroll to the bottom of the chat content
        chatContent.scrollTop = chatContent.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Clear the input field
    inputField.value = "";
}
