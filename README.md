# Prepila Dyson — Plataforma de Gerenciamento Operacional SBSP

**Global Solution 2026/1 — Computational Thinking Using Python (FIAP — 1TDS)**

---

## 1. Descrição da solução

O **Prepila Dyson** é uma plataforma de inteligência operacional voltada para
o gerenciamento de futuras infraestruturas de **Energia Solar Espacial
(SBSP — Space-Based Solar Power)**. Conforme satélites equipados com painéis
solares passam a transmitir energia para estações receptoras terrestres,
surge a necessidade de uma camada centralizada capaz de monitorar a
operação, integrar dados de múltiplas fontes, detectar anomalias, emitir
alertas e apoiar a tomada de decisão.

Este projeto entrega o **protótipo funcional em Python** dessa plataforma:
um sistema executado via terminal, com menu interativo, que simula o
fluxo operacional completo — cadastro de satélites e estações, registro
de monitoramentos de energia, detecção automática de anomalias,
geração de alertas priorizados, relatórios analíticos com estatísticas
operacionais, recomendações geradas por IA simulada e busca/filtros
sobre os dados. O Python é usado para automatizar a análise dos dados
orbitais, calcular eficiência energética e classificar a severidade das
ocorrências, transformando dados brutos em informação estratégica.

A solução conecta-se diretamente ao tema da Global Solution
(**economia espacial / nova fronteira tecnológica**) e contribui para os
**ODS 7, 9 e 13** (energia limpa, inovação e ação climática).

---

## 2. Conceitos técnicos aplicados (cobertura da rubrica)

| Conceito                              | Onde aparece no código |
|---------------------------------------|------------------------|
| `if-elif-else`                        | `severidade_para_prioridade`, validações de status em `registrar_monitoramento` |
| `match-case`                          | `classificar_eficiencia`, `buscar_satelites_por_filtro`, dispatcher do menu em `main` |
| `while`                               | Loop principal do menu, funções de validação (`ler_texto_obrigatorio`, `ler_numero_float`, `ler_opcao_de_tupla`, `ler_inteiro`) |
| `for`                                 | Iteração em `detectar_anomalias_e_gerar_alertas`, `gerar_relatorio_analitico`, `gerar_recomendacao_ia`, `listar_recursos`, `visualizar_alertas` |
| **Listas (`list`)**                   | Toda a base de dados (satélites, estações, monitoramentos, anomalias, alertas, recomendações) |
| **Tuplas (`tuple`)**                  | Conjuntos imutáveis de status válidos: `STATUS_SATELITE`, `STATUS_ESTACAO`, `SEVERIDADES`, `PRIORIDADES_ALERTA` |
| **Strings**                           | IDs, nomes, localizações, formatação tabular, `lower()`, `strip()`, `in` |
| **Funções com parâmetros e retorno**  | `gerar_proximo_id`, `classificar_eficiencia`, `buscar_por_id`, `gerar_relatorio_analitico`, `gerar_recomendacao_ia`, entre outras |
| **Procedimentos (sem retorno)**       | `exibir_menu`, `exibir_titulo`, `listar_recursos`, `visualizar_alertas` |
| **`def` / `import`**                  | Módulo `dados_iniciais.py` importado pelo `main.py` |
| **Validação de input do usuário**     | Todas as entradas passam por validadores dedicados |

---

## 3. Estrutura do projeto

```
python-gs/
├── main.py             # Programa principal com o menu e todas as funcionalidades
├── dados_iniciais.py   # Dados mock (satélites, estações, monitoramentos, anomalias, alertas)
└── README.md           # Este arquivo
```

---

## 4. Menu do sistema

O menu principal possui **10 opções funcionais + saída** (o requisito
mínimo é 5 itens, dos quais 4 devem ser protótipos funcionais
relacionados à GS):

| Opção | Funcionalidade                              | Descrição rápida |
|:-----:|---------------------------------------------|------------------|
| 1     | Sobre a solução                             | Texto descritivo curto (até 5 linhas) |
| 2     | Cadastrar satélite                          | Inclui novo satélite na plataforma |
| 3     | Cadastrar estação receptora                 | Inclui nova estação terrestre |
| 4     | Registrar monitoramento (energia)           | Insere leitura operacional (kW captado/transmitido) |
| 5     | Detectar anomalias e gerar alertas          | Analisa monitoramentos e cria anomalias + alertas |
| 6     | Listar recursos cadastrados                 | Tabela com satélites e estações |
| 7     | Relatório analítico                         | Estatísticas: energia total, eficiência média, anomalias por severidade |
| 8     | Recomendação IA                             | Sugestões baseadas em padrões dos dados |
| 9     | Buscar/filtrar satélites                    | Filtro por nome, organização ou status |
| 10    | Visualizar alertas                          | Lista alertas ordenados por prioridade |
| 0     | Sair                                        | Encerra o sistema |

---

## 5. Como executar

### Pré-requisitos

- **Python 3.10 ou superior** (o programa usa `match-case`).
  Verifique com:

  ```bash
  python --version
  ```

### Passo a passo

1. Abra um terminal na pasta do projeto (`python-gs/`).
2. Execute:

   ```bash
   python main.py
   ```

   No Windows, caso o comando acima abra a Microsoft Store, use:

   ```bash
   py main.py
   ```

3. Use o menu interativo digitando o número da opção desejada.

### Sequência sugerida para a apresentação / correção

1. Opção **1** — apresentar a descrição da solução.
2. Opção **6** — mostrar os dados pré-carregados (satélites e estações).
3. Opção **5** — rodar a detecção de anomalias sobre os dados iniciais
   (gera alertas críticos e altos automaticamente).
4. Opção **7** — exibir o relatório analítico.
5. Opção **8** — exibir as recomendações da IA simulada.
6. Opção **9** — fazer um filtro (por exemplo, status `ativo`).
7. Opção **2/3/4** — cadastrar um satélite, uma estação e um
   monitoramento, depois voltar à **5** e à **7** para mostrar que a
   plataforma reagiu aos novos dados.
8. Opção **10** — visualizar todos os alertas ordenados por prioridade.
9. Opção **0** — sair.

---

## 6. Regras de negócio implementadas

- Apenas satélites com status `ativo` podem participar de operações.
- Apenas estações com status `ativa` podem participar de operações.
- Energia captada e transmitida não podem ser negativas (validado na entrada).
- A severidade da anomalia é definida pela faixa de eficiência da
  transmissão:
  - ≥ 90% → sem anomalia
  - ≥ 75% → severidade `baixo`
  - ≥ 50% → severidade `medio`
  - ≥ 25% → severidade `alto`
  - <  25% → severidade `critico`
- Toda anomalia detectada gera automaticamente um alerta com prioridade
  proporcional à severidade.

---

## 7. Integrantes do grupo

> Preencha com os dados de cada integrante antes da entrega no portal:
>
> - **Nome completo:** _____________________ — **RM:** ______ — **Turma:** ______
> - **Nome completo:** _____________________ — **RM:** ______ — **Turma:** ______
> - **Nome completo:** _____________________ — **RM:** ______ — **Turma:** ______

Também inclua um arquivo `integrantes.txt` dentro do `.zip` final
contendo os mesmos dados, conforme exigido pelo regulamento.
