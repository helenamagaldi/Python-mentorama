def formata_valor(v_in):
    s_out = '{:,.2f}'.format(v_in)
    s_out = s_out.replace(',', '_')
    s_out = s_out.replace('.', ',')
    s_out = s_out.replace('_', '.')
    return s_out        

nome_arq = 'lista_temp.txt'
    
with open(nome_arq) as farq:
    # pula o cabecalho
    linha = farq.readline()

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
    val_unit = '{:>10}'.format('UNIT')
    saida += val_unit
    # valor total
    val_total = '{:>12}'.format('TOTAL')
    saida += val_total
    print(saida)

    item = 0
    while True:
        linha = farq.readline()
        # chegou no final do arquivo?
        if linha == '':
            break
        # colunas estao separadas por virgula
        cols = linha.split(',')
        # atualiza item
        item += 1

        saida = ''
        # item
        saida += '{:03}'.format(item) + ' '
        # codigo
        saida += cols[0] + ' '
        # descricao do produto
        saida += '{:.<30.25}'.format(cols[1])
        # quantidade
        qtd = int(cols[2])
        saida += '{:03}'.format(qtd) + ' '
        # valor unitario
        val = float(cols[3])
        val_unit = '{:>10}'.format(formata_valor(val))
        saida += val_unit
        # valor total
        val *= qtd
        val_total = '{:>12}'.format(formata_valor(val))
        saida += val_total
        print(saida)
