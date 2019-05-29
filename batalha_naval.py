def leia_arquivo(nome):
    arquivo = open(nome)
    torpedos = []
    posicoes = {}
    tipos_navios = "1234"
    for i in arquivo.read.split('\n'):
        if i[0] in tipos_navios:
            posicoes[i] = i.split(';')[1].split('|')
        elif i[0] == 'T':
            torpedos = i.split(';')[1].split('|')
    arquivo.close()
    return posicoes,torpedos

def guarda_posicoes(posicoes):
    overwrite = False
    letras = "ABCDEFGHIJLMNOPQRSTUVXZ"
    tamanhos = {'1':1,'2':1,'3':1,'4':1}
    idNavio = 0
    posicoes_ocupadas = {}
    for key,val in posicoes.items():
        tam = tamanhos[key]
        for pos in val:
            vertical = True
            if pos[-1] in 'HV':
                if pos[-1] == 'H':
                    vertical = False
                pos = pos[:-1]
            h,v = [0,0]
            for i in range(tam):
                if vertical:
                    v += i 
                else:
                    h += i
                novaLinha = letras.find(pos[0])+v
                novaColuna = int(pos[1:])+h
                if novaLinha > 15 or novaLinha < 0 or novaColuna > 15 or novaColuna < 0:
                    print('position nonexistant')
                novaPosicao =  novaLinha+';'+novaColuna
                if novaPosicao in posicoes_ocupadas:
                    overwrite = True
                posicoes_ocupadas[novaPosicao] = idNavio
            idNavio += 1
    if overwrite:
        print('overwrite error')
    return posicoes_ocupadas