#                                                                   #
#                 Explicação dos Scripts de Análise                 #
#                                                                   #

Data da Análise: 19 de junho de 2025

### 1. get_columns.py

* **Objetivo**: Este script faz uma inspeção inicial do arquivo CSV para listar todas as colunas existentes e informar a quantidade total de colunas.

* **Como Funciona**:
    * Carrega o arquivo `State_of_data_BR_2023_Kaggle-df_survey_2023.csv` usando a biblioteca pandas.
    * Utiliza `df.columns.tolist()` para obter os nomes de todas as colunas como uma lista.
    * Utiliza `len(df.columns)` para contar o número total de colunas no dataset.

* **Resultado**: O script imprime no console a lista completa dos nomes das colunas e, em seguida, o número total de colunas.

### 2. get_columns_exact.py

* **Objetivo**: O objetivo deste script é exclusivamente obter e exibir a lista exata dos nomes das colunas do dataset.

* **Como Funciona**:
    * Carrega o arquivo `State_of_data_BR_2023_Kaggle-df_survey_2023.csv` com a biblioteca pandas.
    * Chama a função `df.columns.tolist()` para gerar uma lista com os nomes das colunas.

* **Resultado**: O script imprime no console apenas a lista com os nomes exatos das colunas.

### 3. eda_script.py

* **Objetivo**: Este é o script principal da Análise Exploratória de Dados (EDA). Seu propósito é processar os dados e gerar uma série de visualizações (gráficos) para investigar como diferentes fatores (demográficos, educacionais, profissionais) se relacionam com as disparidades salariais.

* **Como Funciona**:
    * **Carregamento e Limpeza**: Carrega o dataset e aplica uma função (`clean_col_name`) para limpar e padronizar os nomes das colunas.
    * **Processamento de Salário**: Converte a coluna de faixas salariais (que é um texto) em uma nova coluna numérica chamada `salary_numeric_lower_bound`. Esta coluna armazena o limite inferior de cada faixa, permitindo cálculos e comparações estatísticas.
    * **Geração de Gráficos**: Para cada fator a ser analisado, o script cria um gráfico de boxplot usando a biblioteca `seaborn` para comparar a distribuição salarial entre diferentes categorias.
    * **Salvamento das Imagens**: Cada gráfico gerado é salvo como um arquivo de imagem no formato `.png`. Os arquivos salvos são: `formalidade_salario.png`, `genero_salario.png`, `raca_salario.png`, `ensino_salario.png`, `experiencia_salario.png`, `cargo_salario.png` e `regiao_salario.png`.

* **Resultado**: Ao final da execução, o script imprime a mensagem "Análise exploratória concluída e gráficos salvos." e cria sete arquivos de imagem `.png` com as visualizações das disparidades salariais.
