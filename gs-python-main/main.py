"""
PREPILA DYSON - Plataforma de Gerenciamento Operacional SBSP
Global Solution 2026/1 - Computational Thinking Using Python (FIAP - 1TDS)

Solucao computacional voltada para o gerenciamento de futuras
infraestruturas de Energia Solar Espacial (SBSP - Space-Based Solar
Power). O programa simula, via terminal, as principais funcionalidades
da plataforma Prepila Dyson: cadastro de satelites e estacoes
receptoras, registro de monitoramento operacional, deteccao de
anomalias, geracao de alertas, relatorios analiticos, busca e
recomendacoes de IA - tudo a partir de menus interativos.
"""

from dados_iniciais import (
    STATUS_SATELITE,
    STATUS_ESTACAO,
    SEVERIDADES,
    PRIORIDADES_ALERTA,
    carregar_satelites,
    carregar_estacoes,
    carregar_monitoramentos,
    carregar_anomalias,
    carregar_alertas,
    carregar_recomendacoes,
)


# ============================================================
# UTILITARIOS DE INTERFACE (USABILIDADE)
# ============================================================

def exibir_titulo(texto):
    """Imprime um titulo formatado em destaque.

    Parametros:
        texto (str): texto que sera exibido no titulo.
    Retorno:
        None (apenas imprime na tela).
    """
    linha = "=" * 60
    print("\n" + linha)
    print(texto.center(60))
    print(linha)


def exibir_subtitulo(texto):
    """Imprime um subtitulo formatado, com largura padronizada."""
    print("\n" + "-" * 60)
    print(f" {texto}")
    print("-" * 60)


def pausa():
    """Pausa a execucao ate o usuario pressionar ENTER."""
    input("\n>> Pressione ENTER para voltar ao menu...")


# ============================================================
# VALIDACOES E LEITURA SEGURA DE DADOS
# ============================================================

def ler_texto_obrigatorio(rotulo):
    """Le uma string nao vazia do usuario, validando entrada.

    Parametros:
        rotulo (str): mensagem mostrada antes do input.
    Retorno:
        str: texto digitado pelo usuario (sem espacos nas pontas).
    """
    while True:
        valor = input(f"{rotulo}: ").strip()
        if valor:
            return valor
        print("[ERRO] Campo obrigatorio. Digite um valor valido.")


def ler_numero_float(rotulo, minimo=0.0, maximo=1_000_000.0):
    """Le um numero decimal (float) garantindo intervalo valido.

    Parametros:
        rotulo (str): mensagem mostrada antes do input.
        minimo (float): valor minimo aceito (padrao 0.0).
        maximo (float): valor maximo aceito (padrao 1_000_000.0).
    Retorno:
        float: numero validado dentro do intervalo.
    """
    while True:
        bruto = input(f"{rotulo} (formato: numero decimal, ex: 480.5): ").strip()
        bruto = bruto.replace(",", ".")
        try:
            valor = float(bruto)
        except ValueError:
            print("[ERRO] Valor invalido. Use apenas numeros (ex: 480.5).")
            continue
        if valor < minimo or valor > maximo:
            print(f"[ERRO] Valor fora do intervalo permitido ({minimo} a {maximo}).")
            continue
        return valor


def ler_opcao_de_tupla(rotulo, opcoes):
    """Le uma opcao restrita a uma tupla de valores validos.

    Parametros:
        rotulo (str): mensagem antes do input.
        opcoes (tuple): tupla com opcoes validas (strings).
    Retorno:
        str: opcao validada (em minusculo).
    """
    opcoes_formatadas = " | ".join(opcoes)
    while True:
        valor = input(f"{rotulo} [{opcoes_formatadas}]: ").strip().lower()
        if valor in opcoes:
            return valor
        print(f"[ERRO] Opcao invalida. Use uma de: {opcoes_formatadas}")


def ler_inteiro(rotulo, minimo=0, maximo=99):
    """Le um inteiro dentro de um intervalo - usado para opcoes do menu."""
    while True:
        bruto = input(f"{rotulo}: ").strip()
        if not bruto.isdigit():
            print("[ERRO] Digite apenas numeros inteiros.")
            continue
        valor = int(bruto)
        if valor < minimo or valor > maximo:
            print(f"[ERRO] Opcao fora do intervalo ({minimo}-{maximo}).")
            continue
        return valor


# ============================================================
# GERACAO DE IDENTIFICADORES
# ============================================================

