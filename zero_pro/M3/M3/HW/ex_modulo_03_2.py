import datetime as dt

def formata_valor(v_in):
    # 1 -> 0,01
    # 13456 -> 1.234,56
    s_out = '{:,.2f}'.format(v_in)
    s_out = s_out.replace(',', '_')
    s_out = s_out.replace('.', ',')
    s_out = s_out.replace('_', '.')
    return s_out        

def le_arq_cat(nome_arq):
    dict_cat = {}
    with open(nome_arq, 'rt') as farq:
        for linha in farq:
            # retira \n
            linha = linha.rstrip()
            # separa colunas por espaco
            cols = linha.split()
            # A  = Aguas, qtd 0, valor 0
            dict_cat[cols[0]] = [cols[1], 0, 0]
    return dict_cat
    
def le_arq_in(nome_arq):
    # le as linhas do arquivo em um gole so
    itens = []
    with open(nome_arq, 'rt') as farq:
        itens = farq.readlines()
    return itens

def monta_header():
    saida = ''
    # item
    saida += ' IT' + ' '
    # codigo
    saida += ' COD' + ' '
    # descricao do produto
    saida += '{:.<30.25}'.format('Produto')
    # quantidade
    saida += 'QTD' + ' '
    # valor unitario
    saida += '{:>10}'.format('VAL.UNI')
    # valor total
    saida += '{:>10}'.format('VAL.TOT')
    return saida

def monta_linha(item, cols, dict_cat):
    saida = ''
    # item
    i = int(item)
    saida += '{:03}'.format(i) + ' '
    # codigo
    saida += cols[0] + ' '
    # descricao do produto
    saida += '{:.<30.25}'.format(cols[1])
    # quantidade
    qtd = int(cols[2])
    saida += '{:03}'.format(qtd) + ' '
    # valor unitario
    val = float(cols[3])
    val_p = '{:>10}'.format(formata_valor(val))
    saida += val_p
    # valor total
    val *= qtd
    val_p = '{:>10}'.format(formata_valor(val))
    saida += val_p

    # atualiza dicionario das categorias para este item
    chave = cols[0][0]
    dict_cat[chave][1] += qtd
    dict_cat[chave][2] += val
    return saida

def escreve_arq_out(nome_arq, dict_cat, lista_itens):
    with open(nome_arq, 'wt') as farq:
        # varre a lista de itens
        for i, item in enumerate(lista_itens):
            # pula a 1a linha mas monta o header
            if i == 0:
                linha = monta_header()
                farq.write(linha + '\n')
                continue
            # retira \n e separa as colunas por virgula
            item = item.rstrip()
            cols = item.split(',')
            # monta linha de saida formatada
            linha = monta_linha(i, cols, dict_cat)
            farq.write(linha + '\n')

        # header das categorias
        saida = ''
        saida += '{:.<20}'.format('CATEGORIA')
        saida += 'QTD' + ' '
        saida += '{:>10}'.format('VAL.CAT')
        farq.write(saida + '\n')
        # valor total da compra
        val_total = 0
        for chave in dict_cat.keys():
            saida = ''
            saida += '{:.<20}'.format(dict_cat[chave][0])
            saida += '{:03}'.format(dict_cat[chave][1]) + ' '
            val = float(dict_cat[chave][2])
            # atualiza valor total da compra
            val_total += val
            val_p = '{:>10}'.format(formata_valor(val))
            saida += val_p
            farq.write(saida + '\n')

        # grava valor total de data da compra
        saida = 'TOTAL: R$ {:10}'.format(formata_valor(val_total))
        farq.write(saida + '\n')

        data_hora = dt.datetime.now()
        saida = data_hora.strftime('%d/%m/%Y %H:%M:%S')
        farq.write('DATA: ' + saida + '\n')
        
dict_cat = le_arq_cat('categorias.txt')
lista_itens = le_arq_in('lista_temp.txt')
# transacionar com cartao de credito/debito
escreve_arq_out('cupom_fiscal.txt', dict_cat, lista_itens)

