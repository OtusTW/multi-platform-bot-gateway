"""
Telegram message sender module - responsible only for sending messages.
"""

import logging
from typing import Optional

import httpx

from .config import TELEGRAM_API_BASE

logger = logging.getLogger(__name__)


async def send_message(
    chat_id: int, text: str, parse_mode: Optional[str] = None
) -> None:
    """Send a text message to a Telegram chat.

    Args:
        chat_id: Target chat ID.
        text: Message content.
        parse_mode: Optional parse mode (Markdown, HTML, etc.).
    """
    url = f"{TELEGRAM_API_BASE}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    if parse_mode:
        payload["parse_mode"] = parse_mode

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(url, json=payload)
            
            if response.status_code != 200:
                error_detail = response.json()
                logger.error(
                    f"Failed to send Telegram message. "
                    f"Status: {response.status_code} | "
                    f"Error: {error_detail}"
                )
            else:
                logger.info(f"Successfully sent message to chat_id: {chat_id}")
                
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error while sending message: {e.response.text}")
    except httpx.RequestError as e:
        logger.error(f"Request error while sending Telegram message: {e}")
    except Exception as e:  # pylint: disable=broad-except
        logger.exception("Unexpected error in send_message")