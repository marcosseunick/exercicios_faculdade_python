import pandas as pd

arquivo_csv = 'vendas.csv'
arquivo_relatorio = 'relatorio.txt'

try:
    
    df = pd.read_csv(arquivo_csv, sep=';')

    
    df['data'] = pd.to_datetime(df['data']) 
    df['qtd'] = pd.to_numeric(df['qtd'])     
    df['preco'] = pd.to_numeric(df['preco'])   

    
    df['faturamento_linha'] = df['qtd'] * df['preco']

    faturamento_total = df['faturamento_linha'].sum()

    faturamento_por_produto = df.groupby('produto')['faturamento_linha'].sum()

    df['mes_ano'] = df['data'].dt.strftime('%Y-%m')

    faturamento_por_mes = df.groupby('mes_ano')['faturamento_linha'].sum()

    with open(arquivo_relatorio, 'w', encoding='utf-8') as f:
        
        f.write("RELATÓRIO DE VENDAS\n")
        f.write("=" * 30 + "\n\n")

        f.write(f"Faturamento Total: R$ {faturamento_total:,.2f}\n")
        f.write("-" * 30 + "\n\n")

        f.write("Faturamento por Produto:\n")

        for produto, total_prod in faturamento_por_produto.items():
            f.write(f"- {produto}: R$ {total_prod:,.2f}\n")
        f.write("-" * 30 + "\n\n")

        f.write("Faturamento por Mês (AAAA-MM):\n")

        for mes, total_mes in faturamento_por_mes.items():
            f.write(f"- {mes}: R$ {total_mes:,.2f}\n")
        
    print(f"Relatório gerado com sucesso: '{arquivo_relatorio}'")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    print("Verifique se o CSV possui as colunas 'data', 'produto', 'qtd', 'preco'.")