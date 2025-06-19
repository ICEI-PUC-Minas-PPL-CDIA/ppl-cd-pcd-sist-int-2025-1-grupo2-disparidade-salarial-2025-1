
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Carregar o dataset
df = pd.read_csv("/home/ubuntu/upload/State_of_data_BR_2023_Kaggle-df_survey_2023.csv")

# Função para limpar os nomes das colunas
def clean_col_name(col_name):
    # Remove parênteses e aspas extras, e extrai o segundo elemento da tupla se for o caso
    match = re.search(r"\(\'[^\']+\', \'([^\']+)\'\)", col_name)
    if match:
        return match.group(1).strip() # Pega o nome mais descritivo
    return col_name.strip()

df.columns = [clean_col_name(col) for col in df.columns]

# Função para converter faixa salarial em valor numérico (limite inferior)
def parse_salary_range(salary_range):
    if pd.isna(salary_range):
        return None
    salary_range = str(salary_range).replace("R$", "").replace(".", "").replace(" ", "").strip()
    if "até" in salary_range or "Menosde1000/mês" in salary_range:
        return 0
    elif "acima" in salary_range or "Maisde40000/mês" in salary_range:
        return 40001
    else:
        try:
            # Tenta dividir por 
            parts = salary_range.split("-")
            if len(parts) > 0:
                 # Remove caracteres não numéricos antes de converter para int
                numeric_part = re.sub(r'[^0-9]', '', parts[0])
                if numeric_part:
                    return int(numeric_part)
            return None
        except ValueError:
            return None

df["salary_numeric_lower_bound"] = df["Faixa salarial"].apply(parse_salary_range)

# Remover linhas com salários nulos para a análise
df_filtered = df.dropna(subset=["salary_numeric_lower_bound"])

# 1. Formalidade no emprego vs. Salário
plt.figure(figsize=(12, 7))
sns.boxplot(x="Qual sua situação atual de trabalho?", y="salary_numeric_lower_bound", data=df_filtered)
plt.title("Disparidade Salarial por Formalidade no Emprego")
plt.xlabel("Situação Atual de Trabalho")
plt.ylabel("Salário (Limite Inferior - R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("formalidade_salario.png")
plt.close()

# 2. Gênero vs. Salário
plt.figure(figsize=(10, 6))
sns.boxplot(x="Genero", y="salary_numeric_lower_bound", data=df_filtered)
plt.title("Disparidade Salarial por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Salário (Limite Inferior - R$)")
plt.tight_layout()
plt.savefig("genero_salario.png")
plt.close()

# 3. Raça/Etnia vs. Salário
plt.figure(figsize=(12, 7))
sns.boxplot(x="Cor/raca/etnia", y="salary_numeric_lower_bound", data=df_filtered)
plt.title("Disparidade Salarial por Cor/Raça/Etnia")
plt.xlabel("Cor/Raça/Etnia")
plt.ylabel("Salário (Limite Inferior - R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("raca_salario.png")
plt.close()

# 4. Nível de Ensino vs. Salário
plt.figure(figsize=(12, 7))
sns.boxplot(x="Nivel de Ensino", y="salary_numeric_lower_bound", data=df_filtered)
plt.title("Disparidade Salarial por Nível de Ensino")
plt.xlabel("Nível de Ensino")
plt.ylabel("Salário (Limite Inferior - R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("ensino_salario.png")
plt.close()

# 5. Experiência na Área de Dados vs. Salário
experience_mapping = {
    "Menos de 1 ano": 0.5,
    "1 a 2 anos": 1.5,
    "2 a 3 anos": 2.5,
    "3 a 4 anos": 3.5,
    "4 a 5 anos": 4.5,
    "5 a 6 anos": 5.5,
    "6 a 7 anos": 6.5,
    "7 a 8 anos": 7.5,
    "8 a 9 anos": 8.5,
    "9 a 10 anos": 9.5,
    "Mais de 10 anos": 10.5
}
df_filtered["experiencia_na_area_de_dados_numeric"] = df_filtered["Quanto tempo de experiência na área de dados você tem?"].map(experience_mapping)

plt.figure(figsize=(14, 7))
sns.boxplot(x="Quanto tempo de experiência na área de dados você tem?", y="salary_numeric_lower_bound", data=df_filtered.sort_values("experiencia_na_area_de_dados_numeric"))
plt.title("Disparidade Salarial por Tempo de Experiência na Área de Dados")
plt.xlabel("Tempo de Experiência na Área de Dados")
plt.ylabel("Salário (Limite Inferior - R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("experiencia_salario.png")
plt.close()

# 6. Cargo Atual vs. Salário (Top 10 cargos mais frequentes)
top_cargos = df_filtered["Cargo Atual"].value_counts().nlargest(10).index
df_top_cargos = df_filtered[df_filtered["Cargo Atual"].isin(top_cargos)]

plt.figure(figsize=(14, 7))
sns.boxplot(x="Cargo Atual", y="salary_numeric_lower_bound", data=df_top_cargos)
plt.title("Disparidade Salarial por Cargo Atual (Top 10)")
plt.xlabel("Cargo Atual")
plt.ylabel("Salário (Limite Inferior - R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("cargo_salario.png")
plt.close()

# 7. Região onde mora vs. Salário
plt.figure(figsize=(12, 7))
sns.boxplot(x="Regiao onde mora", y="salary_numeric_lower_bound", data=df_filtered)
plt.title("Disparidade Salarial por Região")
plt.xlabel("Região")
plt.ylabel("Salário (Limite Inferior - R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("regiao_salario.png")
plt.close()

print("Análise exploratória concluída e gráficos salvos.")


