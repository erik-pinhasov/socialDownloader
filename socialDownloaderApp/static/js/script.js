document.addEventListener('DOMContentLoaded', () => {
    const mediaUrlInput = document.getElementById('mediaUrl');
    const form = document.getElementById('downloadForm');
    const urlToCopy = "https://www.linkedin.com/posts/erik-pinhasov_try-my-app-now-deployed-on-free-tier-server-" +
                      "activity-7149671038568632320-C7Q7";
    const copyLink = document.getElementById("copyLink");

    copyLink.addEventListener("click", event => copyToClipboard(event, urlToCopy));
    form.addEventListener('submit', event => processFormSubmission(event, mediaUrlInput));
    mediaUrlInput.addEventListener('input', () => handleMediaUrlInput(mediaUrlInput));
    displayServerMessages();
});

function displayServerMessages() {
    const messagesData = document.querySelectorAll('#messagesData .message');
    messagesData.forEach(messageDiv => {
        const messageText = messageDiv.getAttribute('data-text');
        const messageTags = messageDiv.getAttribute('data-tags');
        let backgroundColor = 'white';

        if (messageTags.includes('error')) {
            backgroundColor = 'red';
        } else if (messageTags.includes('success')) {
            backgroundColor = 'blue';
        }
        showCustomAlert(messageText, backgroundColor);
    });
}

function copyToClipboard(event, text) {
    event.preventDefault();
    navigator.clipboard.writeText(text)
    showCustomAlert('הקישור הועתק', 'green');
}

function showCustomAlert(message, backgroundColor) {
    const alertBox = document.getElementById('customAlert');
    alertBox.textContent = message;
    alertBox.style.display = 'block';
    alertBox.style.backgroundColor = backgroundColor;
    setTimeout(() => {
        alertBox.style.display = 'none';
    }, 4000);
}

function processFormSubmission(event, inputElement) {
    clearMessages();
    const url = inputElement.value.trim().toLowerCase();
    const platform = detectPlatform(url);

    if (!url) {
        event.preventDefault();
        showCustomAlert('נא להזין קישור', 'red');
    } else if (!platform) {
        event.preventDefault();
        showCustomAlert('קישור לא נתמכת', 'red');
    }
}

function handleMediaUrlInput(inputElement) {
    const url = inputElement.value.toLowerCase();
    const platform = detectPlatform(url);
    updatePlatformLogos(platform);
}

function updatePlatformLogos(platform) {
    const allLogos = document.querySelectorAll('.logo');
    allLogos.forEach(logo => resetLogoSize(logo));
    if (platform) {
        const logo = document.querySelector(`.logo[data-platform="${platform}"]`);
        if (logo) enlargeLogo(logo);
    }
}

function resetLogoSize(logo) {
    logo.style.height = '80px';
    logo.style.width = '80px';
}

function enlargeLogo(logo) {
    logo.style.height = '120px';
    logo.style.width = '120px';
}

function detectPlatform(url) {
    const patterns = {
        'youtube': /youtube\.com|youtu\.be/,
        'facebook': /facebook\.com/,
        'instagram': /instagram\.com/,
        'linkedin': /linkedin\.com/,
        'twitter': /twitter\.com/,
        'snapchat': /snapchat\.com/
    };
    return Object.keys(patterns).find(platform => patterns[platform].test(url)) || null;
}

function clearMessages() {
    const messagesContainer = document.querySelector('.messages');
    if (messagesContainer) {
        messagesContainer.innerHTML = '';
    }
}
