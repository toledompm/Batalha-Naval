import sys

def leia_arquivo(nome):
    arquivo = open(nome)
    torpedos = []
    posicoes = {}
    tipos_navios = "1234"
    for i in arquivo.read().split('\n'):
        i = i.rstrip()
        if i[0] in tipos_navios:
            posicoes[i[0]] = i.split(';')[1].split('|')
        elif i[0] == 'T':
            torpedos = i.split(';')[1].split('|')
    arquivo.close()
    return {'posicoes':posicoes,'torpedos':torpedos}

def saida(t):
    arquivo = open('resultado.txt','w')
    arquivo.write(t)
    arquivo.close()
    sys.exit()

def validate_parts(jogador,idj):
    tamanho_esperado = {'1':5,'2':2,'3':10,'4':5,'T':25}
    for k,v in jogador['posicoes'].items():
        if len(v) != tamanho_esperado[k]:
            saida("J{} ERROR_NR_PARTS_VALIDATION".format(idj))
    if len(jogador['torpedos']) != tamanho_esperado['T']:
        saida("J{} ERROR_NR_PARTS_VALIDATION".format(idj))
    return

def validate_pos(linha,coluna,idj):
    if linha > 15 or linha < 0 or coluna > 15 or coluna < 0:
        return False
    return True

def validate_torpedos(torpedos,idj):
    for t in torpedos:
        letras = "ABCDEFGHIJLMNOPQRSTUVXZ"
        linha = letras.find(t[:1])
        colu = int(t[1:])
        if not validate_pos(linha,colu,idj):
            saida("J{} ERROR_POSITION_NONEXISTENT_VALIDATION".format(idj))
    return

def guarda_posicoes(posicoes,idj):
    pos_nonexistant = False
    letras = "ABCDEFGHIJLMNOPQRSTUVXZ"
    tamanhos = {'1':4,'2':5,'3':1,'4':2}
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
            h = 0
            v = 0
            for i in range(tam):
                novaLinha = letras.find(pos[0])+v
                novaColuna = int(pos[1:])+h
                if vertical:
                    v += 1 
                else:
                    h += 1
                if not validate_pos(novaLinha,novaColuna,idj):
                    pos_nonexistant = True
                novaPosicao =  str(novaLinha)+';'+str(novaColuna)
                if novaPosicao in posicoes_ocupadas:
                    saida("J{} ERROR_OVERWRITE_PIECES_VALIDATION".format(idj))
                posicoes_ocupadas[novaPosicao] = idNavio
            idNavio += 1
    if pos_nonexistant:
        saida("J{} ERROR_POSITION_NONEXISTENT_VALIDATION".format(idj))
    return posicoes_ocupadas

def bombardeios(torpedos,posicoes_ocupadas,idj):
    pontos = 0
    ids_acertadas = []
    for t in torpedos:
        letras = "ABCDEFGHIJLMNOPQRSTUVXZ"
        linha = letras.find(t[:1])
        colu = int(t[1:])
        posicao = str(linha)+';'+str(colu)
        if posicao in posicoes_ocupadas:
            pontos += 3
            idn = posicoes_ocupadas.pop(posicao)
            ids_acertadas.append(idn)
            if idn not in posicoes_ocupadas.values():
                pontos += 2
    acertos = len(set(ids_acertadas))
    erros = 22 - acertos
    return {'pontos':pontos,'alvos':erros,'acertos':acertos}

def main():
    jogador1 = leia_arquivo('jogador1.txt')
    jogador2 = leia_arquivo('jogador2.txt')

    validate_parts(jogador1,1)  
    validate_parts(jogador2,2)

    posicoes_ocupadas_j1 = guarda_posicoes(jogador1['posicoes'],1)
    validate_torpedos(jogador1['torpedos'],1)

    
    posicoes_ocupadas_j2 = guarda_posicoes(jogador2['posicoes'],2)
    validate_torpedos(jogador2['torpedos'],2)

    result1 = bombardeios(jogador1['torpedos'],posicoes_ocupadas_j2,1)
    result2 = bombardeios(jogador2['torpedos'],posicoes_ocupadas_j1,2)
    
    saida_txt = ''
    ambos = False
    if result1['pontos'] >= result2['pontos']:
        saida_txt += "J1 {}AA {}AE {}PT".format(result1['acertos'],result1['alvos'],result1['pontos'])
        ambos = True
    if result1['pontos'] <= result2['pontos']:
        if ambos:
            saida_txt += '\n'
        saida_txt += "J2 {}AA {}AE {}PT".format(result2['acertos'],result2['alvos'],result2['pontos'])
    saida(saida_txt)
    
main()
            

