// Функция для отправки данных на сервер
function sendData() {
    // Получаем chat_id из параметров URL
    const urlParams = new URLSearchParams(window.location.search);
    const chatId = urlParams.get('chat_id');

    // Отправляем POST-запрос на /web_app с chat_id
    fetch('/web_app', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ chat_id: chatId })
    })
    .then(response => response.text())
    .then(data => {
        console.log('Ответ от сервера:', data);
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
}