def gerar_proximo_id(lista, prefixo):
    """Gera um novo ID sequencial baseado nos itens ja existentes.

    Parametros:
        lista (list): lista de dicionarios ja cadastrados.
        prefixo (str): prefixo do ID (ex: 'SAT', 'EST', 'MON').
    Retorno:
        str: novo ID no formato PREFIXO-NNN (ex: SAT-005).
    """
    if not lista:
        return f"{prefixo}-001"
    numeros = []
    for item in lista:
        partes = item["id"].split("-")
        if len(partes) == 2 and partes[1].isdigit():
            numeros.append(int(partes[1]))
    proximo = (max(numeros) + 1) if numeros else 1
    return f"{prefixo}-{proximo:03d}"


# ============================================================
# DESCRICAO DA SOLUCAO (OPCAO 1 DO MENU - ATE 5 LINHAS)
# ============================================================

def exibir_descricao_solucao():
    """Exibe um resumo curto do projeto (no maximo 5 linhas)."""
    exibir_titulo("SOBRE A SOLUCAO - PREPILA DYSON")
    print("Plataforma de gerenciamento operacional para infraestruturas")
    print("de Energia Solar Espacial (SBSP). Centraliza monitoramento,")
    print("deteccao de anomalias, alertas, relatorios analiticos e")
    print("recomendacoes de IA para satelites e estacoes receptoras,")
    print("transformando dados orbitais em inteligencia operacional.")


# ============================================================
# CADASTROS (SATELITES E ESTACOES)
# ============================================================

def cadastrar_satelite(satelites):
    """Cadastra um novo satelite na plataforma.

    Parametros:
        satelites (list): lista de satelites ja cadastrados.
    Retorno:
        dict: satelite recem cadastrado.
    """
    exibir_titulo("CADASTRO DE SATELITE")
    nome = ler_texto_obrigatorio("Nome do satelite")
    organizacao = ler_texto_obrigatorio("Organizacao responsavel")
    status = ler_opcao_de_tupla("Status operacional", STATUS_SATELITE)
    capacidade = ler_numero_float("Capacidade de geracao em kW", 0.1, 10_000.0)

    novo = {
        "id": gerar_proximo_id(satelites, "SAT"),
        "nome": nome,
        "organizacao": organizacao,
        "status": status,
        "capacidade_kw": capacidade,
    }
    satelites.append(novo)
    print(f"\n[OK] Satelite cadastrado com sucesso! ID gerado: {novo['id']}")
    return novo


def cadastrar_estacao(estacoes):
    """Cadastra uma nova estacao receptora.

    Parametros:
        estacoes (list): lista de estacoes ja cadastradas.
    Retorno:
        dict: estacao recem cadastrada.
    """
    exibir_titulo("CADASTRO DE ESTACAO RECEPTORA")
    nome = ler_texto_obrigatorio("Nome da estacao")
    organizacao = ler_texto_obrigatorio("Organizacao responsavel")
    localizacao = ler_texto_obrigatorio("Localizacao (cidade-pais)")
    status = ler_opcao_de_tupla("Status operacional", STATUS_ESTACAO)

    nova = {
        "id": gerar_proximo_id(estacoes, "EST"),
        "nome": nome,
        "organizacao": organizacao,
        "status": status,
        "localizacao": localizacao,
    }
    estacoes.append(nova)
    print(f"\n[OK] Estacao cadastrada com sucesso! ID gerado: {nova['id']}")
    return nova


# ============================================================
# LISTAGEM DE RECURSOS
# ============================================================

def listar_recursos(satelites, estacoes):
    """Mostra todos os satelites e estacoes cadastrados em formato tabular."""
    exibir_titulo("RECURSOS CADASTRADOS")

    exibir_subtitulo(f"SATELITES ({len(satelites)})")
    if not satelites:
        print("Nenhum satelite cadastrado.")
    else:
        print(f"{'ID':<8} {'NOME':<15} {'ORG':<8} {'STATUS':<15} {'CAP.(kW)':>10}")
        for s in satelites:
            print(
                f"{s['id']:<8} {s['nome']:<15} {s['organizacao']:<8} "
                f"{s['status']:<15} {s['capacidade_kw']:>10.1f}"
            )

    exibir_subtitulo(f"ESTACOES RECEPTORAS ({len(estacoes)})")
    if not estacoes:
        print("Nenhuma estacao cadastrada.")
    else:
        print(f"{'ID':<8} {'NOME':<20} {'ORG':<8} {'STATUS':<15} {'LOCAL':<15}")
        for e in estacoes:
            print(
                f"{e['id']:<8} {e['nome']:<20} {e['organizacao']:<8} "
                f"{e['status']:<15} {e['localizacao']:<15}"
            )


