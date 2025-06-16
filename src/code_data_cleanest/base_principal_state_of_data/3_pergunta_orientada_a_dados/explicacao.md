## 1. Importação de BibliotecasAdd commentMore actions
O script inicia com a importação de diversas bibliotecas Python, cada uma com uma finalidade específica no processo de manipulação e análise de dados.

* Snippet de código
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import plotly.express as px
# from ydata_profiling import ProfileReport
import statsmodels.api as sm
```
---
## 2. Funções de Pré-processamento

O script define um conjunto de funções customizadas para realizar tarefas específicas de limpeza e transformação de dados.

### 2.1. clean_col_name(col_name)

Esta função é projetada para limpar e padronizar os nomes das colunas.

```python
# --- Funções de pré-processamento (Mantidas) ---
def clean_col_name(col_name):
    original_input = col_name
    if isinstance(col_name, tuple):
        col_name = "_".join(str(item).strip() for item in col_name)
    elif not isinstance(col_name, str):
        col_name = str(col_name)
    col_name = re.sub(r'[^\w\s-]', '', col_name).strip()
    col_name = re.sub(r'[-\s]+', '_', col_name)
    col_name = re.sub(r"_+", "_", col_name)
    col_name = col_name.strip("_")
    if not col_name: return f"col_limpa_vazia_{hash(original_input)}"
    if col_name and col_name[0].isdigit(): col_name = "_" + col_name
    return col_name
```

Explicação da Função clean_col_name:  
- Converte nomes de colunas que são tuplas em uma string única, unindo os elementos com underscores.  
- Converte nomes de colunas que não são strings para o tipo string.  
- Remove caracteres especiais (exceto alfanuméricos, espaços e hífens) e remove espaços em branco das extremidades.  
- Substitui sequências de hífens e/ou espaços por um único underscore.  
- Substitui múltiplos underscores consecutivos por um único underscore.  
- Remove underscores no início ou fim do nome da coluna.  
- Se, após a limpeza, o nome da coluna se tornar uma string vazia, um nome único é gerado usando um hash do nome original para evitar conflitos.  
- Se o nome da coluna limpo começar com um dígito, um underscore é prefixado para garantir que seja um identificador válido em muitos contextos de programação e análise.

### 2.2. extract_salary_lower_bound(salary_range_str)

Esta função extrai o limite inferior numérico de uma string que representa uma faixa salarial.

```python
def extract_salary_lower_bound(salary_range_str):
    if pd.isna(salary_range_str): return np.nan
    s = str(salary_range_str).lower().replace('r$', '').replace('.', '').replace('/mês', '').strip()
    match_de_a = re.search(r'de\s*(\d+)\s*a\s*(\d+)', s)
    if match_de_a: return float(match_de_a.group(1))
    match_acima_de = re.search(r'acima de\s*(\d+)', s)
    if match_acima_de: return float(match_acima_de.group(1))
    match_menos_de = re.search(r'menos de\s*(\d+)', s)
    if match_menos_de: return 0
    match_so_numeros = re.findall(r'\d+', s)
    if match_so_numeros: return float(match_so_numeros[0])
    return np.nan
```

Explicação da Função extract_salary_lower_bound:  
- Retorna np.nan se a entrada for nula (ausente).  
- Padroniza a string de entrada: converte para minúsculas, remove "R$", ".", "/mês", além de espaços em branco nas extremidades.  
- Utiliza expressões regulares para identificar e extrair o valor numérico correspondente ao limite inferior da faixa salarial, considerando os seguintes padrões:  
  - de X a Y: Retorna X.  
  - acima de X: Retorna X.  
  - menos de X: Retorna 0 (assumindo que o limite inferior é zero ou um valor mínimo).  
- Se nenhum dos padrões acima for encontrado, extrai o primeiro conjunto de dígitos da string.  
- Retorna np.nan se nenhum valor numérico puder ser extraído.  

### 2.3. map_uf_to_region(uf_series: pd.Series) -> pd.Series

Esta função mapeia uma série de siglas de Unidades Federativas (UF) do Brasil para suas respectivas regiões geográficas.

```python
def map_uf_to_region(uf_series: pd.Series) -> pd.Series:
    mapa_regioes = {
        'AC': 'Norte', 'AL': 'Nordeste', 'AP': 'Norte', 'AM': 'Norte', 'BA': 'Nordeste',
        'CE': 'Nordeste', 'DF': 'Centro-Oeste', 'ES': 'Sudeste', 'GO': 'Centro-Oeste',
        'MA': 'Nordeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste', 'MG': 'Sudeste',
        'PA': 'Norte', 'PB': 'Nordeste', 'PR': 'Sul', 'PE': 'Nordeste', 'PI': 'Nordeste',
        'RJ': 'Sudeste', 'RN': 'Nordeste', 'RS': 'Sul', 'RO': 'Norte', 'RR': 'Norte',
        'SC': 'Sul', 'SP': 'Sudeste', 'SE': 'Nordeste', 'TO': 'Norte'
    }
    uf_series_normalized = uf_series.astype(str).str.upper().str.strip()
    siglas_uf = list(mapa_regioes.keys())
    def extract_sigla(val):
        if val in siglas_uf: return val
        for sigla in siglas_uf:
            if f"({sigla})" in val or f" {sigla} " in val or val.endswith(f" {sigla}"): return sigla
        if "DISTRITO FEDERAL" in val: return "DF"
        if "SAO PAULO" in val: return "SP"
        if "RIO DE JANEIRO" in val: return "RJ"
        if "MINAS GERAIS" in val: return "MG"
        if "ESPIRITO SANTO" in val: return "ES"
        if "RIO GRANDE DO SUL" in val: return "RS"
        if "SANTA CATARINA" in val: return "SC"
        if "PARANA" in val: return "PR"
        return val
    uf_series_normalized = uf_series_normalized.apply(extract_sigla)
    mapped_series = uf_series_normalized.map(mapa_regioes)
    return mapped_series.fillna('Desconhecida')
