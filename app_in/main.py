"""
Main router for incoming webhooks from Line and Telegram.
"""

import logging
from fastapi import FastAPI, Request

from bots.telegram.handler import handle_webhook as telegram_webhook_handler
from bots.line.handler import handle_webhook as line_webhook_handler

app = FastAPI(title="Multi-Platform Bot Gateway")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    """Telegram webhook endpoint."""
    return await telegram_webhook_handler(request)


@app.post("/line/webhook")
async def line_webhook(request: Request):
    """Line webhook endpoint."""
    return await line_webhook_handler(request)


@app.get("/")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "bot-gateway"}