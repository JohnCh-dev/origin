import requests

# --- НАСТРОЙКИ ---
# Замените 'YOUR_BOT_TOKEN' на токен вашего бота.
# Этот токен вы получаете от BotFather при создании бота.
BOT_TOKEN = '7510190936:AAHdvhyIL6hZFL2Hul8RaB4jFYqEYD4hJxs'

# Замените 'YOUR_CHAT_ID' на ID вашего чата или канала.
# Для личного чата с ботом, это ваш User ID.
# Для группового чата или канала, это ID чата/канала (может быть отрицательным числом).
# Узнать CHAT_ID можно, например, отправив боту сообщение и посмотрев обновления через API:
# https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
CHAT_ID = '282781888'

# Текст сообщения, которое вы хотите отправить.
MESSAGE_TEXT = 'Привет, мир!'
# --- КОНЕЦ НАСТРОЕК ---

def send_telegram_message(token, chat_id, text):
    """
    Отправляет текстовое сообщение в указанный чат Telegram через бота.

    :param token: Токен Telegram бота.
    :param chat_id: ID чата или канала для отправки сообщения.
    :param text: Текст сообщения.
    :return: Ответ от API Telegram в формате JSON или None в случае ошибки.
    """
    # URL для отправки сообщений через Telegram Bot API
    send_url = f"https://api.telegram.org/bot{token}/sendMessage"

    # Параметры запроса: ID чата и текст сообщения
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    try:
        # Выполняем POST-запрос к API Telegram
        response = requests.post(send_url, data=payload)
        # Поднимаем исключение, если ответ сервера содержит код ошибки HTTP (4xx или 5xx)
        response.raise_for_status()
        # Возвращаем ответ сервера в виде JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        # Обрабатываем возможные ошибки при выполнении запроса
        print(f"Ошибка при отправке сообщения: {e}")
        return None

# Основная часть скрипта, которая выполняется при его запуске
if __name__ == '__main__':
    # Вызываем функцию для отправки сообщения
    result = send_telegram_message(BOT_TOKEN, CHAT_ID, MESSAGE_TEXT)

    # Проверяем результат отправки
    if result and result.get('ok'):
        print("Сообщение успешно отправлено!")
        print(f"ID сообщения: {result['result']['message_id']}")
    else:
        print("Не удалось отправить сообщение.")
        if result:
            print(f"Ответ API: {result}") 