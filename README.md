# Multi-Platform Bot Gateway

**中文** | **English**

---

### 專案簡介 / Project Introduction

**中文**  
一個基於 **FastAPI** 的多平台 Bot 接入層，支援 Telegram 與 Line Bot。採用模組化設計，將訊息接收與發送分離，方便後續擴展 AI 對話功能。

**English**  
A FastAPI-based multi-platform bot gateway that supports Telegram and Line Bot. It uses a modular design separating message receiving and sending logic, making it easy to extend with AI capabilities.

---

### 主要功能 / Key Features

**中文**
- Telegram Echo Bot（可快速擴展成 AI Bot）
- Line Bot 完整支援（解決 replyToken 30 秒限制，使用 Push Message）
- 接收（Handler）與發送（Sender）職責分離
- Docker 化部署，一鍵啟動
- 完整 logging 與錯誤處理

**English**
- Telegram Echo Bot (easily extendable to AI Bot)
- Full Line Bot support (solves 30-second replyToken limitation with Push Message)
- Separation of concerns: Handler vs Sender
- Docker ready for easy deployment
- Comprehensive logging and error handling

---

## 專案結構 / Project Structure

```bash
app_in/
├── main.py                 # FastAPI 主路由 / Main Router
├── .env                    # 環境變數 / Environment Variables
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── bots/
    ├── telegram/           # Telegram Bot 模組
    │   ├── config.py
    │   ├── sender.py
    │   └── handler.py
    └── line/               # Line Bot 模組
        ├── config.py
        ├── sender.py
        └── handler.py