```

Explicação da Função map_uf_to_region:  
- Define um dicionário `mapa_regioes` que associa cada sigla de UF à sua região correspondente.  
- Normaliza a série de UFs de entrada, convertendo para string, maiúsculas e removendo espaços.  
- Define uma subfunção `extract_sigla` que tenta identificar a sigla da UF dentro de uma string que pode conter informações adicionais (ex: "Nome da Cidade (SP)"). Esta subfunção também lida com nomes completos de alguns estados.  
- Aplica `extract_sigla` para obter as UFs padronizadas.  
- Utiliza o método `.map()` com `mapa_regioes` para traduzir as siglas das UFs para os nomes das regiões.  
- Valores que não puderam ser mapeados são preenchidos com `'Desconhecida'`.  

### 2.4. clean_experience_to_numeric(exp_val)

Esta função converte descrições textuais de tempo de experiência em valores numéricos (em anos).

```python
def clean_experience_to_numeric(exp_val):
    if pd.isna(exp_val):
        return np.nan
    s = str(exp_val).lower().strip()
    if 'menos de 1 ano' in s or 'menos de um ano' in s or '< 1 ano' in s:
        return 0.5
    if 'não tenho experiência' in s or 'sem experiência' in s:
        return 0
    numbers = re.findall(r'\d+\.?\d*', s)
    if numbers:
        return float(numbers[0])
    return np.nan
```

Explicação da Função clean_experience_to_numeric:  
- Retorna `np.nan` se o valor de entrada for nulo.  
- Padroniza a string de entrada (minúsculas, remoção de espaços).  
- Converte expressões específicas para valores numéricos:  
  - "menos de 1 ano" (ou variações) para 0.5 anos.  
  - "não tenho experiência" (ou variações) para 0 anos.  
- Se nenhum dos padrões acima for encontrado, utiliza expressões regulares para extrair o primeiro número (inteiro ou decimal) da string, que é assumido como o tempo de experiência em anos.  
- Retorna `np.nan` se nenhum valor numérico puder ser extraído.  

---

## 3. Configurações da Análise Exploratória de Dados (EDA)
Esta seção define configurações globais para o processo de EDA.

```python
eda_output_dir_script = 'visualizacoes_eda_script_univariada_final'
os.makedirs(eda_output_dir_script, exist_ok=True)
sns.set_style("whitegrid")
```

Explicação das Configurações:  
- `eda_output_dir_script`: Define uma string com o nome do diretório ('visualizacoes_eda_script_univariada_final') onde as visualizações ou outros artefatos gerados durante a EDA podem ser salvos.  
- `os.makedirs(eda_output_dir_script, exist_ok=True)`: Cria o diretório especificado. O parâmetro `exist_ok=True` impede que um erro seja levantado caso o diretório já exista.  
- `sns.set_style("whitegrid")`: Define o estilo padrão para os gráficos gerados pela biblioteca Seaborn como "whitegrid". Este estilo adiciona uma grade clara ao fundo dos gráficos, o que pode melhorar a legibilidade.  

---

## 4. Pipeline de Processamento de Dados  
O script segue um pipeline estruturado para carregar, limpar, selecionar e transformar os dados.

### 4.1. Carregar Dados  
A primeira etapa do pipeline é o carregamento do conjunto de dados a partir de um arquivo Excel.

```python
# --- 1. Carregar Dados ---
print("--- 1. Carregando Dados ---")
file_path = "Main_database (2).xlsx"
if not os.path.exists(file_path):
    print(f"ERRO: Arquivo de dados '{file_path}' não encontrado.")
    exit()
