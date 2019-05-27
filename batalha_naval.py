def leia_arquivo(nome):
    arquivo = open(nome)
    dados = []
    for i in arquivo.read.split('\n'):
        dados.append(i)
    return dados