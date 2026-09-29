# Exercício 6: merge conflict

Tempo sugerido: 60 minutos

## Preparação

Trabalha em pares. Ambos os participantes criam uma branch a partir do mesmo commit de `main`.

O participante A altera em `src/config.py`:

```python
REPORT_TITLE = "Sales summary"
```

para:

```python
REPORT_TITLE = "Completed sales summary"
```

O participante B altera a mesma linha para:

```python
REPORT_TITLE = "Regional sales report"
```

Ambos fazem commit, push e abrem Pull Request. O participante A faz merge primeiro.

## Resolução do participante B

```bash
git fetch origin
git merge origin/main
git status
```

1. Abre `src/config.py`.
2. Identifica os marcadores do conflito.
3. Discute com o participante A qual deve ser o título final.
4. Remove os marcadores.
5. Executa a aplicação e os testes.
6. Conclui a resolução:

```bash
git add src/config.py
git commit
git push
```

