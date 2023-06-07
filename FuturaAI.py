import os
import time
import random

# Variavel booleana para determinar o estado do nosso programa
iniciar_programa = True


# Menu principal contendo o loop do nosso programa


def main():
    msg_bem_vindo()

    while iniciar_programa:
        clean_prompt()

        print(""" 
        ========================
                Menu Geral
        ======================== 
        
        Selecione uma das nossa ferramentas:
        1 - Recomendação de cultivo com base em fatores ambientais
        2 - Previsão de colheira
        3 - Planejamento da cadeia produtiva
        4 - Otimização de insumos
        5 - Sair
        
        """)

        opcao = selecao_menu("Escolha uma das nossas ferramentas: ", 1, 5)

        if opcao == 0:
            print("\nOpção não válida")
        elif opcao == 1:
            recomendacao_cultivo()
        elif opcao == 2:
            previsão_colheita()
        elif opcao == 3:
            planejamento_cadeia_produtiva()
        elif opcao == 4:
            otimizacao_insumos()
        elif opcao == 5:
            break


# Função responsavel captar o input do usuario e verificar se o menu escolhido existe
def selecao_menu(frase, op_inicial, op_final):
    menu_opcao = int(input(frase))

    if op_inicial <= menu_opcao <= op_final:
        return menu_opcao
    else:
        return 0


# Mensagens de boas vindas
def msg_bem_vindo():
    clean_prompt()
    print(f"""
    ======================== 
     
    Bem vindo a aplicação da Futura AI
    
    Aqui você podera simular algumas aplicações que podem ser
    automatizadas com o uso de inteligências artificais.
    
    ======================== 
    """)

    tempo("Carregando menu.", 2)


# Ferramenta 1 - Função responsavel por fazer a simulação de recomendação de cultivo com base em fatores ambientais
def recomendacao_cultivo():
    clean_prompt()
    print(f"""
    ========================
    Recomendação de Cultivo
    ======================== 

    Esta ferramenta ira fornecer  a cultura mais adequada com base
    nas condições de solo fornecido, previsão de chuva anual e a 
    temperatura média.
    
    """)
    resp = captar_decisao()

    if resp == 1:
        tempo("Carregando aplicação.", 2)
        recomendacao_cultivo_main()
    elif resp == 2:
        tempo("Voltando para o menu.", 2)
        main()
    else:
        print("Resposta incompativel.")
        tempo("Voltando para o menu.", 2)
        main()


# Função responsavel por pegar os inputs dos atributos necessarios
def recomendacao_cultivo_main():
    clean_prompt()
    print(f"""
    ========================
    Recomendação de Cultivo
    ======================== 
    
    Forneça os seguintes dados para calcularmos a melhor recomendação:
    
    """)

    tipo_solo = input("Digite o tipo de solo (argiloso, arenoso, calcario): ")
    quantidade_chuva = float(input("Digite a quantidade de chuva anual (mm): "))
    temperatura_media = float(input("Digite a temperatura média anual: "))

    cultura_ideal = recomendacao_cultura(tipo_solo, quantidade_chuva, temperatura_media)

    if cultura_ideal != None:
        print("A cultura que recomendamos para o plantio: " + cultura_ideal)
    else:
        print("Não foi possível recomendar uma cultura com base nas informações fornecidas.")

    input("\nPressione qualquer tecla para voltar para o menu")


# Função responsavel por executar a logica da ferramenta 1
def recomendacao_cultura(tipo_solo, quantidade_chuva, temperatura_media):
    if tipo_solo == "argiloso":
        if quantidade_chuva >= 800 and temperatura_media >= 25:
            return "Arroz"
        elif quantidade_chuva >= 500 and temperatura_media >= 20:
            return "Trigo"

    elif tipo_solo == "arenoso":
        if quantidade_chuva >= 600 and temperatura_media >= 30:
            return "Milho"
        elif quantidade_chuva >= 400 and temperatura_media >= 25:
            return "Feijão"

    elif tipo_solo == "calcario":
        if quantidade_chuva >= 700 and temperatura_media >= 22:
            return "Uva"
        elif quantidade_chuva >= 300 and temperatura_media >= 18:
            return "Laranja"
    else:
        return None


