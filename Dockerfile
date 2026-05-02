FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY legal_mcp/ legal_mcp/

EXPOSE 8000

CMD ["python", "-m", "legal_mcp.server"]
