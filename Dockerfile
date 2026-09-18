FROM python:3.13-slim AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Pokemon.py server.py ./

FROM base AS development

ENV SERVER_PORT=5000
ENV HOST=0.0.0.0
ENV FLASK_DEBUG=1

EXPOSE 5000

CMD ["python", "server.py"]

FROM base AS production

ENV SERVER_PORT=5000
ENV HOST=0.0.0.0
ENV FLASK_DEBUG=0

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "server:app"]
