# Criar arquivo para leitura;
# - Leitura do arquivo;
# Criar permutacatacao;
# Criar soma das distancias;
# Plano cartesiano visualmente com o codigo;
# Criar grafico de tempo com representacao grafica;


#Permutacao:
def per(lista):
    if len(lista) <= 1:
        return [lista]
    lista_sobra = []
    for i, atual in enumerate(lista):
        elementos_restantes = lista[:i] + lista[i+1:]
        for diminuicao in per(elementos_restantes):
            lista_sobra.append([atual]+diminuicao)
    return lista_sobra

pontos = [1, 2, 3, 4]
print(per(pontos))