# ============================================================
# REGISTRO DE MONITORAMENTO
# ============================================================

def buscar_por_id(lista, id_busca):
    """Procura um item em uma lista de dicionarios pelo campo 'id'.

    Parametros:
        lista (list): lista de dicionarios.
        id_busca (str): id procurado.
    Retorno:
        dict | None: item encontrado ou None.
    """
    for item in lista:
        if item["id"].lower() == id_busca.lower():
            return item
    return None


def registrar_monitoramento(satelites, estacoes, monitoramentos):
    """Registra uma nova leitura operacional (energia captada x transmitida).

    Faz validacoes de regra de negocio:
      - Satelite/estacao precisam existir;
      - Satelite/estacao nao podem estar em manutencao ou inativos;
      - Valores de energia nao podem ser negativos.

    Parametros:
        satelites (list): lista de satelites.
        estacoes (list): lista de estacoes receptoras.
        monitoramentos (list): lista de monitoramentos ja registrados.
    Retorno:
        dict | None: registro criado ou None se cancelado.
    """
    exibir_titulo("REGISTRO DE MONITORAMENTO SBSP")

    if not satelites or not estacoes:
        print("[ERRO] Cadastre pelo menos um satelite e uma estacao antes.")
        return None

    listar_recursos(satelites, estacoes)

    sat_id = ler_texto_obrigatorio("\nID do satelite (ex: SAT-001)").upper()
    satelite = buscar_por_id(satelites, sat_id)
    if satelite is None:
        print("[ERRO] Satelite nao encontrado.")
        return None
    if satelite["status"] != "ativo":
        print(f"[ERRO] Satelite '{satelite['nome']}' esta '{satelite['status']}'.")
        print("       Apenas satelites ativos podem participar de operacoes.")
        return None

    est_id = ler_texto_obrigatorio("ID da estacao receptora (ex: EST-001)").upper()
    estacao = buscar_por_id(estacoes, est_id)
    if estacao is None:
        print("[ERRO] Estacao nao encontrada.")
        return None
    if estacao["status"] != "ativa":
        print(f"[ERRO] Estacao '{estacao['nome']}' esta '{estacao['status']}'.")
        print("       Apenas estacoes ativas podem participar de operacoes.")
        return None

    data_hora = ler_texto_obrigatorio("Data e hora da coleta (AAAA-MM-DD HH:MM)")
    energia_captada = ler_numero_float("Energia captada no espaco em kW", 0.0, 50_000.0)
    energia_transmitida = ler_numero_float(
        "Energia transmitida para a Terra em kW", 0.0, 50_000.0
    )

    if energia_transmitida > energia_captada:
        print("[AVISO] Energia transmitida maior que a captada - revise os dados.")

    registro = {
        "id": gerar_proximo_id(monitoramentos, "MON"),
        "satelite_id": satelite["id"],
        "estacao_id": estacao["id"],
        "data_hora": data_hora,
        "energia_captada_kw": energia_captada,
        "energia_transmitida_kw": energia_transmitida,
    }
    monitoramentos.append(registro)
    print(f"\n[OK] Monitoramento {registro['id']} registrado com sucesso.")
    return registro


# ============================================================
# DETECCAO DE ANOMALIAS E ALERTAS
# ============================================================

def classificar_eficiencia(eficiencia):
    """Classifica a eficiencia de transmissao em uma faixa de severidade.

    Usa match-case (Python 3.10+) para selecionar a categoria com base
    em faixas de eficiencia (energia transmitida / energia captada).

    Parametros:
        eficiencia (float): valor entre 0.0 e 1.0.
    Retorno:
        tuple[str, str]: (severidade, descricao) - severidade pertence
        a SEVERIDADES (ou 'ok' quando sem anomalia).
    """
    faixa = int(eficiencia * 100)
    match faixa:
        case f if f >= 90:
            return ("ok", "Operacao dentro do esperado")
        case f if f >= 75:
            return ("baixo", "Pequena perda de eficiencia detectada")
        case f if f >= 50:
            return ("medio", "Perda moderada de eficiencia (entre 25% e 50%)")
        case f if f >= 25:
            return ("alto", "Perda de eficiencia de transmissao acima de 25%")
        case _:
            return ("critico", "Perda de eficiencia de transmissao acima de 50%")


