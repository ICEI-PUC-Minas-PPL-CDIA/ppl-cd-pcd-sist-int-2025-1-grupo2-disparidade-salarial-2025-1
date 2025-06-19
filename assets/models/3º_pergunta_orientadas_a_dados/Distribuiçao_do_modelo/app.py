# app.py

import flask
import pandas as pd
import joblib  # Usado para carregar o arquivo .pkl

# ==============================================================================
# 1. CARREGAR OS ARTEFATOS DO MODELO (VERSÃO DEFINITIVA)
# ==============================================================================
try:
    # Carrega o dicionário salvo no arquivo .pkl
    artifacts = joblib.load('modelo_lgbm_classificacao_faixa_salarial_v7_final_rfecv.pkl')
    
    # Extrai cada objeto do dicionário usando as chaves corretas que investigamos
    model = artifacts['model']
    scaler = artifacts['scaler']
    label_encoder = artifacts['label_encoder']
    selected_features = artifacts['selected_features']
    
    # Vamos pegar a lista de colunas do scaler diretamente do objeto scaler
    # É mais seguro do que carregar uma lista separada
    original_scaler_cols = selected_features[:1] # Assumindo que a primeira feature selecionada é a numérica 'P2_i'

    print(">>> Artefatos do modelo carregados com SUCESSO e 100% de certeza!")

except Exception as e:
    print(f"ERRO CRÍTICO ao carregar os artefatos: {e}")
    model = None
# ==============================================================================
# 2. FUNÇÃO AUXILIAR PARA MAPEAMENTO DE REGIÃO
# ==============================================================================
def map_uf_to_region(uf_series: pd.Series) -> pd.Series:
    """Mapeia uma sigla de UF para a sua respectiva região do Brasil."""
    mapa_regioes = {
        'AC': 'Norte', 'AL': 'Nordeste', 'AP': 'Norte', 'AM': 'Norte', 'BA': 'Nordeste',
        'CE': 'Nordeste', 'DF': 'Centro-Oeste', 'ES': 'Sudeste', 'GO': 'Centro-Oeste',
        'MA': 'Nordeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste', 'MG': 'Sudeste',
        'PA': 'Norte', 'PB': 'Nordeste', 'PR': 'Sul', 'PE': 'Nordeste', 'PI': 'Nordeste',
        'RJ': 'Sudeste', 'RN': 'Nordeste', 'RS': 'Sul', 'RO': 'Norte', 'RR': 'Norte',
        'SC': 'Sul', 'SP': 'Sudeste', 'SE': 'Nordeste', 'TO': 'Norte'
    }
    return uf_series.str.upper().str.strip().map(mapa_regioes).fillna('Desconhecida')

# ==============================================================================
# 3. APLICAÇÃO FLASK
# ==============================================================================
app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    """Renderiza a página inicial com o formulário."""
    if model is None:
        return "<h1>Erro Crítico</h1><p>O arquivo de modelo não foi carregado. Verifique o console.</p>", 500
    return flask.render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Recebe os dados, processa e retorna a previsão."""
    # --- Coleta os dados de entrada do formulário ---
    form_data = {
        'P1_a_1': flask.request.form['P1_a_1'],
        'P1_l': flask.request.form['P1_l'],
        'P2_i': float(flask.request.form['P2_i']),
        'P2_g_Nivel': flask.request.form['P2_g_Nivel'],
        'P2_f_Cargo_Atual': flask.request.form['P2_f_Cargo_Atual'],
        'uf_mora_P1i1': flask.request.form['uf_mora_P1i1']
    }
    input_df = pd.DataFrame([form_data])

    # --- Aplica o mesmo pré-processamento do script de treino ---
    # 1. Cria a feature 'Regiao_Mapeada' a partir da UF
    input_df['Regiao_Mapeada'] = map_uf_to_region(input_df['uf_mora_P1i1'])

    # 2. Escalonar a feature numérica usando o scaler carregado
    input_df[['P2_i']] = scaler.transform(input_df[['P2_i']])

    # 3. Assegurar o tipo 'category' para features categóricas
    for col in input_df.select_dtypes(include=['object']).columns:
        if col in selected_features:
            input_df[col] = input_df[col].astype('category')

    # 4. Selecionar APENAS as features que o modelo espera, na ordem correta
    final_input_df = input_df[selected_features]

    # --- Faz a previsão e decodifica o resultado para texto ---
    prediction_code = model.predict(final_input_df)
    resultado_final = label_encoder.inverse_transform(prediction_code)[0]

    # --- Renderiza a página com o resultado ---
    return flask.render_template('index.html', resultado_previsao=resultado_final)

if __name__ == '__main__':
    app.run(debug=True)