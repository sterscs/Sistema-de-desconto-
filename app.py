# ============================================================
# Programa: Sistema de Desconto Progressivo
# Descrição: Aplica descontos de acordo com o valor da compra
# Autor: [Seu Nome]
# ============================================================

def calcular_desconto(valor_compra):
    """
    Calcula o percentual de desconto com base no valor da compra.
    Regras:
        - Menor que R$ 200,00 ........ 5%  de desconto
        - De R$ 200,00 a R$ 299,99 ... 10% de desconto
        - A partir de R$ 300,00 ...... 15% de desconto
    Retorna o percentual (em decimal) a ser aplicado.
    """
    if valor_compra < 200.00:
        return 0.05
    elif valor_compra < 300.00:
        return 0.10
    else:
        return 0.15


def main():
    """Funcao principal: le o valor, calcula e exibe o resultado."""
    try:
        # Solicita ao usuario o valor total da compra
        valor_compra = float(input("Informe o valor total da compra (R$): "))

        # Valida se o valor informado e positivo
        if valor_compra < 0:
            print("Erro: o valor da compra nao pode ser negativo.")
            return

        # Obtem o percentual de desconto de acordo com a regra
        percentual = calcular_desconto(valor_compra)

        # Calcula o valor do desconto e o total a pagar
        valor_desconto = valor_compra * percentual
        valor_final = valor_compra - valor_desconto

        # Exibe os resultados formatados com duas casas decimais
        print("\n----- Resumo da Compra -----")
        print(f"Valor original .....: R$ {valor_compra:,.2f}")
        print(f"Desconto aplicado ..: {percentual * 100:.0f}%")
        print(f"Valor do desconto ..: R$ {valor_desconto:,.2f}")
        print(f"Valor a pagar ......: R$ {valor_final:,.2f}")
        print("----------------------------")

    except ValueError:
        # Trata o caso em que o usuario digita algo que nao e numero
        print("Erro: por favor, insira um valor numerico valido.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()