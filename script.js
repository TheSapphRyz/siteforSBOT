// static/script.js
document.getElementById('button-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    var formData = new FormData(event.target);

    fetch(event.target.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        var responseContainer = document.getElementById('response-container');
        responseContainer.textContent = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
