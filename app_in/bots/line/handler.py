"""
Line webhook handler - processes incoming events.
"""

import logging
from typing import Any, Dict

from fastapi import Request

from .sender import send_reply, push_message

logger = logging.getLogger(__name__)


async def handle_webhook(request: Request) -> Dict[str, str]:
    """Handle incoming Line webhook events."""
    try:
        body: Dict[str, Any] = await request.json()
        events: list = body.get("events", [])

        for event in events:
            if event.get("type") == "message" and event.get("message", {}).get("type") == "text":
                reply_token: str = event["replyToken"]
                user_id: str = event["source"]["userId"]
                user_text: str = event["message"]["text"]

                # === 立即先回覆（避免超過30秒）===
                await send_reply(reply_token, "正在思考中...")

                # === 這裡放你的長時間處理邏輯（例如呼叫 AI）===
                # response_text = await get_ai_response(user_text)   # 未來替換

                # 模擬長時間處理（測試用）
                # import asyncio
                # await asyncio.sleep(35)

                response_text = f"你說：{user_text}\n\n（這是 Push 示範）"

                # 使用 Push 方式發最終結果
                await push_message(user_id, response_text)

    except Exception as e:  # pylint: disable=broad-except
        logger.exception("Error processing Line webhook")

    return {"status": "ok"}