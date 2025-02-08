FROM python:3.10-slim-buster

# Install PostgreSQL client tools
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["./wait-for-db.sh", "blogger-db", "python", "main.py"]