from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel, Field
from typing import Optional

from avito_messenger.rest import ApiException
from server.app.services.messenger_service import MessengerService


class SendTextRequest(BaseModel):
    bearer: Optional[str] = Field(None, description="Bearer токен (если не передан в заголовке Authorization)")
    user_id: int = Field(..., description="ID аккаунта в Авито")
    chat_id: str = Field(..., description="ID чата")
    text: str = Field(..., max_length=1000, description="Текст сообщения")


class SendTextResponse(BaseModel):
    message_id: Optional[str] = Field(None, description="ID отправленного сообщения")
    status: str = Field(..., description="Состояние обработки")


router = APIRouter(prefix="/messenger", tags=["messenger"])


@router.post("/send-text", response_model=SendTextResponse)
async def send_text(
    req: SendTextRequest,
    authorization: Optional[str] = Header(None, alias="Authorization"),
):
    """
    Эндпоинт отправки текстового сообщения.
    На вход:
    - Authorization: Bearer-токен пользователя (в заголовке запроса) ИЛИ
    - bearer: токен в теле JSON (альтернатива заголовку),
    - user_id, chat_id, text — в теле JSON.

    Токен не сохраняется в окружении; используется только из запроса.
    """
    # Получаем Bearer токен из заголовка или поля тела
    auth_value: Optional[str] = None
    if authorization:
        auth_value = authorization.strip()
        if not auth_value.lower().startswith("bearer "):
            auth_value = f"Bearer {auth_value}"
    elif req.bearer:
        auth_value = req.bearer.strip()
        if not auth_value.lower().startswith("bearer "):
            auth_value = f"Bearer {auth_value}"
    else:
        raise HTTPException(status_code=400, detail="Bearer token required: provide Authorization header or body field 'bearer'")

    service = MessengerService()
    try:
        result = service.send_text(
            authorization=auth_value,
            user_id=req.user_id,
            chat_id=req.chat_id,
            text=req.text,
        )
        return SendTextResponse(message_id=result.message_id, status=result.status)
    except ApiException as e:
        status_code = getattr(e, "status", 502)
        detail = getattr(e, "body", str(e))
        raise HTTPException(status_code=status_code, detail=detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Optional placeholder for future endpoints
@router.post("/send-image")
async def send_image():
    raise HTTPException(status_code=501, detail="Not implemented yet")