# Ferramenta 2 - Com base na colheita anterior e na demanda necessaria, calculamos uma média de colheita ao longo do ano
def previsão_colheita():
    clean_prompt()
    print(f"""
    ========================
      Previsão de Colheita
    ======================== 

    Esta ferramenta ira fornecer  média da colheita para o próximo mês
    com base na colheita do mês anterior e na demanda necessaria.

    """)
    resp = captar_decisao()

    if resp == 1:
        tempo("Carregando aplicação.", 2)
        previsão_colheita_main()
    elif resp == 2:
        tempo("Voltando para o menu.", 2)
        main()
    else:
        print("Resposta incompativel.")
        tempo("Voltando para o menu.", 2)
        main()


# Função responsavel por pegar os inputs dos atributos necessarios para executar a ferramenta 2
def previsão_colheita_main():
    clean_prompt()
    print(f"""
    ========================
      Previsão de Colheita
    ======================== 

    Forneça os seguintes dados para calcularmos a previsão de colheita:

    """)

    colheita_atual = float(input("Digite a quantidade de alimentos colhidos no mês atual (em toneladas): "))

    previsao_colheita, previsao_demanda, probabilidade_positiva, probalidade_negativa = preverDemanda(colheita_atual)

    print("\nPrevisão de Colheitas e Demanda:")
    print(f"Previsão da colheita para o próximo mês: {previsao_colheita:.2f} toneladas")
    print(f"Previsão de demanda para o próximo mês: {previsao_demanda:.2f} toneladas")
    print(f"Probabilidade de aumento na demanda: {probabilidade_positiva * 100:.2f}%")
    print(f"Probabilidade de redução na demanda: {probalidade_negativa * 100:.2f}%")

    input("\nPressione qualquer tecla para voltar para o menu")


def preverDemanda(colheitaAtual):
    # Nesta função, usamos um valor aleatório dentro de uma faixa específica para criar uma randomização na probabilidade
    previsaoColheita = colheitaAtual * random.uniform(0.8, 1.2)
    previsaoDemanda = colheitaAtual * random.uniform(0.8, 1.2)
    probabilidadePositiva = random.uniform(0, 0.2)
    probabilidadeNegativa = random.uniform(0, 0.2)

    return previsaoColheita, previsaoDemanda, probabilidadePositiva, probabilidadeNegativa


# Ferramenta 3 - Previsão para programação da cadeia produtiva com base em dados de produção, demanda e condições climaticas
def planejamento_cadeia_produtiva():
    clean_prompt()
    print(f"""
    ========================
  Planejamento Cadeia Produtiva
    ======================== 

    Esta ferramenta vai te ajudar em uma das etapas da cadeia produtiva,
    aqui ajudamos a fazer uma previsão de ofertas e demandas futuras com 
    base nos dados atuais registrados.

    """)
    resp = captar_decisao()

    if resp == 1:
        tempo("Carregando aplicação.", 2)
        planejamento_cadeia_produtiva_main()
    elif resp == 2:
        tempo("Voltando para o menu.", 2)
        main()
    else:
        print("Resposta incompativel.")
        tempo("Voltando para o menu.", 2)
        main()


# Lógica da cadeia produtiva
def planejamento_cadeia_produtiva_main():
    clean_prompt()
    print(f"""
      ========================
    Planejamento Cadeia Produtiva
      ======================== 

      Forneça os seguintes dados para planejarmos a cadeia produtiva:

      """)

    # Exemplo com produção e demanda com dois produtos diferentes:
    dados_producao = {
        "milho": 500,  # 500 toneladas de milho produzidas
        "trigo": 300  # 300 toneladas de trigo produzidas
    }

    dados_demanda = {
        "milho": 400,  # 400 toneladas de milho demandadas
        "trigo": 200  # 200 toneladas de trigo demandadas
    }

    # Lógica do planejamento
    produto = input("Informe o tipo de produto (milho, trigo): ")

    if produto in dados_producao and produto in dados_demanda:
        producao_atual = dados_producao[produto]
        demanda_atual = dados_demanda[produto]

        print(f"Oferta atual de {produto}: {producao_atual} toneladas")
        print(f"Demanda atual de {produto}: {demanda_atual} toneladas")

        # Lógica de previsão
        oferta_futura, demanda_futura = prever_oferta_demanda(producao_atual, demanda_atual)

        print(f"Previsão de oferta futura de {produto}: {oferta_futura} toneladas")
        print(f"Previsão de demanda futura de {produto}: {demanda_futura} toneladas")

        # Lógica de programação
        quantidade_programada = programar_cadeia_suprimentos(oferta_futura, demanda_futura)

        print(f"Quantidade programada de {produto}: {quantidade_programada} toneladas")
    else:
        print("Produto inválido!")

    input("\nPressione qualquer tecla para voltar para o menu")


