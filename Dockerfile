# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN apt-get update && apt-get install -y build-essential libssl-dev \
    && pip install --no-cache-dir fastapi uvicorn sqlalchemy pymysql requests cryptography \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose the FastAPI port
EXPOSE 8081

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
