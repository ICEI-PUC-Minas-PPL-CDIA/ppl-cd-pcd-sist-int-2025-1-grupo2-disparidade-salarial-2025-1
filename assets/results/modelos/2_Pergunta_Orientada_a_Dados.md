# Relatório de Resultados e Insights (Random Forest Classifier)

1. Resumo do Experimento
Foi treinado um modelo de classificação RandomForest para prever faixas salariais a partir de variáveis relacionadas à experiência, nível profissional e dados regionais de educação. O modelo foi avaliado em um conjunto de teste com 3 exemplos, cada um representando uma faixa salarial distinta.

2. Resultados
Acurácia
Métrica	Valor
Acurácia	33.33%
Matriz de Confusão
Classe	Predito: R$ 1k-2k	Predito: R$ 2k-3k	Predito: R$ 3k-4k
Real: R$ 1k-2k	0	1	0
Real: R$ 2k-3k	0	1	0
Real: R$ 3k-4k	0	1	0
Relatório de Classificação
Classe	Precision	Recall	F1-score	Suporte
de R$ 1.001/mês a R$ 2.000/mês	0.00	0.00	0.00	1
de R$ 2.001/mês a R$ 3.000/mês	0.33	1.00	0.50	1
de R$ 3.001/mês a R$ 4.000/mês	0.00	0.00	0.00	1
Acurácia			0.33	3
Macro avg	0.11	0.33	0.17	3
Weighted avg	0.11	0.33	0.17	3
Importância das Variáveis
Feature	Importância
experiencia_num	0.00%
nivel_cod	0.00%
docentes_regiao	0.00%
tecnicos_regiao	0.00%
docentes_mestrado_regiao	0.00%
num_ies_regiao	0.00%

3. Insights
Baixa performance: O modelo apresentou acurácia de 33%, equivalente ao acaso para três classes. O modelo só conseguiu prever corretamente a classe "de R$ 2.001/mês a R$ 3.000/mês".

Matriz de confusão: Todas as amostras foram classificadas na mesma faixa salarial, indicando que o modelo não conseguiu distinguir entre as classes.

Importância das variáveis: Todas as features tiveram importância zero, sugerindo que o modelo não encontrou padrões relevantes nos dados para realizar as previsões.

Tamanho da amostra: O principal motivo para o baixo desempenho é o número extremamente reduzido de exemplos (apenas 6 no total, 3 no teste). Modelos de machine learning geralmente precisam de dezenas ou centenas de exemplos por classe para aprender padrões úteis.

Avisos de métricas: O relatório de classificação apresenta avisos sobre métricas indefinidas, pois algumas classes não foram previstas pelo modelo.

4. Recomendações
Aumentar a base de dados: Para obter resultados significativos, é fundamental aumentar o número de exemplos por classe.

Agrupar classes: Se houver muitas faixas salariais com poucos exemplos, considere agrupar em menos categorias (ex: baixo, médio, alto).

Validação cruzada: Com poucos dados, utilize validação cruzada para melhor avaliação do modelo.

Revisar features: Certifique-se de que as variáveis utilizadas realmente influenciam o salário.

⚠️ Atenção: Os resultados acima não devem ser interpretados como conclusivos devido ao tamanho reduzido da amostra. Este experimento serve apenas como um teste de pipeline/modelagem.