def severidade_para_prioridade(severidade):
    """Converte a severidade da anomalia em prioridade de alerta.

    Usa if/elif/else para mapear severidade -> prioridade do alerta.
    Parametros:
        severidade (str): valor pertencente a SEVERIDADES.
    Retorno:
        str: prioridade do alerta.
    """
    if severidade == "critico":
        return "critica"
    elif severidade == "alto":
        return "alta"
    elif severidade == "medio":
        return "media"
    else:
        return "baixa"


def detectar_anomalias_e_gerar_alertas(monitoramentos, anomalias, alertas):
    """Varre todos os monitoramentos e cria anomalias/alertas se necessario.

    Para cada monitoramento ainda nao analisado:
      - calcula a eficiencia de transmissao;
      - classifica a faixa em severidade (match-case);
      - se houver anomalia, registra a anomalia e gera um alerta.

    Parametros:
        monitoramentos (list): registros de monitoramento.
        anomalias (list): anomalias ja registradas.
        alertas (list): alertas ja gerados.
    Retorno:
        int: quantidade de novas anomalias detectadas nesta execucao.
    """
    exibir_titulo("DETECCAO DE ANOMALIAS E GERACAO DE ALERTAS")

    if not monitoramentos:
        print("Nenhum monitoramento registrado ainda.")
        return 0

    ids_ja_analisados = [a["monitoramento_id"] for a in anomalias]
    novas = 0

    for mon in monitoramentos:
        if mon["id"] in ids_ja_analisados:
            continue
        captada = mon["energia_captada_kw"]
        transmitida = mon["energia_transmitida_kw"]
        if captada <= 0:
            eficiencia = 0.0
        else:
            eficiencia = transmitida / captada
        severidade, descricao = classificar_eficiencia(eficiencia)

        if severidade == "ok":
            print(
                f"[OK]  {mon['id']} - eficiencia {eficiencia*100:5.1f}% "
                f"({mon['satelite_id']} -> {mon['estacao_id']})"
            )
            continue

        nova_anomalia = {
            "id": gerar_proximo_id(anomalias, "ANO"),
            "monitoramento_id": mon["id"],
            "severidade": severidade,
            "descricao": descricao,
            "data_hora": mon["data_hora"],
        }
        anomalias.append(nova_anomalia)

        prioridade = severidade_para_prioridade(severidade)
        novo_alerta = {
            "id": gerar_proximo_id(alertas, "ALE"),
            "anomalia_id": nova_anomalia["id"],
            "prioridade": prioridade,
            "lido": False,
            "data_hora": mon["data_hora"],
        }
        alertas.append(novo_alerta)
        novas += 1
        print(
            f"[!]   {mon['id']} - eficiencia {eficiencia*100:5.1f}% -> "
            f"anomalia {nova_anomalia['id']} (sev. {severidade}), "
            f"alerta {novo_alerta['id']} (prio. {prioridade})"
        )

    print(f"\nResumo: {novas} nova(s) anomalia(s) detectada(s).")
    return novas


# ============================================================
# RELATORIO ANALITICO
# ============================================================

def gerar_relatorio_analitico(satelites, estacoes, monitoramentos, anomalias):
    """Gera um relatorio textual com estatisticas operacionais.

    Calcula:
      - total de satelites/estacoes/monitoramentos/anomalias;
      - energia total captada e transmitida;
      - eficiencia media de transmissao;
      - quebra de anomalias por severidade.

    Parametros:
        satelites (list)
        estacoes (list)
        monitoramentos (list)
        anomalias (list)
    Retorno:
        dict: dicionario com os indicadores calculados.
    """
    exibir_titulo("RELATORIO ANALITICO - PREPILA DYSON")

    total_captada = 0.0
    total_transmitida = 0.0
    eficiencias = []
    for mon in monitoramentos:
        total_captada += mon["energia_captada_kw"]
        total_transmitida += mon["energia_transmitida_kw"]
        if mon["energia_captada_kw"] > 0:
            eficiencias.append(
                mon["energia_transmitida_kw"] / mon["energia_captada_kw"]
            )

    eficiencia_media = (sum(eficiencias) / len(eficiencias)) if eficiencias else 0.0

    contagem_severidade = {sev: 0 for sev in SEVERIDADES}
    for a in anomalias:
        if a["severidade"] in contagem_severidade:
            contagem_severidade[a["severidade"]] += 1

    print(f"Satelites cadastrados......: {len(satelites)}")
    print(f"Estacoes cadastradas.......: {len(estacoes)}")
    print(f"Monitoramentos registrados.: {len(monitoramentos)}")
    print(f"Anomalias detectadas.......: {len(anomalias)}")
    print(f"Energia total captada......: {total_captada:>10.2f} kW")
    print(f"Energia total transmitida..: {total_transmitida:>10.2f} kW")
    print(f"Eficiencia media de transm.: {eficiencia_media*100:>9.2f} %")

    exibir_subtitulo("Anomalias por severidade")
    for sev in SEVERIDADES:
        print(f"  {sev:<8}: {contagem_severidade[sev]}")

    return {
        "total_captada": total_captada,
        "total_transmitida": total_transmitida,
        "eficiencia_media": eficiencia_media,
        "contagem_severidade": contagem_severidade,
    }