# Programa quantidade mínima entre oferta e demanda
def programar_cadeia_suprimentos(oferta_futura, demanda_futura):
    quantidade_programada = min(oferta_futura, demanda_futura)
    return quantidade_programada


# Lógica de previsão de oferta e demanda futura
def prever_oferta_demanda(producao_atual, demanda_atual):
    oferta_futura = int(producao_atual * 1.2)
    demanda_futura = int(demanda_atual * 0.8)
    return oferta_futura, demanda_futura


# Ferramenta 4 - Com base em dados como, temperatura, umidade do solo, ph do solo e tipo de cultura, calculamos a quantidade ideal de água, fertilizante e pesticida a serem aplicados para cada insumo
def otimizacao_insumos():
    clean_prompt()
    print(f"""
    ========================
      Otimização de Insumos
    ========================
    
    Está ferramenta vai te ajudara gerir melhor os insumos gastos
    na produção. Com base nos dados requisitados, determinamos a 
    quantidade ideal de água, fertilizante e persticida a serem
    aplicados.

        """)
    resp = captar_decisao()

    if resp == 1:
        tempo("Carregando aplicação.", 2)
        otimizacao_insumos_main()
    elif resp == 2:
        tempo("Voltando para o menu.", 2)
        main()
    else:
        print("Resposta incompativel.")
        tempo("Voltando para o menu.", 2)
        main()


# Função responsavel pela lógica da ferramenta de otimização de recursos
def otimizacao_insumos_main():
    clean_prompt()
    print(f"""
    ========================
      Otimização de Insumos
    ======================== 
    
    Forneça as informações corretamente, para
    calcularmos as melhores recomendações.

    """)

    temperatura = float(input("Informe a temperatura atual (em graus celsius): "))
    umidade_solo = float(input("Informe o nível de umidade do solo (em porcentagem): "))
    ph_solo = float(input("Informe o PH do solo (0 à 14): "))
    tipo_cultura = input("Infome o tipo de cultura (trigo, milho, arroz): ")

    exibir_dados = False

    match tipo_cultura:
        case "trigo":
            quantidade_agua = calcular_quantidade_agua(temperatura, umidade_solo)
            quantidade_fertilizante = calcular_quantidade_fertilizante(ph_solo)
            quantidade_pesticida = calcular_quantidade_pesticida(temperatura)
            exibir_dados = True
        case "milho":
            quantidade_agua = calcular_quantidade_agua(temperatura, umidade_solo)
            quantidade_fertilizante = calcular_quantidade_fertilizante(ph_solo)
            quantidade_pesticida = calcular_quantidade_pesticida(temperatura)
            exibir_dados = True
        case "arroz":
            quantidade_agua = calcular_quantidade_agua(temperatura, umidade_solo)
            quantidade_fertilizante = calcular_quantidade_fertilizante(ph_solo)
            quantidade_pesticida = calcular_quantidade_pesticida(temperatura)
            exibir_dados = True
        case _:
            print("Essa cultura ainda não está no nosso sistema.")

    if exibir_dados:
        print("Recomendações para a sua cultura:");
        print(f"Quantidade de água: {quantidade_agua} litros");
        print(f"Quantidade de fertilizante: {quantidade_fertilizante} kg");
        print(f"Quantidade de pesticida: {quantidade_pesticida} ml");

        input("\nPressione qualquer tecla para voltar para o menu")


# Calculamos quantidade de água com base na temperatura e umidade do solo
def calcular_quantidade_agua(temperatura, umidade_solo):
    return temperatura * umidade_solo * 0.1


# Calculamos a quantidade de fertilizante necessaria
def calcular_quantidade_fertilizante(ph_solo):
    return ph_solo * 0.5


# calculamos a quantidade de pesticida
def calcular_quantidade_pesticida(temperatura):
    return temperatura * 0.2


# Método para dar prosseguimento nas ferramentas desejadas
def captar_decisao():
    print("""
    Deseja prosseguir?

    Digite:
    1 - sim
    2 - não

    """)
    resp = int(input("Resposta: "))
    return resp


# Imprimimos uma mensagem de espera para o usuario antes de apagarmos o prompt e avançarmos para a outra tela
def tempo(frase, tempo_espera):
    print(frase + " Aguarde", tempo_espera, "segundos ")
    time.sleep(tempo_espera)


# Limpamos o prompt de comando
def clean_prompt():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


if __name__ == '__main__':
    main()
