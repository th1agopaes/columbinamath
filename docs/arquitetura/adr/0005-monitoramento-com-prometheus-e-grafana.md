# ADR 0005: Monitorar a aplicação com Prometheus e Grafana

- **Status:** Aceito
- **Data:** 2026-11-26
- **Autor:** Thiago Paes de Barros Costa

## Contexto

O RNF001 exige que o feedback de um exercício não passe de 2 segundos, mas até aqui não havia como medir o tempo de resposta da aplicação em execução. O professor de Engenharia de Software indicou que o monitoramento não é obrigatório, mas pode entrar se for útil e profissional. Em 12/11 ele tinha ficado fora da Sprint 3; em 26/11 entrou como item Could, depois da modelagem inteira implementada.

## Decisão

- **Coleta:** a aplicação expõe métricas no formato do Prometheus com a biblioteca oficial `prometheus-client`:
  - `columbinamath_requisicoes_total`: requisições por método, página (view do Django) e código de status;
  - `columbinamath_tempo_resposta_segundos`: histograma do tempo de resposta, com uma faixa em 2 s para o RNF001;
  - `columbinamath_tentativas_total`: respostas dos alunos por resultado (acerto ou erro), uma métrica de negócio.
- **Exposição:** as métricas ficam numa porta própria (9100), aberta pelo Gunicorn (`post_worker_init` no `gunicorn.conf.py`) só quando a variável `METRICAS_PORTA` existe. O compose não publica essa porta no computador: só o Prometheus, na rede dos containers, consegue lê-la.
- **Armazenamento e painéis:** um container do Prometheus coleta as métricas a cada 15 s, e um container do Grafana mostra o painel "ColumbinaMath", criado automaticamente a partir de arquivos em `monitoring/`. O Prometheus e o Grafana só aceitam conexões do próprio computador (`127.0.0.1`).
- **Um processo do Gunicorn:** com um só processo (e 8 threads), todas as métricas ficam num único registro em memória, sem o modo multiprocesso do `prometheus-client`.

## Alternativas consideradas

- **Pacote `django-prometheus`.**
  Descartada: traz mais métricas prontas, mas não declara suporte ao Django 6.1, e um middleware próprio de 40 linhas mede o que o projeto precisa.
- **Rota `/metrics` no próprio site.**
  Descartada: deixaria as métricas públicas na porta 8000, junto com as páginas.
- **Vários processos do Gunicorn com o modo multiprocesso.**
  Descartada por enquanto: exige uma pasta compartilhada entre os processos e limpeza a cada reinício, sem ganho na escala atual. Fica como trabalho futuro se a aplicação precisar de mais processos.

## Consequências

### Positivas

- O RNF001 passa a ter evidência: o painel mostra o percentual de respostas em até 2 s e o percentil 95 do tempo de resposta.
- O painel também mostra o uso real do produto (acertos e erros dos alunos), útil para a validação com os estudantes.
- As métricas não ficam expostas no site.

### Negativas

- Dois containers a mais, com seus próprios volumes de dados.
- Os contadores voltam a zero quando o container da aplicação reinicia; o Prometheus guarda o histórico.
- O Grafana recebe o mesmo `backend/.env`, como o container do banco (ADR 0004).
