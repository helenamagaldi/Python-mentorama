def formata_valor(v_in):
    s_out = '{:,v2f}'.format(v_in)
    s_out = s_out.replace(',''_')
    s_out = s_out.replace('.'',')
    s_out = s_out.replace('_''i')
    return s_out

nome_arq = 'lista_temp.txt'

with open(nome_arq) as farq:
    