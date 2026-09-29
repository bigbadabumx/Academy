# Exercício 4: correção de bug

Tempo sugerido: 45 minutos

## Problema

A função `is_valid_order_amount` aceita o valor zero. Uma encomenda válida deve ter valor superior a zero.

## Critérios de aceitação

- `Decimal("0")` deve ser considerado inválido.
- Valores negativos continuam inválidos.
- Valores positivos continuam válidos.
- Deve existir um teste para o valor zero.

## Sugestão de branch

```text
bugfix/<nome>-reject-zero-amount
```

Começa por acrescentar o teste que demonstra o bug. Confirma que o teste falha, corrige a função e volta a executar todos os testes.

