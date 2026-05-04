"""
Telegram webhook handler - processes incoming updates.
"""

import logging
from typing import Any, Dict

from fastapi import HTTPException, Header, Request

from .config import WEBHOOK_SECRET
from .sender import send_message

logger = logging.getLogger(__name__)


async def handle_webhook(
    request: Request,
    x_telegram_bot_api_secret_token: str = Header(None),
) -> Dict[str, str]:
    """Handle incoming Telegram webhook updates (Echo bot).

    Args:
        request: FastAPI request object.
        x_telegram_bot_api_secret_token: Secret token from Telegram header.

    Returns:
        Status response.
    """
    # Optional secret validation
    if WEBHOOK_SECRET and x_telegram_bot_api_secret_token != WEBHOOK_SECRET:
        logger.warning("Invalid webhook secret token received")
        raise HTTPException(status_code=403, detail="Forbidden")

    try:
        update: Dict[str, Any] = await request.json()

        if "message" in update:
            message = update["message"]
            chat_id: int = message["chat"]["id"]
            text: str = message.get("text", "")

            if text:
                await send_message(chat_id, f"你說：{text}")

    except Exception as e:  # pylint: disable=broad-except
        logger.exception("Error processing Telegram webhook")

    return {"status": "ok"}