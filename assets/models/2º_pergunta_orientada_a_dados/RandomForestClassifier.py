import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Exemplo de dados simulados (ajuste para seu df_merged real)
sample_data = {
    'experiencia_num': [0.5, 1.5, 2.5, 0.5, 1.5, 2.5],
    'nivel_cod': [0, 1, 0, 1, 0, 1],
    'docentes_regiao': [10, 20, 15, 10, 20, 15],
    'tecnicos_regiao': [5, 10, 7, 5, 10, 7],
    'docentes_mestrado_regiao': [3, 6, 4, 3, 6, 4],
    'num_ies_regiao': [2, 3, 2, 2, 3, 2],
    'salario': [
        'de R$ 1.001/mês a R$ 2.000/mês',
        'de R$ 2.001/mês a R$ 3.000/mês',
        'de R$ 3.001/mês a R$ 4.000/mês',
        'de R$ 1.001/mês a R$ 2.000/mês',
        'de R$ 2.001/mês a R$ 3.000/mês',
        'de R$ 3.001/mês a R$ 4.000/mês'
    ]
}
df_merged = pd.DataFrame(sample_data)

# Codificar variável target
le_salario = LabelEncoder()
df_merged['salario_label'] = le_salario.fit_transform(df_merged['salario'])

# Separar features e target
X_class = df_merged.drop(columns=['salario', 'salario_label'])
y_class = df_merged['salario_label']

# Split com test_size suficiente para estratificação
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X_class, y_class, test_size=0.5, random_state=42, stratify=y_class
)

# Treinar classificador
clf = RandomForestClassifier(
    n_estimators=150,
    max_depth=12,
    min_samples_split=5,
    min_samples_leaf=2,
    class_weight='balanced',
    random_state=42
)
clf.fit(X_train_c, y_train_c)

# Predizer
y_pred_c = clf.predict(X_test_c)

# Avaliação
print(f"Acurácia: {accuracy_score(y_test_c, y_pred_c):.2%}")
print("\nMatriz de Confusão:")
print(confusion_matrix(y_test_c, y_pred_c))
print("\nRelatório de Classificação:")
print(classification_report(y_test_c, y_pred_c, target_names=le_salario.classes_))

# Importância das variáveis
importances = clf.feature_importances_
print("\nImportância das Variáveis:")
for name, imp in zip(X_class.columns, importances):
    print(f"{name}: {imp:.2%}")