df_original = pd.read_excel(file_path)
print(f"Base de dados original carregada: {df_original.shape[0]} linhas, {df_original.shape[1]} colunas.")
```

Explicação do Carregamento de Dados:  
- O caminho para o arquivo de dados é definido na variável `file_path`.  
- O script verifica se o arquivo existe no caminho especificado. Se não existir, uma mensagem de erro é exibida e o script é encerrado.  
- Os dados do arquivo Excel são lidos para um DataFrame do Pandas chamado `df_original`.  
- As dimensões (número de linhas e colunas) do DataFrame carregado são impressas para confirmação.  

### 4.2. Limpeza Inicial de Nomes de Colunas  
Após o carregamento, os nomes das colunas do DataFrame são limpos e padronizados.

```python
# --- 2. Limpeza Inicial de Nomes de Colunas ---
print("\n--- 2. Limpando Nomes de Colunas ---")
df_cleaned_names = df_original.copy()
df_cleaned_names.columns = [clean_col_name(col) for col in df_original.columns]
print("Nomes de colunas limpos.")
```

Explicação da Limpeza de Nomes de Colunas:  
- Uma cópia do DataFrame original (`df_original`) é criada como `df_cleaned_names` para preservar os dados brutos.  
- A função `clean_col_name` (definida anteriormente) é aplicada a cada nome de coluna do `df_cleaned_names`.  
- Uma mensagem confirma a conclusão da limpeza dos nomes das colunas.  

### 4.3. Seleção dos Atributos para EDA  
Nesta etapa, colunas específicas são selecionadas do DataFrame para serem incluídas na Análise Exploratória de Dados.

```python
# --- 3. Selecionando Atributos para EDA ---
print("\n--- 3. Selecionando Atributos para EDA ---")
col_identifiers = {
    'P1_a_1': 'P1_a_1', 'P1_b': 'P1_b', 'P1_l': 'P1_l',
    'P2_h': 'P2_h', 'P2_i': 'P2_i', 'P1_i_1': 'P1_i_1_uf_onde_mora',
    'P2_f': 'P2_f_Cargo_Atual', 'P2_g': 'P2_g_Nivel'
}
df_eda = pd.DataFrame()
for original_key, pattern in col_identifiers.items():
    found_col_name = next((cn for cn in df_cleaned_names.columns if pattern.lower() in cn.lower()), None)
    if found_col_name:
        df_eda[original_key] = df_cleaned_names[found_col_name]
        print(f"Coluna '{original_key}' (mapeada de '{found_col_name}') selecionada.")
    else:
        print(f"Aviso: Padrão '{pattern}' para '{original_key}' não encontrado.")
if df_eda.empty or 'P2_h' not in df_eda.columns:
    print("ERRO: Colunas essenciais para EDA não encontradas ou 'P2_h' ausente.")
    exit()
