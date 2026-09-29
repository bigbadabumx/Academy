# Notas do formador

## Preparação do repositório

1. Criar um repositório vazio no Azure DevOps.
2. Colocar o conteúdo desta pasta na branch `main`.
3. Proteger `main` contra push direto.
4. Exigir pelo menos um reviewer.
5. Ativar a verificação de resolução de comentários.
6. Confirmar acessos antes da academia.

## Sequência recomendada

1. Clone e exploração.
2. Branch com dois commits documentais.
3. Funcionalidade `average_order_value`.
4. Correção do valor zero.
5. Pull Request e review em pares.
6. Merge conflict deliberado.

## Solução da funcionalidade

Uma solução possível para `src/orders.py`:

```python
def average_order_value(orders: list[dict[str, str]]) -> Decimal:
    if not orders:
        return Decimal("0")
    return total_amount(orders) / len(orders)
```

O relatório deve chamar a função apenas com as encomendas concluídas.

## Solução do bug

Em `src/pricing.py`:

```python
return amount > Decimal("0")
```

Adicionar um teste que confirme que `Decimal("0")` devolve `False`.

## Merge conflict

Não indicar antecipadamente qual deve ser a frase final. O objetivo é os participantes perceberem que resolver um conflito requer uma decisão sobre o conteúdo, não apenas apagar marcadores.

Possível resultado acordado:

```python
REPORT_TITLE = "Completed sales by region"
```

