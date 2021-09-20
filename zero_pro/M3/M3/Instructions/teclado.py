while True:
    lido = input('Entre um numero: ')
    try:
        num = int(lido)
        print(f'Numero: {num}')
        print(b)
    except ValueError:
        print('Por favor, um numero')
    except:
        print('ops :(')
        
