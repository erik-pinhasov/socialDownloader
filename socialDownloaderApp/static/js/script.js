document.addEventListener('DOMContentLoaded', () => {
    initializeEventListeners();
});

function initializeEventListeners() {
// Initializes event listeners for form submission, media URL input, and copy link button click.
    const form = document.getElementById('downloadForm');
    const mediaUrlInput = document.getElementById('mediaUrl');
    const copyLink = document.getElementById("copyLink");
    const urlToCopy = "https://www.linkedin.com/posts/erik-pinhasov_try-my-app-now-deployed-on-free-tier-server-activity-7149671038568632320-C7Q7";

    copyLink.addEventListener("click", event => copyToClipboard(event, urlToCopy));
    mediaUrlInput.addEventListener('input', event => handleMediaUrlInput(event.target));
    form.addEventListener('submit', event => handleFormSubmission(event, mediaUrlInput, form));
}

function handleFormSubmission(event, mediaUrlInput, form) {
// Handles the form submission by preventing the default behavior, validating the input URL, detecting the platform,
// preparing form data for submission, and resetting the platform logo size
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
// Submits the form data to the server, displays a loading spinner during the process, and handles the response or error.
    const loadingSpinner = document.getElementById('loadingSpinner');
    loadingSpinner.style.display = 'flex';

    fetch('/download/', {
        method: 'POST',
        body: formData,
        credentials: 'same-origin',
    }).then(response => handleResponse(response))
    .catch(error => handleError(error));
}

function handleResponse(response) {
// Handles the server response by validating the response status, extracting the filename from the
// 'Content-Disposition' header, initiating file download if the file is a '.mp4', and displaying a custom alert.
    if (!response.ok) {
        showCustomAlert('ההורדה לא בוצעה.', 'red');
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const contentDisposition = response.headers.get('Content-Disposition');
    const filename = getFilenameFromDisposition(contentDisposition);

    if (!filename.endsWith('.mp4')) {
        showCustomAlert('ההורדה לא בוצעה.', 'red');
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.blob().then(blob => initiateFileDownload(blob, filename));
}


function getFilenameFromDisposition(contentDisposition) {
// Extracts and decodes the filename from the 'Content-Disposition' HTTP header.
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
// Initiates the file download by creating a URL object from the blob, setting up a temporary 'a' element
// for download, and cleaning up after triggering the download.
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
// Handles errors by logging them to the console, hiding the loading spinner, and displaying a custom error alert.
    console.error('Error:', error);
    showCustomAlert('שגיאה, ההורדה נכשלה.', 'red');
    const loadingSpinner = document.getElementById('loadingSpinner');
    loadingSpinner.style.display = 'none';
}

function copyToClipboard(event, text) {
// Copies the provided text to the clipboard and displays a custom alert indicating success.
    event.preventDefault();
    navigator.clipboard.writeText(text)
    showCustomAlert('הקישור הועתק', 'green');
}

function showCustomAlert(message, backgroundColor) {
// Displays a custom alert with the provided message and background color, and hides it after a set duration.
    const alertBox = document.getElementById('customAlert');
    alertBox.textContent = message;
    alertBox.style.display = 'block';
    alertBox.style.backgroundColor = backgroundColor;
    setTimeout(() => {
        alertBox.style.display = 'none';
    }, 3000);
}

function handleMediaUrlInput(inputElement) {
// Handles the input event on the media URL input field by converting the input URL to lowercase and updating the platform-specific logos.
    const url = inputElement.value.toLowerCase();
    const platform = detectPlatform(url);
    updatePlatformLogos(platform);
}

function updatePlatformLogos(platform) {
// Updates the logos based on the detected platform by resetting all logo sizes and enlarging the logo of the detected platform.
    const allLogos = document.querySelectorAll('.logo');
    allLogos.forEach(logo => resetLogoSize(logo));
    if (platform) {
        const logo = document.querySelector(`.logo[data-platform="${platform}"]`);
        if (logo) enlargeLogo(logo);
    }
}

function resetLogoSize(logo) {
// Resets the size of a logo to its original scale.
    logo.style.transform = 'scale(1)';
}

function enlargeLogo(logo) {
// Enlarges the logo of the detected platform for visual emphasis.
    logo.style.transform = 'scale(1.5)';
}

function detectPlatform(url) {
// Detects the platform of the provided URL by matching it against predefined platform URL patterns.
    const patterns = {
        'youtube': /youtube\.com|youtu\.be/,
        'facebook': /facebook\.com|fb\.watch|fb\.me\/[\w-]+/,
        'instagram': /instagram\.com/,
        'linkedin': /linkedin\.com/,
        'twitter': /twitter\.com|t\.co/,
        'snapchat': /snapchat\.com/
    };
    return Object.keys(patterns).find(platform => patterns[platform].test(url)) || null;
}
