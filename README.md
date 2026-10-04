# site-monitor

API REST em Python (FastAPI) para monitorar a disponibilidade de sites. Evolução do [uptime-alert-slack](https://github.com/antoniomanol62-ux/uptime-alert-slack), que começou como um script em Bash.

> Em desenvolvimento.

## Como rodar

```bash
git clone https://github.com/antoniomanol62-ux/site-monitor.git
cd site-monitor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

A documentação interativa (Swagger) fica em `http://localhost:8000/docs`.

## Endpoints

- `GET /health`: verifica se a API está no ar
- `GET /sites`: lista os sites monitorados (por enquanto, uma lista fixa)

## Roadmap

- [x] API mínima com FastAPI
- [ ] Banco SQLite e cadastro de sites (`POST /sites`)
- [ ] Verificador em segundo plano com retry e alerta no Slack
- [ ] Página web que consome a API
- [ ] Testes com pytest e CI no GitHub Actions
- [ ] Docker Compose
