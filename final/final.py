def le_assinatura():
    assinatura = []
    assinatura.append(float(input("Entre o tamanho médio de palavra: ")))
    assinatura.append(float(input("Entre a relação Type-Token: ")))
    assinatura.append(float(input("Entre a Razão Hapax Legomana: ")))
    assinatura.append(float(input("Entre o tamanho médio de sentença: ")))
    assinatura.append(float(input("Entre a complexidade média da sentença: ")))
    assinatura.append(float(input("Entre o tamanho médio de frase: ")))
    return assinatura

def calcula_assinatura(texto):
    sentencas = texto.split('.')
    frases = texto.split('!')
    tokens = texto.split()
    
    soma_tamanho_palavras = sum(len(palavra) for palavra in tokens)
    tamanho_palavras = soma_tamanho_palavras / len(tokens)
    
    type_token = len(set(tokens)) / len(tokens)
    
    hapax_legomana = 0
    for token in set(tokens):
        if tokens.count(token) == 1:
            hapax_legomana += 1
    hapax_legomana /= len(tokens)
    
    tamanho_sentencas = sum(len(sentenca.split()) for sentenca in sentencas) / len(sentencas)
    
    tamanho_frases = sum(len(frase.split()) for frase in frases) / len(frases)
    
    complexidade_sentencas = len(frases) / len(sentencas)
    
    return [tamanho_palavras, type_token, hapax_legomana, tamanho_sentencas, complexidade_sentencas, tamanho_frases]

def compara_assinatura(assinatura1, assinatura2):
    soma = 0
    for i in range(len(assinatura1)):
        soma += abs(assinatura1[i] - assinatura2[i])
    return soma / 6

def avalia_textos(textos, ass_cp):
    similaridade = []
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        similaridade.append(compara_assinatura(ass_texto, ass_cp))
    return similaridade.index(min(similaridade)) + 1

def main():
    ass_cp = le_assinatura()
    textos = []
    print("Digite os textos (pressione Enter para inserir um novo texto e Enter novamente para finalizar):")
    while True:
        texto = input()
        if texto == "":
            break
        textos.append(texto)
    indice_infectado = avalia_textos(textos, ass_cp)
    print(f"O autor do texto {indice_infectado} está infectado com COH-PIAH")

if __name__ == "__main__":
    main()
