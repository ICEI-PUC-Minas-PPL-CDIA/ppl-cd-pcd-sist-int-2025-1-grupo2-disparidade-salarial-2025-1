# Análise Detalhada do Código Python: Modelo Random Forest Classifier para Classificação Salarial

## 1. Visão Geral do Código

* **Objetivo Principal:** O script tem como objetivo construir um modelo de Machine Learning, especificamente um `RandomForestClassifier`, para prever a faixa salarial de profissionais da área de dados. A tarefa é tratada como um problema de classificação multiclasse, onde as diferentes faixas salariais são representadas por rótulos numéricos.

* **Bibliotecas Utilizadas:**
    * **`pandas`**: Para manipulação e análise de dados em forma tabular.
    * **`sklearn.preprocessing.LabelEncoder`**: Para codificação de variáveis categóricas (ex: faixas salariais).
    * **`sklearn.ensemble.RandomForestClassifier`**: Algoritmo de classificação baseado em floresta aleatória.
    * **`sklearn.model_selection.train_test_split`**: Para dividir os dados em conjuntos de treino e teste.
    * **`sklearn.metrics`**:
        * `accuracy_score`: Calcula a acurácia da classificação.
        * `confusion_matrix`: Gera a matriz de confusão com os acertos e erros por classe.
        * `classification_report`: Exibe precisão, recall, F1-score e suporte por classe.

---

## 2. Pré-processamento de Dados e Engenharia de Features

O código simula um conjunto de dados realista com base na estrutura de um dataset de profissionais da área de dados, incluindo atributos individuais e indicadores regionais.

* **Criação da Tabela:**
    * O DataFrame `df_merged` contém as seguintes colunas:
        * `'experiencia_num'`: tempo de experiência (em anos);
        * `'nivel_cod'`: nível de senioridade codificado numericamente;
        * `'docentes_regiao'`: número de docentes na região;
        * `'tecnicos_regiao'`: número de técnicos administrativos na região;
        * `'docentes_mestrado_regiao'`: número de docentes com mestrado;
        * `'num_ies_regiao'`: número de instituições de ensino superior na região;
        * `'salario'`: faixa salarial categórica (string).

* **Codificação da Variável Alvo:**
    * A variável `salario` é transformada em valores numéricos com `LabelEncoder`, criando a coluna `salario_label`:

    ```python
    le_salario = LabelEncoder()
    df_merged['salario_label'] = le_salario.fit_transform(df_merged['salario'])
    ```

* **Separação de Features e Target:**
    * As features são armazenadas em `X_class` e a variável alvo em `y_class`:

    ```python
    X_class = df_merged.drop(columns=['salario', 'salario_label'])
    y_class = df_merged['salario_label']
    ```

---

## 3. Divisão em Conjuntos de Treino e Teste e Balanceamento das Classes

* **Divisão com Estratificação:**
    * Os dados são divididos em treino e teste usando `train_test_split` com estratificação, garantindo que a proporção entre as classes da variável alvo seja mantida em ambos os conjuntos.

    ```python
    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
        X_class, y_class, test_size=0.5, random_state=42, stratify=y_class
    )
    ```

* **Tratamento de Classes Desbalanceadas:**
    * Para evitar que o modelo favoreça classes mais frequentes, o parâmetro `class_weight='balanced'` é utilizado no `RandomForestClassifier`. Ele ajusta automaticamente os pesos de cada classe com base em sua frequência.

---

## 4. Construção e Treinamento do Modelo Random Forest

* **Otimização de Hiperparâmetros:**
    * O modelo `RandomForestClassifier` é instanciado com os seguintes parâmetros:
        * `n_estimators=150`: número de árvores na floresta;
        * `max_depth=12`: profundidade máxima das árvores;
        * `min_samples_split=5`: número mínimo de amostras para dividir um nó interno;
        * `min_samples_leaf=2`: número mínimo de amostras que um nó folha deve ter;
        * `class_weight='balanced'`: compensação automática para classes desbalanceadas;
        * `random_state=42`: garante reprodutibilidade dos resultados.

* **Treinamento do Modelo:**
    * O modelo é treinado com os dados de treino:

    ```python
    clf.fit(X_train_c, y_train_c)
    ```

---

## 5. Realização de Previsões e Avaliação do Modelo

* **Previsão de Classes:**
    * O modelo realiza as previsões das classes no conjunto de teste com:

    ```python
    y_pred_c = clf.predict(X_test_c)
    ```

* **Métricas de Avaliação:**
    * **Acurácia:**
        * Mede a proporção de predições corretas em relação ao total de amostras:

        ```python
        accuracy_score(y_test_c, y_pred_c)
        ```

    * **Matriz de Confusão:**
        * Exibe os acertos e erros por classe, permitindo visualizar onde o modelo errou:

        ```python
        confusion_matrix(y_test_c, y_pred_c)
        ```

    * **Relatório de Classificação:**
        * Contém:
            - **Precisão (Precision):** quantos dos classificados como classe *X* realmente pertencem a *X*;
            - **Recall (Sensibilidade):** quantos da classe *X* foram corretamente identificados;
            - **F1-Score:** média harmônica entre precisão e recall;
            - **Support:** quantidade real de amostras por classe.

        ```python
        classification_report(y_test_c, y_pred_c, target_names=le_salario.classes_)
        ```

---

## 6. Análise de Importância das Features

* **Cálculo:**
    * A importância de cada feature no processo de decisão das árvores é extraída com:

    ```python
    importances = clf.feature_importances_
    ```

* **Valor da Informação:**
    * As importâncias são apresentadas em formato percentual, indicando a contribuição de cada variável para o desempenho do modelo. Exemplo de saída:

    ```
    experiencia_num: 34.72%
    nivel_cod: 28.34%
    docentes_mestrado_regiao: 16.21%
    ...
    ```

* **Aplicações:**
    * Entendimento do que mais influencia o salário previsto;
    * Suporte para decisões políticas sobre educação e capacitação;
    * Refinamento do modelo por possível exclusão de variáveis pouco relevantes.

---
