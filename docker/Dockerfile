FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://github.com/jwilder/dockerize/releases/download/v0.8.0/dockerize-linux-amd64-v0.8.0.tar.gz | tar -xz -C /usr/local/bin \
    && apt-get clean

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r .config/requirements.txt

EXPOSE 8080

CMD ["dockerize", "-wait", "tcp://mysql:3306", "-timeout", "30s", "python", "src/__main__.py"]