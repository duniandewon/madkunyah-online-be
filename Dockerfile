FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    gcc \
    libc-dev \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

WORKDIR /app
RUN uv sync --frozen --no-cache

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENV HOST=0.0.0.0
ENV PORT=8000

EXPOSE 8000

CMD ["/app/entrypoint.sh"]