print(f"Shape do DataFrame de EDA inicial: {df_eda.shape}")
```

Explicação da Seleção de Atributos:  
- Um dicionário `col_identifiers` é definido para mapear nomes de chaves internas (que se tornarão os nomes das colunas no `df_eda`) para padrões de texto. Estes padrões são usados para encontrar as colunas correspondentes no `df_cleaned_names` (após a limpeza dos nomes).  
- Um novo DataFrame vazio, `df_eda`, é inicializado.  
- O script itera sobre `col_identifiers`, procurando por colunas no `df_cleaned_names` cujos nomes (em minúsculas) contenham o padrão especificado (também em minúsculas).  
- Se uma coluna correspondente é encontrada, ela é adicionada ao `df_eda` com o nome da chave interna.  
- Avisos são emitidos se padrões não forem encontrados.  
- Uma verificação crítica é realizada para garantir que o `df_eda` não esteja vazio e que a coluna `'P2_h'` (presumivelmente uma coluna essencial, como salário) esteja presente. Se estas condições não forem atendidas, o script é encerrado.  
- As dimensões do `df_eda` inicial são impressas.  

### 4.4. Limpeza e Transformação dos Atributos Selecionados

Esta é a etapa final do pré-processamento, onde as colunas selecionadas no `df_eda` passam por transformações e limpezas mais detalhadas.

```python
# --- 4. Limpando e Transformando Atributos ---
print("\n--- 4. Limpando e Transformando Atributos ---")
# Processamento de Salário (P2_h)
if 'P2_h' in df_eda.columns:
    df_eda['salary_numeric_lower_bound'] = df_eda['P2_h'].apply(extract_salary_lower_bound)
    df_eda.dropna(subset=['salary_numeric_lower_bound'], inplace=True) # Remove linhas onde o salário não pôde ser convertido
    if not df_eda.empty:
        min_salary_eda = df_eda['salary_numeric_lower_bound'].min()
        max_salary_eda = df_eda['salary_numeric_lower_bound'].max()
        point_of_cut_eda = 7500.0
        print(f"Usando ponto de corte para EDA: {point_of_cut_eda}")
        eda_salary_labels = ["Salário Baixo", "Salário Alto"]

        if min_salary_eda == max_salary_eda: # Caso especial: todos os salários são iguais
            df_eda['faixa_salarial_eda_2cat'] = eda_salary_labels[0] if point_of_cut_eda >= min_salary_eda else eda_salary_labels[1]
        else:
            # Define bins e labels para pd.cut
            bins_eda, labels_eda_cut = ([min_salary_eda, max_salary_eda], [eda_salary_labels[1]]) if point_of_cut_eda <= min_salary_eda else \
                                  ([min_salary_eda, max_salary_eda], [eda_salary_labels[0]]) if point_of_cut_eda >= max_salary_eda else \
                                  ([min_salary_eda, point_of_cut_eda, max_salary_eda], eda_salary_labels)

            unique_bins_eda = sorted(list(set(bins_eda)))
            if len(unique_bins_eda) < 2: unique_bins_eda = [min_salary_eda, max_salary_eda]

            actual_labels = labels_eda_cut # Inicia com os labels determinados pela lógica de bins
            # Ajusta 'actual_labels' se a combinação de 'unique_bins_eda' e 'labels_eda_cut' indicar um único intervalo efetivo
            if len(unique_bins_eda) == 2: # Indica um único intervalo [bin_start, bin_end]
                if len(labels_eda_cut) == 2: # Se havia dois labels possíveis para este intervalo
                    # Cenário 1: O intervalo é [min_salary, point_of_cut] -> Salário Baixo
                    if unique_bins_eda[0] == min_salary_eda and unique_bins_eda[1] == point_of_cut_eda:
                         actual_labels = [labels_eda_cut[0]]
                    # Cenário 2: O intervalo é [point_of_cut, max_salary] -> Salário Alto
                    elif unique_bins_eda[0] == point_of_cut_eda and unique_bins_eda[1] == max_salary_eda:
                         actual_labels = [labels_eda_cut[1]]
                    # Cenário 3: O intervalo é [min_salary, max_salary] (point_of_cut fora da faixa ou na borda)
                    elif unique_bins_eda[0] == min_salary_eda and unique_bins_eda[1] == max_salary_eda:
                        # Aqui, labels_eda_cut já deve ser um único label determinado pela condição inicial
                        # Esta re-verificação garante consistência se a lógica anterior de 1 label foi acionada.
                        if point_of_cut_eda <= min_salary_eda : actual_labels = [eda_salary_labels[1]] # Todos são 'Salário Alto'
                        elif point_of_cut_eda >= max_salary_eda : actual_labels = [eda_salary_labels[0]] # Todos são 'Salário Baixo'
                # Se len(labels_eda_cut) == 1, 'actual_labels' já está correto.
            
            df_eda['faixa_salarial_eda_2cat'] = pd.cut(
                df_eda['salary_numeric_lower_bound'], bins=unique_bins_eda,
                labels=actual_labels, include_lowest=True, duplicates='drop'
            )
        df_eda.dropna(subset=['faixa_salarial_eda_2cat'], inplace=True) # Remove linhas onde a faixa não pôde ser definida
        print(f"'faixa_salarial_eda_2cat' criada. Contas:\n{df_eda['faixa_salarial_eda_2cat'].value_counts(dropna=False)}")
    else: print("DataFrame vazio após processar 'salary_numeric_lower_bound'.")
else: print("ERRO: Coluna 'P2_h' não encontrada."); exit()
```

* Processamento de Experiência (P2_i):
```python
if 'P2_i' in df_eda.columns:
    df_eda['experiencia_anos'] = df_eda['P2_i'].apply(clean_experience_to_numeric)
    median_exp = df_eda['experiencia_anos'].median() # Calcula a mediana ANTES de preencher NaNs
    df_eda['experiencia_anos'].fillna(median_exp, inplace=True)
    print(f"'experiencia_anos' criada. Nulos preenchidos com mediana ({median_exp:.1f}).")

