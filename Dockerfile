FROM python:3.11-slim-bookworm

# Prevent Python from writing .pyc files and buffer output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps: update (with a simple retry) and install required packages, then clean up
RUN set -eux; \
    retry_count=0; \
    until [ $retry_count -ge 3 ]; do \
      apt-get update && apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev gcc pkg-config libc6-dev \
      && break || { retry_count=$((retry_count+1)); echo "apt-get failed, retry $retry_count/3"; sleep 3; }; \
    done; \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
