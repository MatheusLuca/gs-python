"""
Dados iniciais (mock) usados pela plataforma Prepila Dyson.

Estes dados simulam um cenário operacional já em andamento, com
satélites, estações receptoras, operações SBSP, registros de
monitoramento, anomalias e alertas. Servem para que o usuário/professor
consiga executar consultas, relatórios e a recomendação de IA já na
primeira execução, sem precisar cadastrar tudo manualmente.
"""

# Tuplas usadas como conjuntos imutáveis de valores válidos
STATUS_SATELITE = ("ativo", "inativo", "em manutencao")
STATUS_ESTACAO = ("ativa", "inativa", "em manutencao")
SEVERIDADES = ("baixo", "medio", "alto", "critico")
PRIORIDADES_ALERTA = ("baixa", "media", "alta", "critica")


def carregar_satelites():
    """Retorna a lista inicial de satélites cadastrados na plataforma."""
    return [
        {
            "id": "SAT-001",
            "nome": "Helios-1",
            "organizacao": "NASA",
            "status": "ativo",
            "capacidade_kw": 520.0,
        },
        {
            "id": "SAT-002",
            "nome": "Helios-2",
            "organizacao": "NASA",
            "status": "em manutencao",
            "capacidade_kw": 480.0,
        },
        {
            "id": "SAT-003",
            "nome": "SolarisJP",
            "organizacao": "JAXA",
            "status": "ativo",
            "capacidade_kw": 610.0,
        },
        {
            "id": "SAT-004",
            "nome": "Aether-EU",
            "organizacao": "ESA",
            "status": "ativo",
            "capacidade_kw": 550.0,
        },
    ]


def carregar_estacoes():
    """Retorna a lista inicial de estações receptoras."""
    return [
        {
            "id": "EST-001",
            "nome": "Receptora Cuiaba",
            "organizacao": "NASA",
            "status": "ativa",
            "localizacao": "Cuiaba-BR",
        },
        {
            "id": "EST-002",
            "nome": "Receptora Tokyo",
            "organizacao": "JAXA",
            "status": "ativa",
            "localizacao": "Tokyo-JP",
        },
        {
            "id": "EST-003",
            "nome": "Receptora Madrid",
            "organizacao": "ESA",
            "status": "em manutencao",
            "localizacao": "Madrid-ES",
        },
    ]


def carregar_monitoramentos():
    """Retorna registros simulados de monitoramento em tempo real."""
    return [
        {
            "id": "MON-001",
            "satelite_id": "SAT-001",
            "estacao_id": "EST-001",
            "data_hora": "2026-05-27 09:00",
            "energia_captada_kw": 510.0,
            "energia_transmitida_kw": 470.0,
        },
        {
            "id": "MON-002",
            "satelite_id": "SAT-001",
            "estacao_id": "EST-001",
            "data_hora": "2026-05-27 10:00",
            "energia_captada_kw": 505.0,
            "energia_transmitida_kw": 100.0,
        },
        {
            "id": "MON-003",
            "satelite_id": "SAT-003",
            "estacao_id": "EST-002",
            "data_hora": "2026-05-27 09:00",
            "energia_captada_kw": 600.0,
            "energia_transmitida_kw": 590.0,
        },
        {
            "id": "MON-004",
            "satelite_id": "SAT-004",
            "estacao_id": "EST-002",
            "data_hora": "2026-05-27 11:00",
            "energia_captada_kw": 540.0,
            "energia_transmitida_kw": 200.0,
        },
    ]


def carregar_anomalias():
    """Retorna a lista inicial de anomalias.

    Comeca vazia de proposito: as anomalias sao geradas em tempo de
    execucao pela opcao 5 (detectar_anomalias_e_gerar_alertas), a partir
    dos monitoramentos pre-carregados. Assim a demonstracao mostra a
    plataforma realmente detectando ocorrencias (severidade alto e
    critico) em vez de apenas exibir dados ja prontos.
    """
    return []


def carregar_alertas():
    """Retorna a lista inicial de alertas.

    Comeca vazia: cada alerta e criado automaticamente junto com a sua
    anomalia quando a opcao 5 e executada.
    """
    return []


def carregar_recomendacoes():
    """Retorna recomendações geradas pela IA da plataforma."""
    return []
