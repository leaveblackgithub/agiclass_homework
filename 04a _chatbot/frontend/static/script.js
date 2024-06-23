document.getElementById('messageInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

window.onload = function() {
    loadChatHistory();
};

function loadChatHistory() {
    fetch('/get_chat_history')
    .then(response => response.json())
    .then(data => {
        const messageArea = document.getElementById('messageArea');
        data.messages.forEach(message => {
            const messageElement = document.createElement('div');
            messageElement.className = `message ${message.sender}`;
            messageElement.innerHTML = `
                <div class="meta">${message.sender === 'user' ? '客户' : '客服'}：${message.timestamp}</div>
                <div class="bubble">${message.message}</div>`;
            messageArea.appendChild(messageElement);
        });
        // Scroll to the bottom
        messageArea.scrollTop = messageArea.scrollHeight;
    });
}

function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const messageArea = document.getElementById('messageArea');
    const userMessage = messageInput.value;
    const timestamp = new Date().toLocaleTimeString();

    if (userMessage.trim() === '') return;

    // Add user message to the chat
    const userMessageElement = document.createElement('div');
    userMessageElement.className = 'message user';
    userMessageElement.innerHTML = `
        <div class="meta">客户：${timestamp}</div>
        <div class="bubble">${userMessage}</div>`;
    messageArea.appendChild(userMessageElement);

    // Scroll to the bottom
    messageArea.scrollTop = messageArea.scrollHeight;

    // Send message to the server
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = data.response;
        const botTimestamp = new Date().toLocaleTimeString();

        // Add bot message to the chat
        const botMessageElement = document.createElement('div');
        botMessageElement.className = 'message bot';
        botMessageElement.innerHTML = `
            <div class="meta">客服：${botTimestamp}</div>
            <div class="bubble">${botMessage}</div>`;
        messageArea.appendChild(botMessageElement);

        // Scroll to the bottom
        messageArea.scrollTop = messageArea.scrollHeight;
    });

    // Clear the input field
    messageInput.value = '';
}

document.getElementById('clearChatLink').addEventListener('click', function(event) {
    event.preventDefault();
    showModal();
});

function showModal() {
    const modal = document.getElementById('confirmClearModal');
    const confirmationText = document.getElementById('confirmationText');
    const randomText = generateRandomText();
    confirmationText.innerText = `Please type the following text to confirm: ${randomText}`;
    modal.dataset.confirmText = randomText;
    modal.style.display = 'block';
}

function closeModal() {
    const modal = document.getElementById('confirmClearModal');
    modal.style.display = 'none';
}

function confirmClear() {
    const modal = document.getElementById('confirmClearModal');
    const confirmationInput = document.getElementById('confirmationInput');
    if (confirmationInput.value === modal.dataset.confirmText) {
        clearChatHistory();
        closeModal();
    } else {
        alert('Text does not match. Please try again.');
    }
}

function generateRandomText() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < 8; i++) {
        result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return result;
}

function clearChatHistory() {
    fetch('/clear_chat_history', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(() => {
        const messageArea = document.getElementById('messageArea');
        messageArea.innerHTML = '';
    });
}
