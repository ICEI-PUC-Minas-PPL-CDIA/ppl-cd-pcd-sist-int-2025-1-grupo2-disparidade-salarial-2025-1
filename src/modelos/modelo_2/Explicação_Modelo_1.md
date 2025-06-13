# Análise Detalhada do Código Python: Modelo Random Forest para Previsão SalarialAdd commentMore actions

## 1. Visão Geral do Código

* **Objetivo Principal:** O script tem como objetivo construir um modelo de Machine Learning, especificamente um `RandomForestRegressor`, para prever o valor médio da faixa salarial mensal de profissionais da área de dados. A previsão é baseada em variáveis como experiência na área, nível profissional e indicadores educacionais da região onde o profissional reside.

* **Bibliotecas Utilizadas:**
    * **`pandas`**: Para manipulação e análise de dados em DataFrames.
    * **`numpy`**: Para operações numéricas básicas.
    * **`sklearn.preprocessing.LabelEncoder`**: Para codificar variáveis categóricas em formato numérico.
    * **`sklearn.ensemble.RandomForestRegressor`**: Para construir o modelo de regressão baseado em floresta aleatória.
    * **`sklearn.model_selection.train_test_split`**: Para dividir os dados em conjuntos de treino e teste.
    * **`sklearn.metrics`**:
        * `mean_absolute_error`: Para calcular o erro absoluto médio entre os valores reais e previstos.
        * `r2_score`: Para medir o coeficiente de determinação (R²), que indica o quanto o modelo explica da variabilidade da variável alvo.

---

## 2. Pré-processamento de Dados e Engenharia de Features

* **Carregamento dos Dados:**
    * Duas bases CSV são carregadas:
        1. Uma base de survey sobre o mercado de dados (`df_state`);
        2. Uma base do INEP contendo estatísticas regionais sobre instituições de ensino superior (`df_edu`).

* **Seleção e Renomeação de Colunas:**
    * A base `df_state` é filtrada para conter apenas:
        - `'experiencia'`: tempo de experiência na área de dados;
        - `'nivel'`: nível de senioridade;
        - `'salario'`: faixa salarial;
        - `'regiao'`: região onde o profissional reside.
    * As colunas são renomeadas para nomes mais simples e consistentes.

* **Engenharia de Features:**
    * **Mapeamento Ordinal - Experiência:**
        - As faixas textuais de experiência são convertidas para valores numéricos (em anos), por exemplo:
          `'menos de 1 ano'` → `0.5`, `'de 5 a 6 anos'` → `5.5`, `'15 anos ou mais'` → `16.0`.
    * **Mapeamento Ordinal - Salário:**
        - As faixas salariais são mapeadas para valores numéricos médios:
          `'de R$ 6.001 a R$ 8.000'` → `7000`, `'Acima de R$ 40.001/mês'` → `40000`.
    * **Codificação Nominal - Nível Profissional:**
        - O campo `'nivel'` é codificado numericamente com `LabelEncoder`, gerando a nova coluna `nivel_cod`.

---

## 3. Integração com Dados Educacionais Regionais

* **Agregação Regional:**
    * A base `df_edu` é agrupada pela coluna `'NO_REGIAO_IES'`, somando:
        - Quantidade total de docentes (`QT_DOC_TOTAL`);
        - Técnicos administrativos (`QT_TEC_TOTAL`);
        - Docentes com mestrado e doutorado;
        - Quantidade de instituições de ensino superior distintas (`CO_IES`).

* **Renomeação de Colunas:**
    * As colunas agregadas são renomeadas para:
        - `'docentes_regiao'`, `'tecnicos_regiao'`, `'docentes_mestrado_regiao'`, `'docentes_doutorado_regiao'`, `'num_ies_regiao'`.

* **Merge das Bases:**
    * A base `df_state` é unida com a base educacional agregada (`df_edu_group`) pela coluna `'regiao'`, utilizando `merge` com `how='left'`.

---

## 4. Preparação dos Dados para Modelagem

* **Seleção de Variáveis para o Modelo:**
    * A base final (`df_model`) inclui:
        - `'experiencia_num'`: anos de experiência;
        - `'nivel_cod'`: nível profissional codificado;
        - `'docentes_regiao'`, `'tecnicos_regiao'`, `'docentes_mestrado_regiao'`, `'num_ies_regiao'`: indicadores educacionais;
        - `'salario_num'`: variável alvo (salário médio).

* **Remoção de Valores Ausentes:**
    * Linhas com `NaN` em qualquer uma das colunas usadas no modelo são eliminadas com `.dropna()`.

* **Divisão em Conjuntos de Treino e Teste:**
    * Os dados são divididos em `X` (features) e `y` (target).
    * A divisão é feita com `train_test_split`, com `random_state=42` para reprodutibilidade.

---

## 5. Construção e Treinamento do Modelo Random Forest

* **Definição do Modelo:**
    * Um `RandomForestRegressor` é instanciado com os seguintes hiperparâmetros:
        - `n_estimators=100`: número de árvores na floresta;
        - `max_depth=None`: sem limite de profundidade;
        - `max_features='sqrt'`: número de variáveis considerado em cada split é a raiz quadrada do total;
        - `min_samples_split=5`: mínimo de 5 amostras para dividir um nó;
        - `min_samples_leaf=2`: mínimo de 2 amostras por folha;
        - `random_state=42`: para garantir resultados reprodutíveis.

* **Treinamento do Modelo:**
    * O modelo é treinado com os dados de treino:
      ```python
      model.fit(X_train, y_train)
      ```

---

## 6. Realização de Previsões e Avaliação do Modelo

* **Previsão no Conjunto de Teste:**
    * O modelo realiza a previsão dos salários com:
      ```python
      y_pred = model.predict(X_test)
      ```

* **Métricas de Avaliação:**
    * **Erro Médio Absoluto (MAE):**
        - Mede o erro médio entre os valores reais e previstos:
          ```python
          mean_absolute_error(y_test, y_pred)
          ```
    * **Coeficiente de Determinação (R²):**
        - Mede a proporção da variabilidade explicada pelo modelo:
          ```python
          r2_score(y_test, y_pred)
          ```

* **Interpretação:**
    * Quanto menor o MAE, melhor.
    * Quanto mais próximo de 1 o R², maior a capacidade do modelo de explicar a variabilidade do salário.

---

## 7. Análise de Importância das Features
Add commentMore actions
* **Cálculo:**
    * As importâncias das variáveis são extraídas com:
      ```python
      model.feature_importances_
      ```

* **Valor da Informação:**
    * As variáveis mais importantes indicam os fatores que mais influenciam a previsão salarial.
    * Um exemplo de saída pode ser:
      ```
      experiencia_num: 36.2%
      nivel_cod: 28.7%
      docentes_mestrado_regiao: 14.5%
      ...
      ```

* **Aplicações:**
    * Avaliar quais variáveis contribuem mais para o modelo;
    * Reforçar hipóteses do domínio (ex: influência da formação regional);
    * Guiar políticas de desenvolvimento profissional e educacional.

---
