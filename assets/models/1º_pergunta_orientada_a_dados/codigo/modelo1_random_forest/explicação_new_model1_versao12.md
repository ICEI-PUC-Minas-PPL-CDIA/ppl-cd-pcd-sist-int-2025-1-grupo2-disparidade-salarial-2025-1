# Análise Detalhada do Código Python: Modelo Random Forest para Previsão Salarial

## 1. Visão Geral do Código

* **Objetivo Principal:** O script tem como objetivo construir um modelo de Machine Learning, especificamente um `RandomForestClassifier`, para prever se um profissional da área de dados possui um salário "alto" (acima de R$ 8.000/mês) ou "baixo/médio" (até R$ 8.000/mês). Isso é tratado como um problema de classificação binária.
* **Bibliotecas Utilizadas:**
    * **`pandas`**: Para manipulação e análise de dados, principalmente na forma de DataFrames.
    * **`numpy`**: Para operações numéricas, especialmente útil para cálculos de `sample_weights` e manipulação de arrays.
    * **`sklearn.model_selection`**:
        * `train_test_split`: Para dividir os dados em conjuntos de treino e teste.
        * `GridSearchCV`: Para otimização de hiperparâmetros do modelo.
    * **`sklearn.ensemble.RandomForestClassifier`**: A classe principal para a implementação do modelo Random Forest.
    * **`sklearn.metrics`**: Contém diversas funções para avaliar a performance do modelo, como:
        * `confusion_matrix`: Para criar a matriz de confusão.
        * `accuracy_score`: Para calcular a acurácia.
        * `classification_report`: Para gerar um relatório detalhado com precisão, recall, F1-score por classe.
        * `roc_curve`, `auc`: Para gerar e calcular a área sob a Curva ROC.
        * `balanced_accuracy_score`: Acurácia ponderada para classes desbalanceadas.
        * `f1_score`: Métrica F1, que considera precisão e recall.
        * `precision_recall_curve`: Para gerar a curva Precision-Recall.
    * **`sklearn.calibration.CalibratedClassifierCV`**: Para calibrar as probabilidades do modelo, tornando-as mais confiáveis.
    * **`matplotlib.pyplot`**: Para a criação de gráficos estáticos e visualizações.
    * **`sklearn.tree.plot_tree`**: Para visualizar uma árvore de decisão individual do Random Forest.
    * **`seaborn`**: Para criar visualizações estatísticas mais elaboradas e esteticamente agradáveis.
    * **`os`**: Para interagir com o sistema operacional, como criar diretórios para salvar os gráficos.

---

## 2. Pré-processamento de Dados e Engenharia de Features

O código realiza um pré-processamento extenso e uma engenharia de features cuidadosa.

* **Carregamento dos Dados:**
    * Os dados são carregados de um arquivo CSV (`dados_limpos.csv`). O script tenta primeiro um caminho no ambiente Kaggle (`/kaggle/input/dataset-clean/dados_limpos.csv`) e, se não encontrado, tenta carregar localmente.
    * Uma mensagem é impressa indicando a origem do dataset carregado.

* **Seleção e Limpeza Inicial:**
    * São selecionadas colunas específicas para features (`colunas_features`) e a coluna alvo (`coluna_target`).
    * Linhas com valores ausentes (`NaN`) nas colunas cruciais selecionadas são removidas usando `df_limpo.dropna(subset=colunas_necessarias, inplace=True)`.

* **Engenharia de Features:**
    * **Mapeamento Ordinal:** Diversas colunas categóricas ordinais são convertidas para representações numéricas usando mapeamentos predefinidos:
        * `'Nível de ensino alcançado'` -> `formacao_academica_encoded` (e.g., 'Estudante de Graduação': 0, 'Doutorado ou Phd': 4)
        * `'Tempo de experiência na área de dados'` -> `experiencia_profissional_encoded` (e.g., 'Menos de 1 ano': 0, 'Mais de 10 anos': 5)
        * `'Nível de senioridade'` -> `senioridade_encoded` (e.g., 'Júnior': 0, 'Sênior': 2)
        * `'Faixa salarial mensal'` -> `faixa_salarial_encoded` (e.g., 'Menos de R$ 1.000/mês': 0, 'Acima de R$ 40.001/mês': 12)
    * **Criação da Variável Alvo Binária:**
        * A variável alvo `salario_alto` é criada a partir da `faixa_salarial_encoded`. É definida como `1` se `faixa_salarial_encoded > 5` (correspondendo a salários acima de R$ 8.000/mês) e `0` caso contrário.
    * **Codificação One-Hot:**
        * Variáveis categóricas nominais (`'Área de formação acadêmica'`, `'UF onde mora'`, `'Setor de atuação da empresa'`) são transformadas em múltiplas colunas binárias (0 ou 1) usando `pd.get_dummies()`. Isso evita que o modelo interprete uma ordem inexistente nessas categorias.
    * **Remoção Final de NaNs:** Após os mapeamentos, `dropna()` é usado novamente para garantir que não haja NaNs nas colunas codificadas que serão usadas no modelo.

