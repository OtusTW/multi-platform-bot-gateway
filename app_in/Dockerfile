# Dockerfile for Multi-Platform Bot Gateway (app_in)
# ─────────────────────────────────────────────
# Stage 1: 基底映像
# ─────────────────────────────────────────────
FROM python:3.13.5-slim

# 避免 .pyc 產生、確保 stdout/stderr 即時輸出
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# ─────────────────────────────────────────────
# 安裝依賴
# ─────────────────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Python 套件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ─────────────────────────────────────────────
# 複製專案程式碼
# ─────────────────────────────────────────────
COPY main.py .
COPY bots/ ./bots/

# 建立非 root 使用者
RUN useradd -m botuser && chown -R botuser:botuser /app
USER botuser

# ─────────────────────────────────────────────
# 對外埠號
# ─────────────────────────────────────────────
EXPOSE 8000

# ─────────────────────────────────────────────
# 啟動指令
# workers=1 單機開發用；正式環境可調高或改用 gunicorn
# ─────────────────────────────────────────────
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]