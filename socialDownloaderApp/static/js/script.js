document.addEventListener('DOMContentLoaded', () => {
    initializeEventListeners();
});

function initializeEventListeners() {
    const form = document.getElementById('downloadForm');
    const mediaUrlInput = document.getElementById('mediaUrl');
    const copyLink = document.getElementById("copyLink");
    const urlToCopy = "https://www.linkedin.com/posts/erik-pinhasov_try-my-app-now-deployed-on-free-tier-server-activity-7149671038568632320-C7Q7";

    copyLink.addEventListener("click", event => copyToClipboard(event, urlToCopy));
    mediaUrlInput.addEventListener('input', event => handleMediaUrlInput(event.target));
    form.addEventListener('submit', event => handleFormSubmission(event, mediaUrlInput, form));
}

function handleFormSubmission(event, mediaUrlInput, form) {
    event.preventDefault();
    const inputValue = mediaUrlInput.value;
    const platform = detectPlatform(inputValue);

    if (!inputValue) {
        showCustomAlert("נא להזין קישור", "red");
        return;
    }

    if (!platform) {
        showCustomAlert("קישור לא נתמך", "red");
        return;
    }

    const formData = new FormData(form);
    submitFormData(formData);
    resetLogoSize(document.querySelector(`.logo[data-platform="${platform}"]`));
}

function submitFormData(formData) {
    const loadingSpinner = document.getElementById('loadingSpinner');
    loadingSpinner.style.display = 'flex';

    fetch('/download/', {
        method: 'POST',
        body: formData,
        credentials: 'same-origin',
        headers: { 'X-CSRFToken': getCookie('csrftoken') }
    }).then(response => handleResponse(response))
    .catch(error => handleError(error));
}

function handleResponse(response) {
    if (!response.ok) {
        showCustomAlert('ההורדה לא בוצעה.', 'red');
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const contentType = response.headers.get('Content-Type');
    if (!contentType.includes('video/mp4')) {
        showCustomAlert('הקובץ אינו בפורמט mp4.', 'red');
        throw new Error('File is not an mp4.');
    }

    const contentDisposition = response.headers.get('Content-Disposition');
    const filename = getFilenameFromDisposition(contentDisposition) || 'downloaded_file';
    return response.blob().then(blob => initiateFileDownload(blob, filename));
}


function getFilenameFromDisposition(contentDisposition) {
    const utf8FilenameRegex = /filename\*\s*=\s*utf-8''(.+)$/i;
    const asciiFilenameRegex = /filename\s*=\s*"?(.+?)"?(?:;|$)/i;
    const utf8Matches = utf8FilenameRegex.exec(contentDisposition);
    const asciiMatches = asciiFilenameRegex.exec(contentDisposition);

    if (utf8Matches && utf8Matches[1]) {
        return decodeURIComponent(utf8Matches[1]);
    }

    if (asciiMatches && asciiMatches[1]) {
        return asciiMatches[1];
    }

    return null;
}

function initiateFileDownload(blob, filename) {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);

    const loadingSpinner = document.getElementById('loadingSpinner');
    loadingSpinner.style.display = 'none';
    showCustomAlert('ההורדה בוצעה.', 'green');
}

function handleError(error) {
    console.error('Error:', error);
    showCustomAlert('שגיאה, ההורדה נכשלה.', 'red');
    const loadingSpinner = document.getElementById('loadingSpinner');
    loadingSpinner.style.display = 'none';
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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
    }, 3000);
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
    logo.style.transform = 'scale(1)';
}

function enlargeLogo(logo) {
    logo.style.transform = 'scale(1.5)';
}

function detectPlatform(url) {
    const patterns = {
        'youtube': /youtube\.com|youtu\.be/,
        'facebook': /facebook\.com|fb\.watch\/[\w-]+/,
        'instagram': /instagram\.com/,
        'linkedin': /linkedin\.com/,
        'twitter': /twitter\.com/,
        'snapchat': /snapchat\.com/
    };
    return Object.keys(patterns).find(platform => patterns[platform].test(url)) || null;
}