* **Definição das Features (X) e Target (y):**
    * `X`: Contém as colunas de features processadas (codificadas ordinalmente e via one-hot).
    * `y`: Contém a variável alvo binária `salario_alto`.

* **Verificação de Dados e Balanceamento das Classes:**
    * O código verifica se há dados suficientes para o treinamento e se existem pelo menos duas classes na variável alvo.
    * A distribuição das classes (Salário Baixo/Médio vs. Salário Alto) é impressa, mostrando o percentual de cada uma. Isso é crucial para entender o desbalanceamento.

* **Balanceamento dos Dados (Tratamento de Classes Desbalanceadas):**
    * Em vez de usar técnicas de reamostragem como SMOTE, o script opta por duas estratégias:
        1.  **`class_weight` no Modelo:** O hiperparâmetro `class_weight` do `RandomForestClassifier` (e usado no `GridSearchCV`) pode ser configurado como `'balanced'` ou `'balanced_subsample'` para que o modelo penalize mais os erros na classe minoritária.
        2.  **`sample_weights` no Treinamento:** Pesos são calculados para cada amostra (`sample_weights`) com base na frequência das classes. Amostras da classe minoritária recebem um peso maior. Esses pesos são passados diretamente para o método `fit` do `GridSearchCV` e do `CalibratedClassifierCV`.
            ```python
            class_weights_calc = {0: 1.0, 1: class_counts[0] / class_counts[1]}
            sample_weights = np.array([class_weights_calc[cls] for cls in y])
            ```

* **Divisão em Conjuntos de Treino e Teste:**
    * Os dados (`X`, `y`) e os `sample_weights` são divididos em conjuntos de treino e teste usando `train_test_split`.
    * `test_size=0.3`: 30% dos dados são reservados para o conjunto de teste, e 70% para o treino.
    * `random_state=42`: Garante que a divisão seja a mesma toda vez que o código for executado, permitindo reprodutibilidade.
    * `stratify=y`: Assegura que a proporção das classes na variável alvo `y` seja mantida tanto no conjunto de treino quanto no de teste. Isso é especialmente importante para dados desbalanceados.
    * Os tamanhos dos conjuntos resultantes (`X_train`, `X_test`, `y_train`, `y_test`) são impressos.

---

## 3. Construção e Treinamento do Modelo Random Forest

* **Otimização de Hiperparâmetros com `GridSearchCV`:**
    * Uma grade de hiperparâmetros (`param_grid`) é definida para o `RandomForestClassifier`. Os parâmetros testados incluem:
        * `n_estimators`: Número de árvores na floresta (100, 200, 300). Mais árvores geralmente melhoram o desempenho, mas aumentam o custo computacional.
        * `max_depth`: Profundidade máxima de cada árvore (None - sem limite, 10, 20). Controla a complexidade das árvores; None pode levar a overfitting se não controlado por outros parâmetros.
        * `min_samples_split`: Número mínimo de amostras necessárias para dividir um nó interno (5, 10, 15). Ajuda a controlar o overfitting.
        * `min_samples_leaf`: Número mínimo de amostras que um nó folha deve ter (3, 5, 7). Também ajuda a controlar o overfitting.
        * `class_weight`: Estratégia para lidar com classes desbalanceadas ('balanced', 'balanced_subsample').
    * Um modelo base `RandomForestClassifier` é instanciado com `random_state=42` (para reprodutibilidade) e `n_jobs=-1` (para usar todos os processadores disponíveis).
    * `GridSearchCV` é instanciado para testar todas as combinações de hiperparâmetros da `param_grid`.
        * `estimator=rf_base`: O modelo a ser otimizado.
        * `cv=5`: Utiliza validação cruzada de 5 folds. Os dados de treino são divididos em 5 partes; o modelo é treinado em 4 e validado na 5ª, repetindo o processo 5 vezes.
        * `scoring='balanced_accuracy'`: A métrica usada para avaliar qual combinação de hiperparâmetros é a melhor. A acurácia balanceada é preferível à acurácia simples em casos de desbalanceamento.
        * `verbose=1`: Mostra mensagens durante o processo de busca.
    * O `GridSearchCV` é treinado usando `grid_search.fit(X_train, y_train, sample_weight=sample_weights_train)`. Note o uso de `sample_weights_train` aqui.
    * Os melhores parâmetros encontrados pelo `GridSearchCV` são impressos e o melhor estimador (`best_rf_model`) é armazenado.

