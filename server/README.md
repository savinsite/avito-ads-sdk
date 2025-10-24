Avito Messenger Service (FastAPI skeleton)

Назначение
- Бэкенд-сервис для интеграции с Avito Messenger, к которому смогут обращаться фронтенд и n8n в одной сети.
- Сейчас развёрнута базовая структура проекта и эндпоинты-«заглушки» для дальнейшей интеграции с SDK Avito.

Структура
- Приложение:
  - Основной вход: [server/app/main.py](server/app/main.py:1)
  - Конфигурация: [server/app/core/config.py](server/app/core/config.py:1)
  - Роутер API v1 (мессенджер): [server/app/api/v1/messenger.py](server/app/api/v1/messenger.py:1)
  - Сервисный слой (заглушка): [server/app/services/messenger_service.py](server/app/services/messenger_service.py:1)
- Пакеты (инициализация): [server/__init__.py](server/__init__.py:1)
- Зависимости: [server/requirements.txt](server/requirements.txt:1)

Установка (локально)
1) Python venv
   - python -m venv .venv
   - .venv\Scripts\activate
2) Установка зависимостей
   - pip install -r server/requirements.txt

Запуск разработки
- Uvicorn (из корня репозитория):
  - uvicorn server.app.main:app --reload --host 0.0.0.0 --port 8000
- После запуска:
  - Healthcheck: GET http://localhost:8000/health
  - Swagger UI: http://localhost:8000/docs
  - ReDoc: http://localhost:8000/redoc

Переменные окружения
- HOST: адрес биндинга сервера (по умолчанию 0.0.0.0)
- PORT: порт сервера (по умолчанию 8000)
- ORIGINS: список разрешённых источников CORS, CSV (пример: http://localhost:3000,http://n8n.local)
- ACCESS_TOKEN: токен для доступа к API Avito (интеграция будет выполнена в сервисном слое)
- Значения читаются в [server/app/core/config.py](server/app/core/config.py:1)

API эндпоинты (черновик)
- GET /health
  - Возвращает {"status":"ok"}
- POST /api/v1/messenger/send-text
  - Тело (JSON):
    {
      "user_id": 123456789,
      "chat_id": "u2u-xxxxxxxxxxxxxxxxxxxx",
      "text": "Привет!"
    }
  - Сейчас возвращает 501 Not Implemented (интеграция с SDK будет добавлена в [server/app/services/messenger_service.py](server/app/services/messenger_service.py:1) и [server/app/api/v1/messenger.py](server/app/api/v1/messenger.py:1))

Интеграция с Avito SDK (план)
- Сервисный метод для отправки сообщения будет реализован в [MessengerService.send_text()](server/app/services/messenger_service.py:16)
- Роутер [send_text()](server/app/api/v1/messenger.py:17) вызывает сервисный слой.
- Будет использован SDK (клиент) для вызова [MessengerApi.post_send_message()](do_not_for_ai/avito_messenger/docs/MessengerApi.md:789) с [SendMessageRequestBody()](do_not_for_ai/avito_messenger/docs/SendMessageRequestBody.md:1)

Пример запроса (curl)
- Health:
  - curl -X GET http://localhost:8000/health
- Отправка текста (пока заглушка 501):
  - curl -X POST http://localhost:8000/api/v1/messenger/send-text ^
    -H "Content-Type: application/json" ^
    -d "{\"user_id\":123456789,\"chat_id\":\"u2u-xxxx\",\"text\":\"Привет!\"}"

Использование с фронтендом и n8n
- Для клиентов в одной сети (Docker, локальная сеть) настройте ORIGINS, чтобы CORS разрешал ваши источники.
- В n8n используйте HTTP Request node к базовому URL вашего сервиса, например http://avito-service:8000 (если это имя контейнера в docker-compose сети) или http://localhost:8000 при локальном запуске.

Дальнейшие шаги
- Реализовать отправку сообщения через SDK Avito в [server/app/services/messenger_service.py](server/app/services/messenger_service.py:1)
- Добавить Dockerfile и docker-compose.yml для развёртывания фронтенда, n8n и сервиса в одной сети (по мере необходимости)
- Добавить .env.example и загрузку переменных окружения из .env (при желании через python-dotenv)