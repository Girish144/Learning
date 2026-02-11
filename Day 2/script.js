// Folder open
const folderBtn = document.getElementById("folderBtn");
const fileInput = document.getElementById("fileInput");

folderBtn.onclick = () => {
    fileInput.click();
};

// Voice typing
const micBtn = document.getElementById("micBtn");
const input = document.getElementById("searchInput");

micBtn.onclick = () => {
    const recognition = new (window.SpeechRecognition ||
                             window.webkitSpeechRecognition)();

    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = function(event) {
        input.value = event.results[0][0].transcript;
    };
};
