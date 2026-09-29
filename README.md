# Git Academy Python Mini Repository

Este repositório foi criado para praticar Git e Azure DevOps. O código Python é simples e usa apenas a biblioteca standard.

## Cenário

A aplicação lê clientes e encomendas a partir de ficheiros CSV e apresenta um pequeno relatório de vendas.

## Executar

Na raiz do repositório:

```bash
python -m src.main
```

No Windows também podes usar:

```powershell
py -m src.main
```

## Executar os testes

```bash
python -m unittest discover -s tests -v
```

## Estrutura

```text
git-academy-python-mini/
├── .azuredevops/
│   └── pull_request_template.md
├── data/
│   ├── customers.csv
│   └── orders.csv
├── docs/
│   └── team-rules.md
├── exercises/
├── src/
│   ├── config.py
│   ├── customers.py
│   ├── main.py
│   ├── orders.py
│   ├── pricing.py
│   └── reports.py
├── tests/
└── trainer/
    └── TRAINER_NOTES.md
```

## Workflow esperado

1. Atualizar a branch `main`.
2. Criar uma branch para a tarefa.
3. Alterar o código e os testes.
4. Rever o `git diff`.
5. Criar commits pequenos e claros.
6. Fazer `push` da branch.
7. Abrir um Pull Request.
8. Pedir review a um colega.
9. Corrigir o feedback no mesmo Pull Request.
10. Fazer merge depois das políticas passarem.

## Exercícios

- [01 - Clone e exploração](exercises/01-clone-and-explore.md)
- [02 - Primeira branch](exercises/02-first-branch.md)
- [03 - Nova funcionalidade](exercises/03-new-feature.md)
- [04 - Correção de bug](exercises/04-bugfix.md)
- [05 - Pull Request e review](exercises/05-pull-request.md)
- [06 - Merge conflict](exercises/06-merge-conflict.md)