# ============================================================
# RECOMENDACAO DE IA (SIMULADA)
# ============================================================

def gerar_recomendacao_ia(satelites, monitoramentos, anomalias, recomendacoes):
    """Gera uma recomendacao operacional baseada em padroes simples.

    A "IA" aqui e simulada: analisa o historico de anomalias e a
    eficiencia media por satelite, listando recomendacoes objetivas
    (manutencao preventiva, redistribuicao de carga, inspecao).

    Parametros:
        satelites (list)
        monitoramentos (list)
        anomalias (list)
        recomendacoes (list): lista onde a recomendacao sera armazenada.
    Retorno:
        list[str]: lista de recomendacoes geradas nesta execucao.
    """
    exibir_titulo("RECOMENDACAO IA - PREPILA DYSON")

    if not monitoramentos:
        print("Sem dados suficientes para gerar recomendacoes.")
        return []

    sugestoes = []

    eficiencia_por_satelite = {}
    contagem_por_satelite = {}
    for mon in monitoramentos:
        sid = mon["satelite_id"]
        if mon["energia_captada_kw"] > 0:
            ef = mon["energia_transmitida_kw"] / mon["energia_captada_kw"]
            eficiencia_por_satelite[sid] = eficiencia_por_satelite.get(sid, 0.0) + ef
            contagem_por_satelite[sid] = contagem_por_satelite.get(sid, 0) + 1

    for sid, soma in eficiencia_por_satelite.items():
        media = soma / contagem_por_satelite[sid]
        satelite = buscar_por_id(satelites, sid)
        nome = satelite["nome"] if satelite else sid
        if media < 0.5:
            sugestoes.append(
                f"[CRITICO] Satelite {nome} ({sid}) com eficiencia media "
                f"de {media*100:.1f}%. Recomenda-se inspecao tecnica imediata."
            )
        elif media < 0.75:
            sugestoes.append(
                f"[ATENCAO] Satelite {nome} ({sid}) com eficiencia media "
                f"de {media*100:.1f}%. Recomenda-se manutencao preventiva."
            )

    criticas = [a for a in anomalias if a["severidade"] == "critico"]
    if criticas:
        sugestoes.append(
            f"[ACAO] {len(criticas)} anomalia(s) critica(s) ativa(s) - "
            "redistribuir carga para satelites com maior eficiencia."
        )

    inativos = [s for s in satelites if s["status"] != "ativo"]
    if inativos:
        nomes = ", ".join(s["nome"] for s in inativos)
        sugestoes.append(
            f"[OPERACIONAL] Satelites fora de operacao: {nomes}. "
            "Avaliar retorno ao status ativo apos manutencao."
        )

    if not sugestoes:
        sugestoes.append(
            "[OK] Nenhum padrao critico identificado. Operacao saudavel."
        )

    for i, s in enumerate(sugestoes, start=1):
        print(f"{i}. {s}")
        recomendacoes.append({"texto": s, "status": "pendente"})

    return sugestoes


# ============================================================
# BUSCA E FILTROS
# ============================================================

