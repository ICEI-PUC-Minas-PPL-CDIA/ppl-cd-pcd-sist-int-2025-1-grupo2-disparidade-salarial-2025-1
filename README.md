<h1 align="center">DISPARIDADE SALARIAL DOS PROFISSIONAIS DE DADOS DO BRASIL</h1>

A disparidade salarial entre profissionais de dados no Brasil é influenciada por diversos fatores pessoais, educacionais e de mercado. Este estudo busca identificar quais variáveis impactam a remuneração desses profissionais, analisando dados da pesquisa State of Data Brazil 2023 e de bases auxiliares. 

Para isso, são exploradas características como experiência, formação acadêmica, setor de atuação, localização e habilidades técnicas. Através de modelagem preditiva, os resultados indicam que experiência, nível de senioridade e setor da empresa são os fatores com maior impacto na variação salarial. Esses insights podem auxiliar profissionais e empresas na tomada de decisões estratégicas sobre carreira e políticas de remuneração.

---

<h2 align="center">Integrantes</h2>

**Pedro Dias Soares, [pdsoares@sga.pucminas.br]**

**Gabriel Chaves Nascimento, [gabriel.nascimento.1483087@sga.pucminas.br]**

**Enzo Alves Barcelos Gripp, [eabgripp@sga.pucminas.br]**


---

<h2 align="center">Professores</h2>

* Hugo Bastos de Paula

* Hayala Nepomuceno Curto

---

<h2 align="center">Instruções de utilização</h2>

### Como Executar a Aplicação Localmente

### 6.4. Como Executar a Aplicação Localmente

Esta seção detalha os passos para que outro desenvolvedor possa configurar e executar esta aplicação em seu próprio ambiente local.

1.  **Clonar o Repositório:**
    Primeiro, clone o repositório do GitHub para a sua máquina local.
    ```bash
    git clone [https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1]
    ```

2.  **Configurar o Ambiente:**
    É altamente recomendado usar um ambiente virtual para evitar conflitos de dependência. Este projeto foi desenvolvido e testado com Conda.
    ```bash
    # Navegue até a pasta do projeto
    cd preditor_salario_app

    # Crie um novo ambiente Conda (opcional, mas recomendado)
    conda create -n meu_app_ambiente python=3.10
    conda activate meu_app_ambiente
    ```

3.  **Instalar as Dependências:**
    Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Para instalá-las, execute o comando:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Executar a Aplicação:**
    Com as dependências instaladas, inicie o servidor Flask localmente com o seguinte comando:
    ```bash
    python app.py
    ```

5.  **Acessar a Aplicação:**
    Abra seu navegador de internet e acesse o endereço `http://127.0.0.1:5000`. O formulário do previsor de salários deverá ser exibido.

### Instruções de Utilização (Interface Web)

Após iniciar a aplicação, o usuário interagirá com a interface da seguinte forma:

1.  **Acesse a Aplicação:** Abra o navegador no endereço fornecido (`http://127.0.0.1:5000` para teste local ou o link público).
2.  **Preenchimento do Formulário:** A tela principal exibirá um formulário solicitando as seguintes informações:
    * Tempo de Experiência na Área de Dados
    * Nível de Senioridade
    * Cargo Atual
    * Nível de Ensino
    * Faixa Etária
    * UF onde mora
3.  **Obtenção da Previsão:** Após preencher todos os campos, clique no botão "Fazer Previsão".
4.  **Visualização do Resultado:** A página será recarregada e o resultado da predição ('Salário Alto' ou 'Salário Baixo') será exibido de forma destacada abaixo do formulário.


---

<h2 align="center">Histórico de versões</h2>



* 0.1
    * Definição dos integrantes.  
* 0.2
    * Definição do tema.
* 0.3
    * Criação do sumário.
* 0.4
    * 0.4.1
        * Criação do resumo.
    * 0.4.2 
        * Criação da introdução.
    * 0.4.3 
        * Criação da contextualização.
    * 0.4.4 
        * Criação da problematização.
    * 0.4.5 
        * Criação dos objetivos.
    * 0.4.6 
        * Criação das justificativas.
    * 0.4.7 
        * Criação do público alvo.
    * 0.4.8 
        * Criação do dicionário de dados.
    * 0.4.9 
        * Criação do descrição de dados.
* 1.0
    * Definição das perguntas orientadas a dados.
      * 1.1 
          * Preparação de dados.
      * 1.2
          * Enriquecimeno de dados.
* 2.0
    * Criação do sumário das analises exploratórias
      * 2.1
          * Desenvolvimento das analises exploratorias
      * 2.2
          * Anexando resultados obtidos
             * 2.2.1
                 * Explicando resultados obtidos.
* 3.0
    * A partir dos resultados obtidos, inciamos o desenvolvimento do algoritimo de aprendizado de máquina, para previsão da variação salarial com base nos fatores identificados.
      * 3.1
          * Criação do sumário de induções ao modelo
      * 3.2
          * Realização de diversos testes de algoritimos e desenvolviento de diversas versões.
* 4.0 
    * Implementação do algoritimo no colab e no kaggle notebook.
      * 4.1
             * Manutenções e gerações de diversas versões do algoritimo.
      * 4.2
             * Obtenção dos resultados 
* 5.0
    * Explicação dos resultados
      * 5.1 
             * Explicação dos codigos do trabalho
      * 5.2 
             * Interpretação dos modelos
      * 5.3 
             * Analise comparativa dos modelos
* 6.0 Preenchimento do Citation.CFF
