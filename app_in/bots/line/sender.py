"""
Line message sender module - responsible only for sending messages.
"""

import logging
from typing import Dict

import httpx

from .config import LINE_CHANNEL_ACCESS_TOKEN

logger = logging.getLogger(__name__)


async def send_reply(reply_token: str, text: str) -> None:
    """使用 replyToken 快速回覆（必須在30秒內使用）"""
    url = "https://api.line.me/v2/bot/message/reply"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
    }
    payload: Dict = {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": text}],
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(url, json=payload, headers=headers)
            if response.status_code != 200:
                logger.error(f"Reply failed: {response.text}")
            else:
                logger.info("Successfully sent reply")
    except Exception as e:  # pylint: disable=broad-except
        logger.exception("Error in send_reply")


async def push_message(user_id: str, text: str) -> None:
    """使用 Push Message 主動推送（無時間限制）"""
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
    }
    payload: Dict = {
        "to": user_id,
        "messages": [{"type": "text", "text": text}],
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(url, json=payload, headers=headers)
            if response.status_code != 200:
                logger.error(f"Push failed: {response.text}")
            else:
                logger.info(f"Successfully pushed message to user: {user_id}")
    except Exception as e:  # pylint: disable=broad-except
        logger.exception("Error in push_message")