# Usa uma imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*


# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o diretório de trabalho
COPY . .

# Define a variável de ambiente para o Flask
ENV FLASK_APP=main.py

# Expõe a porta que o Flask usará
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "main.py"]