import text

def Observacoes(num_page):
    row = text.Pegar_texto(num_page)
    
    obj = {
        "Dados_1": row[-10],
        "Dados_2": row[-9],
        "Dados_3": row[-8],
        "Informacao_1": row[-7],
        "Informacao_2": row[-6],
        "Informacao_3": f"{row[-5]} {row[-4]}",
        "Informacao_4": f"{row[-3]} {row[-2]}",
        "Adicional": row[-1]
    }
    return obj
