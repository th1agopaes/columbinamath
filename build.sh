#!/usr/bin/env bash
# Constrói e inicia a aplicação em containers (Podman ou Docker) e carrega os conteúdos.
# Uso, na raiz do repositório: ./build.sh
set -euo pipefail

if command -v podman >/dev/null 2>&1; then
  compose="podman compose"
elif command -v docker >/dev/null 2>&1; then
  compose="docker compose"
else
  echo "Instale o Podman ou o Docker para executar em containers." >&2
  exit 1
fi

if [ ! -f backend/.env ]; then
  echo "Crie o backend/.env a partir do backend/.env.example antes de continuar." >&2
  exit 1
fi

echo "==> Construindo e iniciando os containers com: $compose"
$compose up --build --detach

echo "==> Carregando os conteúdos da trilha"
$compose exec web python manage.py loaddata conteudos regra_de_sinais

echo "==> Pronto: http://localhost:8000"
echo "    Criar o administrador: $compose exec web python manage.py createsuperuser"
echo "    Ver os logs:           $compose logs --follow web"
echo "    Parar:                 $compose down"
