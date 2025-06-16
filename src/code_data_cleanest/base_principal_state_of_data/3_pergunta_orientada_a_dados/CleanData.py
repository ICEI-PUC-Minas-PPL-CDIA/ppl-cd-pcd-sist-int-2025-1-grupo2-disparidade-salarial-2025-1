import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import plotly.express as px
import plotly.io as pio # Adicionado para salvar Plotly como imagem
import statsmodels.api as sm
from statsmodels.graphics.mosaicplot import mosaic

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

# --- Configurações da EDA ---
eda_output_dir_script = 'visualizacoes_eda_final_rev3' # Novo diretório para esta versão
os.makedirs(eda_output_dir_script, exist_ok=True)
sns.set_style("whitegrid")

# --- 1. Carregar Dados ---
print("--- 1. Carregando Dados ---")
file_path = "Main_database (2).xlsx"
if not os.path.exists(file_path):
    print(f"ERRO: Arquivo de dados '{file_path}' não encontrado.")
    exit()
df_original = pd.read_excel(file_path)
print(f"Base de dados original carregada: {df_original.shape[0]} linhas, {df_original.shape[1]} colunas.")

# --- 2. Limpeza Inicial de Nomes de Colunas ---
print("\n--- 2. Limpando Nomes de Colunas ---")
df_cleaned_names = df_original.copy()
df_cleaned_names.columns = [clean_col_name(col) for col in df_original.columns]
print("Nomes de colunas limpos.")

# --- 3. Seleção dos Atributos para EDA ---
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

# --- 4. Limpeza e Transformação dos Atributos ---
print("\n--- 4. Limpando e Transformando Atributos ---")
if 'P2_h' in df_eda.columns:
    df_eda['salary_numeric_lower_bound'] = df_eda['P2_h'].apply(extract_salary_lower_bound)
    df_eda.dropna(subset=['salary_numeric_lower_bound'], inplace=True)
    if not df_eda.empty:
        min_salary_eda = df_eda['salary_numeric_lower_bound'].min()
        max_salary_eda = df_eda['salary_numeric_lower_bound'].max()

        # !! AJUSTE ESTE VALOR CONFORME A ANÁLISE DO SEU MODELO E RESULTADOS DESEJADOS !!
        # Este valor deve ser o mesmo que você está ajustando no script de treinamento.
        point_of_cut_eda = 9000.0  # <-- PONTO DE CORTE AJUSTÁVEL PARA A EDA

        print(f"Usando ponto de corte para EDA: {point_of_cut_eda}")
        eda_salary_labels = ["Salário Baixo", "Salário Alto"]
        if min_salary_eda == max_salary_eda:
            df_eda['faixa_salarial_eda_2cat'] = eda_salary_labels[0]
        else:
            bins_eda, labels_eda = ([min_salary_eda, max_salary_eda], [eda_salary_labels[1]]) if point_of_cut_eda <= min_salary_eda else \
                                 ([min_salary_eda, max_salary_eda], [eda_salary_labels[0]]) if point_of_cut_eda >= max_salary_eda else \
                                 ([min_salary_eda, point_of_cut_eda, max_salary_eda], eda_salary_labels)
            unique_bins_eda = sorted(list(set(bins_eda)))
            if len(unique_bins_eda) < 2: unique_bins_eda = [min_salary_eda, max_salary_eda]
            if len(unique_bins_eda) == 2 and len(labels_eda) == 2:
                 labels_eda = [labels_eda[0]] if point_of_cut_eda >= (min_salary_eda + max_salary_eda)/2 else [labels_eda[1]]

            df_eda['faixa_salarial_eda_2cat'] = pd.cut(
                df_eda['salary_numeric_lower_bound'], bins=unique_bins_eda,
                labels=labels_eda, include_lowest=True, duplicates='drop'
            )
        df_eda.dropna(subset=['faixa_salarial_eda_2cat'], inplace=True)
        print(f"'faixa_salarial_eda_2cat' criada. Contas:\n{df_eda['faixa_salarial_eda_2cat'].value_counts(dropna=False)}")
    else: print("DataFrame vazio após processar 'salary_numeric_lower_bound'.")
else: print("ERRO: Coluna 'P2_h' não encontrada."); exit()

if 'P2_i' in df_eda.columns:
    df_eda['experiencia_anos'] = df_eda['P2_i'].apply(clean_experience_to_numeric)
    median_exp = df_eda['experiencia_anos'].median()
    df_eda['experiencia_anos'].fillna(median_exp, inplace=True)
    print(f"'experiencia_anos' criada. Nulos preenchidos com mediana ({median_exp:.1f}).")
if 'P1_i_1' in df_eda.columns:
    df_eda['Regiao_Mapeada'] = map_uf_to_region(df_eda['P1_i_1'])
categorical_cols_original_keys_eda = ['P1_a_1', 'P1_b', 'P1_l', 'P2_f', 'P2_g']
for key in categorical_cols_original_keys_eda:
    if key in df_eda.columns:
        df_eda[key] = df_eda[key].astype(str).fillna("Não Informado").str.strip()
        if df_eda[key].nunique() > 15: # Agrupa em 'Outros' se muitas categorias
            top_categories = df_eda[key].value_counts().nlargest(14).index
            df_eda[key] = df_eda[key].apply(lambda x: x if x in top_categories else 'Outros')
print(f"Shape do DataFrame de EDA final: {df_eda.shape}")
if df_eda.empty or 'faixa_salarial_eda_2cat' not in df_eda.columns:
    print("ERRO: DataFrame de EDA vazio ou sem coluna alvo."); exit()