---

## 4. Calibração do Modelo

* **Objetivo:** As probabilidades brutas de modelos como Random Forest podem não ser bem calibradas (ex: uma probabilidade prevista de 0.7 não significa necessariamente 70% de chance real). A calibração ajusta essas probabilidades para que sejam mais confiáveis.
* **Implementação:**
    * `CalibratedClassifierCV` é usado para calibrar o `best_rf_model` encontrado pelo `GridSearchCV`.
    * `base_estimator=best_rf_model`: O modelo a ser calibrado.
    * `method='isotonic'`: O método de calibração. A regressão isotônica é um método não paramétrico que geralmente funciona bem. Alternativamente, 'sigmoid' (regressão logística) poderia ser usado.
    * `cv=5`: Usa validação cruzada de 5 folds para a calibração.
    * O modelo calibrado (`calibrated_model`) é treinado usando `calibrated_model.fit(X_train, y_train, sample_weight=sample_weights_train)`, novamente utilizando os pesos das amostras.

---

## 5. Realização de Previsões e Otimização do Limiar de Classificação

* **Previsão de Probabilidades:**
    * O modelo calibrado é usado para prever as probabilidades para a classe positiva (salário alto) no conjunto de teste:
        ```python
        y_pred_proba_test = calibrated_model.predict_proba(X_test)[:, 1]
        ```
    * `predict_proba` retorna um array com as probabilidades para cada classe. `[:, 1]` seleciona as probabilidades da classe positiva (índice 1). Essas probabilidades são cruciais porque o limiar de decisão padrão de 0.5 nem sempre é o ideal, especialmente em problemas com classes desbalanceadas ou quando os custos de erros falso positivo e falso negativo são diferentes.

* **Avaliação com Diferentes Limiares:**
    * O código testa uma série de limiares de classificação (`thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]`).
    * Para cada limiar:
        * As probabilidades são convertidas em predições de classe: `(y_pred_proba_test >= threshold).astype(int)`.
        * São calculadas e impressas diversas métricas: Acurácia, Acurácia Balanceada, F1-Score, Matriz de Confusão (TN, FP, FN, TP), e Precisão/Recall para cada classe.
    * **Seleção do Melhor Limiar:** O limiar que resulta na maior `balanced_accuracy` é escolhido como o "melhor limiar".
        ```python
        best_threshold_idx = max(range(len(results)), key=lambda i: results[i]['balanced_accuracy'])
        best_threshold = results[best_threshold_idx]['threshold']
        ```
    * As predições finais no conjunto de teste (`y_pred_final`) são feitas usando este melhor limiar.

---

## 6. Avaliação Final do Modelo

* Com as predições finais (`y_pred_final`) obtidas usando o limiar otimizado, um `classification_report` completo é gerado e impresso.
* Este relatório fornece:
    * **Precisão (Precision):** Das vezes que o modelo previu uma classe, quantas estavam corretas. (TP / (TP + FP))
    * **Recall (Sensibilidade):** Das instâncias reais de uma classe, quantas o modelo conseguiu identificar corretamente. (TP / (TP + FN))
    * **F1-Score:** Média harmônica da precisão e do recall. É uma boa métrica geral, especialmente se houver desbalanceamento.
    * **Support:** Número de ocorrências reais de cada classe.
    * **Accuracy (Acurácia Geral):** Proporção de predições corretas no total.
    * **Macro Avg:** Média aritmética das métricas (precisão, recall, F1) para cada classe, sem ponderação.
    * **Weighted Avg:** Média das métricas ponderada pelo suporte de cada classe.

---

