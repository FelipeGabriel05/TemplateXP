import titulo
import negocios
import resumo
import observacoes
import text

def Main():
    total_page = text.Total_pagina()
    pagina_atual = 0
    num_pagina = 1
    extract = {}
    while pagina_atual < total_page:    
        TemplateXP = {
            "Titulo da Nota": titulo.Titulo(0),
            "Corretora": titulo.Corretora(0),
            "Cliente": titulo.Cliente(0),
            "Negocios Realizados": negocios.Negocios(0),
            "Resumo dos Negocios": resumo.Resumo_negocios(0),
            "Observações": observacoes.Observacoes(0)
        }
        extract[f"Pagina_{num_pagina}"] = TemplateXP
        num_pagina += 1
        pagina_atual += 1

    return extract

if __name__ == '__main__':
    Main()
