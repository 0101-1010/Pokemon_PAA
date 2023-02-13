import pandas as pd

def encontrar_linha(df, resposta):
    for index, row in df.iterrows():
        corresponde = True
        for coluna in df.columns[2:]:
            if row[coluna] != resposta[coluna]:
                corresponde = False
                break
        if corresponde:
            return row[df.columns[0]], row[df.columns[1]]
    return None

# Lê a planilha do Excel
df = pd.read_excel("hashpokemons.xlsx")

# Resposta esperada
resposta = {
    "coluna_pergunta_1": 0,
    "coluna_pergunta_2": 1,
    # ...
}

# Encontra a linha correta
linha = encontrar_linha(df, resposta)

if linha is not None:
    print("Linha encontrada:")
    print(linha)
else:
    print("Linha não encontrada")