## 7. Análise de Importância das Features

* **Cálculo:** A importância de cada feature é extraída do `best_rf_model` (o modelo Random Forest otimizado, antes da calibração, pois `CalibratedClassifierCV` não expõe `feature_importances_` diretamente do `base_estimator` de forma simples, mas o `best_rf_model` é o estimador treinado).
    ```python
    importances = best_rf_model.feature_importances_
    feature_names = X.columns
    indices = np.argsort(importances)[::-1] # Ordena da mais para a menos importante
    ```
* **Valor da Informação:** Entender quais features são mais influentes para as previsões do modelo é crucial para:
    * Interpretabilidade do modelo.
    * Seleção de features (possivelmente removendo as menos importantes para simplificar o modelo).
    * Obter insights sobre o problema em questão.
* **Visualização:**
    * Um gráfico de barras horizontais mostra as **20 features mais importantes**.
    * Para uma análise mais detalhada, são gerados gráficos de barras **por grupo de features** (prefixo do nome da feature, ex: 'Área de formação acadêmica_'), caso haja mais de 20 features no total. Isso ajuda a organizar a visualização quando há muitas features (especialmente após o one-hot encoding).
    * Um gráfico de barras horizontais focado nas **Top 3 features mais importantes** é criado, com os valores de importância anotados nas barras.

---

## 8. Visualizações Geradas

O script gera e salva diversas visualizações para ajudar na compreensão e avaliação do modelo. Todas são salvas no diretório `/kaggle/working/`.

* **Configuração dos Gráficos:** Um estilo (`seaborn-v0_8-whitegrid`) e tamanhos de fonte/figura padrão são definidos para consistência.
* **Gráficos:**
    1.  **Matriz de Confusão (`matriz_confusao_otimizada.png`):**
        * Visualiza o desempenho do modelo no conjunto de teste usando o limiar otimizado. Mostra Verdadeiros Positivos (TP), Verdadeiros Negativos (TN), Falsos Positivos (FP) e Falsos Negativos (FN).
    2.  **Curva ROC (`curva_roc_otimizada.png`):**
        * Plota a Taxa de Verdadeiros Positivos (TPR) contra a Taxa de Falsos Positivos (FPR) para diferentes limiares de classificação.
        * A área sob a curva (AUC) é uma medida da capacidade do modelo de distinguir entre as classes. Um valor maior é melhor.
        * Uma linha vertical indica o melhor limiar encontrado.
    3.  **Curva Precision-Recall (`precision_recall_curve.png`):**
        * Mostra a relação entre precisão e recall para diferentes limiares. É particularmente útil para problemas com classes desbalanceadas.
    4.  **Importância das Features (`importancia_features_top20.png`, `importancia_features_grupo_*.png`, `top3_features.png`):**
        * Conforme descrito na seção anterior, visualiza a relevância de cada feature.
    5.  **Distribuição das Probabilidades Preditas (`distribuicao_probabilidades.png`):**
        * Um histograma das probabilidades previstas para a classe "Salário Alto" no conjunto de teste.
        * Uma linha vertical marca o melhor limiar, ajudando a visualizar como ele separa as predições.
    6.  **Visualização de uma Árvore do Random Forest (`arvore_exemplo_melhorada.png`, `arvore_exemplo_simplificada.png`):**
        * Mostra a estrutura de uma única árvore de decisão do ensemble Random Forest (a primeira árvore, `estimators_[0]`).
        * Duas versões são salvas: uma mais detalhada (`max_depth=4`) e uma mais simplificada (`max_depth=3`) para facilitar a interpretação. É útil para entender como as decisões são tomadas em um nível micro.
    7.  **Análise de Interação entre Formação e Experiência (`interacao_formacao_experiencia.png`):**
        * Um heatmap que mostra a probabilidade média de ter "Salário Alto" para diferentes combinações de `formacao_academica_encoded` e `experiencia_profissional_encoded`. Isso ajuda a identificar interações entre essas duas features importantes.
    8.  **Gráfico de Dispersão para as Duas Features Mais Importantes (`dispersao_top2_features.png`):**
        * Se houver pelo menos duas features, um gráfico de dispersão é criado usando as duas features mais importantes do conjunto de teste. Os pontos são coloridos pela probabilidade prevista de "Salário Alto", permitindo visualizar como essas duas features, em conjunto, se relacionam com a previsão.
