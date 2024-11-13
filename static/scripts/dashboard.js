document.getElementById('options').addEventListener('change', function() {
    var textbox = document.getElementById('textbox');
    var textAreaBox = document.getElementById('textAreaBox');
    if (this.value === 'option1') {
        textbox.style.display = 'none';
        textAreaBox.style.display = 'block';
    } else if (this.value) {
        textbox.style.display = 'block';
        textAreaBox.style.display = 'none';
    } else {
        textbox.style.display = 'none';
        textAreaBox.style.display = 'none';
    }
});

// Autoresize textbox, taken from a personal project. Credit DreamTeK.
document.querySelectorAll("textarea").forEach(function(textarea) {
    textarea.style.height = textarea.scrollHeight + "px";
    textarea.style.overflowY = "hidden";
  
    textarea.addEventListener("input", function() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    });
  });