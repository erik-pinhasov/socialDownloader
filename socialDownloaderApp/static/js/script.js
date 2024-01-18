document.addEventListener('DOMContentLoaded', function () {
    const mediaUrlInput = document.getElementById('mediaUrl');
    const platformLogo = document.getElementById('platformLogo');
    const form = document.getElementById('downloadForm');

    form.addEventListener('submit', clearMessages);

    form.addEventListener('submit', function (event) {
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

    mediaUrlInput.addEventListener('input', function () {
        const lowerCaseUrl = mediaUrlInput.value.toLowerCase();
        const platform = detectPlatform(lowerCaseUrl);

        console.log(`Platform detected: ${platform}`);

        // Reset the styles of all .logo elements
        const allLogos = document.querySelectorAll('.logo');
        allLogos.forEach(logo => {
            logo.style.height = '80px';
            logo.style.width = '80px';// Reset to the original size
        });

        // Get the corresponding logo image element and enlarge it
        const logo = document.querySelector(`.logo[data-platform="${platform}"]`);
        if (logo) {
            logo.style.height = '120px';
            logo.style.width = '120px';// Adjust the height to your desired size
        }
    });
});

function detectPlatform(url) {
    const patterns = {
        'youtube': /youtube\.com|youtu\.be/,
        'facebook': /facebook\.com/,
        'instagram': /instagram\.com/,
        'linkedin': /linkedin\.com/,
        'twitter': /twitter\.com/,
        'snapchat': /snapchat\.com/
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
