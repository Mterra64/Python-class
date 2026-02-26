# Análise de Vendas de Bobinas de Papel com Arquivos

def ler_vendas_csv(arquivo_csv):
    import csv

    vendas = []
    with open(arquivo_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vendas.append(row)
    return vendas

def calcular_total_vendas(vendas):
    #total_vendas = sum(float(venda['Quantidade em Metros']) * float(venda['Preço por Metro']) for venda in vendas)
    total_vendas = 0

    for venda in vendas:
        quantidade = float(venda['Quantidade em Metros'])
        preco = float(venda['Preço por Metro'])
        total = quantidade * preco
        valor_total = valor_total + total
    return total_vendas

def calcular_media_preco_metro(vendas):
    total_quantidade = sum(float(venda['Quantidade em Metros']) for venda in vendas)
    total_vendas = calcular_total_vendas(vendas)
    media_preco_metro = total_vendas / total_quantidade
    return media_preco_metro

def encontrar_bobina_mais_cara(vendas):
    bobina_mais_cara = max(vendas, key=lambda x: float(x['Preço por Metro']))
    return bobina_mais_cara

def listar_bobinas_abaixo_preco(vendas, preco_limite):
    bobinas_abaixo_preco = [venda for venda in vendas if float(venda['Preço por Metro']) < preco_limite]
    return bobinas_abaixo_preco

def main():
    arquivo_csv = 'vendas_bobinas.csv'
    vendas = ler_vendas_csv(arquivo_csv)

    total_vendas = calcular_total_vendas(vendas)
    media_preco_metro = calcular_media_preco_metro(vendas)
    bobina_mais_cara = encontrar_bobina_mais_cara(vendas)
    preco_limite = float(input("Digite um preço limite por metro: "))
    bobinas_abaixo_preco = listar_bobinas_abaixo_preco(vendas, preco_limite)

    print(f"Total de vendas: R${total_vendas:.2f}")
    print(f"Média de preço por metro vendido: R${media_preco_metro:.2f}")
    print(f"Bobina mais cara vendida:")
    print(f"Número de Série: {bobina_mais_cara['Número de Série']}")
    print(f"Preço por Metro: R${bobina_mais_cara['Preço por Metro']:.2f}")

    if bobinas_abaixo_preco:
        print(f"Bobinas vendidas abaixo de R${preco_limite:.2f} por metro:")
        for bobina in bobinas_abaixo_preco:
            print(f"Número de Série: {bobina['Número de Série']}")
            print(f"Preço por Metro: R${bobina['Preço por Metro']:.2f}")
    else:
        print("Nenhuma bobina vendida abaixo do preço limite.")

if __name__ == "__main__":
    main()
