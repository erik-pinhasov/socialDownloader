document.addEventListener('DOMContentLoaded', function () {
    const mediaUrlInput = document.getElementById('mediaUrl');
    const platformDisplay = document.getElementById('detectedPlatform');
    const form = document.getElementById('downloadForm');

    form.addEventListener('submit', clearMessages);

    form.addEventListener('submit', function(event) {
        const lowerCaseUrl = mediaUrlInput.value.toLowerCase();
        const platform = detectPlatform(lowerCaseUrl);

        if (!mediaUrlInput.value.trim()) {
            event.preventDefault();
            alert('כתובת ריקה');
        } else if (!platform) {
            event.preventDefault();
            alert('כתובת מדיה לא נתמכת');
        }
    });

    mediaUrlInput.addEventListener('input', function() {
        const lowerCaseUrl = mediaUrlInput.value.toLowerCase();
        const platform = detectPlatform(lowerCaseUrl);
        platformDisplay.textContent = platform ? platform : '';
    });
});

function detectPlatform(url) {
    const patterns = {
        'YouTube': /youtube\.com|youtu\.be/,
        'Facebook': /facebook\.com/,
        'Instagram': /instagram\.com/,
        'LinkedIn': /linkedin\.com/,
        'Twitter': /twitter\.com/,
        'TikTok': /tiktok\.com/,
        'Snapchat': /snapchat\.com/
    };

    for (let platform in patterns) {
        if (patterns[platform].test(url)) {
            return platform;
        }
    }
    return null;
}

function clearMessages() {
    var messagesContainer = document.querySelector('.messages');
    if (messagesContainer) {
        messagesContainer.innerHTML = '';
    }
}