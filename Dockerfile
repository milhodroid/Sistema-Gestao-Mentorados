# Usa a imagem oficial do Python
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema, incluindo distutils
RUN apt-get update && apt-get install -y \
    git \
    python3-distutils \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Configura um usuário específico do GitHub
ARG GITHUB_USER
ARG GITHUB_EMAIL
RUN git config --global user.name "$GITHUB_USER" && \
    git config --global user.email "$GITHUB_EMAIL"

# Expõe a porta do Django
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
