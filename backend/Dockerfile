# Imagem da aplicação Django (ADR 0004). Construída a partir da raiz do repositório,
# porque precisa do backend/ e do frontend/: veja o docker-compose.yml.
FROM docker.io/library/python:3.14-slim

# uv copiado da imagem oficial, com a versão fixada
COPY --from=ghcr.io/astral-sh/uv:0.13.10 /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0 \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app/backend

# 1. Dependências primeiro: esta camada só é refeita quando o uv.lock muda
COPY backend/pyproject.toml backend/uv.lock backend/.python-version ./
RUN uv sync --locked --no-dev --no-install-project

# 2. Código da aplicação e camada de apresentação
COPY backend/ ./
COPY frontend/ /app/frontend/

# 3. Arquivos estáticos reunidos para o WhiteNoise (a chave aqui só existe no build)
RUN SECRET_KEY=somente-para-o-collectstatic python manage.py collectstatic --noinput

# 4. Usuário sem privilégios de administrador
RUN useradd --create-home --uid 1000 columbina \
    && chown -R columbina /app/backend
USER columbina

# 8000: site e API; 9100: métricas para o Prometheus (só na rede dos containers)
EXPOSE 8000 9100

ENTRYPOINT ["./entrypoint.sh"]
# As opções do servidor ficam no gunicorn.conf.py, lido automaticamente
CMD ["gunicorn", "config.wsgi:application"]
