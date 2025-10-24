from typing import Optional, Callable
from pydantic import BaseModel, Field

import avito_messenger
from avito_messenger.models.send_message_request_body import SendMessageRequestBody
from avito_messenger.models.send_message_request_body_message import SendMessageRequestBodyMessage
from avito_messenger.rest import ApiException


class SendResult(BaseModel):
    message_id: Optional[str] = Field(None, description="ID отправленного сообщения")
    status: str = Field(..., description="Состояние обработки")


class MessengerService:
    def __init__(self, access_token_provider: Optional[Callable[[], Optional[str]]] = None):
        """
        access_token_provider: Функция, возвращающая ACCESS_TOKEN из хранилища/окружения.
        Примечание: для этого сервиса токен передаётся пользователем на каждый запрос,
        поэтому провайдер может не использоваться.
        """
        self._access_token_provider = access_token_provider

    def send_text(self, authorization: str, user_id: int, chat_id: str, text: str) -> SendResult:
        """
        Отправка текстового сообщения через Avito Messenger API.

        Параметры:
        - authorization: Строка заголовка Authorization (например, 'Bearer xxxxx')
        - user_id: ID аккаунта в Авито
        - chat_id: Идентификатор чата
        - text: Текст сообщения (до 1000 символов)

        Возвращает:
        - SendResult с message_id и статусом отправки
        """
        # Готовим конфигурацию SDK
        configuration = avito_messenger.Configuration(host="https://api.avito.ru")

        try:
            # Создаём клиента и вызываем API
            with avito_messenger.ApiClient(configuration) as api_client:
                api = avito_messenger.MessengerApi(api_client)
                body = SendMessageRequestBody(
                    type="text",
                    message=SendMessageRequestBodyMessage(text=text),
                )
                resp = api.post_send_message(authorization, user_id, chat_id, body)

                # У ответа ожидается поле id
                msg_id = getattr(resp, "id", None)
                return SendResult(message_id=msg_id, status="sent")
        except ApiException:
            # Пробрасываем дальше для маппинга на HTTP-ошибку уровнем выше
            raise
        except Exception:
            # Любые иные исключения пробрасываем для корректной диагностики
            raise