def buscar_satelites_por_filtro(satelites):
    """Permite buscar satelites por nome, organizacao ou status.

    Demonstra:
      - uso de string (lower, in, comparacoes);
      - manipulacao de lista via list comprehension;
      - match-case para escolher o criterio de filtro.

    Parametros:
        satelites (list): lista de satelites.
    Retorno:
        list: lista filtrada de satelites.
    """
    exibir_titulo("BUSCA / FILTRO DE SATELITES")
    print("Criterios disponiveis:")
    print("  1 - Nome (contem)")
    print("  2 - Organizacao (igual)")
    print("  3 - Status (igual)")

    criterio = ler_inteiro("Escolha o criterio (1-3)", 1, 3)
    resultado = []

    match criterio:
        case 1:
            termo = ler_texto_obrigatorio("Trecho do nome").lower()
            resultado = [s for s in satelites if termo in s["nome"].lower()]
        case 2:
            org = ler_texto_obrigatorio("Organizacao").lower()
            resultado = [s for s in satelites if s["organizacao"].lower() == org]
        case 3:
            status = ler_opcao_de_tupla("Status", STATUS_SATELITE)
            resultado = [s for s in satelites if s["status"] == status]

    exibir_subtitulo(f"RESULTADO ({len(resultado)} encontrado(s))")
    if not resultado:
        print("Nenhum satelite atende ao filtro.")
    else:
        for s in resultado:
            print(
                f"  {s['id']} | {s['nome']:<15} | {s['organizacao']:<8} | "
                f"{s['status']:<15} | {s['capacidade_kw']:.1f} kW"
            )
    return resultado


# ============================================================
# VISUALIZACAO DE ALERTAS
# ============================================================

def visualizar_alertas(alertas, anomalias):
    """Lista os alertas operacionais ordenados por prioridade."""
    exibir_titulo("ALERTAS OPERACIONAIS")

    if not alertas:
        print("Nenhum alerta gerado ate o momento.")
        return

    ordem = {"critica": 0, "alta": 1, "media": 2, "baixa": 3}
    alertas_ordenados = sorted(alertas, key=lambda a: ordem.get(a["prioridade"], 99))

    print(f"{'ID':<8} {'PRIORIDADE':<10} {'LIDO':<5} {'DATA/HORA':<18} {'DESCRICAO'}")
    for alerta in alertas_ordenados:
        anomalia = buscar_por_id(anomalias, alerta["anomalia_id"])
        descricao = anomalia["descricao"] if anomalia else "(anomalia nao encontrada)"
        lido = "Sim" if alerta["lido"] else "Nao"
        print(
            f"{alerta['id']:<8} {alerta['prioridade']:<10} {lido:<5} "
            f"{alerta['data_hora']:<18} {descricao}"
        )


# ============================================================
# MENU PRINCIPAL
# ============================================================

def exibir_menu():
    """Mostra o menu principal do sistema."""
    exibir_titulo("PREPILA DYSON - MENU PRINCIPAL")
    print(" 1 - Sobre a solucao")
    print(" 2 - Cadastrar satelite")
    print(" 3 - Cadastrar estacao receptora")
    print(" 4 - Registrar monitoramento (energia)")
    print(" 5 - Detectar anomalias e gerar alertas")
    print(" 6 - Listar recursos cadastrados")
    print(" 7 - Relatorio analitico")
    print(" 8 - Recomendacao IA")
    print(" 9 - Buscar/filtrar satelites")
    print("10 - Visualizar alertas")
    print(" 0 - Sair")


def main():
    """Funcao principal: inicializa dados e entra no loop do menu."""
    satelites = carregar_satelites()
    estacoes = carregar_estacoes()
    monitoramentos = carregar_monitoramentos()
    anomalias = carregar_anomalias()
    alertas = carregar_alertas()
    recomendacoes = carregar_recomendacoes()

    print("\n" + "*" * 60)
    print("Bem-vindo(a) ao PREPILA DYSON".center(60))
    print("Gerenciamento Operacional SBSP - Demo Python".center(60))
    print("*" * 60)

    while True:
        exibir_menu()
        opcao = ler_inteiro("\nDigite a opcao desejada", 0, 10)

        match opcao:
            case 0:
                print("\nEncerrando o sistema. Ate a proxima missao!\n")
                break
            case 1:
                exibir_descricao_solucao()
            case 2:
                cadastrar_satelite(satelites)
            case 3:
                cadastrar_estacao(estacoes)
            case 4:
                registrar_monitoramento(satelites, estacoes, monitoramentos)
            case 5:
                detectar_anomalias_e_gerar_alertas(monitoramentos, anomalias, alertas)
            case 6:
                listar_recursos(satelites, estacoes)
            case 7:
                gerar_relatorio_analitico(satelites, estacoes, monitoramentos, anomalias)
            case 8:
                gerar_recomendacao_ia(satelites, monitoramentos, anomalias, recomendacoes)
            case 9:
                buscar_satelites_por_filtro(satelites)
            case 10:
                visualizar_alertas(alertas, anomalias)
            case _:
                print("[ERRO] Opcao invalida.")

        if opcao != 0:
            pausa()


if __name__ == "__main__":
    main()
