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
    return posicoes,torpedos

def guarda_posicoes(posicoes):
    import string
    letras = "ABCDEFGHIJLMNOPQRSTUVXZ"
    sequencia = "ABCDEFGHIJLMNOP"
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
                pos = pos[:len(pos) - 1]
            for i in range(tam):
                h,v = [0,0]
                if vertical:
                    v += i 
                else:
                    h += i
                novaLinha = letras[letras.find(pos[0])+v]
                novaColuna = str(int(pos[1:])+h)
                novaPosicao =  novaLinha+novaColuna 
                if novaPosicao in posicoes_ocupadas:
                    print('overwrite pieces validation')
                posicoes_ocupadas[novaPosicao] = idNavio
            idNavio += 1
    return