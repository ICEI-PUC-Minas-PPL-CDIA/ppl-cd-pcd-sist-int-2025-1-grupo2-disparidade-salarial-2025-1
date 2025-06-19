# investiga.py
import joblib

print("--- Iniciando investigação do arquivo .pkl ---")

try:
    # Carrega o arquivo principal do modelo
    nome_arquivo = 'modelo_lgbm_classificacao_faixa_salarial_v7_final_rfecv.pkl'
    artifacts = joblib.load(nome_arquivo)

    # Verifica se o que foi carregado é um dicionário
    if isinstance(artifacts, dict):
        print(f"\nO arquivo '{nome_arquivo}' contém um dicionário.")
        print("As chaves (nomes corretos) dentro dele são:")

        # Imprime cada chave (cada nome) que existe lá dentro
        for key in artifacts.keys():
            print(f" -> '{key}'")

    else:
        print("\nO arquivo .pkl não contém um dicionário, mas sim um objeto do tipo:", type(artifacts))

except Exception as e:
    print(f"\nOcorreu um erro ao tentar ler o arquivo: {e}")

print("\n--- Fim da investigação ---")