* Processamento de UF para Região (P1_i_1)
# Ajuste para usar o nome da coluna mapeado no passo 3, se existir, ou o nome base.
uf_column_name_in_eda = 'P1_i_1' # Nome da chave como usado em col_identifiers
if uf_column_name_in_eda in df_eda.columns:
    df_eda['Regiao_Mapeada'] = map_uf_to_region(df_eda[uf_column_name_in_eda])
    print(f"'Regiao_Mapeada' criada. Contas:\n{df_eda['Regiao_Mapeada'].value_counts(dropna=False)}")
```
* Processamento de Colunas Categóricas:
```python
categorical_cols_original_keys = ['P1_a_1', 'P1_b', 'P1_l', 'P2_f', 'P2_g']
for key in categorical_cols_original_keys:
    if key in df_eda.columns:
        df_eda[key] = df_eda[key].astype(str).fillna("Não Informado").str.strip()
        if df_eda[key].nunique() > 20: # Limita a cardinalidade
            top_categories = df_eda[key].value_counts().nlargest(19).index
            df_eda[key] = df_eda[key].apply(lambda x: x if x in top_categories else 'Outros')
        print(f"Coluna categórica '{key}' processada. Valores únicos: {df_eda[key].nunique()}")

print(f"Shape do DataFrame de EDA final: {df_eda.shape}")
if df_eda.empty or 'faixa_salarial_eda_2cat' not in df_eda.columns:
    print("ERRO: DataFrame de EDA vazio ou sem coluna alvo ('faixa_salarial_eda_2cat')."); exit()
```
### Explicação da Limpeza e Transformação de Atributos:  
#### Processamento de Salário (coluna `P2_h`):

- Aplica a função `extract_salary_lower_bound` para converter os valores de salário em formato numérico, criando a coluna `salary_numeric_lower_bound`.
- Remove linhas onde a conversão do salário falhou (resultando em `NaN`).
- Se o DataFrame não estiver vazio, categoriza os salários numéricos em **"Salário Baixo"** ou **"Salário Alto"** usando a função `pd.cut`.
- Um ponto de corte (`point_of_cut_eda = 7500.0`) é utilizado.
- A lógica para definir os **bins** (intervalos) e **labels** (rótulos) para `pd.cut` tenta adaptar-se à distribuição dos salários em relação ao ponto de corte.  
  Casos especiais são tratados, como quando todos os salários são iguais ou estão todos de um lado do ponto de corte.  
  A lógica de `actual_labels` foi refinada para garantir que o número correto de rótulos seja usado com base nos bins efetivos.
- A nova coluna categórica é chamada `faixa_salarial_eda_2cat`. Linhas onde esta categorização falha são removidas.
- A contagem de cada categoria de faixa salarial é impressa para validação.

---

### Processamento de Experiência (coluna `P2_i`):

- Aplica a função `clean_experience_to_numeric` para converter as descrições de experiência em anos numéricos, criando a coluna `experiencia_anos`.
- Calcula a mediana dos anos de experiência antes de preencher os valores ausentes, para evitar que o preenchimento influencie a mediana.
- Valores ausentes (`NaN`) na coluna `experiencia_anos` são preenchidos com esta mediana.

### Processamento de UF para Região (coluna referenciada por `P1_i_1`):

- Aplica a função `map_uf_to_region` à coluna de UF (cujo nome no `df_eda` é `P1_i_1`, conforme definido em `col_identifiers`) para criar a coluna `Regiao_Mapeada`.
- A contagem de cada região mapeada é impressa.

### Processamento de Outras Colunas Categóricas:

- Uma lista `categorical_cols_original_keys` define as colunas a serem tratadas.
- Para cada uma dessas colunas:
  - Converte os valores para string.
  - Preenche valores `NaN` com `"Não Informado"`.
  - Remove espaços em branco das extremidades.
  - Se a coluna tiver mais de 20 categorias únicas (alta cardinalidade), as categorias menos frequentes são agrupadas em uma única categoria `"Outros"`, mantendo as 19 mais frequentes.  
    Isso ajuda a simplificar a análise e a modelagem.
- O número de valores únicos após o processamento é impresso.

### Verificações Finais:

- As dimensões do `df_eda` final são impressas.
- Uma verificação final assegura que o `df_eda` não esteja vazio e que a coluna alvo `faixa_salarial_eda_2cat` exista.
- Caso contrário, um erro é impresso e o script é encerrado.

---

# 5 Visualizacao dos dados (Análise Univariada)
