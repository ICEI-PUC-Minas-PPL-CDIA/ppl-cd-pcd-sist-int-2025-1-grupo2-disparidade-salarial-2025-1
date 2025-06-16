<h1 align="center">Disparidade Salarial dos Profissionais de Dados no Brasil</h1>

---

<h2 align="center">INTEGRANTES</h2>

**Pedro Dias Soares, [pdsoares@sga.pucminas.br]** 

**Gabriel Chaves Nascimento, [gabriel.nascimento.1483087@sga.pucminas.br]**

**Enzo Alves Barcelos Gripp, [eabgripp@sga.pucminas.br]**

---

<h2 align="center">PROFESSORES</h2>

**Hugo Bastos de Paula**

**Hayala Nepomuceno Curto**


---

<h2 align="center">CURSO E INSTITUIÇÃO</h2>

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---
<h2 align="center">SUMÁRIO</h2>

*   [1. RESUMO](#resumo)
*   [2. INTRODUÇÃO](#introdução)
    *   [2.1. Contextualização](#contextualização)
    *   [2.2. Problema](#problema)
    *   [2.3. Objetivo geral](#objetivo-geral)
    *   [2.4. Objetivo específico](#objetivos-específicos)
    *   [2.5. Justificativas](#justificativas)
*   [3. PÚBLICO ALVO](#público-alvo)
*   [4. DICIONÁRIO DE DADOS](#dicionário-de-dados)
*   [5. DESCRIÇÃO DE DADOS](#descrição-de-dados)
*   [6. PREPARAÇÃO DE DADOS](#preparação-dos-dados)
*   [7. ENRIQUECIMENTO DE DADOS](#enriquecimento-de-dados)
*   [8. ANÁLISES EXPLORATÓRIAS DE DADOS](#analises-exploratorias-de-dados) 
    *   [8.1. 1º Pergunta Orientada a Dados](#1º-pergunta-orientada-a-dados)
    *   [8.2. 2º Pergunta Orientada a Dados](#2º-pergunta-orientada-a-dados)
    *   [8.3. 3º Pergunta Orientada a Dados](#3º-pergunta-orientada-a-dados)
*   [9. INDUÇÃO DE MODELOS](#indução-de-modelos)
    *   [9.1. Modelos 1° pergunta orietada a dados](#modelos-1º-pergunta-orietada-a-dados)
    *   [9.2. Modelos 2° pergunta orietada a dados](#modelos-2º-pergunta-orietada-a-dados)
    *   [9.3. Modelos 3° pergunta orietada a dados](#modelos-3º-pergunta-orietada-a-dados)
*   [10. RESULTADOS](#resultados)
    *   [10.1. Resultados obtidos com os Modelos 1º pergunta orietada a dados](#resultados-obtidos-com-os-modelos-1º-pergunta-orietada-a-dados)
    *   [10.2. Resultados obtidos com os Modelos 2º pergunta orietada a dados](#resultados-obtidos-com-os-modelos-2º-pergunta-orietada-a-dados)
    *   [10.3. Resultados obtidos com os Modelos 3º pergunta orietada a dados](#resultados-obtidos-com-os-modelos-3º-pergunta-orietada-a-dados)
*   [11. INTERPRETAÇÃO DOS MODELOS](#interpretação-dos-modelos)
    *   [11.1. Interpretação dos Modelos 1° pergunta orietada a dados](#interpretação-dos-modelo-1º-pergunta-orientada-a-dados)
    *   [11.2. Interpretação dos Modelos 2° pergunta orietada a dados](#interpretação-dos-modelo-2º-pergunta-orientada-a-dados)
    *   [11.3. Interpretação dos Modelos 3° pergunta orietada a dados](#interpretação-dos-modelo-3º-pergunta-orientada-a-dados)
*   [12. ANÁLISE COMPARATIVA DOS MODELOS](#análise-comparativa-dos-modelos)
    *   [Análise comparativa dos modelos da 1º pergunta orientada a dados](#análise-comparativa-dos-modelos-da-1º-pergunta-orientada-a-dados)
    *   [Análise comparativa dos modelos da 2º pergunta orientada a dados](#análise-comparativa-dos-modelos-da-2º-pergunta-orientada-a-dados)
    *   [Análise comparativa dos modelos da 3º pergunta orientada a dados](#análise-comparativa-dos-modelos-da-3º-pergunta-orientada-a-dados)
*   [13. CONCLUSÃO](#-conclusão)
*   [14. REFERÊNCIAS](#referências)
*   [15. APÊNDICES](#apêndices)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Resumo

A disparidade salarial entre profissionais de dados no Brasil é influenciada por diversos fatores pessoais, educacionais e de mercado. Este estudo busca identificar quais variáveis impactam a remuneração desses profissionais, analisando, dados da pesquisa State of Data Brasil 2023 e de bases auxiliares. Para isso, são exploradas características como experiência, formação acadêmica, setor de atuação, localização e habilidades técnicas. Por meio de modelagem preditiva, os resultados indicam que experiência, nível de senioridade e setor da empresa são os fatores com maior impacto na variação salarial. Esses insights podem auxiliar profissionais e empresas na tomada de decisões estratégicas sobre carreira e políticas de remuneração.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Introdução

O Brasil experimentou um crescimento exponencial na indústria de dados devido à transformação digital do país e à crescente necessidade de trabalhadores qualificados. Embora as oportunidades sejam abundantes, os salários variam amplamente entre os trabalhadores, com fatores como experiência, gênero, educação, localização geográfica e tipo de empresa influenciando essa disparidade.

O objetivo deste estudo é identificar os principais fatores associados à disparidade na remuneração dos profissionais de dados no Brasil, utilizando informações coletadas de uma ampla pesquisa setorial.

As disparidades salariais entre os profissionais de dados no Brasil são influenciadas por diversos fatores, como idade, gênero dos profissionais de dados, do setor de emprego ou modelo de contratação e ainda o seu histórico educacional e experiência profissional.

Este estudo investiga os principais elementos associados à variação de salários no campo de dados ao utilizar o conjunto de dados State of Data Brasil 2023 e outras bases para complementar a pesquisa. Empregando métodos da ciência de dados, busca-se identificar padrões salariais e oferecer insights relevantes para profissionais e empresas. Espera-se que os resultados tragam um maior entendimento das disparidades salariais no campo, ajudando a desenvolver estratégias que incentivem a igualdade no mercado de tecnologia e ciência de dados.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##    Contextualização

A desigualdade salarial é um desafio enfrentado no mercado de trabalho brasileiro, impactando diversos setores da economia.

Estudos do IBGE apontam que gênero, etnia e escolaridade são fatores cruciais na determinação dos salários. Conforme as pesquisas de 2022 do instituto, o rendimento médio por hora dos trabalhadores brancos foi de R$ 20,00, enquanto para pretos ou pardos foi de R$ 12,40, representando uma diferença de 61,4%. Além disso, pesquisas do mesmo em 2021 indicam que as taxas de desocupação foram de 11,3% para brancos, 16,5% para pretos e 16,2% para pardos, evidenciando a influência desses aspectos na disparidade salarial na atualidade.

No setor de tecnologia, essas disparidades têm características particulares, especialmente devido ao desenvolvimento acelerado da área e à necessidade contínua de atualização profissional. Na ciência de dados, as diferenças salariais são significativas e influenciadas por fatores como a experiência, formação acadêmica, setor de atuação e habilidades técnicas.

Conforme o relatório State of Data Brasil 2023, profissionais que possuem certificações específicas em grandes empresas costumam receber remunerações mais altas, enquanto mulheres e grupos minoritários ainda encontram barreiras para alcançar igualdade salarial.

Diante do exposto, buscamos, por meio desta análise de dados, investigar os fatores determinantes para a variação salarial entre os profissionais de dados no Brasil, visando compreender melhor as desigualdades no setor e identificar caminhos para um mercado mais equitativo.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##    Problema

O agente em questão busca estabelecer quais são os fatores determinantes para a variação salarial entre profissionais de dados no Brasil. Constantemente, empresas brasileiras enfrentam dificuldades em determinar um salário justo ao profissional de dados por não considerarem os requisitos e as variáveis necessárias para isso. Nesse contexto, a análise busca entender o papel de fatores como experiência e nível educacional nas diferenças salariais, visando fornecer um padrão para que o mercado profissional da área seja mais equilibrado no país.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##    Objetivo geral

**Desenvolver um sistema inteligente para compreender os fatores que influenciam a variação salarial dos profissionais de dados no Brasil e para auxiliar na equiparação salarial desses, utilizando técnicas de ciência de dados para identificar padrões e tendências.**

##    Objetivos específicos

1. **Exploração e Análise dos Dados:**
    - Extrair da base de dados State of Data Brazil 2023 e bases auxiliares, dados suficientes para identificar variáveis relevantes associadas aos salários.
      
2. **Identificação de Fatores Relevantes:**
    - Analisar variáveis e compreender o papel de cada uma na carreira profissional do cientista de dados brasileiro, como o nível de experiência, o setor de atuação, o nível educacional, as habilidades técnicas, o gênero e a etnia.
      
3. **Aplicação de Modelos Preditivos:**
    - Aplicar, por meio de algoritmos de aprendizado de máquina, a previsão da variação salarial com base nos fatores identificados.
      
4. **Interpretação dos Resultados:**
    - Aplicar, por meio de algoritmos de aprendizado de máquina, a previsão da variação salarial com base nos fatores identificados.
      
5. **Geração de Insights para o Mercado:**
    - Fornecer recomendações baseadas nos achados, para auxiliar profissionais de dados e empresas na atribuição de salários aos profissionais da área.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##    Justificativas

A desigualdade salarial na área de dados é um tema relevante, impactando profissionais e empresas. Este estudo busca identificar os principais fatores associados aos salários, com foco na experiência, senioridade e setor de atuação. O estudo se destina a profissionais da área que podem utilizar os resultados para planejar suas carreiras, e às empresas, que podem aprimorar suas políticas salariais com base em dados concretos. A pesquisa se apoia em bases de dados reconhecidas, como a State of Data Brasil 2023 da Data Hackers, garantindo a validade e confiabilidade das análises realizadas.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#    Público alvo

Os principais perfis de usuários da aplicação são:

Profissionais de dados: Os quais possuem conhecimento técnico variado. Estão familiarizados com ferramentas de análise e visualização de dados, além de linguagens como Python e SQL. No ambiente corporativo, ocupam cargos que vão de analistas a cientistas de dados sêniores.

Gestores e recrutadores de RH: Estes utilizam plataformas de análise salarial para embasar decisões estratégicas. Eles ocupam posições hierárquicas que incluem gerentes, diretores e especialistas em aquisição de talentos.

Pesquisadores e acadêmicos: Aqueles que têm conhecimento analítico e estatístico. Utilizam tecnologias para explorar padrões e tendências em dados salariais e estão inseridos em universidades, centros de pesquisa e órgãos governamentais.

Órgãos governamentais e associações da indústria: esses utilizam a aplicação para obter informações detalhadas sobre o mercado de trabalho e salários, visando formular políticas públicas, regulamentações e padrões da indústria. Estão envolvidos com dados que ajudam a orientar legislações e relatórios sobre tendências econômicas e de emprego.

A aplicação será útil para esses grupos ao oferecer maneiras de visualizar intuitivas, comparações salariais e insights baseados em machine learning.

## 🎯 Público-alvo da aplicação

A aplicação visa fornecer insights sobre disparidade salarial na área de dados no Brasil, ajudando diferentes perfis de usuários a tomar decisões estratégicas.

## 🏢 Stakeholders e seus papéis

| **Stakeholder**                 | **Nível de Interesse** | **Influência** | **Objetivos** |
|---------------------------------|----------------------|--------------|--------------|
| **Profissionais de Dados**          | Alto                 | Média        | Avaliar sua posição no mercado e planejar crescimento. |
| **Gestores e Recrutadores de RH**   | Alto                 | Alta         | Ajustar faixas salariais e estruturar políticas de retenção. |
| **Pesquisadores e Acadêmicos**      | Médio                | Média        | Explorar padrões e desigualdades no mercado. |
| **Órgãos Governamentais**           | Médio                | Alta         | Criar regulamentações e políticas de inclusão. |

## 👥 Perfis de usuários (Personas)

### **1️⃣ Persona: Analista de Dados Júnior**
- **Nome:** Lucas Mendes  
- **Idade:** 25 anos  
- **Objetivo:** Comparar sua faixa salarial com o mercado para planejar seu crescimento profissional.  
- **Desafios:** Não sabe quais habilidades influenciam no aumento salarial.  

### **2️⃣ Persona: Gerente de RH em Tecnologia**
- **Nome:** Mariana Costa  
- **Idade:** 38 anos  
- **Objetivo:** Definir pacotes salariais competitivos para atrair talentos na área de dados.  
- **Desafios:** Falta de dados estruturados sobre o mercado e diferenças regionais.  

### **3️⃣ Persona: Pesquisador de Mercado de Trabalho**
- **Nome:** Dr. João Ribeiro  
- **Idade:** 45 anos  
- **Objetivo:** Estudar desigualdades salariais no setor de tecnologia.  
- **Desafios:** Precisa de dados confiáveis e ferramentas estatísticas para análise.  

### **4️⃣ Persona: Regulador de Políticas Públicas**
- **Nome:** Ana Beatriz Oliveira  
- **Idade:** 50 anos  
- **Objetivo:** Criar diretrizes para reduzir a disparidade salarial na tecnologia.  
- **Desafios:** Necessita de informações claras e de fácil interpretação.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#    Dicionário de dados

O banco de dados “State of Data Brazil 2023” é o resultado de uma pesquisa conduzida pela comunidade Data Hackers em parceria com a Bain & Company, que visa mapear o mercado brasileiro de dados. A pesquisa contou com a participação de mais de 5.200 profissionais da área, que responderam a perguntas sobre diversos temas, por exemplo:

- **Fatores Pessoais e Demográficos:** Idade, gênero, perfil racial e diversidade no setor de dados; contexto social e fatores que podem influenciar a carreira na área de dados.

- **Experiência e Carreira:** Tempo de atuação no mercado de dados; cargos ocupados e progressão na carreira; transições de carreira para a área de dados.

- **Empresa e Ambiente de Trabalho:**  Tipo e porte da empresa na qual os profissionais trabalham; modelo de trabalho (remoto, híbrido ou presencial); cultura organizacional e satisfação no ambiente de trabalho.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#    Descrição de dados
1. State_of_Data_BR_2023
A pesquisa State_of_Data_BR_2023 é realizada anualmente visando mapear o perfil dos profissionais de dados no Brasil. Ela abrange informações como salários, ferramentas utilizadas, nível de experiência, formação acadêmica e outros aspectos relevantes.

**Salários Médio por Gênero:**  
gênero  
Feminino           R$ 7.000,00  
Masculino         R$ 10.000,00  
Não Informado      R$ 7.000,00  
Nome: `salary_midpoint`, `dtype: object`  

**Salários Médio por Etnia:**  
etnia  
Asiático          R$ 10.000,00  
Negro              R$ 7.000,00  
Indígena           R$ 5.000,00  
Pardo              R$ 7.000,00  
Não Informado      R$ 7.000,00  
Branco            R$ 10.000,00  
Nome: `salary_midpoint`, `dtype: object`  

**Salários Médio por Nível de Educação:**  
nível_educacional  
Graduação                  R$ 7.000,00  
Mestrado                  R$ 10.000,00  
Sem Educação Formal        R$ 5.000,00  
Doutorado                 R$ 14.000,00  
Pós-graduação             R$ 10.000,00  
Estudante de Graduação     R$ 3.500,00  
Nome: `salary_midpoint`, `dtype: object`  

**Salários Médio por Senioridade:**  
senioridade  
Júnior         R$ 3.500,00  
Pleno          R$ 7.000,00  
Sênior        R$ 10.000,00  
Nome: `salary_midpoint`, `dtype: object`  

**Salários Médio por Função:**  
função_atual  
Engenheiro de Analytics       R$ 10.000,00  
Engenheiro/Arquiteto de Dados R$ 10.000,00  
Professor/Pesquisador         R$ 10.000,00  
Economista                    R$ 10.000,00  
Cientista de Dados            R$ 10.000,00  
Analista de Negócios           R$ 7.000,00  
Analista de Dados              R$ 7.000,00  
Desenvolvedor de Software      R$ 7.000,00  
Analista de BI                 R$ 5.000,00  
Nome: `salary_midpoint`, `dtype: object`  

**Salários Médio por Indústria:**  
indústria  
Finanças/Bancos          R$ 10.000,00  
Indústria                R$ 10.000,00  
Internet/E-commerce      R$ 10.000,00  
Tecnologia/Software      R$ 10.000,00  
Varejo                   R$ 10.000,00  
Educação                  R$ 7.000,00  
Setor Público             R$ 7.000,00  
Marketing                 R$ 5.000,00  
Nome: `salary_midpoint`, `dtype: object`  

**Salários Médio por Região:**  
região  
Centro-oeste    R$ 10.000,00  
Sudeste         R$ 10.000,00  
Nordeste         R$ 7.000,00  
Norte            R$ 7.000,00  
Sul              R$ 7.000,00  
Nome: `salary_midpoint`, `dtype: object`  

**Diferença Salarial por Gênero:** 42,86% (Mediana Masculino: R$ 10.000,00; Mediana Feminino: R$ 7.000,00)  

**Diferença Salarial Branco-Negro:** 42,86% (Mediana Branco: R$ 10.000,00; Mediana Negro: R$ 7.000,00)   
**Diferença Salarial Branco-Pardo:** 42,86% (Mediana Branco: R$ 10.000,00; Mediana Pardo: R$ 7.000,00)  

**Correlação entre Experiência Total e Salário:** 0,54   
**Correlação entre Nível Educacional e Salário:** 0,32

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Preparação dos dados



## Atributos relevantes da base de dados principal para 1ºpergunta orientada
**Pergunta orientada a dados:** *Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*


| Atributo                                         | Nome                                      | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância |
|--------------------------------------------------|-------------------------------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| P0                                               | id                 		       | Qualitativo  | Nominal                             | Para identificação da resposta                                    		            | Alta       |
| P1l                                              | Nível de ensino alcançado                 | Qualitativo  | Ordinal                             | Nível de ensino do respondente (graduação, mestrado, etc.)                                    | Alta       |
| P1m                                              | Área de formação acadêmica                | Qualitativo  | Nominal (Multivalorado)             | Área de formação acadêmica do respondente (TI, Economia, etc.)                                | Alta       |
| P2h                                              | Faixa salarial mensal                     | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| P2i                                              | Tempo de experiência na área de dados     | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |
| P2g                                              | Nível de senioridade                      | Qualitativo  | Ordinal                             | Nível de senioridade do respondente (Júnior, Pleno, Sênior)                                   | Alta       |
| P1b                                              | Gênero do profissional                    | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| P1c                                              | Cor/Raça/Etnia                            | Qualitativo  | Nominal (Multivalorado)             | Cor ou raça do respondente                                                                    | Alta       |
| P2b                                              | Setor de atuação da empresa               | Qualitativo  | Nominal (Multivalorado)             | Setor em que a empresa do respondente atua (Tecnologia, Finanças, etc.)                       | Alta       |
| P1i1                                             | UF onde mora                              | Qualitativo  | Nominal (Multivalorado)             | Unidade Federativa onde o respondente reside                                                  | Alta       |
| P2f                                              | Cargo atual                               | Qualitativo  | Nominal (Multivalorado)             | Cargo atual ocupado pelo respondente                                                          | Alta       |
| P2o6                                             | Oportunidade de aprendizado               | Qualitativo  | Nominal (Multivalorado)             | Valorização das oportunidades de aprendizado e crescimento profissional                       | Alta       |
| P2o10                                            | Reputação da empresa                      | Qualitativo  | Nominal (Multivalorado)             | Valorização da reputação que a empresa tem no mercado                                         | Alta       |

---

## Atributos relevantes da base de dados principal para 2ª pergunta orientada
**Pergunta orientada a dados:** *Qual é a relação entre o tempo de experiência na área de dados, o nível de senioridade e a faixa salarial dos profissionais no Brasil?*

| Atributo | Nome | Tipo | Subtipo | Descrição | Relevância |
|----------|------|------|---------|-----------|------------|
| P2i      | Tempo de Experiência | Quantitativo | Discreto | Anos de atuação na área de dados | Alta |
| P2g      | Nível de Senioridade | Qualitativo | Ordinal | Nível profissional alcançado (Júnior, Pleno, Sênior, etc.) | Alta |
| P2h      | Faixa Salarial | Qualitativo | Ordinal | Classificação salarial em faixas | Alta |


---

## Atributos relevantes da base de dados principal para 3ª pergunta orientada
**Pergunta orientada a dados:** *Como fatores como  formalidade no emprego , características demográficas se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*

| Atributo                                           | Código de Referência | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância  |
|----------------------------------------------------|-----------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| Faixa etária                                       | P1a1                  | Qualitativo  | Ordinal                             | Faixa etária do respondente                                                                   | Alta       |
| Gênero                                             | P1b                   | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| Nivel de ensino alcançado                          | P1l                   | Qualitativo  | Ordinal                             | Nível de ensino do respondente (graduação, mestrado, etc.)                                    | Alta       |
| Faixa salarial mensal                              | P2h                   | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| Tempo de experiência na área de dados              | P2i                   | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |
| UF onde mora                                       | P1i1                  | Qualitativo  | Nominal (Multivalorado)             | Unidade Federativa onde o respondente reside                                                  | Alta       |
| Cargo atual                                        | P2f                   | Qualitativo  | Nominal (Multivalorado)             | Cargo atual ocupado pelo respondente                                                          | Alta       |
| Nível de senioridade                               | P2g                   | Qualitativo  | Ordinal                             | Nível de senioridade do respondente (Júnior, Pleno, Sênior)                                   | Alta       |


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Enriquecimento de dados

## Base de dados auxiliar para 1º pergunta orientada a dados
**Pergunta orientada a dados:** *Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*
- Microdados do Censo da Educação Superior
- Link: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior
  
- [Base de dados](/assets/data/bases_principais/bases_auxiliar/1_pergunta_orientada_a_dados/MICRODADOS_ED_SUP_IES_2023.CSV)


## Base de dados auxiliar para 2º pergunta orientada a dados
**Pergunta orientada a dados:** *Qual é a relação entre o tempo de experiência na área de dados, o nível de senioridade e a faixa salarial dos profissionais no Brasil?*
- Relatórios de Transparência Salarial e Critérios Remuneratórios
- Link: [https://relatoriodetransparenciasalarial.trabalho.gov.br/](https://relatoriodetransparenciasalarial.trabalho.gov.br/)
  
- [Base de dados](/assets/data/bases_principais/bases_auxiliar/2_pergunta_orientada_a_dados/)

## Base de dados auxiliar para a 3º pergunta orientada a dados
**Pergunta orientada a dados:** *Como fatores como formalidade no emprego e características demográficas (gênero e raça) interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*
- Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD-C)
- Link: https://basedosdados.org/dataset/9fa532fb-5681-4903-b99d-01dc45fd527a?table=a04fc85d-908a-4393-b51d-1bd517a40210
  
- [Base de dados](/assets/data/bases_principais/bases_auxiliar/3_pergunta_orientada_a_dados/bq-results-20250422-030542-1745291209599.zip)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Analises exploratorias de dados

*   [1. 1º PERGUNTA ORIENTADA A DADOS ](#1º-pergunta-orientada-a-dados)
  
	*   [1.1 Analise exploratoria de dados base de dados State of Data 2023](#analise-exploratoria-de-dados-base-de-dados-state-of-data-2023) 
		   *    [1.1.1 Grafico Distribuição de Salários Mensais](#grafico-distribuição-de-salários-mensais) 
		   *   	[1.1.2 Grafico Relação entre Salário e Tempo de Experiência](#grafico-relação-entre-salário-e-tempo-de-experiência) 
		   *   	[1.1.3 Grafico Distribuição Salarial por Nível de Ensino](#grafico-distribuição-salarial-por-nível-de-ensino) 
		   *   	[1.1.4 Grafico Interação entre Escolaridade, Experiência e Salário](#grafico-interação-entre-escolaridade-experiência-e-salário) 
		   *   	[1.1.5 Grafico Mapa de Calor de Correlações](#grafico-mapa-de-calor-de-correlações) 
		   *   	[1.1.6 Grafico Distribuição por Gênero e Raça-Etnia](#grafico-distribuição-por-gênero-e-raça-etnia) 
		   *   	[1.1.7 Grafico Distribuição Geográfica dos Profissionais](#grafico-distribuição-geográfica-dos-profissionais) 
		   *   	[1.1.8 Grafico Salário por Nível de Senioridade](#grafico-salário-por-nível-de-senioridade) 
		   *   	[1.1.9 Grafico Análise Multivariada das Relações entre Variáveis Selecionadas](#grafico-análise-multivariada-das-relações-entre-variáveis-selecionadas) 
		   *   	[1.1.10 Grafico Sunburst da Distribuição de Profissionais de Dados](#grafico-sunburst-da-distribuição-de-profissionais-de-dados) 


	*   [1.2 Analise exploratoria de dados base de dados Microdados](#analise-exploratoria-de-dados-base-de-dados-microdados) 
		   *   	[1.2.1 Grafico Distribuição Nacional de Níveis de Formação dos Docentes](#grafico-distribuição-nacional-de-níveis-de-formação-dos-docentes) 
		   *   	[1.2.2 Grafico Top 10 Estados por Nível de Formação de Docentes](#grafico-top-10-estados-por-nível-de-formação-de-docentes) 
		   *   	[1.2.3 Grafico Distribuição Etária Nacional dos Docentes](#grafico-distribuição-etária-nacional-dos-docentes) 
		   *   	[1.2.4 Grafico Matriz de Correlação entre Formação e Faixa Etária](#grafico-matriz-de-correlação-entre-formação-e-faixa-etária) 
		   *   	[1.2.5 Grafico Mapa Interativo de Bolhas - Distribuição de Docentes por Nível de Formação e UF](#grafico-mapa-interativo-de-bolhas---distribuição-de-docentes-por-nível-de-formação-e-uf) 
		   *   	[1.2.6 Gráfico de Dispersão 3D Interativo - Mestrado, Doutorado e Média de Idade dos Docentes por UF](#grafico-gráfico-de-dispersão-3d-interativo---mestrado-doutorado-e-média-de-idade-dos-docentes-por-uf) 


	*   [1.3 Analise exploratoria de dados bases integradas](#analise-exploratoria-de-dados-bases-integradas) 
		   *   	[1.3.1 Grafico Salário Médio Estimado e Total de Docentes por UF](#grafico-salário-médio-estimado-e-total-de-docentes-por-uf) 
		   *   	[1.3.2 Grafico Salário Estimado por Área de Formação - Top 5](#grafico-salário-estimado-por-área-de-formação---top-5) 
		   *   	[1.3.3 Grafico Salário Estimado por Tempo de Experiência](#grafico-salário-estimado-por-tempo-de-experiência) 
		   *   	[1.3.4 Grafico Salário Estimado por Tempo de Experiência em Dados](#grafico-salário-estimado-por-tempo-de-experiência-em-dados)
		   *   	[1.3.5 Grafico Salário Estimado por Nível de Ensino](#grafico-salário-estimado-por-nível-de-ensino) 
		   *   	[1.3.6 Grafico Salário Estimado por Experiência, Agrupado por Nível de Ensino](#grafico-salário-estimado-por-experiência-agrupado-por-nível-de-ensino) 
		   *   	[1.3.7 Grafico Distribuição de Profissionais por Área de Formação Acadêmica](#grafico-distribuição-de-profissionais-por-área-de-formação-acadêmica) 
		   *   	[1.3.8 Grafico Distribuição de Profissionais por Faixa Salarial Mensal](#grafico-distribuição-de-profissionais-por-faixa-salarial-mensal) 
		   *   	[1.3.9 Grafico Distribuição de Profissionais por Nível de Ensino](#grafico-distribuição-de-profissionais-por-nível-de-ensino) 
		   *   	[1.3.10 Grafico Distribuição do Salário Estimado](#grafico-distribuição-do-salário-estimado) 
		   *   	[1.3.11 Grafico Distribuição de Profissionais por Tempo de Experiência em Dados](#grafico-distribuição-de-profissionais-por-tempo-de-experiência-em-dados)
		   *   	[1.3.12 Grafico Top 10 UF de Residência dos Profissionais de Dados](#grafico-top-10-uf-de-residência-dos-profissionais-de-dados)
		   *   	[1.3.13 Grafico Heatmap de Correlação entre Salário, Experiência e Nível de Ensino](#grafico-heatmap-de-correlação-entre-salário-experiência-e-nível-de-ensino)
		   *   	[1.3.14 Grafico Salário Médio Estimado vs. Anos de Experiência por Nível de Ensino](#grafico-salário-médio-estimado-vs-anos-de-experiência-por-nível-de-ensino)
		   *   	[1.3.15 Grafico Relação 3D entre Salário, Experiência e Nível de Ensino](#grafico-relação-3d-entre-salário-experiência-e-nível-de-ensino)
		   *   	[1.3.16 Grafico Salário Estimado vs. Proporção de Docentes com Doutorado na UF de Residência](#grafico-salário-estimado-vs-proporção-de-docentes-com-doutorado-na-uf-de-residência)
		   *   	[1.3.17 Gráfico Relação 3D entre Salário, Experiência e Nível de Ensino](#gráfico-relação-3d-entre-salário-experiência-e-nível-de-ensino)

*   [2. 2º PERGUNTA ORIENTADA A DADOS ](#2º-pergunta-orientada-a-dados)
  
* [3. 3º PERGUNTA ORIENTADA A DADOS](#3º-pergunta-orientada-a-dados)
    * [3.1 Análise Univariada](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#1-visualizacao-dos-dados-an%C3%A1lise-univariada)
        * [3.1.1 Gráfico: Histograma e KDE dos salários numéricos](#análise-do-histograma-e-kde-dos-salarios-numericos)
        * [3.1.2 Gráfico: Histograma e KDE de salários](#análise-histograma-e-estimativa-de-densidade-do-kernel-kde-de-salarios)
        * [3.1.3 Gráfico: ECDF de salários](#análise-do-gráfico-ecdf-de-salarios)
        * [3.1.4 Gráfico: QQ plot de salários](#análise-do-gráfico-qq-plot-de-salarios)
        * [3.1.5 Gráfico: Histograma e KDE de experiência em anos](#análise-do-gráfico-histograma-e-kde-de-experiencia_anos)
        * [3.1.6 Gráfico: Boxplot de experiência em anos](#análise-do-gráfico-boxplot-de-experiencia_anos)
        * [3.1.7 Gráfico: Distribuição de Nível de Senioridade](#análise-do-gráfico-distribuição-de-p2_g--nível-de-senioridade)
        * [3.1.8 Gráfico: Distribuição de Região](#análise-do-gráfico-distribuição-de-regiao_mapeada)
    * [3.2. Análise Bivariada](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#2-visualizacao-dos-dados-an%C3%A1lise-bivariada)
        * [3.2.1 Gráfico: Histograma sobreposto com curva KDE](#análise-do-gráfico-grafico-de-barras-sobreposto)
        * [3.2.2 Gráfico: Barras empilhadas](#análise-do-gráfico-gráfico-de-barras-empilhadas)
        * [3.2.3 Gráfico: Barras agrupadas por gênero](#análise-do-gráfico-gráfico-de-barras-agrupadas-por-gênero)
        * [3.2.4 Gráfico: Barras agrupadas por escolaridade](#análise-do-gráfico-gráfico-de-barras-agrupadas-senioridade-por-escolaridade)
    * [3.3. Análise Multivariada](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#3-visualizacao-dos-dados-an%C3%A1lise-multivariada)
        * [3.3.1 Gráfico: Experiência vs Salário por nível de senioridade](#análise-do-gráfico-de-dispersão-experiência-vs-limite-inferior-do-salário-por-nível-de-senioridade)
        * [3.3.2 Gráfico: Limite salarial por nível de ensino e faixa salarial](#análise-do-gráfico-de-boxplots-limite-inferior-do-salário-por-nível-de-ensino-e-faixa-salarial-alvo)
        * [3.3.3 Gráfico: Violin plot - experiência por senioridade e faixa salarial](#análise-do-gráfico-de-violin-plots-divididos-experiência-anos-por-nível-de-senioridade-e-faixa-salarial-alvo)
        * [3.3.4 Gráfico: Nível de ensino por região e faixa salarial](#análise-do-gráfico-nível-de-ensino-por-região-e-faixa-salarial-alvo)		

# 1º Pergunta orientada a dados 
**Pergunta Orientada a Dados:** *Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?*

## Analise exploratoria de dados base de dados State of Data 2023

---

### Grafico Distribuição de Salários Mensais
![__results___0_1](https://github.com/user-attachments/assets/6204cac8-9875-4db3-b6d7-6bf52b038d49)
## Explicação do Gráfico: Distribuição de Salários Mensais

O gráfico apresentado é um histograma que ilustra a **Distribuição de Salários Mensais** de profissionais de dados no Brasil, com uma curva de estimativa de densidade do kernel (KDE) sobreposta para suavizar a representação da distribuição.

**Eixos do Gráfico:**
*   **Eixo X (Horizontal):** Representa o "Salário Médio (R$)", indicando as faixas salariais mensais em Reais. A escala varia de R$ 0 até valores próximos ou superiores a R$ 40.000.
*   **Eixo Y (Vertical):** Indica a "Contagem", ou seja, o número de profissionais que se enquadram em cada faixa salarial representada pelas barras do histograma. A contagem máxima observada no gráfico aproxima-se de 800 profissionais em uma determinada faixa salarial.

**Interpretação da Distribuição:**
*   **Concentração de Salários:** A maior concentração de profissionais encontra-se nas faixas salariais mais baixas. Observa-se um pico principal (a barra mais alta) na faixa de aproximadamente R$ 9.000 a R$ 10.000, onde cerca de 800 profissionais estão localizados.
*   **Múltiplos Picos (Multimodalidade):** A distribuição aparenta ser multimodal, sugerida pela curva KDE e pelas barras do histograma. Além do pico principal, há outras concentrações notáveis:
    *   Uma concentração significativa entre R$ 4.000 e R$ 6.000, com mais de 600 profissionais.
    *   Outro pico menor ao redor de R$ 13.000 a R$ 14.000, com quase 300 profissionais.
    *   Pequenas elevações em faixas salariais mais altas, como em torno de R$ 17.000-R$18.000 e R$ 22.000-R$23.000, indicando grupos menores de profissionais nesses níveis salariais.
*   **Assimetria à Direita (Right-Skewed):** A distribuição é assimétrica à direita. Isso significa que, embora a maioria dos salários esteja concentrada nas faixas mais baixas e médias, existe uma "cauda" longa para a direita, indicando que um número menor de profissionais recebe salários consideravelmente mais altos (acima de R$ 20.000, R$ 30.000, e chegando a R$ 40.000 ou mais). Essa assimetria é comum em distribuições de renda e salário.
*   **Dispersão:** Há uma grande dispersão nos salários, variando desde valores abaixo de R$ 5.000 até mais de R$ 40.000, refletindo a diversidade de remuneração na área de dados no Brasil.

Em resumo, o gráfico evidencia que a maioria dos profissionais de dados no Brasil, conforme o dataset analisado, possui salários concentrados nas faixas inferiores a R$ 15.000, com picos importantes em torno de R$ 4.000-R$6.000 e R$ 9.000-R$10.000. No entanto, existe uma parcela de profissionais que alcança remunerações significativamente mais elevadas, estendendo a distribuição para a direita.


## Grafico Relação entre Salário e Tempo de Experiência
![__results___0_2](https://github.com/user-attachments/assets/5b842f17-cbc8-46af-8bf5-7c8bf30bc7e7)
## Explicação do Gráfico: Relação entre Salário e Tempo de Experiência

O gráfico de boxplot intitulado "Relação entre Salário e Tempo de Experiência" ilustra como a faixa salarial numérica ("Faixa_salarial_num") varia conforme o "Tempo de experiência na área de dados" no Brasil.

**Como ler este gráfico de Boxplot:**
*   **Caixa (Box):** Representa o intervalo interquartil (IQR), onde se concentram 50% dos salários. A linha inferior da caixa é o primeiro quartil (Q1 - 25º percentil), e a linha superior é o terceiro quartil (Q3 - 75º percentil).
*   **Linha na Caixa:** indica a mediana (Q2 - 50º percentil), sendo o valor salarial central para cada grupo de experiência.
*   **Hastess/"Bigodes" (Whiskers):** As linhas que se estendem a partir da caixa mostram o alcance dos dados, geralmente até 1,5 vezes o IQR. Pontos além dessas hastes são considerados outliers.
*   **Outliers:** São pontos individuais (losangos no gráfico) que representam salários atípicos, muito acima ou abaixo da maioria dos salários para aquele grupo de experiência.
*   **Eixo Y (Vertical):** "Faixa\_salarial\_num" representa os salários em Reais (R$), variando de R$ 0 a R$ 40.000.
*   **Eixo X (Horizontal):** "Tempo de experiência na área de dados" categoriza os profissionais em diferentes faixas de anos de experiência: "Menos de 1 ano", "de 1 a 2 anos", "de 3 a 4 anos", "de 4 a 6 anos", "de 5 a 6 anos", e "de 7 a 10 anos". As categorias no eixo X do gráfico original não estão em ordem crescente de experiência.

**Interpretação das tendências observadas:**

Ao analisar os boxplots para cada faixa de experiência (considerando-os em ordem crescente de experiência):

*   **Tendência Geral de Aumento Salarial com a Experiência:**
    *   **Menos de 1 ano:** Este grupo apresenta a menor mediana salarial, situando-se em torno de R$ 3.500 - R$ 4.000. A maioria dos salários (IQR) está entre aproximadamente R$ 2.000 e R$ 5.000.
    *   **De 1 a 2 anos:** A mediana salarial sobe para cerca de R$ 5.000. O IQR varia de R$ 3.500 a R$ 7.000.
    *   **De 3 a 4 anos:** Observa-se um aumento mais significativo na mediana, que se localiza em torno de R$ 8.000 - R$ 8.500. O IQR está entre R$ 5.000 e R$ 10.000.
    *   **De 4 a 6 anos / De 5 a 6 anos / De 7 a 10 anos:** estes grupos com maior experiência apresentam medianas salariais consideravelmente mais altas e bastante próximas entre si.
        *   A mediana para "de 4 a 6 anos" e "de 5 a 6 anos" (que parecem muito similares no gráfico) está em torno de R$ 11.000 - R$ 12.000, com IQR entre R$ 10.000 e R$ 14.000.
        *   Para "de 7 a 10 anos", a mediana é ligeiramente superior, em torno de R$ 12.000 - R$ 13.000, com um IQR similar (R$ 10.000 a R$ 14.000).

*   **Variabilidade Salarial (Dispersão):**
    *   A dispersão salarial (representada pela altura da caixa e o comprimento das hastes) tende a aumentar com a experiência. Profissionais nos níveis iniciais de carreira ("Menos de 1 ano") apresentam uma faixa salarial mais concentrada em comparação com aqueles com mais experiência, onde a variabilidade é maior.
    *   Os grupos com mais experiência ("de 4 a 6 anos" em diante) mostram uma dispersão salarial maior, indicando que, embora a média seja mais alta, há uma gama mais ampla de salários sendo pagos.

*   **Outliers:**
    *   Outliers (salários muito acima do comum para o grupo) são observados em todas as categorias de experiência.
    *   Nos grupos com mais experiência (a partir de "de 3 a 4 anos"), alguns profissionais atingem salários de até R$ 40.000, indicando um potencial de alta remuneração para os mais experientes ou em posições de destaque.
    *   Mesmo no grupo com "Menos de 1 ano", existe um outlier próximo a R$ 14.000.

**Conclusão do gráfico:**
O gráfico demonstra uma clara correlação positiva entre o tempo de experiência na área de dados e o nível salarial. Profissionais com mais anos de atuação tendem a ter salários medianos mais altos e também uma maior variabilidade salarial, com alguns indivíduos alcançando remunerações substancialmente elevadas. A progressão salarial parece ser mais acentuada nos primeiros anos de carreira, estabilizando-se em um patamar mais elevado para profissionais com 4 ou mais anos de experiência.


## Grafico Interação entre Escolaridade, Experiência e Salário
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/99901a7169839052f5473ff6f4b57242/raw/6c71c7167850cb50f4e98432a646db7c69f2ffa1/grafico_3d_interativo.html)

![newplot](https://github.com/user-attachments/assets/5bb94b6a-aa5d-416d-be48-9bac9d9d01c0)
## Explicação do Gráfico 3D Interativo: Interação entre Escolaridade, Experiência e Salário.

O gráfico apresentado é uma visualização 3D interativa cujo objetivo é investigar a interação entre o nível de escolaridade, o tempo de experiência e o salário dos profissionais de dados no Brasil. Gráficos de superfície ou dispersão 3D são úteis para investigar como uma variável de resposta (neste caso, o salário) se relaciona com duas variáveis preditoras (escolaridade e experiência).

**Eixos do gráfico:**
*   **Eixo X (Horizontal, profundidade):** "Tempo de Experiência (anos)" – Representa os anos de experiência profissional na área de dados. A escala parece variar de 0 a aproximadamente 10 anos.
*   **Eixo Y (Horizontal, largura):** "Nível de Escolaridade (numérico)" – Representa o nível de escolaridade, convertido para uma escala numérica para permitir a plotagem. A legenda indica a correspondência:
    *   0: Doutorado ou PhD
    *   1: Estudante de Graduação
    *   2: Graduação/Bacharelado
    *   3: Mestrado
    *   4: Pós-graduação
*   **Eixo Z (Vertical):** "Salário (R$)" – Representa a remuneração mensal em Reais. A escala vai de R$0 até valores superiores a R$35.000.

**Interpretação dos dados e visualização:**
*   **Pontos de Dados (Scatter Plot 3D):** Cada ponto no gráfico representa um profissional de dados, posicionado de acordo com seu tempo de experiência, nível de escolaridade (numérico) e salário.
*   **Cores por Nível de Escolaridade:** Os pontos são coloridos de acordo com o nível de escolaridade, facilitando a distinção e a análise de como cada grupo educacional se distribui em relação à experiência e ao salário.
    *   **Doutorado ou PhD (Azul Escuro/Roxo):** Pontos para este grupo.
    *   **Estudante de Graduação (Azul Claro/Ciano):** Pontos para este grupo.
    *   **Graduação/Bacharelado (Verde):** Pontos para este grupo.
    *   **Mestrado (Laranja/Amarelo):** Pontos para este grupo.
    *   **Pós-graduação (Vermelho):** Pontos para este grupo.
*   **Interatividade:** A natureza interativa do gráfico permite ao usuário girar a visualização, alterar o ângulo de visão e dar zoom. Isso é crucial para explorar as relações complexas em um espaço tridimensional, identificando padrões, concentrações de pontos e outliers que poderiam não ser evidentes em gráficos 2D.

**Observações Gerais e Tendências (Inferidas pela Exploração Visual):**
*   **Impacto da Experiência:** Geralmente, observa-se que, para todos os níveis de escolaridade, um aumento no tempo de experiência (movimento ao longo do eixo X) tende a estar associado a salários mais altos (pontos mais elevados no eixo Z).
*   **Impacto da escolaridade:**
    *   **Estudantes de Graduação (cor Azul Claro/Ciano):** Tendem a se concentrar na parte inferior da escala salarial e com menor tempo de experiência.
    *   **Graduação/Bacharelado (cor Verde) e Pós-graduação (cor Vermelho):** Mostram uma dispersão maior, com salários aumentando com a experiência. Muitos pontos se situam em faixas salariais intermediárias, mas com potencial de alcançar salários mais altos com mais experiência.
    *   **Mestrado (cor Laranja/Amarelo) e Doutorado/PhD (cor Azul Escuro/Roxo):** Estes grupos tendem a ter pontos que alcançam os níveis salariais mais altos, especialmente quando combinados com maior tempo de experiência. Pode-se observar se há uma "elevação" geral dos pontos dessas cores no eixo Z.
*   **Interação entre Escolaridade e Experiência:** O objetivo principal deste gráfico é visualizar como a combinação específica de um nível de escolaridade e anos de experiência influencia o salário. Por exemplo, pode-se tentar observar se o "retorno" (aumento salarial) por ano adicional de experiência diferente para quem tem um Mestrado em comparação com quem tem somente Graduação. A densidade de pontos em certas regiões do gráfico (por exemplo, alta experiência e alto nível de escolaridade resultando em altos salários) pode indicar essas interações. Picos e vales na distribuição dos pontos podem corresponder a combinações que produzem valores máximos ou mínimos de salário.

**Como explorar o Gráfico Interativo:**
*   **Girar:** Clique e arraste para mudar o ponto de vista e observar a nuvem de pontos de diferentes ângulos. Isso ajuda a entender a profundidade e a sobreposição dos dados.
*   **Zoom:** Use o scroll do mouse para aproximar ou afastar, permitindo focar em áreas específicas de interesse (por exemplo, a distribuição salarial para um nível de escolaridade específico com muitos anos de experiência).
*   **Observar agrupamentos:** Procure por concentrações de pontos de uma mesma cor em determinadas regiões do espaço 3D.

Este tipo de gráfico é uma ferramenta poderosa na análise exploratória de dados (EDA) para identificar relações multivariadas e gerar hipóteses sobre as interações entre diferentes fatores.

## Grafico Mapa de Calor de Correlações
![__results___0_5](https://github.com/user-attachments/assets/5cf1cb29-6d4c-46dc-bc80-b9b32d679b12)
## Explicação do Gráfico: Mapa de Calor de Correlações

O gráfico apresentado é um **Mapa de Calor de Correlações** (heatmap) que visualiza a força e a direção das relações lineares entre três variáveis numéricas: "Faixa\_salarial\_num", "Oportunidade de aprendizado" e "Reputação da empresa".

**Como ler este Mapa de Calor:**
*   **Variáveis:** As variáveis analisadas estão listadas tanto nas linhas (eixo Y) quanto nas colunas (eixo X) da matriz.
*   **Células Coloridas:** Cada célula na interseção de duas variáveis mostra o coeficiente de correlação entre elas. A cor da célula representa visualmente esse coeficiente.
*   **Barra de Cores (Escala):** Localizada à direita do gráfico, a barra de cores indica como os valores de correlação mapeiam para as cores. Nesta visualização:
    *   Cores quentes (como vermelho intenso) indicam correlações positivas fortes, aproximando-se de +1.0.
    *   Cores frias (como azul intenso/roxo) indicam correlações negativas fortes (aproximando-se de -1.0) ou, como neste caso, correlações muito fracas ou próximas de zero.
    *   Cores neutras ou claras no meio da escala (se presentes) indicariam correlações próximas de 0. A escala no gráfico vai de 0.0 (azul escuro) a 1.0 (vermelho escuro).
*   **Valores Numéricos:** Dentro de cada célula, o valor numérico exato do coeficiente de correlação é exibido. Estes coeficientes variam de -1 (correlação negativa perfeita) a +1 (correlação positiva perfeita), com 0 indicando ausência de correlação linear.

**Interpretação das Correlações Exibidas:**

1.  **Diagonal Principal (de cima para baixo, da esquerda para a direita):**
    *   As células na diagonal principal mostram a correlação de cada variável consigo mesma. Esses valores são sempre **1.00** (vermelho intenso), indicando uma correlação positiva perfeita, o que é esperado.
        *   Faixa\_salarial\_num com Faixa\_salarial\_num: 1.00
        *   Oportunidade de aprendizado com Oportunidade de aprendizado: 1.00
        *   Reputação da empresa com Reputação da empresa: 1.00

2.  **Correlações entre Variáveis Distintas:**
    *   **Faixa\_salarial\_num e Oportunidade de aprendizado:**
        *   Coeficiente: **-0.04**.
        *   Cor: Azul escuro.
        *   Interpretação: Existe uma correlação linear negativa muito fraca, praticamente inexistente, entre a faixa salarial e a oportunidade de aprendizado. Um valor tão próximo de zero sugere não haver uma tendência clara de aumento ou diminuição salarial associada diretamente a maiores, ou menores oportunidades de aprendizado, conforme os dados analisados.

    *   **Faixa\_salarial\_num e Reputação da empresa:**
        *   Coeficiente: **0.00**.
        *   Cor: Azul escuro.
        *   Interpretação: Não há correlação linear entre a faixa salarial e a reputação da empresa. Isso indica que, neste conjunto de dados, a reputação da empresa não está linearmente associada a salários mais altos ou mais baixos.

    *   **Oportunidade de aprendizado e Reputação da empresa:**
        *   Coeficiente: **-0.05**.
        *   Cor: Azul escuro.
        *   Interpretação: Há uma correlação linear negativa muito fraca, quase nula, entre a oportunidade de aprendizado e a reputação da empresa. Isso sugere não haver uma relação linear significativa onde empresas com melhor reputação ofereçam consistentemente mais (ou menos) oportunidades de aprendizado, ou vice-versa, conforme os dados.

**Conclusão Geral do Mapa de Calor:**
Este mapa de calor indica que as três variáveis analisadas ("Faixa\_salarial\_num", "Oportunidade de aprendizado" e "Reputação da empresa") não possuem correlações lineares fortes entre si no contexto dos dados utilizados para esta análise. Todos os coeficientes de correlação entre pares de variáveis distintas são muito próximos de zero, sugerindo que essas variáveis são, em grande medida, linearmente independentes umas das outras. É importante notar que a correlação mede somente relações lineares; podem existir relações não lineares que não seriam capturadas por este tipo de análise.

## Grafico Distribuição por Gênero e Raça-Etnia
![__results___0_6](https://github.com/user-attachments/assets/46d749b3-6293-46b5-bca7-021d3843a544)
## Explicação dos gráficos: Distribuição por Gênero e Raça/Etnia

A imagem anexa exibe dois gráficos de barras que ilustram a distribuição demográfica dos profissionais no conjunto de dados analisados, um por gênero e outro por raça/etnia.

### Gráfico 1: Distribuição por Gênero

*   **Título:** "Distribuição por Gênero"
*   **Tipo de gráfico:** gráfico de barras verticais.
*   **Eixo Y (Vertical):** "count" (Contagem) – Indica o número de profissionais. A escala vai de 0 a 2500.
*   **Eixo X (Horizontal):** "Gênero do profissional" – Apresenta as categorias de gênero.
*   **Observações:**
    *   **Masculino:** É a categoria predominante, com uma contagem de aproximadamente 2500 profissionais. Esta é a barra mais alta no gráfico.
    *   **Feminino:** A segunda maior categoria, com uma contagem significativamente menor, em torno de 800 profissionais.
    *   **Outro:** Representa uma contagem muito pequena, quase insignificante visualmente no gráfico.
    *   **Prefiro não informar:** Também representa uma contagem muito pequena, similar à categoria "Outro".
*   **Conclusão:** O gráfico demonstra uma expressiva maioria de profissionais do gênero masculino no conjunto de dados analisado.

### Gráfico 2: Distribuição por Raça/Etnia

*   **Título:** "Distribuição por Raça/Etnia"
*   **Tipo de Gráfico:** Gráfico de barras verticais.
*   **Eixo Y (Vertical):** "count" (Contagem) – Indica o número de profissionais. A escala vai de 0 a mais de 2000.
*   **Eixo X (Horizontal):** "Cor/Raça/Etnia" – Apresenta as categorias de raça ou etnia.
*   **Observações:**
    *   **Branca:** É a categoria com a maior contagem, superando 2000 profissionais. Esta é a barra mais alta.
    *   **Parda:** A segunda categoria mais representada, com uma contagem de aproximadamente 800 profissionais.
    *   **Preta:** Apresenta uma contagem de cerca de 250 profissionais.
    *   **Amarela:** Possui uma contagem menor, em torno de 100 profissionais.
    *   **Prefiro não informar:** Representa uma contagem muito pequena,inferior a 50 profissionais.
    *   **Outra:** Contagem visualmente insignificante.
    *   **Indígena:** Contagem visualmente insignificante.
*   **Conclusão:** O gráfico indica que a maioria dos profissionais no conjunto de dados se identifica como branca, seguida pela categoria Parda. Outras categorias raciais/étnicas têm representação consideravelmente menor.

**Resumo Geral:**
Ambos os gráficos evidenciam desequilíbrios significativos nas distribuições. Há uma predominância de profissionais do gênero masculino e de profissionais que se identificam como da cor/raça Branca no dataset utilizado para a análise exploratória de dados.

## Grafico Distribuição Geográfica dos Profissionais
![__results___0_8](https://github.com/user-attachments/assets/b1f41cbe-9705-44ac-8b50-9407b5b07dd2)
## Explicação do Gráfico: Distribuição Geográfica dos Profissionais

O gráfico de barras verticais intitulado "Distribuição Geográfica dos Profissionais" ilustra a contagem de profissionais de dados distribuídos pelos diferentes estados (Unidades Federativas - UF) do Brasil, conforme o conjunto de dados analisado.

**Eixos do Gráfico:**
*   **Eixo Y (Vertical):** "Contagem" – Representa o número de profissionais em cada estado. A escala varia de 0 a mais de 1200.
*   **Eixo X (Horizontal):** "Estado (UF)" – Apresenta as siglas dos estados brasileiros.

**Interpretação da Distribuição Geográfica:**

*   **Concentração em São Paulo (SP):** O estado de São Paulo (SP) destaca-se com a maior concentração de profissionais, com uma contagem que ultrapassa 1200. Esta é, de longe, a barra mais alta no gráfico, indicando que uma parcela muito significativa dos profissionais no dataset está localizada em SP.
*   **Estados com Representação Significativa:** Após São Paulo, alguns outros estados apresentam contagens notáveis, embora consideravelmente menores:
    *   **Minas Gerais (MG):** É o segundo estado com maior número de profissionais, com uma contagem próxima de 400 (especificamente, cerca de 380).
    *   **Paraná (PR):** Apresenta uma contagem um pouco acima de 300 profissionais.
    *   **Rio de Janeiro (RJ):** Também com uma contagem em torno de 300 profissionais.
    *   **Rio Grande do Sul (RS):** Possui cerca de 200 profissionais.
    *   **Santa Catarina (SC):** Apresenta uma contagem um pouco abaixo de 200, em torno de 180 profissionais.
*   **Demais Estados:**
    *   **Distrito Federal (DF), Bahia (BA), Ceará (CE), Pernambuco (PE), Espírito Santo (ES), Goiás (GO), Paraíba (PB):** Estes estados formam um grupo com contagens menores, variando aproximadamente entre 50 e 100 profissionais cada.
    *   **Outros Estados (MT, RN, AM, PA, SE, AL, MS, MA, PI, RO, AP, TO):** A grande maioria dos demais estados brasileiros apresenta contagens muito baixas, com barras quase insignificantes em comparação com os estados mais populosos em termos de profissionais de dados. Muitos desses estados têm menos de 50 profissionais representados no dataset.

**Conclusão Geral do Gráfico:**
O gráfico evidencia uma forte concentração geográfica dos profissionais de dados no Brasil, com o estado de São Paulo dominando expressivamente. A região Sudeste (com SP, MG, RJ, ES) e a região Sul (com PR, RS, SC) concentram a maioria desses profissionais. As demais regiões e estados possuem uma representação significativamente menor no conjunto de dados analisado.

## Grafico Salário por Nível de Senioridade
![__results___0_9](https://github.com/user-attachments/assets/4cb778a5-1f36-40a9-b815-b0e97c02d2c8)
## Explicação do Gráfico: Salário por Nível de Senioridade

O gráfico de boxplot intitulado "Salário por Nível de Senioridade" ilustra a distribuição da faixa salarial numérica ("Faixa\_salarial\_num") entre diferentes níveis de senioridade profissional: Júnior, Pleno e Sênior.

**Como ler este gráfico de Boxplot:**
*   **Caixa (Box):** Representa o intervalo interquartil (IQR), onde se concentram 50% dos salários. A linha inferior da caixa é o primeiro quartil (Q1 - 25º percentil), e a linha superior é o terceiro quartil (Q3 - 75º percentil).
*   **Linha na Caixa:** Indica a mediana (Q2 - 50º percentil), sendo o valor salarial central para cada nível de senioridade.
*   **Hastess/"Bigodes" (Whiskers):** As linhas que se estendem a partir da caixa mostram o alcance dos dados, geralmente até 1,5 vezes o IQR. Pontos além dessas hastes são considerados outliers.
*   **Outliers:** São pontos individuais (representados por losangos no gráfico) que indicam salários atípicos, significativamente mais altos ou mais baixos do que a maioria dos salários para aquele nível de senioridade.
*   **Eixo Y (Vertical):** "Faixa\_salarial\_num" representa os salários em Reais (R$), com a escala variando de R$0 a R$40.000.
*   **Eixo X (Horizontal):** "Nível de senioridade" categoriza os profissionais em "Júnior", "Pleno" e "Sênior".

**Interpretação das Distribuições Salariais por Nível de Senioridade:**

*   **Júnior (Caixa Verde):**
    *   **Mediana Salarial:** É a mais baixa entre os três níveis, situando-se em torno de R$3.500 - R$4.000.
    *   **Intervalo Interquartil (IQR):** A maioria dos salários (50% centrais) está concentrada entre aproximadamente R$2.500 e R$5.000.
    *   **Dispersão e Outliers:** A faixa salarial típica (incluindo os "bigodes") vai de perto de R$0 até cerca de R$7.000. Observam-se alguns outliers com salários mais altos chegando até aproximadamente R$18.000.

*   **Pleno (Caixa Laranja):**
    *   **Mediana Salarial:** Apresenta um aumento significativo em relação ao nível Júnior, localizando-se em torno de R$7.000.
    *   **Intervalo Interquartil (IQR):** Os 50% centrais dos salários estão entre aproximadamente R$5.000 e R$10.000.
    *   **Dispersão e Outliers:** A faixa salarial típica se estende de cerca de R$1.000 até aproximadamente R$14.000. Este nível possui vários outliers com salários mais elevados, incluindo valores próximos a R$18.000, R$22.500 e até um ponto próximo a R$40.000.

*   **Sênior (Caixa Azul):**
    *   **Mediana Salarial:** É a mais alta dos três níveis, posicionando-se em torno de R$11.500 - R$12.000.
    *   **Intervalo Interquartil (IQR):** A maior parte dos salários (50% centrais) varia entre R$10.000 e R$14.000.
    *   **Dispersão e Outliers:** A faixa salarial típica vai de aproximadamente R$5.000 até cerca de R$18.500. Assim como o nível Pleno, o nível Sênior também apresenta outliers com salários significativamente altos, com pontos próximos a R$22.500 e um próximo a R$40.000. Existem também alguns outliers inferiores, indicando salários mais baixos que o usual para esta senioridade.

**Conclusões Gerais do Gráfico:**
*   **Progressão Salarial Clara:** O gráfico demonstra uma clara progressão salarial à medida que o nível de senioridade aumenta. Profissionais Sênior têm a maior mediana salarial, seguidos por Pleno e depois Júnior.
*   **Aumento da Dispersão:** A variabilidade salarial (altura da caixa e extensão dos "bigodes") tende a aumentar com a senioridade, indicando uma gama mais ampla de salários pagos nos níveis Pleno e Sênior em comparação com o Júnior.
*   **Potencial de Altos Salários:** Embora os outliers existam em todos os níveis, eles atingem valores mais altos e são mais frequentes nos níveis Pleno e Sênior, sugerindo que profissionais com maior senioridade têm maior potencial para alcançar remunerações excepcionalmente elevadas.

Em resumo, o nível de senioridade é um fator importante na determinação da faixa salarial, com um aumento consistente na remuneração e na variabilidade salarial à medida que os profissionais progridem de Júnior para Pleno e Sênior.

## Grafico Análise Multivariada das Relações entre Variáveis Selecionadas
![__results___0_11](https://github.com/user-attachments/assets/f8a270d1-8bb7-4612-9c54-0c083f46936a)
## Explicação do Gráfico: Análise Multivariada das Relações entre Variáveis Selecionadas (Pair Plot)

O gráfico apresentado é uma **matriz de gráficos de dispersão (pair plot)**, intitulada "Análise Multivariada das Relações entre Variáveis Selecionadas". Este tipo de visualização é utilizado para mostrar as relações entre pares de múltiplas variáveis simultaneamente, bem como a distribuição individual de cada variável.

As variáveis analisadas são:
*   "Faixa\_salarial\_num" (Salário)
*   "Oportunidade de aprendizado"
*   "Reputação da empresa"

**Estrutura do Gráfico:**

*   **Diagonal Principal:** Os gráficos ao longo da diagonal (do canto superior esquerdo ao canto inferior direito) mostram a **distribuição de cada variável individualmente**, geralmente por meio de um histograma ou, como neste caso, uma estimativa de densidade do kernel (KDE).
*   **Fora da Diagonal:** Os gráficos fora da diagonal são **gráficos de dispersão (scatter plots)** que mostram a relação entre duas variáveis diferentes. Cada gráfico de dispersão (i,j) mostra a variável do eixo i contra a variável do eixo j.

**Interpretação dos Gráficos Individuais:**

1.  **Distribuições Individuais (Diagonal):**
    *   **Faixa\_salarial\_num (Topo Esquerdo):** A distribuição dos salários é multimodal (apresenta múltiplos picos) e assimétrica à direita. Há uma concentração maior em salários mais baixos (em torno de R$5.000-R$10.000), com picos menores em salários mais altos e uma cauda que se estende até R$40.000.
    *   **Oportunidade de aprendizado (Meio):** Esta variável parece ser binária ou categórica, com a grande maioria dos dados concentrada em dois valores principais (provavelmente 0 e 1, representando, por exemplo, baixa/alta oportunidade ou sim/não). Há um pico maior em um dos valores e um pico menor no outro.
    *   **Reputação da empresa (Inferior Direito):** Similar à "Oportunidade de aprendizado", esta variável também parece ser binária ou categórica, com a maioria dos dados concentrados em dois valores principais. Um dos valores tem uma densidade muito maior que o outro.

2.  **Relações entre Pares de Variáveis (Fora da Diagonal):**

    *   **Oportunidade de aprendizado vs. Faixa\_salarial\_num (Linha 1, Coluna 2 e Linha 2, Coluna 1):**
        *   Os pontos estão concentrados em duas faixas horizontais (ou verticais, dependendo da orientação do par), correspondentes aos dois principais valores da variável "Oportunidade de aprendizado".
        *   Visualmente, não há uma tendência clara (ascendente ou descendente) que sugira uma forte correlação linear entre salário e oportunidade de aprendizado. Os salários parecem variar amplamente para ambos os níveis de oportunidade de aprendizado.

    *   **Reputação da empresa vs. Faixa\_salarial\_num (Linha 1, Coluna 3 e Linha 3, Coluna 1):**
        *   Similar ao par anterior, os pontos se agrupam em duas faixas horizontais (ou verticais) correspondentes aos valores da "Reputação da empresa".
        *   Não se observa uma relação linear forte. Os salários variam amplamente, independentemente do nível de reputação da empresa exibido.

    *   **Reputação da empresa vs. Oportunidade de aprendizado (Linha 2, Coluna 3 e Linha 3, Coluna 2):**
        *   Este gráfico evidencia como ambos os valores de "Oportunidade de aprendizado" se distribuem em relação aos dois valores de "Reputação da empresa". Os pontos se agrupam nos quatro cantos possíveis (0,0; 0,1; 1,0; 1,1), se as variáveis forem binárias 0/1. A densidade de pontos em cada um desses "cantos" indicaria a frequência dessas combinações.
        *   Visualmente, parece não haver um padrão forte de associação. Por exemplo, não parece que empresas com alta reputação consistentemente oferecem alta oportunidade de aprendizado, ou vice-versa.

**Conclusão Geral do Gráfico:**
O pair plot reforça visualmente a ausência de correlações lineares fortes entre "Faixa\_salarial\_num", "Oportunidade de aprendizado" e "Reputação da empresa", o que já havia sido sugerido pelo mapa de calor de correlações anteriormente. As variáveis "Oportunidade de aprendizado" e "Reputação da empresa" apresentam distribuições que sugerem natureza binária ou categórica com poucos níveis. As relações entre os pares de variáveis não exibem padrões lineares claros, indicando que esses fatores, isoladamente ou em pares diretos, não explicam de forma linear e significativa a variação salarial ou mutualmente neste conjunto de dados.

## Grafico Sunburst da Distribuição de Profissionais de Dados
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/11ec6c319fd644ad08f61cff87cc702c/raw/392be6308934280602be52c7a1ec9cab21e1ad03/sunburst_chart.html)
![newplot (1)](https://github.com/user-attachments/assets/fc4076b1-1a10-48d1-89b2-3f76a107321b)

## Explicação do Gráfico Interativo: Sunburst da Distribuição de Profissionais de Dados.

O gráfico apresentado é um **gráfico de explosão solar (sunburst chart)** interativo. Este tipo de visualização é ideal para exibir dados hierárquicos, mostrando como um grupo principal se divide em subgrupos e assim por diante, em uma série de anéis concêntricos.

**Como ler este gráfico Sunburst:**

*   **Círculos Concêntricos (Anéis):** Cada anel representa um nível na hierarquia dos dados.
    *   **Centro do Gráfico:** O círculo mais interno representa o topo da hierarquia, neste caso, o total de "Profissionais de Dados" no dataset analisado.
    *   **Anéis Subsequentes:** Cada anel externo subdivide as categorias do anel interno adjacente.
*   **Segmentos (Fatias):** Cada anel é dividido em segmentos. O tamanho (ângulo ou área) de cada segmento é proporcional à sua participação ou contagem na categoria pai no anel interno.
*   **Cores:** Cores diferentes são usadas para distinguir as categorias em cada nível, auxiliando na visualização das proporções e relações.
*   **Interatividade:**
    *   **Hover (Passar o Mouse):** Ao passar o mouse sobre um segmento, ele é destacado, e geralmente uma dica de ferramenta (tooltip) exibe informações detalhadas, como o caminho hierárquico completo e o valor (contagem de profissionais) para aquele segmento específico.
    *   **Clique:** Clicar em um segmento geralmente "foca" ou "dá zoom" naquela categoria, tornando-a o novo centro do gráfico e exibindo suas subdivisões com mais detalhes. Clicar no centro do gráfico retorna ao nível hierárquico anterior.

**Hierarquia e Interpretação dos Dados Neste Gráfico Específico:**

Observando o gráfico interativo:

1.  **Nível Central (Raiz):**
    *   Representa o total de "Profissionais de Dados" considerados na análise.

2.  **Primeiro Anel (Nível de Escolaridade):**
    *   Subdivide os profissionais de dados pelo "Nível de Escolaridade".
    *   As categorias visíveis são: "Graduação/Bacharelado", "Pós-graduação", "Mestrado", "Estudante de Graduação" e "Doutorado ou PhD".
    *   O tamanho de cada segmento neste anel indica a proporção de profissionais com aquele nível de escolaridade. Por exemplo, "Graduação/Bacharelado" parece ser a maior fatia, indicando o nível de escolaridade mais comum.

3.  **Segundo Anel (Tempo de Experiência):**
    *   Subdivide cada categoria de "Nível de Escolaridade" pelo "Tempo de experiência na área de dados".
    *   As faixas de experiência incluem: "de 1 a 2 anos", "de 3 a 4 anos", "Menos de 1 ano", "de 4 a 6 anos", "de 7 a 10 anos" e "de 5 a 6 anos".
    *   O tamanho de um segmento neste anel mostra, por exemplo, quantos profissionais com "Graduação/Bacharelado" têm "de 1 a 2 anos" de experiência.

4.  **Terceiro Anel (Faixa Salarial Média):**
    *   Subdivide cada combinação de "Nível de Escolaridade" e "Tempo de Experiência" pela "Faixa Salarial Média (R$)".
    *   As faixas salariais incluem: "0-5000", "5001-10000", "10001-15000", "15001-20000", etc.
    *   O tamanho de um segmento neste anel mais externo indica, por exemplo, quantos profissionais com "Graduação/Bacharelado" e "de 1 a 2 anos" de experiência se enquadram na faixa salarial de "5001-10000". Os números nos segmentos representam a contagem de profissionais.

**Como Extrair Insights:**

*   **Proporções Dominantes:** Identifique rapidamente os níveis de escolaridade mais comuns, as faixas de experiência predominantes dentro de cada nível de escolaridade e as faixas salariais mais frequentes para cada combinação de escolaridade e experiência.
*   **Relações Hierárquicas:** Entenda como os grupos se subdividem. Por exemplo, pode-se explorar se profissionais com "Mestrado" e "de 7 a 10 anos" de experiência tendem a se concentrar em faixas salariais mais altas em comparação com aqueles com "Graduação/Bacharelado" e a mesma experiência.
*   **Exploração Interativa:** Use o clique para focar em segmentos de interesse. Por exemplo, clicando em "Mestrado", o gráfico se reorganizará para mostrar somente as subdivisões de experiência e salário para mestres, permitindo uma análise mais detalhada desse subgrupo específico.

Este gráfico sunburst oferece uma visão rica e interativa da composição da força de trabalho de profissionais de dados no Brasil, conforme o dataset, permitindo a exploração de como a escolaridade, a experiência e os salários se inter-relacionam em diferentes níveis.

---

## Analise exploratoria de dados base de dados Microdados

---

## Grafico Distribuição Nacional de Níveis de Formação dos Docentes
![01_distribuicao_formacao_nacional](https://github.com/user-attachments/assets/0052b7ec-4124-4e90-a500-8abd26d0ccc8)
## Explicação do Gráfico: Distribuição Nacional de Níveis de Formação dos Docentes

O gráfico de pizza ilustra a proporção dos docentes ao nível nacional, classificados de acordo com seu nível de formação acadêmica. Os dados são provenientes do arquivo `microdados_agrupados_por_uf.csv`.

**Principais observações do gráfico:**

*   **Docentes com Doutorado:** Este grupo constitui a maior fatia, representando **52,3%** do total de docentes analisados. Isso indica que mais da metade dos docentes possui o título acadêmico mais elevado.
*   **Docentes com Mestrado:** Correspondem a **33,3%** do corpo docente. Somados aos doutores, os docentes com pós-graduação *stricto sensu* (mestrado ou doutorado) são a grande maioria.
*   **Docentes com Especialização:** Representam **13,9%** dos docentes. Este grupo possui pós-graduação *lato sensu*.
*   **Docentes com Graduação:** Apenas **0,6%** dos docentes possuem somente a graduação como nível de formação mais alto. Este é o menor grupo, sugerindo que a progressão para níveis de pós-graduação é comum na carreira docente.

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico de pizza fornece uma visão geral do perfil educacional dos docentes no Brasil, com base nos dados disponíveis. Ele demonstra uma alta qualificação acadêmica, com a maioria possuindo títulos de mestre ou doutor.

Para a pergunta de pesquisa original sobre "como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil", este gráfico oferece um panorama da variável "formação acadêmica" para o grupo de "docentes". No entanto, conforme discutido anteriormente, para analisar a disparidade salarial, seriam necessários dados de remuneração e uma clara identificação de "profissionais de dados", que não estão presentes no dataset atual.

A predominância de altos níveis de escolaridade é um fator importante, mas sua interação com a experiência profissional e o impacto na disparidade salarial demandariam um conjunto de dados mais completo.


## Grafico Top 10 Estados por Nível de Formação de Docentes
![02_top10_estados_formacao](https://github.com/user-attachments/assets/4513d6de-20bd-4e5b-9b93-1cd10b819ad5)
## Explicação do Gráfico: Top 10 Estados por Nível de Formação de Docentes

O gráfico de barras empilhadas ilustra o número total de docentes nos 10 estados com maior contingente, detalhando a distribuição desses profissionais conforme seu nível de formação acadêmica. O eixo vertical ("Número de Docentes") quantifica o total de docentes, enquanto o eixo horizontal ("Estado") lista as siglas dos respectivos estados. Cada barra é segmentada por cores que representam os diferentes níveis de formação:

*   **Rosa:** Docentes com Graduação
*   **Dourado/Marrom:** Docentes com Especialização
*   **Verde:** Docentes com Mestrado
*   **Azul-petróleo (Teal):** Docentes com Doutorado

**Principais observações do gráfico:**

*   **Liderança de São Paulo (SP):** O estado de São Paulo (SP) destaca-se com o maior número absoluto de docentes, ultrapassando 70.000 profissionais. Dentro deste total, a maior parcela é composta por docentes com doutorado, seguida por mestrado e especialização.
*   **Minas Gerais (MG) e Rio de Janeiro (RJ):** Minas Gerais (MG) ocupa a segunda posição, com aproximadamente 40.000 docentes, seguido pelo Rio de Janeiro (RJ), com pouco mais de 30.000. Ambos os estados também apresentam uma predominância de docentes com doutorado e mestrado.
*   **Demais estados no Top 10:** Os estados do Paraná (PR), Rio Grande do Sul (RS), Bahia (BA), Santa Catarina (SC), Pernambuco (PE), Ceará (CE) e Goiás (GO) completam o ranking dos 10 estados com mais docentes. Neles todos, a tendência de maior concentração nos níveis de doutorado e mestrado se mantém, embora em menor escala absoluta comparado a SP, MG e RJ.
*   **Proporção dos Níveis de Formação:** Em todos os estados visualizados, a formação de doutorado (azul-petróleo) representa a maior ou uma das maiores parcelas do total de docentes. Em seguida, aparecem geralmente os docentes com mestrado (verde). Docentes com somente especialização (dourado/marrom) formam um grupo menor, e aqueles com somente graduação (rosa) são a menor fração, quase imperceptível em alguns estados, indicando um alto nível de qualificação formal do corpo docente nesses estados.

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico permite uma comparação visual da quantidade e do perfil de formação dos docentes entre os principais estados brasileiros. Ele reforça a observação de que o corpo docente, especialmente nos estados com maior número de profissionais, possui elevada qualificação acadêmica, com forte presença de doutores e mestres.

Para a pergunta de pesquisa sobre a influência da formação acadêmica e experiência profissional na disparidade salarial entre profissionais de dados, este gráfico detalha a variável "formação acadêmica" em um nível geográfico (estadual) para "docentes". A análise da disparidade salarial, contudo, ainda dependeria da inclusão de dados de remuneração e da identificação específica de "profissionais de dados" dentro desse universo de docentes ou em um dataset complementar. Observar onde se concentram os docentes mais qualificados pode ser um ponto de partida para investigar se há correlação com polos de desenvolvimento em ciência de dados, mas a relação direta com salários não pode ser inferida somente com este gráfico.

## Grafico Distribuição Etária Nacional dos Docentes
![03_distribuicao_etaria_nacional](https://github.com/user-attachments/assets/38b315e0-7eb6-4c40-820f-3b0281b1b1d8)
## Explicação do Gráfico: Distribuição Etária Nacional dos Docentes

O gráfico de barras verticais, intitulado "Distribuição Etária Nacional dos Docentes", exibe a quantidade de docentes em nível nacional, agrupados por diferentes faixas etárias. O eixo vertical ("Quantidade") indica o número de docentes, enquanto o eixo horizontal ("Faixa Etária") categoriza os docentes em grupos de idade.

**Principais observações do gráfico:**

*   **Pico na Faixa de 40-44 anos:** A faixa etária com o maior número de docentes é a de "Docentes\_Idade\_40\_44", com quase 70.000 profissionais. Isso sugere que o maior contingente de docentes se encontra nessa fase da carreira.
*   **Concentração entre 35 e 49 anos:** As faixas etárias "Docentes\_Idade\_35\_39" (pouco mais de 60.000 docentes) e "Docentes\_Idade\_45\_49" (pouco menos de 60.000 docentes) também apresentam um número elevado de profissionais, indicando que uma parcela significativa do corpo docente nacional está entre 35 e 49 anos.
*   **Presença Significativa em Faixas Mais Elevadas:** A faixa "Docentes\_Idade\_60\_mais" também mostra um número considerável de docentes, com mais de 45.000 profissionais. Isso indica uma retenção de docentes mais experientes no sistema ou um envelhecimento da força de trabalho docente.
*   **Menor Quantidade nas Faixas Mais Jovens e Intermediárias Superiores:** As faixas "Docentes\_Idade\_30\_34" (pouco menos de 40.000), "Docentes\_Idade\_50\_54" (aproximadamente 45.000) e "Docentes\_Idade\_55\_59" (pouco menos de 40.000) apresentam quantidades menores em comparação com o pico, mas ainda representam um número substancial de docentes. A distribuição geral se assemelha a uma curva que atinge seu pico na faixa dos 40-44 anos e depois declina gradualmente, com uma leve recuperação na faixa de 60 anos ou mais.

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico fornece um panorama da distribuição etária dos docentes no Brasil. No contexto da pergunta de pesquisa sobre "como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil", a idade pode ser utilizada como um *proxy* (uma aproximação) para a experiência profissional. Geralmente, espera-se que profissionais mais velhos tenham acumulado mais anos de experiência.

A concentração de docentes em faixas etárias mais maduras (40-49 anos) e a presença significativa de docentes com 60 anos ou mais podem indicar um corpo docente experiente. Para analisar a disparidade salarial, seria necessário cruzar esses dados etários (como proxy de experiência) com informações sobre a formação acadêmica (analisada em gráficos anteriores) e, crucialmente, com dados de remuneração específicos para "profissionais de dados", os quais não estão presentes no dataset atual. Este gráfico ajuda a caracterizar uma dimensão da "experiência profissional" agregadamente para o grupo de docentes.


## Grafico Matriz de Correlação entre Formação e Faixa Etária
![04_heatmap_correlacao](https://github.com/user-attachments/assets/18c3148a-1e19-49af-bc4e-bbc1b61910bf)
## Explicação do Gráfico: Matriz de Correlação entre Formação e Faixa Etária

O gráfico apresentado é uma **matriz de correlação**, visualizada como um *heatmap* (mapa de calor). Ele exibe a força e a direção da relação linear entre diferentes níveis de formação acadêmica dos docentes e suas faixas etárias, com base nos dados agregados por Unidade da Federação (UF).

**Como interpretar o gráfico:**

*   **Eixos:** Tanto o eixo horizontal quanto o vertical listam as mesmas variáveis: os diferentes níveis de formação (`Docentes_Graduacao`, `Docentes_Especializacao`, `Docentes_Mestrado`, `Docentes_Doutorado`) e as diferentes faixas etárias (`Docentes_Idade_30_34`, ..., `Docentes_Idade_60_mais`).
*   **Células e Valores:** Cada célula na interseção de duas variáveis evidencia  o coeficiente de correlação de Pearson entre elas. Este coeficiente varia de -1 a +1:
    *   **+1:** Correlação positiva perfeita (quando uma variável aumenta, a outra também aumenta proporcionalmente).
    *   **0:** Nenhuma correlação linear.
    *   **-1:** Correlação negativa perfeita (quando uma variável aumenta, a outra diminui proporcionalmente).
*   **Cores:** A barra de cores à direita indica a intensidade da correlação:
    *   **Cores quentes (vermelho intenso):** Correlação positiva forte (próxima de +1).
    *   **Cores frias (azul intenso):** Correlação negativa forte (próxima de -1).
    *   **Cores neutras (próximo ao branco/cinza claro):** Correlação fraca (próxima de 0).
*   **Diagonal Principal:** A diagonal de cima para baixo, da esquerda para a direita, sempre mostra o valor 1.00 (vermelho intenso), ao representar a correlação de cada variável consigo mesma, sendo sempre perfeita.

**Principais observações e correlações:**

1.  **Alta Correlação entre Níveis de Pós-Graduação:**
    *   Há correlações muito fortes e positivas entre os diferentes níveis de pós-graduação. Por exemplo, `Docentes_Mestrado` e `Docentes_Doutorado` têm uma correlação de 0.98. Similarmente, `Docentes_Especializacao` e `Docentes_Mestrado` também apresentam 0.98.
    *   Isso sugere que as UFs que possuem um alto número de docentes com um tipo de pós-graduação (ex: mestrado) tendem a ter também um alto número de docentes com outros tipos de pós-graduação (ex: doutorado, especialização).

2.  **Alta Correlação entre Faixas Etárias Adjacentes e Próximas:**
    *   As faixas etárias demonstram correlações positivas muito altas entre si, especialmente as adjacentes. Por exemplo, `Docentes_Idade_35_39` e `Docentes_Idade_40_44` têm correlação de 0.99.
    *   Isso indica que UFs com muitos docentes em uma faixa etária específica tendem a ter também muitos docentes nas faixas etárias vizinhas.

3.  **Forte Correlação entre Níveis de Pós-Graduação e a Maioria das Faixas Etárias:**
    *   Os níveis de pós-graduação (`Docentes_Especializacao`, `Docentes_Mestrado`, `Docentes_Doutorado`) mostram correlações positivas consistentemente altas (geralmente acima de 0.90) com a maioria das faixas etárias, especialmente as intermediárias e mais velhas (a partir de `Docentes_Idade_35_39` até `Docentes_Idade_55_59`).
    *   Por exemplo, `Docentes_Mestrado` tem correlação de 1.00 com `Docentes_Idade_45_49`, e `Docentes_Doutorado` tem 0.99 com `Docentes_Idade_40_44` e `Docentes_Idade_45_49`.
    *   Isso sugere que UFs com inúmeros docentes pós-graduados tendem a ter muitos docentes distribuídos por diversas faixas etárias, refletindo um corpo docente qualificado e maduro.

4.  **Correlações Mais Baixas com `Docentes_Graduacao`:**
    *   A variável `Docentes_Graduacao` (que representa docentes somente com graduação) apresenta correlações consideravelmente mais baixas com todos os outros níveis de formação e com todas as faixas etárias (valores variando de 0.26 a 0.40).
    *   Por exemplo, a correlação entre `Docentes_Graduacao` e `Docentes_Doutorado` é de 0.38, e entre `Docentes_Graduacao` e `Docentes_Idade_35_39` é de 0.40.
    *   Isso pode indicar que a distribuição de docentes somente com graduação pelas UFs não segue o mesmo padrão da distribuição de docentes pós-graduados ou das diferentes faixas etárias de forma tão intensa.

5.  **Correlações Ligeiramente Menores nas Faixas Etárias Extremas com Formação:**
    *   Para a faixa etária mais jovem (`Docentes_Idade_30_34`), as correlações com os níveis mais altos de formação (Mestrado e Doutorado) são um pouco menores (0.95 e 0.94, respectivamente) em comparação com faixas etárias intermediárias. Isso é esperado, por levar tempo para obter esses títulos.
    *   Da mesma forma, para a faixa `Docentes_Idade_60_mais`, as correlações com os níveis de pós-graduação também são um pouco menores, embora ainda altas (ex: 0.96 com Doutorado, 0.89 com `Docentes_Idade_35_39`).

**Contextualização para a Análise Exploratória de Dados:**

Esta matriz de correlação revela que, em nível estadual, a presença de docentes com alta qualificação (mestrado, doutorado) está fortemente associada à presença de docentes em diversas faixas etárias, especialmente as mais experientes. Indica também que estados com um forte contingente em um nível de pós-graduação tendem a ser fortes nos outros.

Para a pergunta de pesquisa sobre como formação e experiência (proxy pela idade) interagem para influenciar a disparidade salarial, esta análise evidencia que, nos estados, há uma coocorrência significativa de alta formação e diversas faixas etárias. No entanto, a matriz não inclui dados salariais. Se dados salariais fossem adicionados, poderíamos investigar se UFs com alta correlação entre formação e idade (experiência) apresentam padrões específicos de disparidade salarial para "profissionais de dados". A ausência de uma forte correlação da variável `Docentes_Graduacao` com as demais sugere que este grupo pode ter características distintas que precisariam ser exploradas separadamente.


## Grafico Mapa Interativo de Bolhas - Distribuição de Docentes por Nível de Formação e UF
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/9d708a6e00717a471ed00ab3e3742a40/raw/c1f0d385f7c9ad6f156de6d78dfcc9d245c68c99/06_mapa_bolhas_interativo.html)
![06_mapa_bolhas](https://github.com/user-attachments/assets/8a39d31d-a20f-4e3a-a51a-010005ad43b1)
## Explicação do Gráfico: Mapa Interativo de Bolhas - Distribuição de Docentes por Nível de Formação e UF

O gráfico apresentado é um **mapa de bolhas interativo** que visualiza a distribuição do número de docentes em cada Unidade da Federação (UF) do Brasil, segmentado por nível de formação acadêmica. Este tipo de gráfico utiliza círculos (bolhas) de tamanhos variados sobre um mapa para representar a magnitude de uma variável em diferentes regiões geográficas.

**Como interpretar o gráfico:**

*   **Base Geográfica:** O mapa do Brasil serve como plano de fundo, com as bolhas posicionadas sobre os respectivos estados.
*   **Bolhas:** Cada bolha no mapa representa um nível de formação específico dentro de um estado.
    *   **Cor da Bolha:** A cor da bolha indica o nível de formação acadêmica, conforme a legenda fornecida no gráfico:
        *   **Azul:** Docentes com Doutorado
        *   **Verde:** Docentes com Mestrado
        *   **Laranja/Amarelo:** Docentes com Especialização
        *   **Vermelho:** Docentes com Graduação
    *   **Tamanho da Bolha:** O tamanho da bolha é diretamente proporcional ao **número de docentes** com aquele nível de formação específico naquela UF. Bolhas maiores indicam um número maior de docentes.
    *   **Interatividade:** Ao passar o cursor do mouse sobre uma bolha, uma caixa de informações (tooltip) aparece, exibindo detalhes como a sigla da UF, o nível de formação representado pela bolha e o número exato de docentes correspondente.

**Principais observações do gráfico:**

*   **Concentração Regional de Alta Qualificação:** Observa-se visualmente que estados como São Paulo (SP), Minas Gerais (MG), Rio de Janeiro (RJ), Paraná (PR) e Rio Grande do Sul (RS) tendem a apresentar bolhas azuis (Doutorado) e verdes (Mestrado) proeminentes, indicando uma concentração significativa de docentes com alta qualificação nessas regiões.
*   **Predominância de Doutorado e Mestrado:** Em muitos estados, as bolhas azuis (Doutorado) e verdes (Mestrado) são as de maior tamanho, reforçando a constatação de gráficos anteriores sobre a alta qualificação (pós-graduação *stricto sensu*) do corpo docente na maioria das UFs.
*   **Variações Estaduais:** O mapa permite uma rápida comparação entre os estados. Alguns estados, especialmente nas regiões Norte e Nordeste, podem apresentar um volume total de docentes menor (bolhas geralmente menores) ou uma distribuição proporcional diferente entre os níveis de formação quando comparados aos estados do Sul e Sudeste.
*   **Baixa Representatividade da Graduação:** As bolhas vermelhas (Graduação), que representam docentes com apenas graduação, são consistentemente as menores em todos os estados, muitas vezes quase imperceptíveis, confirmando o baixo número de docentes que não possuem pós-graduação.

**Contextualização para a Análise Exploratória de Dados:**

Este mapa de bolhas interativo oferece uma dimensão geográfica à análise da formação acadêmica dos docentes. Ele permite identificar visualmente "hotspots" ou áreas de maior concentração de docentes por nível de formação.

No contexto da pergunta de pesquisa sobre "como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil", este gráfico contribui ao:
*   Mapear a distribuição da **formação acadêmica** dos docentes (o grupo disponível no dataset) pelo território nacional.
*   Permitir a identificação de estados com maior ou menor concentração de docentes altamente qualificados.

Para avançar na resposta à pergunta de pesquisa, seria necessário cruzar essas informações geográficas de formação com dados de experiência profissional (que poderiam ser agregados por UF) e, fundamentalmente, com dados salariais específicos para "profissionais de dados" em cada estado. O mapa atual é uma ferramenta exploratória valiosa para entender a distribuição da qualificação docente, mas não contém, por si só, informações sobre salários ou experiência para analisar diretamente a disparidade salarial de profissionais de dados.


## Grafico Gráfico de Dispersão 3D Interativo - Mestrado, Doutorado e Média de Idade dos Docentes por UF
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/5edbfdc4c69d324455e65eef06c591b6/raw/d304db3742f4839c7bf4360c2ed75a06bce75bbe/07_3d_interativo.html)
![07_3d_interativo](https://github.com/user-attachments/assets/7b396546-3b72-4dc2-9897-0f6af9600cc7)
## Explicação do Gráfico: Gráfico de Dispersão 3D Interativo - Mestrado, Doutorado e Média de Idade dos Docentes por UF

O gráfico apresentado é um **gráfico de dispersão 3D interativo**. Ele visualiza a relação entre três variáveis para cada Unidade da Federação (UF) do Brasil: o número de docentes com mestrado, o número de docentes com doutorado e a média de idade dos docentes.

**Como interpretar o gráfico:**

*   **Eixos:** O gráfico possui três eixos, cada um representando uma variável quantitativa:
    *   **Eixo X (horizontal, profundidade):** `Docentes_Mestrado` - Número de docentes com título de Mestre na UF.
    *   **Eixo Y (horizontal, largura):** `Docentes_Doutorado` - Número de docentes com título de Doutor na UF.
    *   **Eixo Z (vertical, altura):** `Media_Idade_Docentes` - Média de idade dos docentes na UF.
*   **Pontos:** Cada ponto (esfera) no espaço 3D representa uma Unidade da Federação (UF). A posição do ponto é determinada pelos valores das três variáveis para aquela UF.
*   **Cores dos Pontos:** No gráfico visualizado, os pontos parecem ter uma cor azulada uniforme. A legenda ou interatividade poderiam revelar se a cor representa alguma outra variável, mas com base na imagem estática, ela parece ser somente  para visualização dos pontos.
*   **Interatividade:** Por ser um gráfico interativo (geralmente criado com bibliotecas como Plotly):
    *   **Rotação:** É possível girar o gráfico para visualizar a dispersão dos pontos de diferentes ângulos, ajudando a perceber padrões e relações espaciais.
    *   **Zoom:** Pode-se aproximar ou afastar para focar em regiões específicas do gráfico.
    *   **Hover (Passar o mouse):** Ao passar o cursor sobre um ponto, informações adicionais sobre aquela UF (como o nome da UF e os valores exatos das três variáveis) são tipicamente exibidas.

**Principais observações (baseadas na estrutura visual):**

*   **Relação entre Mestrado e Doutorado:** Observa-se uma tendência geral de que UFs com um alto número de docentes com mestrado (valores mais altos no eixo X) também tendem a ter um alto número de docentes com doutorado (valores mais altos no eixo Y). Isso é indicado pela dispersão dos pontos que tende a se estender diagonalmente no plano XY.
*   **Variação na Média de Idade:** Os pontos se distribuem em diferentes alturas ao longo do eixo Z, indicando variação na média de idade dos docentes entre as UFs.
*   **Identificação de Clusters e Outliers:**
    *   Pode haver agrupamentos (clusters) de UFs com características semelhantes (por exemplo, UFs com muitos mestres, muitos doutores e alta média de idade).
    *   Alguns pontos podem estar mais isolados (outliers), representando UFs com combinações menos comuns dessas três variáveis. Por exemplo, um ponto no canto superior direito do plano XY e alto no eixo Z representaria uma UF com muitos mestres, muitos doutores e uma alta média de idade dos docentes.
*   **Concentração de UFs:** A maioria dos pontos parece se concentrar em uma região onde os números de docentes com mestrado e doutorado não são os máximos observados, e a média de idade varia. Estados com grandes contingentes de docentes (como São Paulo, visualizado em gráficos anteriores) provavelmente se destacariam nas extremidades superiores dos eixos X e Y.

**Contextualização para a Análise Exploratória de Dados:**

Este gráfico 3D permite uma análise simultânea da **formação acadêmica** (níveis de mestrado e doutorado) e de um proxy para a **experiência profissional** (média de idade dos docentes) em nível estadual.

Para a pergunta de pesquisa ("Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?"):
*   Este gráfico visualiza diretamente a coocorrência de altos níveis de formação (mestrado e doutorado) e diferentes médias de idade (experiência) nas UFs.
*   Ele ajuda a identificar se UFs com um perfil específico de formação e idade (ex: alta formação e alta média de idade) se agrupam.

Contudo, assim como os gráficos anteriores, este não inclui dados salariais. Para analisar a disparidade salarial, seria necessário integrar informações de remuneração a essa análise tridimensional, usando possivelmente a cor ou o tamanho dos pontos para representar uma variável salarial, ou realizando análises estatísticas subsequentes com dados mais completos. Este gráfico é uma ferramenta exploratória poderosa para entender a inter-relação das variáveis de formação e idade dos docentes entre os estados.


---

## Analise exploratoria de dados bases integradas

---

## Grafico Salário Médio Estimado e Total de Docentes por UF
![bar_line_salario_medio_total_docentes_uf](https://github.com/user-attachments/assets/6060f457-2f9f-4c68-9839-82f9f4ac9312)
## Análise do Gráfico: Salário Médio Estimado e Total de Docentes por UF

O gráfico apresentado é uma visualização combinada que utiliza barras para representar o "Salário Médio Estimado (R$)" dos profissionais de dados e uma linha para mostrar o "Total de Docentes na UF" (Unidade Federativa) onde esses profissionais residem.

**Elementos do Gráfico:**

*   **Eixo X (Horizontal):** Apresenta as Unidades Federativas (UF onde mora), ordenadas da esquerda para a direita, aparentemente pela ordem decrescente do salário médio estimado.
*   **Eixo Y Esquerdo (Vertical):** Indica o "Salário Médio Estimado (R$)" e corresponde às barras vermelhas. A escala varia de R$0 a R$14.000.
*   **Eixo Y Direito (Vertical):** Representa o "Total de Docentes na UF" e corresponde à linha azul tracejada com marcadores. A escala vai de 0 a aproximadamente 70.000.
*   **Barras Vermelhas (Salário Médio):** Cada barra mostra o salário médio estimado dos profissionais de dados para uma UF específica.
*   **Linha Azul Tracejada (Total Docentes):** A linha indica o número total de docentes em cada UF.

**Observações e Interpretações:**

*   **Salário Médio Estimado:**
    *   Tocantins (TO) exibe o maior salário médio estimado, superando os R$14.000.
    *   O Distrito Federal (DF) e São Paulo (SP) aparecem em seguida, com salários médios entre R$9.000 e R$10.000 para o DF e um pouco acima de R$9.000 para SP.
    *   Observa-se uma tendência de diminuição do salário médio ao se mover da esquerda para a direita do gráfico. UFs como Piauí (PI) e Rondônia (RO) apresentam os menores salários médios, em torno de R$4.000.

*   **Total de Docentes:**
    *   São Paulo (SP) possui, de longe, o maior número de docentes, ultrapassando 70.000.
    *   Minas Gerais (MG) e Rio de Janeiro (RJ) também têm um volume expressivo de docentes (MG entre 30.000 e 40.000, RJ acima de 30.000).
    *   Muitas outras UFs, incluindo aquelas com salários médios mais baixos e algumas com salários mais altos como TO e DF, têm um número consideravelmente menor de docentes (frequentemente abaixo de 10.000 ou 20.000).

*   **Relação entre Salário Médio e Total de Docentes:**
    *   **Não se observa uma correlação direta e simples** entre o salário médio dos profissionais de dados e o número total de docentes na UF.
        *   Por exemplo, TO tem o salário médio mais alto, mas um número relativamente baixo de docentes.
        *   SP combina um salário médio alto (terceiro maior) com o maior número de docentes.
        *   DF possui o segundo maior salário médio, mas um número de docentes bem inferior ao de SP, MG ou RJ.
    *   Isso sugere que o salário médio dos profissionais de dados em cada estado é influenciado por um conjunto de fatores que vai além da quantidade de docentes (que poderia ser um indicador da oferta de formação ou do tamanho do sistema educacional). Fatores como a demanda do mercado de trabalho local, o custo de vida, a concentração de empresas de tecnologia e o nível de desenvolvimento econômico da UF provavelmente desempenham papéis cruciais.

**Conclusão do Gráfico:**

O gráfico demonstra não haver uma relação causal direta entre o número de docentes em uma UF e o salário médio dos profissionais de dados nessa mesma UF. Enquanto São Paulo apresenta um alto volume de docentes e um alto salário médio, o caso de Tocantins (alto salário médio, poucos docentes) exemplifica que outros fatores são determinantes para a remuneração na área de dados. A dinâmica salarial é complexa e moldada por múltiplas variáveis, não sendo explicada isoladamente pela infraestrutura educacional em termos de quantidade de docentes.

## Grafico Salário Estimado por Área de Formação - Top 5
![boxplot_salario_por_area_formacao_top5](https://github.com/user-attachments/assets/521f1e12-e4bb-445e-982d-733d52142401)
## Análise do Gráfico: Salário Estimado por Área de Formação (Top 5)

O gráfico apresentado é um boxplot que ilustra a distribuição do "Salário Estimado (R$)" para as cinco principais áreas de formação dos profissionais de dados. Cada boxplot resume a distribuição salarial para uma área específica, permitindo comparações entre elas.

**Elementos do Gráfico:**

*   **Eixo Y (Vertical):** "Área de Formação", listando as cinco categorias de formação mais comuns ou relevantes.
    *   Computação / Engenharia de Software / Sistemas de Informação/ TI
    *   Outras Engenharias
    *   Economia/ Administração / Contabilidade / Finanças/ Negócios
    *   Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais
    *   Outra opção
*   **Eixo X (Horizontal):** "Salário Estimado (R$)", variando de R$0 até mais de R$40.000.
*   **Boxplot (Caixa e Bigodes):** Para cada área de formação:
    *   A **linha central** dentro da caixa representa a **mediana** salarial (o valor que divide os salários em 50% abaixo e 50% acima).
    *   A **caixa** em si abrange o **intervalo interquartil (IQR)**, ou seja, os 50% centrais dos salários (do primeiro quartil - Q1 - ao terceiro quartil - Q3). A largura da caixa indica a dispersão desses salários centrais.
    *   Os **"bigodes"** (linhas que se estendem a partir da caixa) mostram o alcance dos salários, geralmente até 1.5 vezes o IQR a partir da caixa.
    *   Os **pontos individuais** (losangos) fora dos bigodes são considerados **outliers**, indicando salários atipicamente altos ou baixos em relação ao restante do grupo.

**Observações e Interpretações por Área de Formação:**

1.  **Computação / Engenharia de Software / Sistemas de Informação/ TI:**
    *   **Mediana Salarial:** Parece ser a mais alta entre as áreas, situada próxima a R$10.000.
    *   **Dispersão (IQR):** A caixa é relativamente compacta, sugerindo que a maioria dos profissionais dessa área tem salários concentrados em torno da mediana.
    *   **Alcance e Outliers:** Apresenta um alcance considerável nos bigodes e múltiplos outliers indicando salários bem elevados, alguns ultrapassando R$40.000.

2.  **Outras Engenharias:**
    *   **Mediana Salarial:** Ligeiramente inferior à de Computação/TI, talvez em torno de R$8.000 - R$9.000.
    *   **Dispersão (IQR):** Similar ou um pouco maior que Computação/TI.
    *   **Alcance e Outliers:** Também possui um bom alcance e múltiplos outliers com salários altos.

3.  **Economia/ Administração / Contabilidade / Finanças/ Negócios:**
    *   **Mediana Salarial:** Parece estar na faixa de R$7.000 - R$8.000.
    *   **Dispersão (IQR):** A caixa aparenta ser um pouco mais larga, indicando uma maior variabilidade nos salários do grupo central em comparação com Computação/TI.
    *   **Alcance e Outliers:** Presença de outliers com salários elevados.

4.  **Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais:**
    *   **Mediana Salarial:** Próxima à área de Economia/Negócios, possivelmente entre R$7.000 e R$8.000.
    *   **Dispersão (IQR):** A caixa parece ter uma dispersão considerável.
    *   **Alcance e Outliers:** Também exibe outliers significativos.

5.  **Outra opção:**
    *   **Mediana Salarial:** Aparenta ter a menor mediana entre as cinco categorias, talvez em torno de R$6.000 - R$7.000.
    *   **Dispersão (IQR):** A caixa parece ser relativamente larga, sugerindo uma variabilidade salarial significativa dentro deste grupo.
    *   **Alcance e Outliers:** Possui outliers, incluindo um que se destaca próximo a R$40.000.

**Comparações e Conclusões Gerais:**

*   Profissionais com formação na área de **Computação / Engenharia de Software / Sistemas de Informação/ TI** tendem a ter a mediana salarial mais alta.
*   Todas as áreas de formação apresentam uma dispersão salarial considerável, evidenciada pelos tamanhos das caixas e, principalmente, pela presença de outliers com salários significativamente altos. Isso sugere que, dentro de cada área, há profissionais que conseguem remunerações bem acima da média do seu grupo.
*   A categoria "Outra opção" apresenta a menor mediana salarial, o que é esperado, ao agrupar diversas formações menos diretamente ligadas às habilidades centrais da área de dados.
*   As áreas de "Outras Engenharias", "Economia/Administração/etc." e "Estatística/Matemática/etc." apresentam medianas salariais intermediárias e relativamente próximas entre si, mas com variações na dispersão dos salários.

Este gráfico é útil para entender como a área de formação inicial se relaciona com os níveis salariais no campo de dados, destacando que, embora formações em TI/Computação pareçam ter uma vantagem na mediana, todas as áreas analisadas possuem profissionais alcançando altos patamares salariais.


## Grafico Salário Estimado por Tempo de Experiência
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/a62a1fa0a659e7a351b966759dafa417/raw/4b807c1571bb235ffa8469985f8f14d4f3c80d74/boxplot_salario_por_experiencia_plotly.html)
![newplot](https://github.com/user-attachments/assets/3733a3c3-9327-497c-87db-1550f799e558)
## Análise do Gráfico: Salário Estimado por Tempo de Experiência

O gráfico visualizado é um boxplot que demonstra a distribuição do "Salário Estimado (R$)" para diferentes níveis de "Tempo de Experiência na Área de Dados (Anos Estimados)". Essa representação gráfica permite comparar como a remuneração varia conforme os profissionais acumulam mais anos de experiência na área.

**Elementos do Gráfico:**

*   **Eixo Y (Vertical):** Representa as categorias de "Tempo de Experiência na Área de Dados (Anos Estimados)". As categorias são:
    *   Menos de 1 ano (Rotulado como 0.5 no gráfico)
    *   de 1 a 2 anos (Rotulado como 1.5)
    *   de 3 a 4 anos (Rotulado como 3.5)
    *   de 4 a 6 anos (Rotulado como 5.0)
    *   de 6 a 10 anos (Rotulado como 8.0)
    *   Mais de 10 anos (Rotulado como 10.0)
*   **Eixo X (Horizontal):** Indica o "Salário Estimado (R$)", com valores que vão de R$0 até mais de R$30.000.
*   **Boxplot (Diagrama de Caixa):** Para cada faixa de experiência, o boxplot exibe:
    *   A **linha central** na caixa: Representa a **mediana** salarial (50º percentil), o valor que divide os salários em duas metades iguais.
    *   A **caixa**: Abrange o **intervalo interquartil (IQR)**, que contém os 50% centrais dos dados salariais (do primeiro quartil, Q1 ou 25º percentil, ao terceiro quartil, Q3 ou 75º percentil). A altura da caixa indica a dispersão dos salários nesse intervalo central.
    *   Os **"bigodes" (whiskers)**: Linhas que se estendem da caixa para mostrar o alcance dos dados salariais, geralmente até 1.5 vezes o IQR. Valores além dos bigodes podem ser outliers.
    *   **Outliers**: Pontos individuais (neste gráfico, parecem pequenos círculos) que se localizam fora dos bigodes, indicando salários atipicamente altos ou baixos em comparação com o restante do grupo para aquela faixa de experiência.

**Observações e Interpretações por Faixa de Experiência:**

1.  **Menos de 1 ano (0.5):**
    *   **Mediana Salarial:** A mais baixa entre todas as faixas, situando-se em torno de R$2.000 - R$3.000.
    *   **Dispersão (IQR):** A caixa é relativamente compacta, mas há uma concentração na parte inferior da faixa salarial.
    *   **Outliers:** Apresenta alguns outliers, indicando que mesmo com pouca experiência, alguns profissionais conseguem salários acima da média do grupo.

2.  **de 1 a 2 anos (1.5):**
    *   **Mediana Salarial:** Aumenta visivelmente em relação à faixa anterior, provavelmente entre R$4.000 e R$5.000.
    *   **Dispersão (IQR):** A caixa se expande, mostrando maior variabilidade salarial.
    *   **Outliers:** Mais outliers presentes, e com valores mais altos.

3.  **de 3 a 4 anos (3.5):**
    *   **Mediana Salarial:** Continua a crescer, situando-se talvez em torno de R$7.000 - R$8.000.
    *   **Dispersão (IQR):** A dispersão dos 50% centrais dos salários aumenta.
    *   **Outliers:** Número significativo de outliers, alcançando salários mais elevados.

4.  **de 4 a 6 anos (5.0):**
    *   **Mediana Salarial:** Apresenta um salto expressivo, posicionando-se próximo ou acima de R$10.000.
    *   **Dispersão (IQR):** A caixa é mais ampla, refletindo uma maior diversidade salarial.
    *   **Outliers:** Muitos outliers, com alguns ultrapassando R$30.000.

5.  **de 6 a 10 anos (8.0):**
    *   **Mediana Salarial:** Continua a tendência de alta, possivelmente entre R$12.000 e R$14.000.
    *   **Dispersão (IQR):** Grande dispersão salarial, com a caixa sendo bastante longa.
    *   **Outliers:** Vários outliers com salários muito altos.

6.  **Mais de 10 anos (10.0):**
    *   **Mediana Salarial:** Atinge o patamar mais alto, superando R$15.000 e aproximando-se de R$18.000 - R$20.000.
    *   **Dispersão (IQR):** A maior dispersão entre todas as faixas, indicando uma ampla gama de salários para os profissionais mais experientes.
    *   **Outliers:** Presença marcante de outliers com os salários mais altos do dataset, muitos acima de R$30.000.

**Conclusões Gerais:**

*   **Impacto Positivo da Experiência:** Há uma clara e consistente tendência de aumento da mediana salarial à medida que o tempo de experiência na área de dados aumenta. Profissionais com mais anos de atuação tendem a receber salários significativamente maiores.
*   **Aumento da Dispersão Salarial com a Experiência:** Não somente a mediana, mas também a dispersão dos salários (representada pelo tamanho da caixa e pelo alcance dos bigodes e outliers) tende a aumentar com a experiência. Isso sugere que, entre os profissionais mais experientes, há uma variação salarial maior – alguns podem ter salários excepcionalmente altos, enquanto outros podem permanecer em faixas mais modestas em comparação com os "top earners" do mesmo nível de experiência.
*   **Potencial de Altos Salários:** Em todas as faixas de experiência, a presença de outliers superiores indica que existem oportunidades para alcançar salários acima da média do respectivo grupo, mas essa possibilidade se torna mais pronunciada e os valores mais altos com o aumento da experiência.

Este gráfico reforça a noção de que a experiência profissional é um fator crucial na progressão salarial na área de dados no Brasil, com os profissionais mais experientes não somente alcançando medianas salariais mais altas, mas também apresentando uma gama mais ampla de possibilidades de remuneração.


## Grafico Salário Estimado por Tempo de Experiência em Dados
![boxplot_salario_por_experiencia_seaborn](https://github.com/user-attachments/assets/1ae56e9f-614e-490c-9cea-c70402bd333c)
## Análise do Gráfico: Salário Estimado por Tempo de Experiência em Dados

O gráfico de boxplot anexado ilustra a relação entre o "Tempo de Experiência" dos profissionais de dados e o "Salário Estimado (R$)". Cada caixa no gráfico representa a distribuição salarial para uma faixa específica de anos de experiência.

**Elementos do Gráfico:**

*   **Eixo Y (Vertical):** "Tempo de Experiência", dividido nas seguintes categorias:
    *   Menos de 1 ano
    *   de 1 a 2 anos
    *   de 3 a 4 anos
    *   de 5 a 6 anos
    *   de 7 a 10 anos
    *   Mais de 10 anos
*   **Eixo X (Horizontal):** "Salário Estimado (R$)", com escala de R$0 até mais de R$40.000.
*   **Boxplot (Diagrama de Caixa):** Para cada categoria de experiência:
    *   A **linha vertical dentro da caixa** indica a **mediana** salarial (o valor central que divide os salários em 50% abaixo e 50% acima).
    *   A **caixa (box)** representa o **intervalo interquartil (IQR)**, contendo os 50% centrais dos salários (do primeiro quartil - Q1 - ao terceiro quartil - Q3). A largura da caixa mostra a dispersão desses salários centrais.
    *   Os **"bigodes" (whiskers)** são as linhas horizontais que se estendem da caixa, mostrando o alcance principal dos salários (tipicamente 1.5 vezes o IQR).
    *   Os **pontos individuais (losangos)** fora dos bigodes são considerados **outliers**, representando salários atipicamente altos ou baixos em relação ao grosso dos dados para aquela faixa de experiência.

**Observações e Interpretações por Faixa de Experiência:**

1.  **Menos de 1 ano:**
    *   **Mediana Salarial:** A mais baixa, em torno de R$4.000.
    *   **Dispersão (IQR):** Relativamente concentrada, com a maioria dos salários entre aproximadamente R$2.000 e R$6.000.
    *   **Outliers:** Alguns outliers superiores, chegando até cerca de R$20.000.

2.  **de 1 a 2 anos:**
    *   **Mediana Salarial:** Aumenta para cerca de R$6.000.
    *   **Dispersão (IQR):** A caixa se alarga um pouco, com salários centrais entre R$4.000 e R$8.000, aproximadamente.
    *   **Outliers:** Mais outliers e com valores mais altos, alguns ultrapassando R$30.000.

3.  **de 3 a 4 anos:**
    *   **Mediana Salarial:** Um salto significativo, posicionando-se em torno de R$9.000 - R$10.000.
    *   **Dispersão (IQR):** Maior variabilidade, com a caixa indo de cerca de R$6.000 a R$12.000.
    *   **Outliers:** Vários outliers, com alguns alcançando e ultrapassando R$40.000.

4.  **de 5 a 6 anos:**
    *   **Mediana Salarial:** Continua a crescer, situando-se em torno de R$12.000.
    *   **Dispersão (IQR):** A caixa é ampla, indicando diversidade salarial, aproximadamente entre R$8.000 e R$16.000.
    *   **Outliers:** Presença de outliers tanto superiores (ultrapassando R$40.000) quanto inferiores (próximos a R$0).

5.  **de 7 a 10 anos:**
    *   **Mediana Salarial:** Aumenta para cerca de R$14.000 - R$15.000.
    *   **Dispersão (IQR):** A caixa se estende de aproximadamente R$10.000 a R$20.000.
    *   **Outliers:** Similar à faixa anterior, com outliers em ambas as extremidades.

6.  **Mais de 10 anos:**
    *   **Mediana Salarial:** A mais alta, em torno de R$16.000 - R$18.000.
    *   **Dispersão (IQR):** A maior dispersão dos salários centrais, com a caixa indo de cerca de R$12.000 a R$25.000. Isso indica uma grande variação salarial entre os profissionais mais experientes.
    *   **Outliers:** Numerosos outliers, especialmente na extremidade superior, indicando que profissionais com vasta experiência podem alcançar remunerações muito elevadas. Também há outliers inferiores.

**Conclusões Gerais:**

*   **Progressão Salarial com Experiência:** O gráfico demonstra claramente que a mediana salarial tende a aumentar consistentemente com o aumento do tempo de experiência na área de dados.
*   **Aumento da Variabilidade Salarial:** À medida que a experiência aumenta, não só a mediana salarial cresce, mas também a dispersão dos salários (indicada pela largura da caixa e pela presença de outliers). Isso sugere que, com mais experiência, as faixas salariais se tornam mais amplas.
*   **Potencial de Alta Remuneração:** Em todos os níveis de experiência, existem profissionais (outliers) que ganham significativamente mais do que a mediana do seu grupo. Esse potencial para salários muito altos é particularmente evidente nas faixas de maior experiência.
*   **Outliers Inferiores:** A presença de outliers na extremidade inferior, especialmente nas faixas de maior experiência, pode indicar diversos cenários, como transições de carreira, atuação em setores ou regiões com menor remuneração, ou outros fatores não capturados somente  pela variável "tempo de experiência".

Este gráfico é uma ferramenta visual eficaz para entender como a remuneração na área de dados evolui com a experiência, destacando a valorização progressiva dos profissionais à medida que acumulam mais anos de atuação.


## Grafico Salário Estimado por Nível de Ensino
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/d4a35514b072e73dcb602e3c936f3324/raw/da8b4afe7bd6ce83a87a646bfc6e978bee28b69a/gistfile1.txt)
![newplot(1)](https://github.com/user-attachments/assets/933aba1b-01fa-45fe-b4ad-6380af43469e)
## Análise do Gráfico: Salário Estimado por Nível de Ensino

O gráfico visualizado é um boxplot que ilustra a distribuição do "Salário Estimado (R$)" para diferentes categorias de "Nível de Ensino" alcançado pelos profissionais de dados. Este tipo de gráfico é uma ferramenta eficaz na análise exploratória de dados para comparar a tendência central, dispersão e identificar valores atípicos entre diferentes grupos.

**Elementos do Gráfico:**

*   **Eixo Y (Vertical):** "Nível de Ensino", apresentando as seguintes categorias:
    *   Estudante de Graduação
    *   Graduação/Bacharelado
    *   Pós-graduação
    *   Mestrado
    *   Doutorado ou Phd
*   **Eixo X (Horizontal):** "Salário Estimado (R$)", com a escala variando de R$0 até mais de R$30.000.
*   **Boxplot (Diagrama de Caixa):** Para cada nível de ensino, o boxplot resume a distribuição salarial da seguinte forma:
    *   A **linha vertical dentro da caixa** representa a **mediana** salarial (o 50º percentil), que é o valor central dividindo os salários em duas metades iguais.
    *   A **caixa (box)** delimita o **intervalo interquartil (IQR)**, que contém os 50% centrais dos dados salariais (do primeiro quartil, Q1 ou 25º percentil, ao terceiro quartil, Q3 ou 75º percentil). A largura da caixa indica a dispersão dos salários neste intervalo.
    *   Os **"bigodes" (whiskers)** são as linhas horizontais que se estendem a partir da caixa, mostrando o alcance dos dados salariais considerados típicos (geralmente até 1.5 vezes o IQR a partir da caixa).
    *   Os **pontos individuais (losangos)** localizados fora dos bigodes são considerados **outliers**, indicando salários que são atipicamente altos ou baixos em comparação com o restante dos profissionais naquele nível de ensino.

**Observações e Interpretações por Nível de Ensino:**

1.  **Estudante de Graduação:**
    *   **Mediana Salarial:** A mais baixa entre todos os níveis, situando-se em torno de R$2.000 - R$3.000.
    *   **Dispersão (IQR):** A caixa é relativamente compacta, indicando que a maioria dos estudantes de graduação tem salários próximos a essa mediana baixa.
    *   **Outliers:** Apresenta alguns outliers superiores, sugerindo que alguns estudantes já conseguem remunerações mais elevadas.

2.  **Graduação/Bacharelado:**
    *   **Mediana Salarial:** Aumenta consideravelmente em relação aos estudantes, posicionando-se em torno de R$7.000 - R$8.000.
    *   **Dispersão (IQR):** A caixa é mais ampla, mostrando uma maior variabilidade nos salários dos graduados.
    *   **Outliers:** Presença significativa de outliers, com alguns salários ultrapassando R$30.000.

3.  **Pós-graduação:**
    *   **Mediana Salarial:** Ligeiramente superior à da graduação, talvez em torno de R$8.000 - R$9.000.
    *   **Dispersão (IQR):** A dispersão parece similar ou um pouco maior que a dos graduados.
    *   **Outliers:** Muitos outliers, alcançando patamares salariais elevados.

4.  **Mestrado:**
    *   **Mediana Salarial:** Apresenta um aumento notável em relação à pós-graduação, situando-se acima de R$10.000, talvez próximo a R$12.000.
    *   **Dispersão (IQR):** A caixa é relativamente ampla, indicando uma boa variabilidade salarial.
    *   **Outliers:** Muitos outliers com salários altos, alguns bem acima de R$30.000.

5.  **Doutorado ou Phd:**
    *   **Mediana Salarial:** A mais alta entre todos os níveis de ensino, superando a do mestrado e posicionando-se em torno de R$14.000 - R$15.000.
    *   **Dispersão (IQR):** A caixa é bastante extensa, refletindo uma grande dispersão salarial entre os doutores.
    *   **Outliers:** Presença marcante de outliers com os salários mais elevados do conjunto de dados, indicando um alto potencial de ganhos para este grupo.

**Conclusões Gerais:**

*   **Impacto Positivo do Nível de Ensino:** O gráfico demonstra uma tendência clara de aumento da mediana salarial à medida que o nível de ensino aumenta. Profissionais com níveis de formação mais elevados (Mestrado, Doutorado) tendem a ter medianas salariais significativamente maiores.
*   **Aumento da Dispersão Salarial em Níveis Mais Altos:** Nos níveis de ensino mais elevados, especialmente Doutorado, não apenas a mediana é maior, mas também a dispersão dos salários (o tamanho da caixa e o alcance dos outliers). Isso sugere uma gama mais ampla de remunerações, com alguns profissionais alcançando salários excepcionalmente altos.
*   **Valor da Graduação:** Há um salto salarial expressivo ao se completar a graduação em comparação com o nível de estudante.
*   **Outliers Significativos:** Em todos os níveis a partir da graduação, a presença de outliers superiores indica que, independentemente do nível de formação específico (pós-graduação, mestrado), existem oportunidades para alcançar salários bem acima da média do grupo.

Este gráfico reforça a ideia de que o investimento em educação formal, especialmente em níveis mais avançados como mestrado e doutorado, está associado a um maior potencial de remuneração na área de dados no Brasil.


## Grafico Salário Estimado por Nível de Ensino
![boxplot_salario_por_nivel_ensino_seaborn](https://github.com/user-attachments/assets/320b22fc-43fb-40af-be93-e02572699fec)
## Análise do Gráfico: Salário Estimado por Nível de Ensino

O gráfico anexado é um boxplot que exibe a distribuição do "Salário Estimado (R$)" para diferentes níveis de escolaridade ("Nível de Ensino") alcançados pelos profissionais de dados. Esta visualização permite comparar como a remuneração varia entre os diferentes graus de formação acadêmica.

**Elementos do Gráfico:**

*   **Eixo Y (Vertical):** "Nível de Ensino", com as seguintes categorias (de cima para baixo):
    *   Estudante de Graduação
    *   Graduação/Bacharelado
    *   Pós-graduação
    *   Mestrado
    *   Doutorado ou Phd
*   **Eixo X (Horizontal):** "Salário Estimado (R$)", com uma escala que se estende de R$0 até mais de R$40.000.
*   **Boxplot (Diagrama de Caixa):** Para cada nível de ensino, o boxplot mostra:
    *   A **linha vertical dentro da caixa**: Indica a **mediana** salarial (o valor que divide a distribuição dos salários em duas metades iguais).
    *   A **caixa**: Representa o **intervalo interquartil (IQR)**, que contém os 50% centrais dos salários (entre o primeiro quartil - Q1 - e o terceiro quartil - Q3). A largura da caixa reflete a dispersão desses salários centrais.
    *   Os **"bigodes" (whiskers)**: Linhas horizontais que se estendem da caixa para mostrar o alcance dos salários considerados típicos.
    *   Os **pontos individuais (losangos)**: Representam **outliers**, ou seja, salários que são atipicamente altos (ou baixos) em comparação com a maioria dos profissionais daquele nível de ensino.

**Observações e Interpretações por Nível de Ensino:**

1.  **Estudante de Graduação:**
    *   **Mediana Salarial:** É a mais baixa de todas as categorias, situando-se em torno de R$4.000 - R$5.000.
    *   **Dispersão (IQR):** A caixa é relativamente estreita, indicando que a maioria dos estudantes de graduação tem salários concentrados em uma faixa menor, aproximadamente entre R$2.500 e R$6.000.
    *   **Outliers:** Apresenta alguns outliers superiores, com salários chegando a cerca de R$15.000, e um outlier próximo a R$20.000.

2.  **Graduação/Bacharelado:**
    *   **Mediana Salarial:** Aumenta significativamente em relação aos estudantes, localizando-se em torno de R$8.000 - R$9.000.
    *   **Dispersão (IQR):** A caixa é consideravelmente mais larga, com os 50% centrais dos salários variando aproximadamente de R$5.000 a R$12.000, indicando maior variabilidade salarial.
    *   **Outliers:** Numerosos outliers superiores, com vários profissionais alcançando salários acima de R$20.000, R$30.000 e até R$40.000.

3.  **Pós-graduação:**
    *   **Mediana Salarial:** Um pouco superior à da graduação, possivelmente em torno de R$9.000 - R$10.000.
    *   **Dispersão (IQR):** Semelhante ou ligeiramente maior que a da graduação, com salários centrais entre aproximadamente R$6.000 e R$14.000.
    *   **Outliers:** Também apresenta muitos outliers com salários elevados, ultrapassando R$40.000 em alguns casos.

4.  **Mestrado:**
    *   **Mediana Salarial:** Demonstra um novo aumento, situando-se em torno de R$10.000 - R$12.000.
    *   **Dispersão (IQR):** A caixa é ampla, indicando uma variabilidade salarial considerável, com os 50% centrais entre aproximadamente R$7.000 e R$15.000.
    *   **Outliers:** Vários outliers superiores, incluindo salários acima de R$20.000, R$30.000 e alguns próximos ou acima de R$40.000.

5.  **Doutorado ou Phd:**
    *   **Mediana Salarial:** A mais alta entre todos os níveis de ensino, posicionando-se em torno de R$12.000 - R$14.000.
    *   **Dispersão (IQR):** A caixa é bastante larga, indicando uma grande dispersão salarial. Os 50% centrais dos salários parecem estar entre R$8.000 e R$20.000.
    *   **Outliers:** Presença marcante de outliers com salários elevados, com vários profissionais superando R$30.000 e R$40.000. Há também um outlier inferior, próximo a R$0.

**Conclusões Gerais:**

*   **Valorização da Educação:** O gráfico evidencia uma tendência geral de aumento da mediana salarial conforme o nível de ensino aumenta. Profissionais com níveis de formação mais avançados, como Mestrado e Doutorado, tendem a ter medianas salariais mais altas.
*   **Aumento da Dispersão com Níveis Mais Altos:** A variabilidade salarial (largura da caixa e presença de outliers) também tende a ser maior nos níveis de ensino mais elevados. Isso sugere que, embora a mediana aumente, a faixa de salários possíveis também se amplia, especialmente para cima.
*   **Salto Salarial Pós-Graduação (Lato Sensu e Stricto Sensu):** Completar uma graduação representa um salto salarial significativo em relação ao status de estudante. Pós-graduações (incluindo especializações, mestrado e doutorado) continuam essa tendência de aumento na mediana salarial.
*   **Potencial de Alta Remuneração:** Em todos os níveis a partir da Graduação/Bacharelado, a existência de múltiplos outliers superiores indica que há profissionais que alcançam remunerações consideravelmente acima da média de seus respectivos grupos de escolaridade. Esse potencial parece se acentuar com o Doutorado.

Este gráfico sugere que o investimento em educação formal, particularmente em níveis mais avançados, está associado a um maior potencial de ganhos na área de dados.


## Grafico Salário Estimado por Experiência, Agrupado por Nível de Ensino
![catplot_salario_exp_facet_nivel_ensino](https://github.com/user-attachments/assets/71164ccd-585b-4354-8473-631eac8a4f02)
## Análise do Gráfico: Salário Estimado por Experiência, Agrupado por Nível de Ensino

O gráfico apresentado é um conjunto de boxplots (diagramas de caixa) que visualiza a interação entre "Tempo de Experiência" e "Nível de Ensino" na determinação do "Salário Estimado (R$)" dos profissionais de dados. O gráfico é facetado por "Nível de Ensino", o que significa que para cada nível de escolaridade, há uma série de boxplots mostrando a distribuição salarial para diferentes faixas de tempo de experiência.

**Elementos do Gráfico:**

*   **Título Principal:** "Salário Estimado por Experiência, Agrupado por Nível de Ensino".
*   **Facetas (Subgráficos):** Cada subgráfico representa um "Nível de Ensino" específico:
    *   Estudante de Graduação
    *   Graduação/Bacharelado
    *   Pós-graduação
    *   Mestrado
    *   Doutorado ou Phd
*   **Eixo Y (Vertical) de cada subgráfico:** "Salário Estimado (R$)", com escala de R$0 a R$40.000.
*   **Eixo X (Horizontal) de cada subgráfico:** "Tempo de Experiência". Embora as categorias exatas não estejam rotuladas individualmente no eixo x de cada faceta, a progressão das caixas da esquerda para a direita (e as cores distintas das caixas) dentro de cada subgráfico representa o aumento do tempo de experiência. Podemos inferir que são as mesmas faixas de experiência usadas em gráficos anteriores (ex: <1 ano, 1-2 anos, 3-4 anos, 5-6 anos, 7-10 anos, Mais de 10 anos).
*   **Boxplot (Diagrama de Caixa):** Para cada combinação de nível de ensino e faixa de experiência:
    *   A **linha horizontal dentro da caixa** indica a **mediana** salarial.
    *   A **caixa** representa o **intervalo interquartil (IQR)**, contendo os 50% centrais dos salários.
    *   Os **"bigodes" (whiskers)** mostram o alcance dos salários considerados típicos.
    *   Os **pontos individuais (losangos)** são **outliers**, indicando salários atipicamente altos ou baixos.

**Observações e Interpretações:**

**Tendência Geral Dentro de Cada Nível de Ensino:**

*   **Progressão Salarial com Experiência:** Em *todos* os níveis de ensino, há uma clara tendência de aumento da mediana salarial (a linha dentro da caixa) à medida que o tempo de experiência aumenta (movendo-se da esquerda para a direita dentro de cada subgráfico). Isso é visível pela subida geral das caixas.
*   **Aumento da Dispersão com Experiência:** Frequentemente, a dispersão salarial (altura da caixa e alcance dos bigodes/outliers) também aumenta com mais experiência. Isso significa que, entre os mais experientes, há uma variação salarial maior.

**Comparações Entre Níveis de Ensino para Faixas de Experiência Similares:**

1.  **Início de Carreira (Faixas de Menor Experiência - caixas à esquerda):**
    *   **Estudantes de Graduação:** Apresentam as menores medianas salariais em todas as faixas de experiência que participam.
    *   **Graduação/Bacharelado e Pós-graduação:** Para pouca experiência, as medianas salariais são semelhantes e mais altas que as dos estudantes. A pós-graduação parece oferecer uma ligeira vantagem inicial sobre somente a graduação.
    *   **Mestrado e Doutorado:** Mesmo com pouca experiência, profissionais com mestrado e, especialmente, doutorado, tendem a ter medianas salariais iniciais mais altas em comparação com os níveis de ensino inferiores.

2.  **Meio de Carreira (Faixas de Experiência Intermediárias - caixas centrais):**
    *   A diferença salarial entre os níveis de ensino torna-se mais pronunciada.
    *   **Graduação/Bacharelado e Pós-graduação:** A pós-graduação continua a mostrar uma vantagem sobre a graduação.
    *   **Mestrado e Doutorado:** Apresentam medianas salariais consistentemente mais altas. Profissionais com doutorado, com experiência intermediária, já alcançam patamares salariais elevados.

3.  **Final de Carreira (Faixas de Maior Experiência - caixas à direita):**
    *   **Estudantes de Graduação:** Mesmo com mais experiência (se aplicável dentro do status de estudante), os salários permanecem os mais baixos.
    *   **Graduação/Bacharelado e Pós-graduação:** A progressão continua, mas as medianas tendem a ser superadas pelos níveis de mestrado e doutorado.
    *   **Mestrado:** Profissionais com mestrado e vasta experiência alcançam salários significativamente altos.
    *   **Doutorado ou Phd:** Este grupo, com alta experiência, apresenta as maiores medianas salariais e também uma dispersão muito grande, com outliers indicando salários excepcionalmente altos (alguns acima de R$40.000). A caixa para o maior nível de experiência em Doutorado é notavelmente alta.

**Interação entre Experiência e Nível de Ensino:**

*   **Benefício da Experiência é Universal:** A experiência aumenta o potencial salarial em todos os níveis de ensino.
*   **Nível de Ensino Potencializa o Efeito da Experiência:** O "retorno" da experiência parece ser maior para níveis de ensino mais altos. Ou seja, um ano adicional de experiência pode resultar em um aumento salarial proporcionalmente maior para quem tem mestrado ou doutorado em comparação com quem tem apenas graduação. Isso é visualizado pela inclinação mais acentuada da progressão salarial com a experiência nos níveis de ensino mais altos.
*   **Teto Salarial Mais Alto com Maior Escolaridade e Experiência:** Os salários mais altos no dataset (outliers superiores) são geralmente encontrados entre profissionais com níveis de ensino mais elevados (Mestrado, Doutorado) *e* mais tempo de experiência.

**Conclusões Gerais:**

Este gráfico é particularmente elucidativo ao mostrar que tanto a formação acadêmica quanto a experiência profissional são fatores cruciais na determinação salarial, e eles interagem positivamente.
*   Para alcançar os patamares salariais mais elevados na área de dados, a combinação de um alto nível de ensino (especialmente Mestrado ou Doutorado) com uma experiência profissional substancial parece ser o caminho mais promissor.
*   Enquanto a experiência por si só eleva os salários em todos os níveis de formação, o nível de formação parece definir diferentes "faixas" ou "tetos" potenciais de remuneração então explorados e alcançados através da experiência.


## Grafico Distribuição de Profissionais por Área de Formação Acadêmica
![distribuicao_area_formacao](https://github.com/user-attachments/assets/fd0d4cb9-5e30-4f52-8a7e-9cd074ee04c5)
## Análise do Gráfico: Distribuição de Profissionais por Área de Formação Acadêmica

O gráfico em anexo é um gráfico de barras horizontais que ilustra a "Distribuição de Profissionais por Área de Formação Acadêmica". Ele mostra a contagem de profissionais de dados provenientes de diferentes campos de estudo.

**Elementos do Gráfico:**

*   **Título:** "Distribuição de Profissionais por Área de Formação Acadêmica".
*   **Eixo Y (Vertical):** "Área de Formação". Lista as diversas áreas de formação acadêmica dos profissionais.
*   **Eixo X (Horizontal):** "Contagem". Indica o número de profissionais correspondente a cada área de formação, com a escala variando de 0 a mais de 1200.
*   **Barras Horizontais:** O comprimento de cada barra é proporcional à quantidade de profissionais com formação naquela área específica. As áreas estão ordenadas da maior para a menor contagem, de cima para baixo.

**Observações e Interpretações:**

1.  **Computação / Engenharia de Software / Sistemas de Informação/ TI:**
    *   Esta é, de longe, a área de formação mais comum entre os profissionais de dados no dataset, com uma contagem superior a 1200 profissionais. Isso indica uma forte predominância de backgrounds técnicos diretamente relacionados à computação e tecnologia da informação na área de dados.

2.  **Outras Engenharias:**
    *   A segunda área mais representativa, com aproximadamente 800 profissionais. Isso sugere que as habilidades analíticas e de resolução de problemas desenvolvidas em diversas engenharias são transferíveis e valorizadas no campo de dados.

3.  **Economia/ Administração / Contabilidade / Finanças/ Negócios:**
    *   Esta categoria ocupa a terceira posição, com cerca de 450 profissionais. Profissionais com formação em negócios e áreas correlatas trazem uma perspectiva de aplicação e valor de negócio para a análise de dados.

4.  **Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais:**
    *   Com pouco mais de 200 profissionais, esta área, que possui fundamentos quantitativos essenciais para a ciência de dados, aparece em quarto lugar em termos de volume.

5.  **Outra opção:**
    *   Uma categoria genérica que agrupa formações não especificadas nas demais, com pouco menos de 200 profissionais.

6.  **Áreas Menos Representadas:**
    *   As demais áreas listadas apresentam contagens significativamente menores (abaixo de 100 profissionais cada):
        *   Química / Física
        *   Ciências Biológicas/ Farmácia/ Medicina/ Área da Saúde
        *   Marketing / Publicidade / Comunicação / Jornalismo
        *   Ciências Sociais
    *   Isso indica que, embora profissionais dessas áreas também atuem no campo de dados, eles representam uma parcela menor do total.

**Conclusões Gerais:**

*   **Predominância de Formações Técnicas e Quantitativas:** As áreas de Computação/TI, Engenharias e, em menor grau, Estatística/Matemática, dominam o cenário de formação dos profissionais de dados, o que é esperado dada a natureza técnica e analítica da área.
*   **Relevância de Formações em Negócios:** A presença significativa de profissionais com background em Economia, Administração e áreas afins destaca a importância do entendimento do contexto de negócios para a aplicação eficaz de técnicas de dados.
*   **Multidisciplinaridade Crescente, Mas Concentrada:** Embora a área de dados seja conhecida por sua multidisciplinaridade, este gráfico evidencia que a maioria dos profissionais ainda provém de um conjunto relativamente concentrado de formações mais tradicionais para o setor de tecnologia e análise.
*   **Oportunidades para Diversas Formações:** A presença, mesmo que minoritária, de profissionais de áreas como Ciências Sociais, Saúde e Comunicação sugere haver espaço para diferentes perspectivas e habilidades no campo de dados, embora a transição possa ser menos comum ou exigir aquisição de habilidades técnicas adicionais.

Este gráfico oferece um panorama claro sobre as origens acadêmicas mais comuns dos profissionais que atualmente trabalham com dados, ressaltando a forte base em tecnologia e engenharias.


## Grafico Distribuição de Profissionais por Faixa Salarial Mensal
![distribuicao_faixa_salarial](https://github.com/user-attachments/assets/29688dff-55fd-492f-a897-ad9a4e89a657)
## Análise do Gráfico: Distribuição de Profissionais por Faixa Salarial Mensal

O gráfico apresentado é um gráfico de barras horizontais que ilustra a "Distribuição de Profissionais por Faixa Salarial Mensal". Ele mostra quantas pessoas se enquadram em cada faixa salarial.

**Elementos do Gráfico:**

*   **Título:** "Distribuição de Profissionais por Faixa Salarial Mensal".
*   **Eixo Y (Vertical):** "Faixa Salarial Mensal". Lista as diferentes faixas de salários mensais.
*   **Eixo X (Horizontal):** "Contagem". Indica o número de profissionais em cada faixa salarial, variando de 0 a 800.
*   **Barras Horizontais:** O comprimento de cada barra representa o número de profissionais naquela faixa salarial. As barras são organizadas verticalmente, com as faixas salariais mais baixas na parte superior e as mais altas na parte inferior.

**Observações e Interpretações:**

1.  **de R$8.001/mês a R$12.000/mês:**
    *   Esta é a faixa salarial com o maior número de profissionais, com uma contagem próxima a 800. Isso sugere que a maioria dos profissionais de dados no conjunto de dados ganha entre R$8.001 e R$12.000 por mês.

2.  **de R$12.001/mês a R$16.000/mês:**
    *   A segunda maior concentração está nesta faixa salarial, com uma contagem em torno de 400. Isso indica que muitos profissionais também ganham entre R$12.001 e R$16.000 por mês.

3.  **de R$6.001/mês a R$8.000/mês:**
    *   A terceira maior concentração está nesta faixa salarial, com uma contagem também em torno de 550.

4.  **de R$3.001/mês a R$4.000/mês:**
    *   A contagem é aproximadamente 300.

5.  **de R$4.001/mês a R$6.000/mês:**
    *   A contagem é aproximadamente 300.

6.  **de R$2.001/mês a R$3.000/mês:**
    *   A contagem é aproximadamente 200.

7.  **de R$1.001/mês a R$2.000/mês:**
    *   A contagem é pouco acima de 100.

8.  **Faixas Salariais Mais Altas (de R$16.001/mês a Acima de R$40.001/mês):**
    *   As faixas salariais mais altas apresentam contagens progressivamente menores. Isso indica haver menos profissionais ganhando salários mais elevados.
    *   As faixas de R$16.001/mês a R$20.000/mês e de R$20.001/mês a R$25.000/mês são as mais representadas entre as faixas salariais mais altas.

9.  **Menos de R$1.000/mês:**
    *   A menor contagem é para essa categoria, indicando que poucos profissionais ganham menos de R$1.000 por mês.

**Conclusões Gerais:**

*   **Concentração em Faixas Salariais Intermediárias:** A maioria dos profissionais de dados neste conjunto de dados se concentra nas faixas salariais entre R$6.001 e R$16.000 por mês.
*   **Distribuição Assimétrica:** A distribuição salarial é assimétrica, com uma cauda longa para a direita, indicando que, embora a maioria ganhe entre R$6.001 e R$16.000, alguns profissionais ganham significativamente mais.
*   **Minoria nas Faixas Mais Baixas:** Poucos profissionais relatam ganhar menos de R$2.000 por mês.

Este gráfico fornece uma visão geral da distribuição de salários entre os profissionais de dados, evidenciando onde a maioria se concentra e como os salários se distribuem nas faixas mais altas e mais baixas.


## Grafico Distribuição de Profissionais por Nível de Ensino
![distribuicao_nivel_ensino](https://github.com/user-attachments/assets/044e5446-b6bd-474d-86d4-3c8a94ca44c7)
## Análise do Gráfico: Distribuição de Profissionais por Nível de Ensino

O gráfico anexado é um gráfico de barras horizontais que mostra a "Distribuição de Profissionais por Nível de Ensino". Ele quantifica o número de profissionais de dados em diferentes estágios de sua formação acadêmica.

**Elementos do Gráfico:**

*   **Título:** "Distribuição de Profissionais por Nível de Ensino".
*   **Eixo Y (Vertical):** "Nível de Ensino". Lista as categorias de escolaridade dos profissionais:
    *   Estudante de Graduação
    *   Graduação/Bacharelado
    *   Pós-graduação
    *   Mestrado
    *   Doutorado ou Phd
*   **Eixo X (Horizontal):** "Contagem". Indica o número de profissionais correspondente a cada nível de ensino, com a escala variando de 0 a 1200.
*   **Barras Horizontais:** O comprimento de cada barra é proporcional à quantidade de profissionais com aquele nível de ensino. As categorias estão ordenadas de cima para baixo, aparentemente refletindo uma progressão no nível educacional.

**Observações e Interpretações:**

1.  **Graduação/Bacharelado:**
    *   Esta é a categoria com o maior número de profissionais, ultrapassando a marca de 1200. Isso indica que a maioria dos profissionais de dados no dataset possui, no mínimo, um diploma de graduação completo.

2.  **Pós-graduação:**
    *   A segunda maior concentração de profissionais está neste nível, com uma contagem superior a 1000, mas inferior à da graduação (aproximadamente 1050). Este grupo inclui provavelmente especializações e MBAs (pós-graduação lato sensu).

3.  **Estudante de Graduação:**
    *   Este grupo representa a terceira maior contagem, com aproximadamente 450 profissionais. Isso mostra uma presença significativa de indivíduos que continuam cursando a graduação, mas já atuam na área de dados.

4.  **Mestrado:**
    *   Profissionais com mestrado (pós-graduação stricto sensu) somam cerca de 350, representando o quarto maior grupo.

5.  **Doutorado ou Phd:**
    *   Este é o grupo com a menor representatividade, com uma contagem de aproximadamente 100 profissionais. Embora seja o nível de ensino mais alto, é o menos comum entre os profissionais de dados no dataset.

**Conclusões Gerais:**

*   **Base Educacional Sólida:** A grande maioria dos profissionais de dados possui pelo menos uma graduação completa, com um número expressivo também tendo concluído algum tipo de pós-graduação (lato sensu ou stricto sensu).
*   **Entrada Precoce no Mercado:** A presença considerável de estudantes de graduação sugere que muitos iniciam suas carreiras na área de dados antes mesmo de concluir a formação universitária inicial.
*   **Funil Educacional:** Observa-se um afunilamento no número de profissionais à medida que o nível de ensino se torna mais avançado (Mestrado e, especialmente, Doutorado). Isso é comum em diversas áreas, refletindo o menor número de pessoas que prosseguem para os níveis mais altos de qualificação acadêmica.
*   **Valorização de Diferentes Níveis:** O gráfico demonstra haver profissionais de dados em todos os principais níveis de ensino, desde estudantes até doutores, indicando que o mercado absorve talentos com diferentes graus de formação.

Este gráfico oferece uma visão clara do perfil educacional dos profissionais de dados, destacando a importância da graduação e da pós-graduação, ao mesmo tempo que mostra participar estudantes e o menor, porém qualificado, contingente de mestres e doutores.


## Grafico Distribuição do Salário Estimado
![distribuicao_salario_estimado](https://github.com/user-attachments/assets/cb8d3675-ed41-4fcb-bf09-7f1c8b69cda4)
## Análise do Gráfico: Distribuição do Salário Estimado (R$)

O gráfico anexado é um histograma que representa a "Distribuição do Salário Estimado (R$)" dos profissionais de dados. Ele mostra a frequência de profissionais em diferentes intervalos de salário estimado.

**Elementos do Gráfico:**

*   **Título:** "Distribuição do Salário Estimado (R$)".
*   **Eixo Y (Vertical):** "Frequência". Indica o número de profissionais (contagem) para cada intervalo de salário. A escala vai de 0 a mais de 800.
*   **Eixo X (Horizontal):** "Salário Estimado (R$)". Representa os valores dos salários estimados em Reais, agrupados em intervalos (bins). A escala vai de R$0 a mais de R$40.000.
*   **Barras (Histograma):** A altura de cada barra corresponde à frequência (número de profissionais) cujo salário estimado cai dentro do intervalo (bin) que a barra representa.
*   **Linha Azul (Estimativa de Densidade do Kernel - KDE):** Sobreposta às barras, há uma linha curva suave que representa uma estimativa da função de densidade de probabilidade da distribuição dos salários. Ela ajuda a visualizar a forma geral da distribuição.

**Observações e Interpretações:**

1.  **Picos Principais (Modas):**
    *   O gráfico exibe uma distribuição multimodal, com pelo menos dois picos proeminentes.
    *   O primeiro pico, e o mais alto, ocorre na faixa salarial em torno de R$4.000 - R$6.000 (aproximadamente), onde a frequência ultrapassa 900 profissionais.
    *   O segundo pico significativo está na faixa de R$10.000 - R$12.000 (aproximadamente), com uma frequência em torno de 800 profissionais.
    *   Um terceiro pico menor, mas notável, aparece em torno de R$14.000 - R$16.000, com frequência próxima a 400.

2.  **Concentração de Salários:**
    *   A maioria dos profissionais parece se concentrar nas faixas salariais abaixo de R$16.000, com as maiores concentrações nos dois primeiros picos mencionados.

3.  **Cauda à Direita (Assimetria Positiva):**
    *   A distribuição é assimétrica à direita (ou positivamente assimétrica). Isso significa que, embora a maioria dos salários esteja concentrada nas faixas mais baixas e médias, há uma "cauda" de profissionais que recebem salários consideravelmente mais altos, estendendo-se para além de R$20.000, R$30.000 e até R$40.000. As frequências nessas faixas mais altas são progressivamente menores.

4.  **Intervalos de Salário:**
    *   A primeira barra, de R$0 a aproximadamente R$2.500, tem uma frequência em torno de 400.
    *   Após o pico principal em torno de R$5.000, há uma queda na frequência antes de subir novamente para o segundo pico em torno de R$11.000.
    *   Depois do terceiro pico em torno de R$15.000, as frequências diminuem consideravelmente, indicando que menos profissionais se encontram nas faixas salariais mais elevadas.

**Conclusões Gerais:**

*   **Distribuição Salarial Heterogênea:** A presença de múltiplos picos sugere que pode haver subgrupos distintos na população de profissionais de dados com diferentes níveis salariais predominantes. Isso pode ser influenciado por fatores como nível de experiência, área de atuação, nível de ensino, região geográfica, etc.
*   **Maioria em Faixas Médias-Baixas:** Uma grande proporção dos profissionais aufere salários nas faixas que vão até aproximadamente R$16.000, com picos notáveis em torno de R$5.000 e R$11.000.
*   **Potencial para Altos Salários:** A cauda longa à direita indica que, embora menos comuns, existem salários significativamente altos na área de dados, ultrapassando R$40.000.
*   **Necessidade de Análise Multivariada:** A forma multimodal do histograma sugere que analisar somente a distribuição geral do salário pode não contar a história completa. Seria interessante investigar quais fatores contribuem para os diferentes picos observados, como feito nas análises anteriores que segmentaram por experiência e nível de ensino.

Este histograma fornece uma visão geral da estrutura salarial dos profissionais de dados, destacando as faixas de remuneração mais comuns e a existência de um segmento com ganhos consideravelmente mais altos.


## Grafico Distribuição de Profissionais por Tempo de Experiência em Dados
![distribuicao_tempo_experiencia](https://github.com/user-attachments/assets/986f2138-2838-4ff8-ae15-8495f36f0728)
## Análise do Gráfico: Distribuição de Profissionais por Tempo de Experiência em Dados

O gráfico anexado é um gráfico de barras horizontais que ilustra a "Distribuição de Profissionais por Tempo de Experiência em Dados". Ele mostra o número de profissionais de dados classificados em diferentes faixas de tempo de experiência na área.

**Elementos do Gráfico:**

*   **Título:** "Distribuição de Profissionais por Tempo de Experiência em Dados".
*   **Eixo Y (Vertical):** "Tempo de Experiência". Apresenta as seguintes categorias de tempo de atuação profissional na área de dados:
    *   Menos de 1 ano
    *   de 1 a 2 anos
    *   de 3 a 4 anos
    *   de 5 a 6 anos
    *   de 7 a 10 anos
    *   Mais de 10 anos
*   **Eixo X (Horizontal):** "Contagem". Indica o número de profissionais correspondente a cada faixa de experiência, com a escala variando de 0 a mais de 1000.
*   **Barras Horizontais:** O comprimento de cada barra é proporcional à quantidade de profissionais naquela faixa de experiência específica. As barras estão ordenadas de cima para baixo, começando com a menor experiência e progredindo para a maior.

**Observações e Interpretações por Faixa de Experiência:**

1.  **de 1 a 2 anos:**
    *   Esta é a faixa com o maior número de profissionais, com uma contagem superior a 1000 (aproximadamente 1050-1100). Isso sugere que uma grande parcela dos profissionais de dados no dataset possui uma experiência relativamente inicial, mas já consolidada, na área.

2.  **de 3 a 4 anos:**
    *   A segunda maior concentração de profissionais está nesta faixa, com uma contagem próxima a 950. Juntamente com a faixa anterior, indica que a maioria dos profissionais tem entre 1 e 4 anos de experiência.

3.  **Menos de 1 ano:**
    *   Profissionais com menos de um ano de experiência representam o terceiro maior grupo, com uma contagem em torno de 400. Isso mostra um contingente significativo de recém-chegados à área.

4.  **de 5 a 6 anos:**
    *   A contagem de profissionais nesta faixa é de aproximadamente 250-280, indicando um número menor de profissionais com este nível de experiência intermediária mais longa.

5.  **de 7 a 10 anos:**
    *   Esta faixa possui uma contagem similar à anterior, em torno de 250-280 profissionais.

6.  **Mais de 10 anos:**
    *   Este é o grupo com a menor representatividade, com uma contagem visivelmente inferior às demais, parecendo ser inferior a 100 (talvez em torno de 50-80). Isso indica que profissionais com vasta experiência (mais de uma década) na área de dados são menos comuns no dataset, o que pode refletir a relativa novidade da área de "dados" como um campo formalizado ou a nomenclatura utilizada.

**Conclusões Gerais:**

*   **Concentração em Níveis Iniciais e Intermediários de Experiência:** A maioria dos profissionais de dados no dataset possui entre 1 e 4 anos de experiência, com um número também considerável de iniciantes (menos de 1 ano).
*   **Menor Representatividade de Profissionais Altamente Experientes:** Há um declínio no número de profissionais à medida que o tempo de experiência aumenta, sendo que aqueles com mais de 10 anos de experiência são os menos numerosos.
*   **Perfil da Área de Dados:** A distribuição pode sugerir que a área de dados, como campo profissional distinto, tem crescido rapidamente nos últimos anos, resultando em muitos profissionais com menos anos de experiência específica "em dados". Também pode indicar uma alta rotatividade ou transição para outras funções após alguns anos.
*   **Formato de Funil:** A distribuição se assemelha a um funil, onde muitos entram na área, mas o número de profissionais diminui nas faixas de experiência mais longas.

Este gráfico fornece uma visão clara do perfil de experiência dos profissionais de dados, destacando uma concentração maior nos estágios iniciais e intermediários da carreira na área.


## Grafico Top 10 UF de Residência dos Profissionais de Dados
![distribuicao_top10_uf](https://github.com/user-attachments/assets/1cf90782-fb39-475d-b70e-ac4b18bb3f7d)
## Análise do Gráfico: Top 10 UF de Residência dos Profissionais de Dados

O gráfico em anexo é um gráfico de barras verticais que apresenta o "Top 10 UF de Residência dos Profissionais de Dados". Ele mostra a contagem de profissionais de dados que residem nas dez Unidades Federativas (estados) com maior representatividade no dataset.

**Elementos do Gráfico:**

*   **Título:** "Top 10 UF de Residência dos Profissionais de Dados".
*   **Eixo Y (Vertical):** "Contagem". Indica o número de profissionais de dados, com a escala variando de 0 a mais de 1200.
*   **Eixo X (Horizontal):** "UF". Apresenta as siglas das Unidades Federativas. As UFs estão ordenadas da esquerda para a direita, da maior para a menor contagem de profissionais.
*   **Barras Verticais:** A altura de cada barra é proporcional ao número de profissionais de dados que residem naquela UF. As barras possuem diferentes tonalidades de azul, possivelmente para melhor distinção visual ou para indicar uma hierarquia, embora a ordenação já cumpra essa função.

**Observações e Interpretações por UF:**

1.  **SP (São Paulo):**
    *   Destaca-se como a UF com a maior concentração de profissionais de dados, com uma contagem muito superior às demais, ultrapassando 1200 (aproximadamente 1300 profissionais). Isso indica que São Paulo é o principal polo de profissionais de dados no Brasil, de acordo com este dataset.

2.  **MG (Minas Gerais):**
    *   A segunda UF com mais profissionais, com uma contagem em torno de 350-380. Embora seja um número significativo, é consideravelmente menor que o de São Paulo.

3.  **PR (Paraná):**
    *   Ocupa a terceira posição, com uma contagem próxima a 300 profissionais.

4.  **RJ (Rio de Janeiro):**
    *   Apresenta uma contagem muito similar à do Paraná, também em torno de 290-300 profissionais, posicionando-se como o quarto estado com mais profissionais de dados.

5.  **RS (Rio Grande do Sul):**
    *   A contagem de profissionais é de aproximadamente 180.

6.  **SC (Santa Catarina):**
    *   Possui uma contagem ligeiramente inferior ao RS, em torno de 160-170 profissionais.

7.  **DF (Distrito Federal):**
    *   Apresenta uma contagem próxima a 90-100 profissionais.

8.  **BA (Bahia), CE (Ceará), PE (Pernambuco):**
    *   Estas três UFs da região Nordeste encerram o top 10, com contagens menores e relativamente próximas entre si, todas abaixo de 100 (aproximadamente entre 70 e 85 profissionais cada).

**Conclusões Gerais:**

*   **Concentração Regional Sudeste-Sul:** A grande maioria dos profissionais de dados está concentrada na região Sudeste (SP, MG, RJ) e Sul (PR, RS, SC), com São Paulo liderando proeminentemente.
*   **Disparidade Geográfica:** Existe uma notável disparidade na distribuição geográfica dos profissionais de dados, com um número muito maior de profissionais em São Paulo em comparação com todos os outros estados.
*   **Presença em Outras Regiões:** Embora em menor número, o Distrito Federal (Centro-Oeste) e estados do Nordeste (BA, CE, PE) também figuram no top 10, indicando a presença de polos de profissionais de dados nessas regiões, ainda que menos expressivos em volume.
*   **Implicações para o Mercado:** Essa concentração pode refletir onde estão as maiores oportunidades de emprego, os principais centros de formação ou os ecossistemas de inovação e tecnologia mais desenvolvidos no país.

Este gráfico fornece uma visão clara da distribuição geográfica dos profissionais de dados no Brasil, destacando a liderança de São Paulo e a importância das regiões Sudeste e Sul como principais centros para esses profissionais.


## Grafico Heatmap de Correlação entre Salário, Experiência e Nível de Ensino
![heatmap_correlacao_salario_exp_ensino](https://github.com/user-attachments/assets/2cd9887a-0a1d-4c89-b513-3a852d07b35c)
## Análise do Gráfico: Heatmap de Correlação entre Salário, Experiência (anos) e Nível de Ensino (ordinal)

O gráfico apresentado é um heatmap (mapa de calor) que visualiza a matriz de correlação entre três variáveis quantitativas: "Salário Estimado", "Experiência (anos) Estimados" e "Nível de Ensino (ordinal)". Este tipo de gráfico utiliza cores para representar a força e a direção das correlações lineares entre pares de variáveis.

**Elementos do Gráfico:**

*   **Título:** "Heatmap de Correlação entre Salário, Experiência (anos) e Nível de Ensino (ordinal)".
*   **Eixos (Linhas e Colunas):** As mesmas três variáveis são listadas tanto nas linhas quanto nas colunas:
    *   Salario_Estimado
    *   Experiencia_Anos_Estimados
    *   Nivel_Ensino_Ordinal
*   **Células da Matriz:** Cada célula na interseção de uma linha e uma coluna mostra o coeficiente de correlação de Pearson entre as duas variáveis correspondentes. O valor do coeficiente é exibido numericamente dentro da célula.
*   **Escala de Cores (Barra Lateral):** À direita do heatmap, uma barra de cores indica como os valores de correlação são mapeados para as cores. A escala varia de aproximadamente 0.2 (azul escuro) a 1.0 (vermelho escuro).
    *   Cores mais quentes (tendendo ao vermelho) indicam correlações positivas mais fortes.
    *   Cores mais frias (tendendo ao azul) indicam correlações positivas mais fracas (neste caso, todas as correlações são positivas).
    *   Se houvesse correlações negativas, elas seriam normalmente representadas por uma gama diferente de cores.

**Interpretação dos Coeficientes de Correlação:**

Os coeficientes de correlação variam de -1 a +1:
*   +1 indica uma correlação linear positiva perfeita.
*   -1 indica uma correlação linear negativa perfeita.
*   0 indica ausência de correlação linear.
*   Valores próximos de +1 ou -1 indicam correlações fortes, enquanto valores próximos de 0 indicam correlações fracas.

**Análise das Correlações Específicas:**

1.  **Diagonal Principal (Vermelho Escuro - Valor 1.00):**
    *   Salario_Estimado com Salario_Estimado: 1.00
    *   Experiencia_Anos_Estimados com Experiencia_Anos_Estimados: 1.00
    *   Nivel_Ensino_Ordinal com Nivel_Ensino_Ordinal: 1.00
    *   Isso é esperado, pois a correlação de qualquer variável consigo mesma é sempre perfeita e positiva.

2.  **Salario_Estimado vs. Experiencia_Anos_Estimados:**
    *   Coeficiente: 0.53
    *   Cor: Azul claro, tendendo para o centro da escala.
    *   Interpretação: Existe uma correlação positiva moderada entre o salário estimado e os anos de experiência. Isso sugere que, de forma geral, à medida que os anos de experiência aumentam, o salário estimado também tende a aumentar.

3.  **Salario_Estimado vs. Nivel_Ensino_Ordinal:**
    *   Coeficiente: 0.30
    *   Cor: Azul médio.
    *   Interpretação: Há uma correlação positiva fraca a moderada entre o salário estimado e o nível de ensino ordinal. Isso indica que, em geral, níveis de ensino mais altos estão associados a salários estimados mais altos, mas a relação é menos forte do que a observada com a experiência.

4.  **Experiencia_Anos_Estimados vs. Nivel_Ensino_Ordinal:**
    *   Coeficiente: 0.24
    *   Cor: Azul mais escuro, na parte inferior da escala de cores.
    *   Interpretação: Existe uma correlação positiva fraca entre os anos de experiência estimados e o nível de ensino ordinal. Isso pode sugerir uma leve tendência de que profissionais com níveis de ensino mais altos também possam ter um pouco mais de tempo de experiência, ou vice-versa, mas a relação é bastante tênue.

**Conclusões Gerais:**

*   **Influência da Experiência no Salário:** A experiência profissional ("Experiencia_Anos_Estimados") apresenta a correlação positiva mais forte com o salário ("Salario_Estimado") entre as variáveis analisadas (0.53), indicando que é um fator importante associado à remuneração.
*   **Influência do Nível de Ensino no Salário:** O nível de ensino ("Nivel_Ensino_Ordinal") também tem uma correlação positiva com o salário (0.30), mas essa relação é menos acentuada do que a da experiência.
*   **Relação entre Experiência e Nível de Ensino:** A correlação entre experiência e nível de ensino é a mais fraca entre os pares (0.24), sugerindo que esses dois fatores, embora ambos influenciem o salário, não estão fortemente interligados entre si no dataset.

Este heatmap fornece uma visão concisa de como essas três variáveis-chave estão linearmente relacionadas, destacando a importância da experiência e, em menor grau, do nível de ensino, na determinação do salário estimado dos profissionais de dados.


## Grafico Salário Médio Estimado vs. Anos de Experiência por Nível de Ensino
![lineplot_salario_exp_por_nivel_ensino](https://github.com/user-attachments/assets/8e847b68-732a-4df6-ac5f-3abde32e4245)
## Análise do Gráfico: Salário Médio Estimado vs. Anos de Experiência por Nível de Ensino

O gráfico apresentado é um gráfico de linhas que ilustra a relação entre o "Salário Médio Estimado (R$)" e os "Anos de Experiência Estimados", segmentado por "Nível de Ensino". Cada linha representa um nível de formação acadêmica diferente, mostrando como a trajetória salarial se desenvolve com o aumento da experiência para cada grupo.

**Elementos do Gráfico:**

*   **Título:** "Salário Médio Estimado vs. Anos de Experiência por Nível de Ensino".
*   **Eixo Y (Vertical):** "Salário Médio Estimado (R$)", com a escala variando de R$2.500 a R$22.500.
*   **Eixo X (Horizontal):** "Anos de Experiência Estimados", variando de aproximadamente 0.5 (representando "Menos de 1 ano") até 8 anos (representando "de 7 a 10 anos", e possivelmente agrupando "Mais de 10 anos" no ponto final, embora a imagem corte antes de mostrar o extremo dos 10+ anos de forma explícita).
*   **Linhas Coloridas:** Cada linha representa um "Nível de Ensino" diferente, conforme a legenda:
    *   **Azul escuro/Roxo:** Estudante de Graduação
    *   **Azul médio:** Graduação/Bacharelado
    *   **Verde-azulado (Turquesa):** Pós-graduação
    *   **Verde:** Mestrado
    *   **Verde claro (Lima):** Doutorado ou Phd
*   **Pontos nas Linhas:** Marcam os valores médios de salário para faixas específicas de experiência dentro de cada nível de ensino.
*   **Áreas Sombreadas (Intervalos de Confiança):** As faixas coloridas translúcidas ao redor de cada linha provavelmente representam intervalos de confiança para o salário médio estimado. Isso indica a variabilidade ou incerteza em torno da média estimada; quanto mais larga a faixa, maior a incerteza ou dispersão dos dados.

**Observações e Interpretações:**

1.  **Progressão Salarial com Experiência (Geral):**
    *   Para *todos* os níveis de ensino, há uma clara tendência ascendente: o salário médio estimado aumenta consistentemente com o aumento dos anos de experiência. As linhas sobem da esquerda para a direita.

2.  **Impacto do Nível de Ensino no Salário Inicial (Ponto de Partida):**
    *   Mesmo com pouca ou nenhuma experiência (extrema esquerda do gráfico), os níveis de ensino mais altos tendem a começar com salários médios estimados mais elevados.
        *   "Doutorado ou Phd" e "Mestrado" iniciam com os maiores salários médios, seguidos por "Pós-graduação", "Graduação/Bacharelado", e por último "Estudante de Graduação".

3.  **Diferenças Salariais Ampliadas com a Experiência:**
    *   As linhas tendem a se divergir mais à medida que os anos de experiência aumentam. Isso significa que a diferença salarial entre os níveis de ensino se torna mais pronunciada para profissionais mais experientes.
    *   Por exemplo, a diferença salarial entre um "Doutorado ou Phd" e um "Graduado/Bacharel" com 1 ano de experiência é menor do que a diferença entre esses mesmos dois níveis com 5 ou 8 anos de experiência.

4.  **Hierarquia dos Níveis de Ensino:**
    *   Ao longo da maior parte da trajetória de experiência, a hierarquia salarial segue geralmente a ordem do nível de ensino: Doutorado > Mestrado > Pós-graduação > Graduação > Estudante de Graduação.
    *   Há um cruzamento ou proximidade muito grande entre as linhas de "Graduação/Bacharelado" e "Pós-graduação" em certos pontos, sugerindo que, para algumas faixas de experiência, a diferença salarial média entre ter somente graduação e ter uma pós-graduação (lato sensu, provavelmente) pode não ser tão acentuada como a diferença para mestrado ou doutorado.

5.  **Retorno da Experiência por Nível de Ensino:**
    *   As inclinações das linhas sugerem que o "retorno" por ano adicional de experiência pode variar entre os níveis de ensino. As linhas para "Doutorado ou Phd" e "Mestrado" parecem ter inclinações consistentemente acentuadas, indicando um forte crescimento salarial com a experiência.

6.  **Variabilidade (Áreas Sombreadas):**
    *   As áreas sombreadas para "Doutorado ou Phd" e "Mestrado", especialmente nos níveis mais altos de experiência, parecem ser mais largas. Isso pode indicar uma maior variabilidade nos salários para esses grupos (ou seja, alguns doutores/mestres experientes ganham muito bem, enquanto outros podem ter salários mais próximos dos demais grupos, aumentando a dispersão) ou menor número de amostras nessas categorias, levando a maior incerteza na estimativa da média.
    *   A faixa para "Estudante de Graduação" é consistentemente a mais baixa e parece ter uma variabilidade relativamente menor em comparação com os níveis superiores.

**Conclusões Gerais:**

*   **Valorização da Experiência e Educação:** O gráfico demonstra claramente que tanto o tempo de experiência quanto o nível de ensino são fatores cruciais que influenciam positivamente o salário médio estimado dos profissionais de dados.
*   **Efeito Combinado:** O maior potencial salarial é observado em profissionais que combinam um alto nível de ensino (Mestrado ou Doutorado) com um volume significativo de anos de experiência.
*   **Investimento em Educação:** Níveis mais altos de educação formal tendem a proporcionar um ponto de partida salarial mais elevado e mantêm uma trajetória de crescimento salarial superior ao longo da carreira, em média.

Este gráfico sintetiza eficazmente como a formação acadêmica e a experiência profissional interagem para moldar a progressão salarial na área de dados, reforçando a importância de ambos os fatores para o desenvolvimento de carreira e potencial de ganhos.


## Grafico Relação 3D entre Salário, Experiência e Nível de Ensino
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/c8f65f4a0c3ba1736c5a2687f8a7c448/raw/b83fdbae94c7706b5fbc5cd2215d132558201ddb/scatter3d_salario_exp_ensino.html)
![newplot(2)](https://github.com/user-attachments/assets/ec28770a-f3a3-4129-b517-f0fc40afd8f1)
## Análise do Gráfico: Relação 3D entre Salário, Experiência e Nível de Ensino

O gráfico interativo apresentado é um gráfico de dispersão 3D (3D Scatter Plot) que visualiza a relação entre três variáveis principais: "Salário Estimado (R$)", "Experiência (Anos Estimados)" e "Nível de Ensino (Ordinal)". Cada ponto no espaço tridimensional representa um profissional de dados.

**Elementos do Gráfico:**

*   **Eixos:**
    *   **Eixo X (Horizontal, profundidade):** "Experiencia_Anos_Estimados". Este eixo representa o tempo de experiência profissional em anos, variando de aproximadamente 0.5 (menos de 1 ano) até 10.0 (mais de 10 anos).
    *   **Eixo Y (Horizontal, largura):** "Nivel_Ensino_Ordinal". Este eixo representa o nível de formação acadêmica de forma ordinal, onde valores menores indicam níveis de ensino mais básicos (0 para Estudante de Graduação) e valores maiores indicam níveis mais avançados (4 para Doutorado ou Phd).
    *   **Eixo Z (Vertical, altura):** "Salario_Estimado". Este eixo representa a remuneração estimada em Reais, variando de R$0 até mais de R$40.000.
*   **Pontos de Dados:** Cada ponto (esfera) no gráfico representa um profissional individual no dataset, posicionado de acordo com seus valores nas três variáveis mencionadas.
*   **Cor dos Pontos (Nivel_Ensino_Ordinal):** Os pontos são coloridos de acordo com o "Nivel_Ensino_Ordinal", facilitando a identificação de grupos com diferentes níveis de formação. A legenda de cores normalmente acompanha esse tipo de gráfico (embora não visível estaticamente na imagem fornecida, é um padrão em gráficos interativos como os do Plotly):
    *   Estudante de Graduação (Ordinal 0): Cor específica (ex: azul)
    *   Graduação/Bacharelado (Ordinal 1): Outra cor (ex: laranja)
    *   Pós-graduação (Ordinal 2): Outra cor (ex: verde)
    *   Mestrado (Ordinal 3): Outra cor (ex: vermelho)
    *   Doutorado ou Phd (Ordinal 4): Outra cor (ex: roxo)

**Observações e Interpretações (Baseadas na Interação Típica com Gráficos 3D):**

1.  **Concentração de Pontos:**
    *   Observa-se uma maior concentração de pontos nas regiões de menor "Salario_Estimado", especialmente para níveis de ensino mais baixos e menor tempo de experiência.
    *   À medida que o "Nivel_Ensino_Ordinal" e a "Experiencia_Anos_Estimados" aumentam (movendo-se para "cima" no eixo Y e para "frente" no eixo X), os pontos tendem a se posicionar mais alto no eixo Z ("Salario_Estimado").

2.  **Tendência Geral:**
    *   Há uma tendência visual clara de que salários mais altos (pontos mais altos no eixo Z) estão associados a combinações de maior experiência e/ou níveis de ensino mais elevados.
    *   A "nuvem" de pontos parece se inclinar para cima à medida que se avança nos eixos de experiência e nível de ensino.

3.  **Impacto Combinado de Experiência e Nível de Ensino:**
    *   **Baixa Experiência, Qualquer Nível de Ensino:** Profissionais com pouca experiência (próximo ao plano traseiro do gráfico) geralmente apresentam salários mais baixos, mesmo aqueles com níveis de ensino mais altos (ex: Doutorado com pouca experiência pode ter salário menor que um Graduado com muita experiência).
    *   **Alta Experiência, Nível de Ensino Variado:** Profissionais com muita experiência (próximo ao plano frontal) mostram uma ampla gama de salários. No entanto, dentro desse grupo de alta experiência, aqueles com níveis de ensino mais altos (cores associadas a Mestrado/Doutorado) tendem a alcançar os patamares salariais mais elevados.
    *   **Nível de Ensino Alto, Experiência Variada:** Profissionais com Doutorado (cor específica, ordinal 4), por exemplo, estão espalhados ao longo do eixo de experiência. Aqueles com mais experiência nesse grupo tendem a ter os salários mais altos do dataset.

4.  **Visualização de Outliers:**
    *   O gráfico 3D permite identificar visualmente outliers – profissionais que, por exemplo, têm um salário muito alto para seu nível de experiência e ensino, ou vice-versa. Esses pontos se destacariam da "nuvem" principal.

5.  **Interatividade:**
    *   A natureza interativa desses gráficos (possibilidade de girar, dar zoom) é crucial para uma exploração completa. Girar o gráfico permite observar a relação entre pares de variáveis, mantendo a terceira como referência, ou identificar clusters e padrões que não seriam óbvios em visualizações 2D separadas.

**Conclusões Gerais:**

*   O gráfico de dispersão 3D reforça as conclusões de análises 2D anteriores: tanto a experiência profissional quanto o nível de formação acadêmica são fatores importantes que influenciam positivamente o salário estimado dos profissionais de dados.
*   A visualização tridimensional destaca a **interação** entre esses dois fatores. Para alcançar os salários mais altos, geralmente é necessária uma combinação de alto nível de ensino *e* experiência substancial.
*   Profissionais com níveis de ensino mais baixos, mesmo com muita experiência, podem ter um "teto" salarial inferior ao de profissionais com formação mais avançada e experiência similar.
*   Da mesma forma, profissionais com alta formação, mas pouca experiência, podem não atingir os salários mais elevados até que acumulem mais tempo de atuação no mercado.

Este tipo de visualização é poderoso para entender relações multivariadas complexas, mostrando como diferentes fatores se combinam para influenciar um resultado, neste caso, o salário.


## Grafico Salário Estimado vs. Proporção de Docentes com Doutorado na UF de Residência
![scatterplot_salario_vs_prop_doc_doutorado_uf](https://github.com/user-attachments/assets/004cf9f3-3691-4536-aa8a-ae2a9ec938e9)
## Análise do Gráfico: Salário Estimado vs. Proporção de Docentes com Doutorado na UF de Residência

O gráfico apresentado é um gráfico de dispersão (scatter plot) que busca explorar a relação entre o "Salário Estimado (R$)" dos profissionais de dados e a "Proporção de Docentes com Doutorado na UF de Residência". Adicionalmente, os pontos no gráfico são codificados por cor para representar o "Nível de ensino alcançado" e por tamanho para indicar os "Experiencia_Anos_Estimados".

**Elementos do Gráfico:**

*   **Título:** "Salário Estimado vs. Proporção de Docentes com Doutorado na UF de Residência".
*   **Eixo Y (Vertical):** "Salário Estimado (R$)", com escala de R$0 até mais de R$40.000.
*   **Eixo X (Horizontal):** "Proporção de Docentes com Doutorado na UF de Residência", variando aproximadamente de 0.30 a pouco mais de 0.60. Este eixo representa a fração de docentes em uma determinada Unidade Federativa que possuem doutorado.
*   **Pontos de Dados:** Cada ponto representa um profissional de dados.
    *   **Cor (Nível de ensino alcançado):** Conforme a legenda:
        *   Verde claro/Turquesa: Estudante de Graduação
        *   Laranja: Graduação/Bacharelado
        *   Azul: Pós-graduação
        *   Roxo/Rosa: Mestrado
        *   Verde escuro: Doutorado ou Phd
    *   **Tamanho (Experiencia_Anos_Estimados):** Pontos maiores indicam maior tempo de experiência (0.5, 1.5, 3.5, 5.5, 8.5 anos estimados), conforme a legenda.

**Observações e Interpretações:**

1.  **Dispersão Geral dos Pontos:**
    *   Os pontos estão amplamente dispersos pelo gráfico, não formando um padrão linear claro (positivo ou negativo) entre a proporção de docentes com doutorado na UF e o salário estimado dos profissionais de dados.
    *   Isso sugere que, isoladamente, a proporção de docentes com doutorado em uma UF não parece ser um forte preditor direto do salário individual de um profissional de dados que reside naquela UF.

2.  **Distribuição Salarial:**
    *   Profissionais com salários muito variados (desde próximos a R$0 até acima de R$40.000) são encontrados em UFs com diferentes proporções de docentes com doutorado. Por exemplo, tanto em UFs com proporção em torno de 0.45 quanto em UFs com proporção em torno de 0.55, observa-se toda a gama de salários.

3.  **Impacto do Nível de Ensino (Cor):**
    *   **Estudantes de Graduação (Verde claro/Turquesa):** Concentram-se predominantemente nas faixas salariais mais baixas, independentemente da proporção de docentes com doutorado na UF.
    *   **Outros Níveis de Ensino:** Profissionais com Graduação (Laranja), Pós-graduação (Azul), Mestrado (Roxo/Rosa) e Doutorado (Verde escuro) estão espalhados por uma ampla faixa de salários. Os salários mais altos (acima de R$30.000) são alcançados por profissionais de diversos níveis de ensino a partir da graduação, mas frequentemente associados a maior experiência.

4.  **Impacto da Experiência (Tamanho):**
    *   Visualmente, os pontos maiores (mais experiência) tendem a se localizar nas faixas salariais mais altas. Por exemplo, muitos dos pontos com salários acima de R$20.000 são de tamanho médio a grande. Isso reforça a observação de análises anteriores de que a experiência é um fator importante na determinação salarial.
    *   Os salários mais elevados (acima de R$40.000) são consistentemente representados por pontos de tamanho médio a grande, indicando profissionais com experiência considerável (3.5 anos ou mais).

5.  **Ausência de Relação Clara com a Proporção de Docentes com Doutorado:**
    *   Não se observa que UFs com maior proporção de docentes com doutorado tenham consistentemente profissionais de dados com salários mais altos, ou vice-versa.
    *   Por exemplo, alguns dos salários mais altos (>R$40.000) aparecem em UFs com proporção de docentes com doutorado em torno de 0.45-0.50, enquanto outros salários altos também aparecem em UFs com proporção em torno de 0.55-0.60.

**Conclusões Gerais:**

*   O gráfico sugere que a proporção de docentes com doutorado na UF de residência de um profissional de dados **não é um fator determinante primário** para o salário estimado desse profissional. A qualidade do ambiente acadêmico local, se proxy pela qualificação dos docentes, não se traduz diretamente em maiores salários individuais para os profissionais de dados ali residentes.
*   Fatores individuais, como **nível de ensino alcançado e, principalmente, anos de experiência**, parecem ter uma influência mais visível na determinação salarial, como indicado pela distribuição das cores e tamanhos dos pontos em relação ao eixo do salário.
*   Outros fatores não representados neste gráfico específico, como o setor de atuação da empresa, o cargo específico, as habilidades individuais, a demanda do mercado local na UF e o custo de vida, provavelmente desempenham papéis mais significativos na definição dos salários dos profissionais de dados.

Este gráfico é útil para descartar uma relação causal ou correlacional forte entre a proporção de docentes com doutorado na UF e os salários dos profissionais de dados, direcionando a atenção para outros fatores mais diretamente ligados ao perfil do profissional e ao mercado de trabalho.


## Gráfico Relação 3D entre Salário, Experiência e Nível de Ensino
### [Grafico Interativo - Clique aqui](https://htmlpreview.github.io/?https://gist.githubusercontent.com/pedrinndias/6bdfb7fdb2be6a819758ca7b1b05d011/raw/7db0af70c340fb3c01d6a052579873f03cacbf1c/gistfile1.txt)
![newplot(3)](https://github.com/user-attachments/assets/6ebf06b9-3667-4d2f-bb06-2802e19b8949)
## Análise do Gráfico: Relação 3D entre Salário, Experiência e Nível de Ensino

O gráfico interativo apresentado é um gráfico de dispersão 3D (3D Scatter Plot) que visualiza a relação entre três variáveis principais: "Salário Estimado (R$)", "Experiência (Anos Estimados)" e "Nível de Ensino (Ordinal)". Cada ponto no espaço tridimensional representa um profissional de dados. Este tipo de análise exploratória de dados (AED) ajuda a investigar conjuntos de dados e resumir suas principais características usando métodos de visualização.

**Elementos do Gráfico:**

*   **Eixos:**
    *   **Eixo X (Horizontal, geralmente representado como profundidade ou eixo frontal):** "Experiencia_Anos_Estimados". Este eixo representa o tempo de experiência profissional em anos, variando de aproximadamente 0.5 (para "Menos de 1 ano") até 10.0 (para "Mais de 10 anos").
    *   **Eixo Y (Horizontal, geralmente representado como largura ou eixo lateral):** "Nivel_Ensino_Ordinal". Este eixo representa o nível de formação acadêmica de forma ordinal, onde valores menores indicam níveis de ensino mais básicos (0 para Estudante de Graduação) e valores maiores indicam níveis mais avançados (4 para Doutorado ou Phd).
    *   **Eixo Z (Vertical, altura):** "Salario_Estimado". Este eixo representa a remuneração estimada em Reais, variando de R$0 até valores que podem exceder R$40.000.
*   **Pontos de Dados:** Cada ponto (esfera) no gráfico representa um profissional individual no dataset, posicionado de acordo com seus valores nas três variáveis mencionadas.
*   **Cor dos Pontos (Nivel_Ensino_Ordinal):** Os pontos são coloridos de acordo com o "Nivel_Ensino_Ordinal", o que facilita a identificação visual de grupos com diferentes níveis de formação acadêmica. A legenda de cores, que tipicamente acompanha esses gráficos interativos, seria (assumindo um esquema de cores padrão para variáveis ordinais):
    *   Estudante de Graduação (Ordinal 0): Uma cor específica (ex: azul)
    *   Graduação/Bacharelado (Ordinal 1): Outra cor (ex: laranja)
    *   Pós-graduação (Ordinal 2): Outra cor (ex: verde)
    *   Mestrado (Ordinal 3): Outra cor (ex: vermelho)
    *   Doutorado ou Phd (Ordinal 4): Outra cor (ex: roxo)

**Observações e Interpretações (Baseadas na Interação Típica com Gráficos 3D):**

1.  **Concentração Geral dos Pontos:**
    *   Observa-se uma maior densidade de pontos nas regiões correspondentes a menores salários estimados (parte inferior do eixo Z), especialmente para combinações de baixo nível de ensino e pouco tempo de experiência.
    *   À medida que os valores nos eixos "Nivel_Ensino_Ordinal" e "Experiencia_Anos_Estimados" aumentam (movendo-se para valores ordinais mais altos no eixo Y e para mais anos no eixo X), os pontos tendem a se posicionar em níveis mais elevados no eixo Z ("Salario_Estimado").

2.  **Tendência Global:**
    *   Visualmente, existe uma tendência clara de que salários mais altos (pontos mais altos no eixo Z) estão associados a combinações de maior tempo de experiência e/ou níveis de ensino mais elevados. A "nuvem" de pontos parece se elevar à medida que se avança ao longo dos eixos de experiência e nível de ensino.

3.  **Impacto Combinado e Interação entre Experiência e Nível de Ensino:**
    *   **Profissionais com Baixa Experiência:** Independentemente do nível de ensino, aqueles com pouca experiência (valores baixos no eixo X) geralmente apresentam salários mais baixos. Mesmo um doutor com pouca experiência pode ter um salário menor do que um graduado com muitos anos de experiência.
    *   **Profissionais com Alta Experiência:** Aqueles com muitos anos de experiência (valores altos no eixo X) exibem uma gama mais ampla de salários. Dentro deste grupo, os profissionais com níveis de ensino mais altos (cores associadas a Mestrado/Doutorado) tendem a alcançar os patamares salariais mais elevados.
    *   **Profissionais com Nível de Ensino Elevado:** Por exemplo, indivíduos com Doutorado (ordinal 4, cor específica) estão distribuídos ao longo de diferentes faixas de experiência. Aqueles que combinam doutorado com mais anos de experiência tendem a estar entre os que recebem os salários mais altos do dataset.

4.  **Identificação de Outliers:**
    *   A visualização 3D pode ajudar a identificar outliers – por exemplo, profissionais com um salário muito alto para seu nível de experiência e ensino, ou o contrário. Esses pontos se destacariam da concentração principal de dados.

5.  **Vantagem da Interatividade:**
    *   A capacidade de girar, dar zoom e interagir com o gráfico 3D é fundamental para uma análise completa. Isso permite observar as relações entre pares de variáveis de diferentes ângulos, facilitando a identificação de padrões, clusters ou tendências que poderiam não ser evidentes em gráficos 2D estáticos.

**Conclusões Gerais:**

*   O gráfico de dispersão 3D corrobora e integra as descobertas de análises 2D anteriores: tanto a experiência profissional quanto o nível de formação acadêmica são fatores positivamente correlacionados com o salário estimado dos profissionais de dados.
*   A principal contribuição desta visualização é destacar a **interação** entre esses dois fatores. Para alcançar os salários mais elevados, geralmente é necessária uma combinação de um alto nível de ensino *e* uma experiência profissional substancial.
*   Profissionais com níveis de ensino mais baixos podem encontrar um "teto" salarial mais baixo, mesmo com muita experiência, em comparação com aqueles com formação mais avançada e experiência similar.
*   Da mesma forma, profissionais com alta qualificação acadêmica, mas pouca experiência prática, podem não atingir os salários mais altos até acumularem mais tempo de atuação no mercado.

Este tipo de gráfico é uma ferramenta poderosa para a análise exploratória de dados (AED), ao permitir uma compreensão mais intuitiva de relações multivariadas complexas, mostrando como diferentes fatores se combinam para influenciar um resultado específico como o salário.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2º Pergunta orientada a dados 
**Pergunta Orientada a Dados:**
*Qual é a relação entre o tempo de experiência na área de dados, o nível de senioridade e a faixa salarial dos profissionais no Brasil?*

## Objetivo

Investigar as relações entre os principais fatores da carreira de profissionais de dados no Brasil e suas faixas salariais, utilizando dados da base survey_cleaned.csv. Esta análise busca entender como variáveis como experiência, senioridade, formação acadêmica, estado (UF) e habilidades técnicas (ex: Python, SQL) influenciam a remuneração.

## Dicionário de Dados

*Análise Numérica da coluna `salary_numeric_lower_bound`*

O script exibe estatísticas descritivas para a coluna `salary_numeric_lower_bound`. Esta coluna representa o limite inferior da faixa salarial convertida para um valor numérico.

| Estatística     | Valor     | Descrição                                       |
|-----------------|-----------|-------------------------------------------------|
| count           | 4753      | Número de observações não nulas na coluna       |
| mean            | 8935.37   | Média do limite inferior do salário (R$ 8.935,37)|
| std             | 7308.44   | Desvio padrão, indicando grande dispersão dos salários |
| min             | 0         | Valor mínimo (pode indicar salários \"menos de X\") |
| 25% (1º Quartil)| 4001      | 25% dos respondentes ganham até R$ 4.001        |
| 50% (Mediana)   | 8001      | Mediana do limite inferior do salário           |
| 75% (3º Quartil)| 12001     | 75% dos respondentes ganham até R$ 12.001       |
| max             | 40001     | Valor máximo registrado                         |

**Comentários:**  
Esta saída é típica do método `.describe()` do Pandas aplicado a séries numéricas, fornecendo um resumo estatístico essencial.


## Comandos e Visualizações Utilizadas

1. Importação e preparo dos dados

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuração de estilo
plt.style.use('seaborn')
sns.set_palette("viridis")

# Leitura da base de dados
df = pd.read_csv("survey_cleaned.csv")

# Função para converter faixas salariais em valores médios
def convert_salary_range(salary_range):
    conversions = {
        'de R$ 4.001/mês a R$ 6.000/mês': 5000.50,
        'de R$ 6.001/mês a R$ 8.000/mês': 7000.50,
        'de R$ 8.001/mês a R$ 12.000/mês': 10000.50,
        'de R$ 12.001/mês a R$ 16.000/mês': 14000.50,
        'de R$ 16.001/mês a R$ 20.000/mês': 18000.50,
        'de R$ 20.001/mês a R$ 25.000/mês': 22500.50,
        'Acima de R$ 25.001/mês': 27500.50
    }
    return conversions.get(salary_range, np.nan)

# Aplicação da função e criação da coluna 'Salario_Medio'
df['Salario_Medio'] = df['Faixa_Salarial'].apply(convert_salary_range)

# Criação da coluna 'Habilidades' (soma de conhecimento em SQL e Python)
df['Habilidades'] = df['SQL'] + df['Python']
```

## Resultados e Gráficos

**Faixa Salarial por Grau de Escolaridade**

**O gráfico abaixo apresenta a distribuição das faixas salariais por grau de escolaridade dos profissionais de dados no Brasil, utilizando boxplots para visualizar medianas, dispersão e outliers. De forma geral, observa-se que níveis mais altos de escolaridade, como mestrado e doutorado, tendem a estar associados a faixas salariais superiores, embora haja sobreposição entre categorias e variações dentro de cada grupo.**

![Faixa Salarial por Grau de Escolaridade](docs/imagens/graficos_analise_exploratoria_2_pergunta_orientada_a_dados/Faixa_Salarial_Por_Grau_Escolaridade.png)

```python
# Importando bibliotecas necessárias
import matplotlib.pyplot as plt
import seaborn as sns

# Ordem desejada para o eixo x (níveis de ensino)
order = ['Estudante de Graduação', 'Graduação/Bacharelado', 'Pós-graduação', 'Mestrado', 'Doutorado ou Phd']

# Configuração da figura com tamanho personalizado
plt.figure(figsize=(14, 7))

# Criando o boxplot para faixa salarial por grau de escolaridade
sns.boxplot(
    x='Nivel_Ensino',
    y='Salario_Medio',
    data=df,
    order=order
)

# Adicionando título e ajustes visuais
plt.title('Faixa Salarial por Grau de Escolaridade')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor leitura
plt.tight_layout()       # Ajusta o layout para evitar cortes

# Exibindo o gráfico
plt.show()
```

*Insight: Profissionais com médias salariais mais altas tendem a possuir formação em pós-graduação, mestrado ou doutorado. Contudo, a dispersão salarial é ampla em todos os níveis, indicando variação mesmo entre indivíduos com mesma formação.*

## Distribuição Salarial por Estado (UF)

**O gráfico abaixo apresenta uma matriz de calor com a distribuição das faixas salariais por estado no Brasil. Observa-se uma forte concentração de salários mais altos nos estados de São Paulo, Rio de Janeiro e Minas Gerais, indicando que esses centros urbanos oferecem mais oportunidades ou melhor remuneração para profissionais de dados. A visualização também evidencia disparidades regionais significativas, com muitos estados apresentando predominância de faixas salariais mais baixas.**

![Distribuica_Faixa_salarial_por_Estado](docs/imagens/graficos_analise_exploratoria_2_pergunta_orientada_a_dados/Distribuica_Faixa_salarial_por_Estado.png)

```python
uf_stats = df.groupby('UF')['Salario_Medio'].agg(['median', 'count']).reset_index()
uf_stats = uf_stats[uf_stats['count'] >= 10].sort_values('median', ascending=False)
sns.barplot(x='UF', y='median', data=uf_stats)
```

*Insight: Estados como SP, RJ e MG concentram os maiores salários. Há disparidade relevante entre estados do Norte/Nordeste e Sul/Sudeste, refletindo desigualdade estrutural no setor de tecnologia.*

## Linguagens de Programação Mais Utilizadas

**O gráfico abaixo mostra as 10 linguagens de programação mais utilizadas no trabalho entre profissionais de dados no Brasil. Destacam-se SQL e Python como as mais utilizadas, refletindo seu papel essencial em tarefas de manipulação de dados, análise e machine learning. Linguagens como R, Visual Basic/VBA e JavaScript aparecem com menor frequência, indicando uso mais específico ou nichado. O domínio de SQL e Python se confirma como requisito central na área.**

![10_linguagens_mais_utilizadas](docs/imagens/graficos_analise_exploratoria_2_pergunta_orientada_a_dados/10_linguagens_mais_utilizadas.png)

```python
tech_counts = df[['SQL', 'Python']].sum().sort_values(ascending=False)
tech_counts.plot(kind='barh')
```

*Insight: As linguagens SQL e Python dominam a atuação dos profissionais de dados. São amplamente mais utilizadas que outras tecnologias, sugerindo que o conhecimento nelas é quase obrigatório no setor.*

##Conclusões

#Escolaridade influencia positivamente a remuneração, embora haja grande variabilidade dentro de cada grupo.

#Região geográfica (UF) é um dos maiores fatores de desigualdade salarial. SP lidera com folga, seguido de RJ, MG e SC.

#Proeficiência técnica, principalmente em SQL e Python, está presente nos perfis com maiores salários.

#A experiência e senioridade contribuem diretamente para a progressão salarial — o que está de acordo com o esperado.



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3º Pergunta orientada a dados
**Pergunta Orientada a Dados:**
Como fatores como formalidade no emprego , características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?
---
# 1 Visualizacao dos dados (Análise Univariada)
Esta seção do script inicializa a análise exploratória de dados univariada, onde cada variável é analisada individualmente. O foco aqui é entender a distribuição e as características de cada atributo.

---

**Mensagem do Script:**

---

**Análise Numérica da coluna `salary_numeric_lower_bound`:**

O script exibe estatísticas descritivas para a coluna `salary_numeric_lower_bound`. Esta coluna representa o limite inferior da faixa salarial convertida para um valor numérico.

| Estatística       | Valor         | Descrição                                                      |
|-------------------|---------------|----------------------------------------------------------------|
| count             | 4753          | Número de observações não nulas na coluna                      |
| mean              | 8935.37       | Média do limite inferior do salário (R$ 8.935,37)              |
| std               | 7308.44       | Desvio padrão, indicando grande dispersão dos salários         |
| min               | 0             | Valor mínimo (pode indicar salários "menos de X")              |
| 25% (1º Quartil)   | 4001          | 25% dos respondentes ganham até R$ 4.001                        |
| 50% (Mediana)     | 8001          | Mediana do limite inferior do salário (metade ganha até isso)  |
| 75% (3º Quartil)   | 12001         | 75% dos respondentes ganham até R$ 12.001                       |
| max               | 40001         | Valor máximo registrado                                        |
| Name & dtype      | salary_numeric_lower_bound (float64) | Nome e tipo de dado da coluna              |

---

**Comentários:**  
Esta saída é típica do método `.describe()` do Pandas aplicado a séries numéricas, fornecendo um resumo estatístico essencial para entender a distribuição central, a dispersão e a amplitude dos dados salariais.

---

### Análise do histograma e KDE dos salarios numericos 

O gráfico apresentado é uma combinação de um histograma e uma estimativa de densidade do kernel (KDE) para a variável `salary_numeric_lower_bound`, que representa o limite inferior da faixa salarial dos profissionais de dados no Brasil. Este tipo de visualização é fundamental para entendermos a distribuição dos salários e, consequentemente, as disparidades existentes.


![Histogrma e KDE de salary_numeric_lower_bound](https://github.com/user-attachments/assets/62391c2d-14eb-4784-90a3-fc1062bda7ba)

---

#### Como Interpretar o Gráfico

- **Eixo X (`salary_numeric_lower_bound`)**:  
  Representa os valores do limite inferior da faixa salarial. No gráfico, varia de valores próximos a zero até acima de R$ 40.000.

- **Eixo Y Esquerdo (Contagem - Histograma)**:  
  Associado às barras azuis (histograma). Cada barra representa um intervalo de salários (bin), e a altura indica o número de profissionais de dados cujo limite inferior da faixa salarial se encontra naquele intervalo.

- **Eixo Y Direito (Densidade - Linha KDE)**:  
  Associado à linha azul escura (linha KDE estimada). A curva KDE é uma versão suavizada do histograma, mostrando a forma da distribuição salarial de forma contínua. A área sob a curva em um intervalo representa a proporção de profissionais naquela faixa salarial. Picos indicam concentrações maiores.

- **Título**:  
  "Histograma e KDE de salary_numeric_lower_bound" – indica claramente o conteúdo do gráfico.

---

#### Informações Extraídas do Gráfico

- **Concentração Salarial**:  
  Há uma concentração significativa de profissionais na faixa salarial mais baixa. O pico principal do histograma e da curva KDE está em torno de R$ 5.000 a R$ 10.000, indicando que a maioria dos profissionais de dados está nessa faixa de remuneração inicial.

- **Assimetria Positiva (Skewness)**:  
  A distribuição é assimétrica à direita, com a maioria dos salários em valores mais baixos, mas com uma cauda longa para valores altos. Alguns profissionais recebem salários muito superiores, elevando a média geral.

- **Multimodalidade Sugerida**:  
  A curva KDE mostra múltiplos picos (modas). Além do pico dominante na faixa baixa, há picos menores em faixas salariais superiores (ex.: em torno de R$ 15.000, R$ 20.000 e outros menos pronunciados), sugerindo diferentes grupos salariais.

---

#### Possíveis Insights e Conexão com a Pergunta Orientada a Dados

**Pergunta central:**  
*"Como fatores como formalidade no emprego, características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?"*

- O gráfico evidencia que existem disparidades salariais significativas.
- A longa cauda à direita e os múltiplos picos na distribuição mostram visualmente essa variação salarial.
- Este ponto de partida visual ajuda a direcionar análises mais detalhadas sobre como os fatores demográficos, regionais e de proficiência técnica afetam essas disparidades.

> Em resumo, o gráfico de Histograma e KDE do salary_numeric_lower_bound visualiza as disparidades salariais existentes entre profissionais de dados no Brasil. A forma da distribuição, com sua assimetria e múltiplos picos, sugere que diversos fatores, incluindo formalidade no emprego, características demográficas, regionais e, crucialmente, a proficiência técnica, estão interagindo de maneiras complexas para criar esses diferentes patamares salariais. O gráfico é a evidência do "o quê" (as disparidades), e a análise mais aprofundada dos fatores mencionados permitirá entender o "porquê" e o "como".

---

### Análise histograma e estimativa de densidade do kernel (KDE) de salarios:

O gráfico apresentado é uma combinação de um histograma e uma estimativa de densidade do kernel (KDE) para a variável `salary_numeric_lower_bound`, que representa o limite inferior da faixa salarial dos profissionais de dados no Brasil. Este tipo de visualização é fundamental para entendermos a distribuição dos salários e, consequentemente, as disparidades existentes.

![box plot salary_numeric_lower](https://github.com/user-attachments/assets/a9d63676-9522-4665-b1d4-66b716fcc70c)


---

#### Como Interpretar o Gráfico

- **Eixo X (`salary_numeric_lower_bound`)**  
  Representa os valores do limite inferior da faixa salarial. No gráfico, varia de valores próximos a zero até acima de R$ 40.000.

- **Eixo Y Esquerdo (Contagem - Histograma)**  
  Associado às barras azuis (histograma). Cada barra representa um intervalo de salários (bin), e a altura indica o número de profissionais de dados cujo limite inferior da faixa salarial se encontra naquele intervalo.

- **Eixo Y Direito (Densidade - Linha KDE)**  
  Associado à linha azul escura (linha KDE estimada). A curva KDE é uma versão suavizada do histograma, mostrando a forma da distribuição salarial de forma contínua. A área sob a curva em um intervalo representa a proporção de profissionais naquela faixa salarial. Picos indicam concentrações maiores.

- **Título**  
  "Histograma e KDE de salary_numeric_lower_bound" – indica claramente o conteúdo do gráfico.

---

#### Informações Extraídas do Gráfico

- **Concentração Salarial**  
  Observa-se uma concentração significativa de profissionais na faixa salarial mais baixa. O pico mais alto do histograma e da curva KDE está em torno de R$ 5.000 a R$ 10.000, indicando que a maioria dos profissionais de dados se encontra nessa faixa de remuneração inicial.

- **Assimetria Positiva (Skewness)**  
  A distribuição é assimétrica à direita (ou positiva). Isso significa que, embora a maioria dos salários esteja concentrada em valores mais baixos, existem alguns profissionais com salários consideravelmente mais altos, o que "puxa" a cauda da distribuição para a direita. Esses salários mais altos são menos frequentes, mas elevam a média geral.

- **Multimodalidade Sugerida**  
  A curva KDE apresenta múltiplos picos (modas), embora um seja dominante. Há um pico principal na faixa mais baixa já mencionada, e picos secundários menores em faixas salariais mais altas (por exemplo, em torno de R$ 15.000, R$ 20.000 e possivelmente outros menos pronunciados). Isso sugere a existência de diferentes grupos de profissionais de dados com níveis salariais distintos.

---

#### Possíveis Insights e Conexão com a Pergunta Orientada a Dados

**Pergunta central:**  
*"Como fatores como formalidade no emprego, características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?"*

O gráfico, ao mostrar a distribuição e as disparidades salariais, serve como ponto de partida para investigar essa questão. Os insights abaixo conectam o gráfico à pergunta:

- **Existência de Disparidades**  
  O gráfico demonstra claramente que existem disparidades salariais significativas. A longa cauda à direita e os múltiplos picos são evidências visuais dessa variação.

>Em resumo, o gráfico de Histograma e KDE do salary_numeric_lower_bound visualiza as disparidades salariais existentes entre profissionais de dados no Brasil. A forma da distribuição, com sua assimetria e múltiplos picos, sugere que diversos fatores, incluindo formalidade no emprego, características demográficas, regionais e, crucialmente, a proficiência técnica, estão interagindo de maneiras complexas para criar esses diferentes patamares salariais. O gráfico é a evidência do "o quê" (as disparidades), e a análise mais aprofundada dos fatores mencionados permitirá entender o "porquê" e o "como".

---

---

### Análise do Gráfico ECDF de salarios 

![ECDF de salary_numeric_lower](https://github.com/user-attachments/assets/45ac6402-0f8b-494a-ab58-71bef586ac65)

**O que o Gráfico ECDF Mostra:**

- **Eixo X (salary_numeric_lower_bound):**  
  Representa os valores do limite inferior da faixa salarial, ordenados do menor para o maior.

- **Eixo Y (Proporção Cumulativa):**  
  Varia de 0 a 1 (ou 0% a 100%). Para qualquer valor de salário no eixo X, o valor correspondente no eixo Y indica a proporção (ou porcentagem) de profissionais de dados que ganham até aquele valor salarial.

- **Forma da Curva:**  
  A curva sobe em "degraus". Cada degrau representa um ou mais profissionais com aquele valor salarial específico. A altura de cada salto vertical corresponde à proporção de observações naquele ponto. Onde a curva é mais íngreme, há uma maior concentração de dados.

**Informações Extraídas Diretamente:**

- **Percentis Salariais:**  
  É fácil ler percentis diretamente no gráfico.

- **Mediana (P50):**  
  Encontrando 0.5 no eixo Y e seguindo horizontalmente até a curva e depois verticalmente até o eixo X, observa-se que a mediana está próxima de R$ 7.500 - R$ 8.000.

- **Outros Percentis:**  
  Aproximadamente 20% (0.2 no eixo Y) dos profissionais ganham até cerca de R$ 4.000. Cerca de 80% (0.8 no eixo Y) ganham até aproximadamente R$ 12.000 - R$ 13.000. Quase 90% (0.9 no eixo Y) ganham até R$ 20.000.

- **Concentração de Salários:**  
  Degraus mais longos horizontalmente indicam faixas salariais com poucos profissionais, enquanto saltos verticais altos indicam concentrações salariais específicas. A subida rápida da curva até R$10.000-R$15.000 mostra a maioria concentrada nessa faixa.

- **Dispersão e Cauda Superior:**  
  A curva continua subindo até atingir 1.0 próximo a R$ 40.000, indicando a presença de salários elevados, embora menos frequentes.

**Conexão com a Pergunta Orientada a Dados:**

- A ECDF oferece uma visão quantitativa das disparidades salariais e da distribuição dos profissionais ao longo da faixa salarial.

- Permite quantificar desigualdades, por exemplo: "X% dos profissionais de dados no Brasil têm um limite inferior de salário até Y reais".  
  Exemplo: Se 90% ganham até R$ 20.000, os 10% restantes estão distribuídos em uma faixa salarial mais ampla, evidenciando disparidade entre os mais bem pagos.

>Em resumo, a ECDF do salary_numeric_lower_bound oferece uma maneira clara de visualizar a proporção acumulada de profissionais em cada nível salarial. Ela quantifica as disparidades mostrando quantos profissionais estão abaixo de certos tetos salariais e destaca as faixas de concentração. Para responder à pergunta sobre a influência e interação dos fatores, seria necessário comparar ECDFs de diferentes segmentos da população de profissionais de dados, usando este gráfico como uma linha de base da distribuição geral.
---

![QQ-plot salary_numeric_lower](https://github.com/user-attachments/assets/6d31facb-2e17-410c-a524-4c3d772644d9)

### Análise do Gráfico QQ-Plot de salarios 

**O que o Gráfico QQ-Plot Mostra:**

- **Eixo X (Quantis Teóricos - Distribuição Normal Padrão):**  
  Valores que seriam esperados se os dados seguissem perfeitamente uma distribuição normal.

- **Eixo Y (Quantis da Amostra - Ordenados):**  
  Os valores reais do `salary_numeric_lower_bound`, ordenados do menor para o maior.

- **Linha de Referência (Normal Teórica):**  
  Linha diagonal que representa a distribuição normal perfeita. Se os pontos estivessem alinhados a esta linha, indicaria que os dados seguem uma distribuição normal.

- **Pontos Azuis:**  
  Quantis dos salários observados plotados contra os quantis teóricos de uma distribuição normal.

---

**Informações Extraídas do Gráfico:**

- **Não Normalidade dos Dados Salariais:**  
  Os pontos azuis não seguem a linha de referência consistentemente, indicando que a distribuição dos salários não é normal.

- **Desvios da Linha:**  
  - *Cauda Inferior (Valores Baixos de Salário):*  
    Na extremidade esquerda, pontos estão ligeiramente abaixo da linha ou apresentam comportamento em "degraus", sugerindo concentração em salários baixos, inclusive valores zero ou próximos a zero, que não seguem uma distribuição normal.  
  - *Corpo Central da Distribuição:*  
    Os pontos se aproximam da linha, mas ainda com alguma curvatura.  
  - *Cauda Superior (Valores Altos de Salário):*  
    Na extremidade direita, os pontos desviam-se acima da linha, caracterizando uma cauda direita pesada (longa). Isso indica que os salários mais altos são mais elevados e frequentes do que o esperado numa normal.

- **Assimetria Positiva:**  
  O desvio acentuado na cauda superior reforça a presença de assimetria positiva — maioria dos salários baixos, com uma minoria recebendo salários substancialmente mais altos.

---

**Conexão com a Pergunta Orientada a Dados:**

- O QQ-Plot ajuda a caracterizar a natureza da distribuição salarial e as disparidades associadas.

- **Caracterização da Disparidade Salarial:**  
  A não normalidade, especialmente a cauda direita pesada, evidencia visualmente a disparidade salarial. Os salários não estão distribuídos simetricamente; há uma minoria que ganha significativamente mais, impactando a média e a desigualdade no setor.

>Em resumo, o QQ-Plot contra uma distribuição normal demonstra que os salários dos profissionais de dados no Brasil não seguem esse padrão teórico, exibindo notavelmente uma cauda direita mais pesada. Isso significa que os salários mais altos são consideravelmente maiores do que o esperado em uma distribuição normal. Essa característica da distribuição é uma manifestação das disparidades salariais, onde fatores como alta proficiência técnica, combinados com aspectos regionais, demográficos e de formalidade, provavelmente impulsionam os ganhos de uma minoria para níveis significativamente elevados em comparação com o restante dos profissionais.
---

![Histogrma e KDE de experiencia_anos](https://github.com/user-attachments/assets/ac711cb0-d98a-4bf8-8a0a-830b6800c5ca)

---

### Análise do Gráfico (Histograma e KDE de `experiencia_anos`)

**O que o Gráfico Mostra:**

Este gráfico exibe a distribuição dos **anos de experiência** dos profissionais de dados na amostra.

- **Eixo X (`experiencia_anos`)**:  
  Representa o número de anos de experiência.

- **Eixo Y Esquerdo (Contagem - Histograma)**:  
  Altura das barras indica o número de profissionais em cada faixa de experiência.

- **Eixo Y Direito (Densidade - Linha KDE Estimada)**:  
  Curva suavizada que mostra a forma contínua da distribuição.

---

**Informações Extraídas do Gráfico:**

- **Picos de Concentração:**  
  - Pico mais alto em torno de **1 ano de experiência** — grande concentração de profissionais iniciantes ou em transição.
  - Outro pico relevante em torno de **3-4 anos**.
  - Concentrações menores aparecem em torno de **0 anos**, **5-6 anos**, **7-8 anos** e **cerca de 10 anos**.

- **Multimodalidade:**  
  A presença de múltiplos picos sugere diferentes grupos de profissionais com perfis distintos de experiência no mercado de dados.

- **Assimetria:**  
  Leve assimetria à direita — mais profissionais com pouca experiência, mas uma cauda indicando presença significativa de profissionais experientes.

- **Amplitude da Experiência:**  
  A distribuição abrange desde iniciantes (0 anos) até profissionais com mais de 10 anos de atuação.

---

**Conexão com a Pergunta Orientada a Dados (Disparidades Salariais):**

- A variável `experiencia_anos` é um **proxy essencial para proficiência técnica**, um dos pilares da sua pergunta de pesquisa.

#### 🧠 **Fundamento para Disparidades Salariais:**

- **Variabilidade na Experiência → Variabilidade Salarial**  
  Espera-se que profissionais com mais anos de experiência possuam maior proficiência, responsabilidades e, consequentemente, salários mais elevados.

- **Relacionamento com a Distribuição Salarial:**  
  - O grupo com ~1 ano de experiência provavelmente compõe boa parte da base da distribuição salarial (faixas júnior/iniciais).  
  - Picos em 3-4 e 5-6 anos sugerem profissionais plenos e seniores.  
  - Picos em 10+ anos podem indicar especialistas, gestores ou profissionais altamente experientes — esses contribuem para a cauda direita da distribuição de salários.

---

**Interação da Experiência (Proficiência) com Outros Fatores:**

- **Formalidade no Emprego:**  
  Profissionais experientes tendem a ter mais barganha por contratos formais (ex: CLT sênior, PJ com altos valores), ou ocupam posições de liderança com estruturas salariais diferenciadas.

- **Características Regionais:**  
  O retorno financeiro por ano de experiência varia por região. Mercados maiores ou com maior demanda podem valorizar mais a senioridade.

- **Características Demográficas:**  
  Idade se correlaciona com experiência, e outros fatores como gênero e raça podem influenciar progressões salariais mesmo entre profissionais com o mesmo tempo de atuação.

---

**Base para Análises Segmentadas:**

A distribuição de `experiencia_anos` permite formar **grupos de análise comparativa**:

- Disparidade salarial entre iniciantes (0-2 anos) vs. seniores (8-10+ anos).  
- Como **formalidade** e **região** afetam o salário em cada faixa de experiência?  
- A experiência amplifica ou atenua desigualdades causadas por outras variáveis?

  
>Em resumo: O gráfico da distribuição de `experiencia_anos` revela a estrutura da força de trabalho em dados no Brasil em termos de tempo de atuação, um dos principais indicadores de proficiência técnica. Os múltiplos picos e ampla variação são peças-chave para entender as disparidades salariais. A experiência interage com formalidade, região e características demográficas, moldando de maneira complexa a estrutura salarial observada no setor.

---

![boxplot de experiencia_anos](https://github.com/user-attachments/assets/6554d62f-4069-4111-8870-6862f26c1eae)

---

### Análise do Gráfico (Boxplot de `experiencia_anos`)

**O que o Gráfico Mostra:**

Este boxplot resume visualmente a distribuição dos **anos de experiência** dos profissionais de dados na amostra.

- **Caixa (Intervalo Interquartil - IQR):**  
  Contém os 50% centrais dos dados — de Q1 a Q3.

- **Linha Central (Mediana - Q2):**  
  Divide a distribuição em duas metades. Está posicionada em **aproximadamente 3 anos**.

- **Bordas da Caixa:**  
  - **Q1 (25%)**: Cerca de **1 ano** de experiência.  
  - **Q3 (75%)**: Cerca de **5 anos** de experiência.

- **Hastes (Whiskers):**  
  - **Inferior**: Vai até **0 anos**, indicando presença de iniciantes.  
  - **Superior**: Vai até cerca de **10 anos**, representando os mais experientes da amostra.

- **Outliers:**  
  O gráfico não exibe explicitamente pontos além das hastes como outliers, sugerindo que valores até 10 anos são considerados dentro da faixa aceitável pela definição padrão de 1.5×IQR.

---

**Informações Extraídas do Gráfico:**

- **Experiência Mediana:**  
  Metade dos profissionais tem até **3 anos** de experiência.

- **Concentração da Experiência:**  
  50% da amostra está concentrada entre **1 e 5 anos** (IQR), indicando um mercado composto majoritariamente por profissionais júnior a pleno.

- **Amplitude da Experiência Comum:**  
  A maior parte da distribuição está entre **0 e 10 anos**, cobrindo a maior parte das fases da carreira técnica.

- **Assimetria Positiva:**  
  A mediana (3 anos) está mais próxima de Q1 (1 ano) do que de Q3 (5 anos), e a haste superior é mais longa — características típicas de uma assimetria à direita.  
  Isso sugere maior concentração em níveis iniciais, com alguns profissionais se estendendo para níveis mais altos de senioridade.

---

**Conexão com a Pergunta Orientada a Dados (Disparidades Salariais):**

O boxplot de `experiencia_anos` fornece um resumo conciso de um dos fatores centrais de sua análise: **proficiência técnica** como motor das **disparidades salariais**.

#### 🧠 **Perfil de Senioridade e Disparidade Salarial:**

- A mediana de 3 anos mostra que boa parte do mercado é composta por profissionais em início ou meio de carreira.
- A variação dentro do IQR (1–5 anos) já representa um potencial de diferenciação salarial significativa, pois o acúmulo de experiência geralmente implica maior conhecimento e responsabilidades.
- A faixa de 5 a 10 anos (acima de Q3) abrange profissionais mais seniores, que provavelmente ocupam cargos com salários mais elevados.

---

**Interação da Experiência com Outros Fatores:**

- **Formalidade no Emprego:**  
  Profissionais mais experientes (Q3 em diante) tendem a acessar formatos de trabalho mais estruturados (CLT sênior, PJ consultivo) com salários mais altos. Iniciantes, por outro lado, podem estar em estágios ou vínculos mais precários.

- **Impacto Regional:**  
  A valorização da experiência pode variar regionalmente. Polos tecnológicos ou regiões com alta demanda podem oferecer salários mais altos mesmo para profissionais com experiência mediana.

- **Conexão com Demografia:**  
  A experiência está fortemente relacionada à idade. Outras variáveis, como gênero, raça ou formação, podem influenciar como a experiência se converte em retorno financeiro.

---

**Ponto de Partida para Análises Salariais Segmentadas:**

O boxplot permite a definição de **faixas de experiência** para investigar disparidades salariais:

- **Q1 e abaixo (0–1 ano)**: Profissionais em início de carreira.  
- **IQR (1–5 anos)**: Base representativa do mercado pleno.  
- **Q3 em diante (5–10 anos)**: Profissionais seniores ou especialistas.

🔍 *Exemplo de pergunta de análise:*  
Como variam os salários de profissionais com 4 anos de experiência trabalhando como CLT em São Paulo, em comparação com profissionais com mesma experiência atuando como PJ no Nordeste?
  
>Em resumo: O boxplot de `experiencia_anos` mostra uma mediana de cerca de **3 anos** e uma concentração de 50% dos profissionais entre **1 e 5 anos**, indicando um mercado majoritariamente jovem, com distribuição assimétrica à direita. A variação da experiência é um componente central da proficiência técnica e um dos **principais impulsionadores das disparidades salariais**. A interação entre experiência, formalidade, localização geográfica e perfil demográfico delineia os padrões salariais observados no setor de dados no Brasil.

---

![Distribuicao de nivel ](https://github.com/user-attachments/assets/b15039bb-1771-4c20-a06b-a0ba54aa7cae)

### Análise do Gráfico (Distribuição de `P2_g` – Nível de Senioridade)

---

#### **O que o Gráfico Mostra:**

Este gráfico de barras horizontais exibe a **frequência de profissionais de dados** em diferentes categorias de senioridade (`P2_g`):

- **Eixo Y (P2_g):** Categorias de nível de senioridade: `Júnior`, `Pleno`, `Sênior` e `nan` (não informado).
- **Eixo X (Contagem):** Número de profissionais em cada categoria.

#### **Distribuição Observada:**

- **Sênior:** Categoria mais numerosa, com mais de **1.400 profissionais**.
- **Pleno:** Segunda mais frequente, próxima de **1.350**.
- **Júnior:** Menor grupo entre os níveis definidos, com **pouco mais de 1.000**.
- **`nan`:** Categoria ausente ou indefinida, com cerca de **900 profissionais**, representando uma **proporção significativa** da amostra.

---

### Conexão com a Pergunta Orientadora (Disparidades Salariais)

> *Como fatores como formalidade no emprego, características demográficas e regionais interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?*

#### **1. Senioridade como Determinante Salarial:**

- A hierarquia Júnior → Pleno → Sênior está geralmente associada a uma **progressão salarial crescente**.
- Profissionais Sênior tendem a ter **maior remuneração**, dado seu nível de responsabilidade, autonomia e experiência técnica.

#### **2. Correlação com Proficiência Técnica e Experiência:**

- O nível de `P2_g` reflete, em muitos casos, os **anos de experiência** e o grau de **proficiência técnica**.
- A distribuição observada (predominância de Plenos e Sêniors) é consistente com a **mediana de 3 anos** de experiência já identificada anteriormente.

#### **3. Segmentação Necessária para Análise Salarial:**

- Avaliar as **faixas salariais dentro de cada nível de senioridade** é essencial.
  - Ex: Como variam os salários entre Júnior x Pleno x Sênior?
- **`nan`** deve ser analisado separadamente:
  - São profissionais com perfil atípico? Freelancers? Gestores? Ou apenas dados faltantes?
  - Comparar sua remuneração com os demais pode revelar **subgrupos ocultos** no mercado.

#### **4. Interações com Outros Fatores:**

- **Formalidade no emprego:**
  - Níveis mais altos de senioridade costumam vir acompanhados de **contratos mais formais** (ex: PJ de alto valor, CLT com benefícios).
- **Região:**
  - O mesmo cargo (ex: Pleno) pode ter **valores salariais distintos** entre São Paulo, Nordeste ou interior.
- **Demografia:**
  - Características como **gênero, raça, idade, escolaridade** podem impactar tanto a **progressão entre níveis** quanto a **remuneração dentro de cada nível**.

#### **5. Reflexões sobre o Grupo `nan`:**

- Pode conter perfis como:
  - Autônomos/freelancers sem classificação tradicional;
  - Profissionais em transição ou multifuncionais;
  - Dados ausentes por falha ou omissão.
- Deve ser avaliado com atenção para **evitar viés** ou perda de insights valiosos.

>Em resumo: O gráfico de `P2_g` revela uma **estrutura de senioridade equilibrada**, com leve predominância de níveis mais experientes. Essa variável é **fundamental para entender a segmentação salarial** no setor de dados. Ao combiná-la com variáveis como **experiência, formalidade contratual, região e demografia**, é possível **compreender as múltiplas dimensões das disparidades salariais** entre os profissionais da área no Brasil.

---

![Distribuicao_regiao](https://github.com/user-attachments/assets/61c205ef-3dea-4c72-93f1-9435efcfa160)

---

### Análise do Gráfico (Distribuição de `Regiao_Mapeada`)

---

#### O que o Gráfico Mostra

Este gráfico de barras horizontais exibe a **contagem de profissionais de dados** distribuídos pelas diferentes regiões mapeadas do Brasil, além de uma categoria "Desconhecida".

- **Eixo Y (`Regiao_Mapeada`)**: Categorias regionais – Sudeste, Sul, Nordeste, Centro-Oeste, Norte e Desconhecida.  
- **Eixo X (Contagem)**: Número de profissionais em cada uma dessas regiões.

---

#### Informações Extraídas do Gráfico

**Concentração Regional:**

- **Sudeste**: É a região com a maior concentração de profissionais, com uma contagem próxima de **3.000**.
- **Sul**: Segunda maior representatividade, com cerca de **900 a 1.000** profissionais.
- **Nordeste**: Terceira maior, com aproximadamente **500** profissionais.
- **Centro-Oeste**: Cerca de **250 a 300**.
- **Norte**: A menor contagem, abaixo de **100** profissionais.
- **Desconhecida**: Aproximadamente **100 a 150**, com região não identificada.

**Perfil Geográfico da Amostra:**  
A maior parte dos profissionais de dados está concentrada no Sudeste, seguido pela região Sul. As demais regiões apresentam participação significativamente menor.

---

#### Conexão com a Pergunta Orientadora

**Como fatores como formalidade no emprego, características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?**

---

#### Impactos da Região nas Disparidades Salariais

**Mercados Regionais Diferenciados:**  
Cada região do Brasil possui níveis distintos de desenvolvimento econômico, maturidade do mercado de trabalho, custo de vida e demanda por profissionais de dados, afetando diretamente as faixas salariais.

**Polos Econômicos e Tecnológicos:**  
O Sudeste e o Sul concentram os principais centros urbanos e tecnológicos, com maior volume de vagas e salários mais competitivos.

**Interações com Outros Fatores:**

- **Proficiência Técnica:** O retorno salarial da qualificação técnica varia conforme a região; o mesmo nível de competência pode ter maior valorização no Sudeste do que no Norte, por exemplo.
- **Formalidade no Emprego:** A predominância de modelos como CLT ou PJ pode variar entre regiões, afetando a renda líquida e benefícios.
- **Demografia Regional:** A distribuição de perfis demográficos (gênero, raça, escolaridade) também não é uniforme, o que impacta oportunidades salariais.
- **Custo de Vida:** Salários nominais maiores no Sudeste podem ser compensados por custos de vida igualmente altos.

---

#### Considerações Analíticas

- **Disparidades Intra e Inter-Regionais:**  
  - Dentro da mesma região (ex: Sudeste), diferentes níveis de proficiência ou tipos de contrato podem gerar variações salariais relevantes.
  - Entre regiões, a mediana salarial para a mesma senioridade pode variar substancialmente.

- **Categoria “Desconhecida”:**  
  Pode valer a pena investigar se seus salários se assemelham aos de alguma região específica ou se compõem um grupo com características distintas.

>Em resumo: A forte concentração de profissionais no Sudeste pode influenciar de maneira significativa as médias salariais nacionais. Portanto, análises regionais segmentadas são fundamentais para entender as **disparidades salariais reais** no setor de dados no Brasil, considerando a **interação entre localização, qualificação técnica, tipo de contrato e perfil demográfico**.

---

# 2 Visualizacao dos dados (Análise Bivariada)

---

### Análise do Gráfico (Grafico de barras sobreposto)

![Histograma_sobreposto_salario](https://github.com/user-attachments/assets/7e26cf54-1306-4748-a3c1-7bcd87a12005)

---

#### O que o Gráfico Mostra

Este histograma sobreposto compara a distribuição de frequência da variável `salary_numeric_lower_bound` (limite inferior da faixa salarial) entre duas categorias: **"Salário Baixo"** (vermelho) e **"Salário Alto"** (azul). As curvas suaves sobrepostas são as Estimativas de Densidade do Kernel (KDE), que ajudam a visualizar a forma da distribuição de cada grupo.

- **Eixo X (`salary_numeric_lower_bound`)**: Representa os valores do limite inferior da faixa salarial em Reais (R$).
- **Eixo Y (`Count`)**: Mostra a contagem (frequência) de profissionais em cada faixa salarial.
- **Cores (Legenda)**: Separam os dados entre os grupos "Salário Baixo" e "Salário Alto".

> **Observação**: A altura de cada barra indica quantos profissionais estão naquele intervalo de salário específico para cada categoria.

---

#### Informações Extraídas do Gráfico

**Distribuições Salariais Claramente Separadas**
O gráfico mostra uma divisão nítida e quase sem sobreposição entre os dois grupos.

- **Salário Baixo (Vermelho)**:
    - **Concentração Massiva**: A grande maioria dos profissionais deste grupo tem salários com limite inferior **abaixo de R$ 10.000**.
    - **Picos Múltiplos**: A distribuição é multimodal, com picos notáveis em torno de R$ 5.000, R$ 7.500 e um pico muito grande próximo de R$ 9.000, sugerindo faixas salariais comuns para níveis de entrada ou júnior.
    - **Cauda Curta**: Praticamente não há ocorrências acima de R$ 10.000.

- **Salário Alto (Azul)**:
    - **Ponto de Partida**: A distribuição deste grupo começa efetivamente em torno de R$ 10.000.
    - **Distribuição Ampla**: Os salários se espalham por uma faixa muito mais larga, indo de R$ 10.000 até mais de R$ 40.000.
    - **Picos Diversificados**: Também é multimodal, com um pico principal logo após R$ 10.000 e outros picos menores em salários mais altos (ex: ~R$ 18.000), indicando diferentes níveis de senioridade ou especialização dentro deste grupo.
    - **Cauda Longa à Direita**: A presença de profissionais em faixas salariais muito elevadas indica uma grande variabilidade e a existência de outliers com alta remuneração.

**Disparidade Visualizada**
A separação visual entre as duas distribuições é a principal mensagem do gráfico, ilustrando uma forte segmentação no mercado de dados.

---

#### Conexão com a Pergunta Orientadora

**Como fatores como formalidade no emprego, características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?**

---

#### Caracterizando os Grupos "Salário Baixo" e "Salário Alto"

1.  **Proficiência Técnica**
    - O grupo **"Salário Baixo"**, concentrado abaixo de R$ 10.000, provavelmente representa profissionais de nível júnior, estagiários ou em transição de carreira, com menor experiência e complexidade técnica.
    - O grupo **"Salário Alto"**, com sua ampla e variada distribuição, deve abranger desde perfis plenos até sêniores, especialistas e gestores, onde a proficiência técnica avançada é um forte diferencial.

2.  **Formalidade no Emprego**
    - A natureza do contrato (CLT, PJ), o porte da empresa e o setor de atuação certamente influenciam em qual grupo um profissional se encaixa. Contratos PJ em empresas de tecnologia podem explicar parte da cauda longa no grupo de "Salário Alto".

3.  **Características Regionais**
    - É muito provável que profissionais no grupo "Salário Alto" estejam concentrados em pólos tecnológicos e grandes centros urbanos (como Sudeste), onde a demanda e o custo de vida são maiores.

4.  **Características Demográficas**
    - Fatores como nível de escolaridade (graduação vs. pós-graduação) e idade (proxy para experiência) devem ser significativamente diferentes entre os dois grupos. O grupo "Salário Alto" tende a ter maior proporção de profissionais com mais idade e maior nível educacional.

---

#### Interação dos Fatores Dentro de Cada Categoria

Mesmo dentro de cada grupo, a variabilidade (os vários picos) sugere interações complexas:

-   **No grupo "Salário Alto"**: Os diferentes picos podem representar subgrupos. Por exemplo, um pico para sêniores CLT no Sudeste e outro pico para especialistas PJ trabalhando remotamente para o exterior.
-   **No grupo "Salário Baixo"**: Os picos podem diferenciar estágios, analistas júnior I e analistas júnior II, ou refletir diferenças salariais para a mesma função em regiões distintas do país.

---

#### Considerações Adicionais

-   **Definição das Categorias**
    O critério exato usado para criar as categorias "Salário Baixo" e "Salário Alto" é fundamental. A análise depende de como essa fronteira (aparentemente em R$ 10.000) foi definida.

-   **Potencial para Modelagem**
    Essas duas categorias são uma excelente variável-alvo para um modelo de classificação. O objetivo do modelo seria prever a qual grupo um profissional pertence com base em sua proficiência, demografia, região e tipo de contrato.

> **Em resumo**: O histograma sobreposto evidencia uma clara segmentação do mercado de dados em dois universos salariais distintos. Ele serve como um poderoso ponto de partida visual para investigar quais são os fatores determinantes que colocam um profissional em um ou outro grupo, respondendo diretamente à pergunta orientadora da análise.  
---
### Análise do Gráfico (Gráfico de Barras Empilhadas)

![proporcao de faixa salarial](https://github.com/user-attachments/assets/b83c3e0c-6bcd-4409-b363-82aabd4607cf)

---

#### O que o Gráfico Mostra

Este gráfico de barras empilhadas 100% apresenta a **proporção de profissionais** nas categorias **"Salário Baixo"** e **"Salário Alto"** (definidas pela variável `faixa_salarial_eda_2cat`) em diferentes **faixas etárias** (`P1_a_1`).

- **Eixo Y (`P1_a_1`)**: Faixas etárias dos profissionais (ex: 25-29, 30-34, ..., 55+).
- **Eixo X (Porcentagem)**: Representa de 0% a 100% dos profissionais em cada faixa etária.
- **Legenda (`faixa_salarial_eda_2cat`)**:
  - **Amarelo (cor clara)**: Salário Baixo  
  - **Azul Marinho (cor escura)**: Salário Alto

Cada barra horizontal representa uma faixa etária, e a proporção de cada cor indica o percentual de profissionais naquela faixa que pertencem a cada grupo salarial.

---

#### Informações Extraídas do Gráfico

**Tendência Geral com a Idade**  
Há uma tendência clara: **quanto maior a faixa etária, maior a proporção de profissionais na categoria "Salário Alto"**.

- **Faixas Jovens (17-21, 22-24)**:
  - Predominância quase total de "Salário Baixo".
  - A faixa 22-24 possui um pequeno percentual em "Salário Alto", mas ainda muito reduzido.

- **Faixas Intermediárias (25-29, 30-34, 35-39)**:
  - Proporção de "Salário Alto" aumenta gradualmente.
  - Faixa 25-29: Cerca de 25% já em "Salário Alto".
  - Faixa 35-39: "Salário Alto" se aproxima (ou ultrapassa) 50%.

- **Faixas Maduras (40-44, 45-49, 50-54, 55+)**:
  - "Salário Alto" torna-se predominante.
  - Para "55+", mais de 60% já estão na categoria de alta remuneração.

- **Ponto de Virada**: A faixa de 35-44 anos parece marcar a transição para quando "Salário Alto" começa a superar "Salário Baixo".

---

#### Conexão com a Pergunta Orientadora

**Como fatores como idade, experiência, formalidade e características técnicas/demográficas influenciam as disparidades salariais entre profissionais de dados no Brasil?**

Este gráfico reforça o papel da **idade** (como **proxy de experiência/proficiência**) na explicação da **disparidade salarial**.

---

#### Idade como Indicador de Experiência e Impacto Salarial

- A forte correlação entre idade e "Salário Alto" confirma que:
  - Profissionais mais velhos → Mais experiência acumulada → Maior proficiência técnica → Maior probabilidade de estarem em faixas salariais elevadas.
  - Jovens → Menos tempo de carreira → Salários iniciais, frequentemente associados a cargos Júnior/Pleno.

---

#### Interação da Idade/Experiência com Outros Fatores

- **Formalidade no Emprego**:
  - Profissionais mais velhos podem ocupar cargos de gestão ou atuar como PJs altamente remunerados.

- **Características Regionais**:
  - A valorização da experiência pode variar conforme a região.
  - Mercados mais aquecidos (como Sudeste) podem oferecer melhores oportunidades salariais para profissionais experientes.

- **Educação**:
  - Profissionais mais maduros também podem ter investido mais em formação (pós-graduação, certificações), o que amplia as chances de alcançar salários altos.

---

#### Ciclo de Carreira e Remuneração

Este gráfico representa, visualmente, a progressão natural de carreira:

> Início com salários baixos → Crescimento com a experiência → Consolidação salarial em estágios mais avançados.

---

#### Disparidades Dentro da Mesma Faixa Etária

Mesmo dentro de faixas mais maduras (ex: 35-39), há divisão entre "Salário Baixo" e "Salário Alto", o que sugere que **idade/experiência não explicam tudo**.

Para entender as disparidades dentro da mesma faixa etária, é preciso investigar:

- **Proficiência Técnica Específica** (ex: habilidades em demanda, especializações).
- **Tipo de Contrato e Setor** (CLT vs. PJ, privado vs. público).
- **Região de Atuação**.
- **Educação e Certificações**.

>Em resumo: O gráfico **"Proporção de faixa_salarial_eda_2cat por P1_a_1 (Top 9)"** revela uma forte associação entre avanço da idade e maior probabilidade de estar na categoria "Salário Alto". Isso reforça a hipótese de que **experiência e proficiência acumulada** são fatores centrais nas disparidades salariais.
---
### Análise do Gráfico (Gráfico de Barras Agrupadas por Gênero)
![Contagem_faixa_salarial](https://github.com/user-attachments/assets/2518b56c-80b8-45fa-b1b6-6964c63b67f3)

---

#### O que o Gráfico Mostra

Este gráfico de barras apresenta a **contagem absoluta** de profissionais em cada faixa da variável `faixa_salarial_eda_2cat` ("Salário Baixo" e "Salário Alto") por **categoria de gênero** (`P1_b`).

- **Eixo Y (`P1_b`)**: Categorias de gênero ("Masculino", "Feminino", "Prefiro não informar", "Outro").
- **Eixo X (Contagem)**: Número de respondentes em cada combinação de gênero e faixa salarial.
- **Legenda (`faixa_salarial_eda_2cat`)**:
  - **Vermelho**: Salário Baixo  
  - **Azul/Cinza**: Salário Alto

Cada categoria de gênero possui duas barras (agrupadas ou sobrepostas), representando a quantidade de pessoas daquele gênero em cada faixa salarial.

---

#### Informações Extraídas do Gráfico

**Distribuição por Gênero e Faixa Salarial:**

- **Masculino**:
  - Maior número absoluto de respondentes.
  - Cerca de 2.400 homens estão na faixa de **Salário Baixo** e 1.200 em **Salário Alto**.
  - Proporcionalmente: ~1/3 dos homens estão em "Salário Alto".

- **Feminino**:
  - Número total significativamente menor que o masculino.
  - Cerca de 850 mulheres estão em **Salário Baixo** e 250 em **Salário Alto**.
  - Proporcionalmente: A fração de mulheres na faixa "Salário Alto" é **menor que a dos homens**, indicando possível desigualdade.

- **"Prefiro não informar" e "Outro"**:
  - Contagens muito pequenas (praticamente invisíveis no gráfico).
  - A maioria aparenta estar em "Salário Baixo".

---

#### Disparidade de Gênero Sugerida

O gráfico indica duas dimensões de possível desigualdade:

1. **Representatividade**:
   - Homens são maioria na amostra.
   - Mulheres e outras identidades de gênero aparecem em número muito inferior.

2. **Distribuição Salarial**:
   - Apesar de a maioria dos profissionais (de ambos os gêneros) estar em "Salário Baixo", **homens têm uma proporção maior em "Salário Alto"** do que mulheres.
   - Isso pode indicar **disparidade salarial de gênero** no setor de dados.

---

#### Conexão com a Pergunta Orientadora

> Como fatores como características demográficas (como gênero), formalidade no emprego e proficiência técnica influenciam as disparidades salariais entre profissionais de dados no Brasil?

Este gráfico contribui diretamente para essa investigação, ao evidenciar uma **diferença na distribuição de salários entre gêneros** — um ponto-chave para compreender disparidades estruturais.

---

#### Gênero como Fator nas Disparidades Salariais

- A **menor proporção de mulheres** em "Salário Alto" pode refletir uma combinação de fatores, como:
  - Menor tempo de mercado ou acesso limitado a oportunidades de progressão.
  - Diferenças na formalidade do emprego.
  - Barreiras estruturais e vieses de gênero no setor de tecnologia/dados.

---

#### Interações Possíveis a Serem Investigadas

1. **Proficiência Técnica e Experiência**:
   - As mulheres da amostra possuem, em média, menos anos de experiência?
   - Estão em cargos mais júnior?
   - Mesmo nível de proficiência técnica leva à mesma remuneração entre homens e mulheres?

2. **Formalidade no Emprego**:
   - Há diferenças significativas nos tipos de contrato (CLT vs PJ) entre gêneros?

3. **Características Regionais**:
   - A diferença de salários por gênero se mantém constante entre regiões?  
     Ou em algumas regiões a desigualdade é mais acentuada?

4. **Educação e Idade**:
   - Mulheres com o mesmo nível de formação e idade que os homens estão sendo remuneradas de forma equivalente?

---

#### Necessidade de Análise Proporcional e Controle de Variáveis

- Este gráfico mostra **contagens absolutas**, mas para compreender as **disparidades reais**, é necessário:
  - Calcular proporções dentro de cada gênero.
  - Utilizar **análises multivariadas** que controlem fatores como:
    - Experiência
    - Escolaridade
    - Região
    - Formalidade
    - Carga horária

Isso permitirá isolar o **efeito do gênero** sobre o salário.

---

#### Representatividade e Grupos Minoritários

- As categorias **"Prefiro não informar"** e **"Outro"** têm amostras muito pequenas, limitando a análise.
- A baixa resposta desses grupos pode refletir:
  - Falta de segurança para se identificar.
  - Invisibilidade estatística.
- Reforça a importância de promover **ambientes mais inclusivos** e **coletas mais sensíveis** a essas realidades.

>Em resumo: O gráfico **"Contagem de faixa_salarial_eda_2cat por P1_b (Top 4)"** sugere que:

- Existe uma **desigualdade de gênero** na **representação** e **distribuição de salários** entre profissionais de dados no Brasil.
- Mulheres são minoria e, dentro do grupo, **menos propensas a alcançar a faixa de "Salário Alto"**.
- Para compreender essa desigualdade, é necessário investigar:
  - Experiência e proficiência técnica
  - Tipo de contrato e setor
  - Região
  - Educação
- A **interação entre esses fatores** será essencial para entender por que, mesmo com idade ou experiência similares, homens e mulheres têm salários distintos.
---
### Análise do Gráfico (Gráfico de Barras Agrupadas: Senioridade por Escolaridade)

![Distribuicao de Senioridade](https://github.com/user-attachments/assets/b6cd4f6c-91cf-479f-a153-fd04f3ecb6d9)
---

#### O que o Gráfico Mostra

Este gráfico exibe a **contagem absoluta** de profissionais para diferentes níveis de senioridade (`P2_g`) dentro de cada categoria de nível de escolaridade (`P1_l`).

- **Eixo Y (`P1_l`)**: Níveis de escolaridade (ex.: Pós-graduação, Graduação/Bacharelado, Mestrado, Estudante de Graduação, Doutorado/PhD, Não tenho graduação formal, Prefiro não informar).
- **Eixo X (Contagem)**: Número de profissionais em cada combinação escolaridade × senioridade.
- **Legenda (`P2_g`)**: Cores indicando níveis de senioridade:
  - Azul Escuro: Sênior  
  - Azul Claro: Pleno  
  - Laranja Escuro: Júnior  
  - Laranja Claro: nan (não especificado/ausente)

Cada nível de escolaridade possui barras que indicam a distribuição dos profissionais pelos níveis de senioridade.

---

#### Informações Extraídas do Gráfico

- **Pós-graduação e Graduação/Bacharelado** são os níveis mais comuns, concentrando a maior parte dos profissionais em todos os níveis de senioridade.
- **Distribuição de Senioridade por Escolaridade**:
  - **Pós-graduação**: forte concentração nos níveis Sênior e Pleno, mas também presença considerável em Júnior e nan.
  - **Graduação/Bacharelado**: ampla distribuição em Sênior, Pleno e Júnior, com representação similar ou maior em nan comparada à Pós-graduação.
  - **Mestrado**: predominância em Sênior, Pleno e nan, menos em Júnior.
  - **Estudante de Graduação**: maioria em Júnior e nan, pouca ou nenhuma presença em Sênior.
  - **Doutorado ou PhD**: embora menos numerosos, proporcionalmente muitos estão em Sênior e Pleno; nan também relevante.
  - **Não tenho graduação formal / Prefiro não informar**: pequenas contagens, maior concentração em Júnior e nan.

- **Categoria "nan" (Senioridade)** aparece em todos os níveis, especialmente em Pós-graduação, Graduação/Bacharelado e Mestrado, indicando necessidade de investigar quem são esses profissionais (ex: consultores, autônomos, gestores).

---

#### Conexão com a Pergunta Orientadora (Disparidades Salariais)

- O gráfico relaciona escolaridade (característica demográfica) com senioridade (proxy para proficiência técnica/experiência), ambos fatores chave que impactam salário.
- Níveis educacionais mais elevados (Pós, Mestrado, Doutorado) tendem a se associar a níveis mais altos de senioridade (Sênior e Pleno), sugerindo que educação avançada pode facilitar posições de maior responsabilidade e remuneração.
- Contudo, profissionais com apenas graduação também alcançam senioridade elevada, indicando que experiência e outros fatores são relevantes.

---

#### Interações e Implicações para Disparidades Salariais

- **Proficiência Técnica Específica**: Salários podem variar dentro de mesmo nível educacional e senioridade, dependendo da especialização e habilidades.
- **Formalidade no Emprego**: Tipo de contrato e setor podem influenciar salários mesmo para profissionais similares em escolaridade/senioridade.
- **Características Regionais**: O valor salarial da escolaridade e senioridade pode variar por região do Brasil.
- **Idade e Experiência**: Escolaridade interage com tempo de experiência — um Doutorado com pouca experiência pode ter remuneração diferente de um graduado experiente.

---

#### Considerações Importantes

- O prêmio salarial da educação formal avançada deve ser analisado controlando senioridade e experiência.
- A presença expressiva da categoria "nan" em senioridade, principalmente em níveis altos de escolaridade, sugere perfis diversos que merecem análise detalhada (ex: autônomos, gestores).
- Análises posteriores devem comparar salários para combinações específicas (ex: Sênior com graduação vs. Sênior com pós-graduação) para quantificar impacto real.

>Em resumo: O gráfico **"Distribuição de senioridade (P2_g) por escolaridade (P1_l)"** mostra que:

- Senioridade ocorre em todos os níveis educacionais, mas níveis mais altos de escolaridade concentram profissionais em níveis superiores (Sênior e Pleno).
- Esta interação entre educação e senioridade é fundamental para compreender as disparidades salariais no setor de dados.
- A análise salarial deve aprofundar-se nas diferenças dentro desses grupos para entender o impacto isolado da escolaridade e da senioridade.

---

# 3 Visualizacao dos dados (Análise multivariada)

### Análise do Gráfico de Dispersão: Experiência vs. Limite Inferior do Salário por Nível de Senioridade

![Experiencia vs Salario por nivel de senioridade](https://github.com/user-attachments/assets/cf0500fa-2de4-44c6-8e5d-f6d040b2fed1)

---

#### O que o Gráfico Mostra

- **Variáveis representadas:**
  - Eixo X: Anos de Experiência
  - Eixo Y: Limite Inferior do Salário
- **Cores indicam o Nível de Senioridade (`P2_g`):**
  - Verde Claro: Sênior
  - Verde Azulado/Turquesa: Pleno
  - Azul Escuro/Roxo: Júnior
  - Cinza/Azul muito escuro: nan (não especificado/ausente)
- Cada ponto representa um profissional, mostrando sua experiência, salário mínimo estimado e senioridade.

---

#### Informações Extraídas do Gráfico

- **Tendência geral positiva:**  
  Salários tendem a aumentar com o crescimento da experiência.
  
- **Dispersão salarial ampla:**  
  Para um mesmo número de anos de experiência, salários podem variar bastante, indicando que experiência sozinha não explica tudo.

- **Distribuição por senioridade:**
  - **Júnior:** Concentrados em experiências baixas (0-4 anos) e salários baixos (muitos abaixo de R$5.000, quase todos abaixo de R$10.000).
  - **Pleno:** Abrangem faixa intermediária de experiência (0-10 anos, concentração em 1-7 anos) e salários (até cerca de R$15.000–R$20.000). Sobreposição significativa com Júnior em experiência baixa e com Sênior em experiência alta.
  - **Sênior:** Geralmente mais experientes (a partir de 2-3 anos), dominando os salários mais altos (acima de R$10.000, chegando a R$40.000). Presentes em quase toda faixa de experiência, exceto zero absoluto.
  - **nan:** Dispersos em vários níveis, frequentemente sobrepostos a Júnior e Pleno em salários baixos e médios, indicando grupo heterogêneo.

- **Salários máximos:**
  - Faixa alta (R$30.000–R$40.000) quase exclusivamente de Sêniores, com experiência variando bastante (3-4 anos a mais de 10 anos).

- **Casos notáveis:**
  - Alguns profissionais com pouca experiência (0-2 anos) alcançam salários altos, especialmente se Pleno ou Sênior, sugerindo rápida progressão, habilidades muito demandadas ou critérios internos de senioridade flexíveis.

---

#### Conexão com a Pergunta Orientadora (Disparidades Salariais)

- **Experiência e senioridade como fatores principais:**  
  Ambos são fortes determinantes dos salários, com combinação mais alta em experiência e senioridade resultando em maiores remunerações.

- **Variabilidade dentro de mesma experiência:**  
  A dispersão vertical mostra que experiência isolada não explica disparidades; senioridade adiciona uma camada explicativa importante.

- **Interação experiência-senioridade:**  
  Relação não perfeita — há Júniores com vários anos e Sêniores com relativamente poucos anos, indicando que critérios de senioridade são influenciados por outros fatores além do tempo.

---

#### Influência de Outros Fatores (implícitos)

- **Formalidade no emprego:**  
  Regimes PJ, CLT, empresas grandes e pequenas afetam salários mesmo para profissionais similares.

- **Região geográfica:**  
  Mercados regionais podem valorizar experiência e senioridade de forma diferente.

- **Características demográficas e educacionais:**  
  Escolaridade, gênero, idade influenciam salários além de experiência e senioridade.

- **Especialização técnica:**  
  Habilidades específicas (ex.: IA, Big Data, linguagens) impactam fortemente remuneração.

---

#### Pontos para Investigar

- **Sêniores com pouca experiência e alto salário:**  
  O que explica essa combinação? Educação, setor, empresa, região?

- **Júniores/Plenos com experiência e salário baixos:**  
  Barreiras regionais, setoriais ou formais que limitam progressão?

- **Perfil e impacto dos "nan":**  
  Grupo heterogêneo que pode incluir autônomos, consultores ou iniciantes sem classificação definida.

>Em resumo: O gráfico evidencia a complexa interação entre:

- **Anos de experiência (proxy para proficiência técnica)**
- **Nível de senioridade (proxy para proficiência e posição)**
- **Salário**

Essa tríade é central para compreender disparidades salariais, mas as variações dentro de níveis semelhantes indicam a necessidade de considerar fatores adicionais para explicar plenamente os diferentes padrões salariais observados.

---

### Análise do Gráfico de Dispersão: Experiência vs. Limite Inferior do Salário  

![Experiencia vs Salario por nivel de ensino e faixa salarial](https://github.com/user-attachments/assets/f474a8f4-8245-4b02-9f80-f4650fbc7eb4)

---

#### O que o Gráfico Mostra

- **Eixo X:** Anos de Experiência  
- **Eixo Y:** Limite Inferior do Salário  
- **Cores:**  
  - Vermelho = Faixa Salarial Alta ("Salário Alto")  
  - Azul = Faixa Salarial Baixa ("Salário Baixo")  
- **Formas (Marcadores):** Diferenciam o Nível de Ensino (P1_l)  
  - Pós-graduação, Graduação/Bacharelado, Mestrado, Estudante de Graduação  
- **Legenda:** Explica as cores e as formas usadas.

---

#### Informações Extraídas

- **Separação clara por faixa salarial:**  
  Pontos vermelhos concentram-se na parte superior (salários altos), azuis na inferior (salários baixos).

- **Tendência geral:**  
  Salários maiores tendem a se associar a mais anos de experiência, mas há grande variabilidade.

- **Distribuição do nível de ensino dentro das faixas salariais:**

  - **Faixa Salário Baixo (Azul):**  
    - Presentes em toda faixa de experiência.  
    - Todos os níveis de ensino aparecem, incluindo pós-graduação e mestrado, especialmente em níveis iniciais de experiência.  
    - Estudantes de graduação quase exclusivos dessa faixa e com pouca experiência (0-3 anos).  
    - Pós-graduação e mestrado aparecem aqui, mostrando que a educação avançada isolada não garante salários altos, principalmente no começo da carreira.

  - **Faixa Salário Alto (Vermelho):**  
    - Geralmente profissionais com mais experiência, mas há pontos com 0-2 anos.  
    - Graduação/Bacharelado já pode levar a faixa alta em vários níveis de experiência.  
    - Pós-graduação e mestrado fortemente representados em toda a faixa de experiência, especialmente entre os salários mais altos.  
    - Estudantes de graduação praticamente ausentes nesta faixa.

- **Educação e teto salarial:**  
  Profissionais com pós-graduação e mestrado aparecem em maior proporção nas faixas salariais mais elevadas (ex: R$30.000 - R$40.000), embora graduados também alcancem esses patamares.

- **Salários altos com pouca experiência:**  
  Indivíduos com graduação, pós-graduação ou mestrado e poucos anos de experiência que já recebem salários altos indicam aceleração possível por educação, demanda de mercado ou outras vantagens.

---

#### Conexão com a Pergunta Orientadora (Disparidades Salariais)

- **Educação como potencializadora:**  
  Para mesma experiência, níveis educacionais mais altos aumentam a probabilidade de estar na faixa de salário alto.

- **Experiência ainda essencial:**  
  Salários muito altos tendem a requerer também alguns anos de experiência.

- **Presença de pós-graduados e mestres em faixa salarial baixa:**  
  Educação avançada não garante salário alto imediato — fatores adicionais entram em jogo.

---

#### Fatores Adicionais (não visíveis no gráfico, mas sugeridos pela dispersão)

- **Proficiência técnica e qualidade da experiência:** Relevância e especialização das habilidades.  
- **Formalidade no emprego:** Tipo de contrato, porte e setor da empresa.  
- **Características regionais:** Diferenças salariais regionais significativas.  
- **Demografia:** Gênero, idade e senioridade interagem com experiência e educação.

---

#### Implicações para Disparidades Salariais

- Disparidades são resultado da interação complexa entre experiência, nível de ensino e outros fatores.  
- Educação avançada pode acelerar a entrada em faixas salariais altas, mas não é suficiente isoladamente.  
- Profissionais com formação sólida podem permanecer em faixas baixas por motivos ligados a local de trabalho, contrato, região, entre outros.  
- Profissionais com pouca experiência e salário alto provavelmente atuam em nichos muito demandados ou têm diferenciais específicos.

>Em resumo: O gráfico revela como **experiência e nível de ensino** interagem para moldar a faixa salarial dos profissionais de dados no Brasil.  
Apesar da experiência ser um fator crucial, níveis mais elevados de escolaridade (pós-graduação, mestrado) facilitam o acesso a salários mais altos, especialmente quando combinados com experiência.  
No entanto, a ampla dispersão e a presença de todas as formações em ambas as faixas salariais indicam que variáveis adicionais, como proficiência técnica específica, formalidade no emprego, região e outras características demográficas, são fundamentais para compreender plenamente as disparidades salariais observadas.

---
### Análise do Gráfico de Boxplots: Limite Inferior do Salário por Nível de Ensino e Faixa Salarial (Alvo)

![Salario por nivel de ensino e faixa salarial](https://github.com/user-attachments/assets/03c2160b-f21f-442b-ab0d-d5b31d3292da)

---

#### O que o Gráfico Mostra

- **Eixo X:** Nível de Ensino (P1_l)  
- **Eixo Y:** Limite Inferior do Salário  
- Para cada nível de ensino, há dois boxplots lado a lado, correspondendo a:  
  - **Vermelho:** Faixa "Salário Baixo"  
  - **Azul:** Faixa "Salário Alto"  
- Cada boxplot exibe mediana, quartis (Q1, Q3), hastes (whiskers) e outliers da distribuição salarial naquela combinação.

---

#### Informações Extraídas

- **Separação clara por faixa salarial:**  
  Boxplots vermelhos ("Salário Baixo") apresentam níveis salariais significativamente mais baixos que os azuis ("Salário Alto") em todos os níveis de ensino, validando a variável "Faixa Salarial (Alvo)".

- **Distribuição para "Salário Baixo":**  
  - Medianas geralmente próximas de R$ 5.000 para Pós-graduação, Graduação, Mestrado, Doutorado.  
  - Estudantes de Graduação possuem a mediana mais baixa, refletindo salários de entrada ou estágio.  
  - Indivíduos sem graduação formal ou que preferem não informar mostram medianas baixas, com alguma variabilidade.

- **Distribuição para "Salário Alto":**  
  - Medianas tipicamente entre R$ 15.000 e R$ 20.000 para os níveis mais comuns (Pós-graduação, Graduação, Mestrado, Doutorado).  
  - Mestrado e Doutorado apresentam medianas ligeiramente superiores, com maior dispersão indicando maior variabilidade salarial.  
  - Estudantes de Graduação têm boxplot azul achatado com poucos dados, indicando que poucos alcançam essa faixa alta — provavelmente dados pouco representativos.  
  - Pessoas sem graduação formal ou que preferem não informar mostram medianas elevadas e grande dispersão, mas o baixo número de casos pode influenciar.

- **Outliers:**  
  Presentes especialmente nos boxplots de "Salário Alto" para níveis mais comuns, sugerindo profissionais que atingem salários excepcionalmente altos.

---

#### Conexão com a Pergunta Orientadora (Disparidades Salariais)

- **Educação e remuneração:**  
  Níveis de ensino mais elevados estão associados a medianas salariais maiores dentro da faixa "Salário Alto", indicando que educação formal facilita acesso a salários mais altos.

- **Pouca variação entre níveis na faixa "Salário Baixo":**  
  Isso sugere que, para salários menores, o nível de escolaridade formal é menos determinante, e outros fatores podem ter papel mais relevante.

- **Dispersão maior na faixa "Salário Alto":**  
  Indica que, ao alcançar patamares salariais altos, a educação pode definir um piso salarial, mas outras variáveis (experiência, senioridade, setor, localização) são fundamentais para a variação salarial dentro desse grupo.

---

#### Considerações sobre Casos Atípicos

- "Salário Alto" para estudantes ou sem graduação formal podem ser casos reais de profissionais com alta proficiência técnica, habilidades diferenciadas, ou empreendedorismo, mas o baixo número desses casos torna as inferências cautelosas.

---

#### Interação entre Educação e Proficiência Técnica

- A educação formal atua como base para o desenvolvimento profissional, mas o avanço salarial até níveis elevados depende também de proficiência técnica adquirida via experiência e aprendizado contínuo.

>Em resumo: O gráfico confirma que a educação formal é um fator importante para o alcance da faixa de "Salário Alto" e está associada a medianas salariais maiores.  
Porém, a significativa variabilidade salarial dentro de cada nível de ensino — mesmo segmentada pela faixa salarial — indica que fatores como experiência, senioridade, formalidade no emprego e características regionais são essenciais para explicar as disparidades salariais entre profissionais de dados no Brasil.  
A educação pode garantir um “piso” mais alto para salários, mas não determina sozinha o teto salarial.

---
### Análise do Gráfico de Violin Plots Divididos: Experiência (anos) por Nível de Senioridade e Faixa Salarial (Alvo)

![Experiencia por seneridade e faixa salarial (Alvo)](https://github.com/user-attachments/assets/7cb4de01-50f5-439c-9baa-42b91cdb7a58)

---

#### O que o Gráfico Mostra

- **Eixo X:** Nível de Senioridade (P2_g) — Sênior, Pleno, Júnior, nan (não especificado).  
- **Eixo Y:** Experiência (anos).  
- Cada violino está dividido verticalmente em duas metades:  
  - **Vermelho (esquerda):** Distribuição da experiência para profissionais na faixa "Salário Baixo".  
  - **Azul (direita):** Distribuição da experiência para profissionais na faixa "Salário Alto".  
- A largura do violino em determinado ponto indica a densidade de profissionais com aquela experiência.

---

#### Informações Extraídas

- **Júnior:**  
  - Salário Baixo: Maioria concentrada entre 0 e 2-3 anos de experiência, com alta densidade em níveis muito baixos.  
  - Salário Alto: Poucos Júniores, com experiência ligeiramente maior (2-4 anos), porém baixa densidade, indicando raridade desse caso.

- **Pleno:**  
  - Salário Baixo: Distribuição ampla até 5-6 anos, com picos entre 1-3 anos.  
  - Salário Alto: Distribuição deslocada para mais experiência (3-7 anos), mostrando que mais experiência é necessária para atingir salário alto nesta senioridade.

- **Sênior:**  
  - Salário Baixo: Grupo menor, concentrado entre 2-6 anos de experiência.  
  - Salário Alto: Distribuição ampla, de 3-4 até 10+ anos, com densidade maior em experiências elevadas.

- **nan (senioridade não informada):**  
  - Ambos os grupos apresentam ampla variação em anos de experiência, com tendência de maior experiência para o grupo de salário alto, mas heterogeneidade alta.

---

#### Tendências e Interpretações

- Para cada nível de senioridade, a distribuição azul ("Salário Alto") tende a deslocar-se para mais anos de experiência e maior densidade em faixas elevadas, em comparação com a distribuição vermelha ("Salário Baixo").  
- Isso reforça que, mesmo com o mesmo título de senioridade, mais experiência costuma estar associada a salários mais altos.  
- A progressão natural da carreira reflete-se: Júniores com pouca experiência geralmente ganham salários baixos; para Plenos e Seniores, experiência crescente é correlacionada com faixas salariais elevadas.

---

#### Conexão com a Pergunta Orientadora (Disparidades Salariais)

- **Experiência como diferencial dentro da senioridade:**  
  O gráfico destaca que o título de senioridade por si só não explica as diferenças salariais. A profundidade da experiência (anos no campo) é fundamental para compreender a faixa salarial dentro de cada nível.

- **Interação Proficiência Técnica e Salário:**  
  Anos de experiência e reconhecimento formal (senioridade) juntos explicam grande parte das disparidades salariais observadas.

- **Fatores adicionais para variações restantes:**  
  - **Formalidade no emprego:** Contrato CLT, PJ, setor e tamanho da empresa impactam salários.  
  - **Características regionais:** Mercado local, custo de vida e demanda influenciam remuneração.  
  - **Demografia e formação:** Gênero, raça, nível de educação e suas interações com o mercado.  
  - **Qualidade da experiência:** Tecnologias, responsabilidades e escopo de atuação, que não são capturados só por anos ou título.

- **Grupo nan:**  
  Alta heterogeneidade sugere perfis diversos, possivelmente freelancers ou profissionais fora das classificações tradicionais.

>Em resumo: O gráfico "Experiência por Senioridade e Faixa Salarial" evidencia que, dentro de cada título profissional, mais anos de experiência tendem a associar-se a salários mais altos, reforçando a importância da proficiência técnica aprofundada.  
As diferenças que permanecem após controlar senioridade e experiência apontam para a necessidade de incluir análise de formalidade no emprego, fatores regionais e demográficos para compreender plenamente as disparidades salariais no setor de dados brasileiro.

---

## Análise do Gráfico "Nível de Ensino por Região e Faixa Salarial (Alvo)"
![Nivel de ensino por regiao e faixa salarial (alvo)](https://github.com/user-attachments/assets/65516cef-91cd-4308-a150-582c26d0bb50)

---

### O que o Gráfico Mostra:

Este gráfico consiste em múltiplos subplots, cada um representando uma região do Brasil (Sudeste, Sul, Nordeste, Centro-Oeste).  
A região Norte e "Desconhecida" não aparecem nestes subplots, provavelmente devido a um menor número de respondentes ou por decisão de focar nas regiões com mais dados.  
Dentro de cada subplot regional, são exibidas barras horizontais que mostram a contagem de profissionais para diferentes Níveis de Ensino (P1_l).  
Cada barra de nível de ensino é dividida (ou acompanhada) por cores que representam a faixa_salarial_eda_2cat ("Salário Baixo" em vermelho e "Salário Alto" em azul).  
Eixo Y (Comum aos subplots, implícito dentro de cada um): Nível de Ensino (P1_l) (Pós-graduação, Graduação/Bacharelado, Mestrado, Estudante de Graduação, Doutorado ou Phd).  
Eixo X (Dentro de cada subplot): Contagem de profissionais.  
Legenda (Comum ao gráfico geral):  
- Vermelho: "Salário Baixo"  
- Azul: "Salário Alto"  

### Interpretação:

Para cada região, pode-se observar quantos profissionais de cada nível de ensino se enquadram na faixa de "Salário Baixo" versus "Salário Alto".

### Informações Extraídas do Gráfico (Comparando as Regiões):

- **Predominância da Região Sudeste:**  
O eixo X da contagem para o Sudeste vai até valores muito mais altos (ex: 1000) em comparação com as outras regiões (Sul até ~400, Nordeste e Centro-Oeste até ~200 ou menos), refletindo a maior concentração de profissionais nesta região, como visto em gráficos anteriores.

- **Padrão Geral (Salário Baixo vs. Salário Alto por Escolaridade):**  
Em todas as regiões, para a maioria dos níveis de ensino, a contagem de profissionais em "Salário Baixo" (vermelho) é geralmente maior ou comparável à de "Salário Alto" (azul).  
Estudantes de Graduação: Consistentemente, em todas as regiões, estão quase que exclusivamente na faixa de "Salário Baixo". A barra azul para "Salário Alto" é inexistente ou minúscula.  
Graduação/Bacharelado e Pós-graduação: São os níveis de ensino com maior número de profissionais em todas as regiões. Em ambos, há representação tanto em "Salário Baixo" quanto em "Salário Alto".

- **Diferenças Regionais na Proporção Salário Alto/Baixo (Análise Visual Aproximada):**  
Sudeste: Para Pós-graduação e Graduação/Bacharelado, embora a contagem absoluta em "Salário Baixo" seja alta, a contagem em "Salário Alto" (azul) também é muito significativa. A proporção de profissionais com Pós-graduação em "Salário Alto" parece ser relativamente boa. Para Mestrado e Doutorado, a barra azul ("Salário Alto") é proeminente, muitas vezes superando ou igualando a vermelha, apesar das contagens absolutas serem menores.  
Sul: O padrão é similar ao Sudeste, mas com contagens menores. Para Pós-graduação e Graduação, há uma boa representação em "Salário Alto". Mestrado e Doutorado também mostram uma tendência a "Salário Alto", proporcionalmente.  
Nordeste: As barras azuis ("Salário Alto") são visivelmente menores em comparação com as vermelhas ("Salário Baixo") para a maioria dos níveis de ensino, mesmo para Pós-graduação e Graduação. Proporcionalmente, parece haver uma menor chance de estar na faixa de "Salário Alto" nesta região em comparação com Sudeste e Sul para um mesmo nível de escolaridade.  
Centro-Oeste: Similar ao Nordeste, as contagens em "Salário Alto" são mais modestas. Para Pós-graduação e Graduação, a barra vermelha é dominantemente maior que a azul.

- **Impacto do Mestrado e Doutorado:**  
Em regiões como Sudeste e Sul, ter Mestrado ou Doutorado parece estar mais consistentemente associado à faixa de "Salário Alto" (barras azuis proporcionalmente grandes ou maiores que as vermelhas).  
Nas regiões Nordeste e Centro-Oeste, o número absoluto de profissionais com Mestrado/Doutorado é menor, mas aqueles que existem também tendem a estar em "Salário Alto", embora a oportunidade geral pareça mais restrita.

### Conexão com a Pergunta Orientada a Dados (Disparidades Salariais):

- **Região como Moduladora do Retorno da Educação:**  
Fica claro que o "retorno" salarial (chance de estar em "Salário Alto") para um determinado nível de ensino não é o mesmo em todas as regiões. Profissionais com Pós-graduação no Sudeste ou Sul parecem ter uma probabilidade maior de alcançar salários altos do que seus pares com a mesma formação no Nordeste ou Centro-Oeste.  
Isso sugere que o mercado de trabalho regional (demanda por qualificações, tipos de indústrias presentes, custo de vida e capacidade de pagamento das empresas) influencia significativamente o valor atribuído à educação formal.

- **Interação com Proficiência Técnica (Implícita):**  
Embora a proficiência técnica (experiência, senioridade, habilidades específicas) não esteja explicitada neste gráfico, ela interage com a educação e a região. Por exemplo, a disponibilidade de vagas que exigem alta proficiência (e pagam mais) pode ser maior no Sudeste, beneficiando aqueles com alta escolaridade e experiência relevante naquela região.  
Pode ser que, para atingir "Salário Alto" no Nordeste ou Centro-Oeste com um diploma de Graduação, seja necessário um nível de proficiência técnica/experiência ainda maior do que no Sudeste, ou que as oportunidades simplesmente sejam mais escassas.

- **Formalidade no Emprego (Implícita):**  
A natureza das vagas (CLT, PJ, tamanho da empresa, setor) também varia regionalmente e pode interagir com a escolaridade. Regiões com mais empresas de grande porte ou setores tecnológicos podem oferecer mais vagas formais com salários mais altos para profissionais qualificados.

- **Disparidades Salariais Explicadas pela Interação:**  
Um profissional com Pós-graduação (demografia/educação) trabalhando no Sudeste (região) tem um perfil de chance salarial diferente de um com a mesma Pós-graduação no Nordeste.  
Para entender completamente a disparidade, precisaríamos adicionar a camada de proficiência técnica (quantos anos de experiência tem o pós-graduado no Sudeste vs. Nordeste para estar em "Salário Alto"?) e a formalidade do emprego.

- **Concentração de Oportunidades:**  
A maior contagem de profissionais em "Salário Alto" (barras azuis) no Sudeste e Sul, em diversos níveis de escolaridade, sugere uma maior concentração de oportunidades de alta remuneração nessas regiões.

>Em resumo: O gráfico "Nível de Ensino por Região e Faixa Salarial (Alvo)" é fundamental para ilustrar que a região é um fator crucial que interage com o nível de ensino para influenciar a probabilidade de um profissional de dados alcançar uma faixa salarial mais alta.  
As disparidades salariais no Brasil para profissionais de dados não podem ser entendidas sem considerar o contexto regional, que modula o valor da educação e, provavelmente, da proficiência técnica.  
Para uma análise mais completa, seria ideal cruzar esses dados também com a experiência/senioridade e a formalidade do emprego dentro de cada combinação de região e nível de ensino.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Indução de modelos

*   [1. 1º PERGUNTA ORIENTADA A DADOS ](#modelos-1º-pergunta-orietada-a-dados)
  
	*   [1.1 Modelo 1 Análise de Disparidade Salarial de Profissionais de Dados no Brasil Utilizando o Modelo Random Forest](#modelo-1-análise-de-disparidade-salarial-de-profissionais-de-dados-no-brasil-utilizando-o-modelo-random-forest)
  
		*   [1.1.1 Justificativa1.1](#justificativa1-1)
		*   [1.1.2 Processo de Amostragem de Dados (Particionamento e Cross-Validation1.1)](#processo-de-amostragem-de-dados1-1)
		*   [1.1.3 Parâmetros utilizados1.1](#parâmetros-utilizados1-1)
		*   [1.1.4 Explicação do Código1.1](#explicação-do-código1-1)

	*   [1.2 Modelo 2 Análise de Disparidade Salarial de Profissionais de Dados no Brasil Utilizando o Arvore de decisão por classificação](#modelo-1-análise-de-disparidade-salarial-de-profissionais-de-dados-no-brasil-utilizando-o-arvore-de-decisão-por-classificação)

		*   [1.2.1 Justificativa1.2](#justificativa1-2)
		*   [1.2.2 Processo de Amostragem de Dados (Particionamento e Cross-Validation1.2)](#processo-de-amostragem-de-dados1-2)
		*   [1.2.3 Parâmetros utilizados1.2](#parâmetros-utilizados1-2)
		*   [1.2.4 Explicação do Código1.2](#explicação-do-código1-2)

 
* [2. 2º PERGUNTA ORIENTADA A DADOS ](#modelos-2º-pergunta-orietada-a-dados)

* [3. 3ª PERGUNTA ORIENTADA A DADOS](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#modelos-3%C2%BA-pergunta-orietada-a-dados)
    * [3.1 Modelo 3.1: Relatório Técnico de Classificação Salarial](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#modelos-3%C2%BA-pergunta-orietada-a-dados)
        * [3.1.1 Justificativa e Objetivo](#1-justificativa-e-objetivo-modelo-31)
        * [3.1.2 Metodologia](#2-metodologia-modelo-31)
        * [3.1.3 Fluxo de Execução do Código](#3-fluxo-de-execucao-do-código-modelo-31)
    * [3.2 Modelo 3.2: Rede Neural com Embeddings e Otimização via Ray Tune (RNA v2)](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#modelos-3%C2%BA-pergunta-orietada-a-dados-1)
        * [3.2.1 Justificativa e Objetivo](#1-justificativa-e-objetivo-modelo-32)
        * [3.2.2 Processo de Amostragem de Dados](#2-processo-de-amostragem-de-dados-modelo-32)
        * [3.2.3 Parâmetros Utilizados (Principais)](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#3-par%C3%A2metros-utilizados-principais---modelo-32)
        * [3.2.4 Resultados da Avaliação (RNA V2)](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#4-resultados-da-avalia%C3%A7%C3%A3o-rna-v2---modelo-32)
        * [3.2.5 Explicação do Código (Fluxo Principal para RNA v2)](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#5-explica%C3%A7%C3%A3o-do-c%C3%B3digo-fluxo-principal-para-rna-v2----modelo-32)



# Modelos 1º pergunta orietada a dados

## Modelo 1 Análise de Disparidade Salarial de Profissionais de Dados no Brasil Utilizando o Modelo Random Forest

## *Justificativa1-1*

O modelo `RandomForestClassifier` é uma boa escolha para sua pergunta porque ele consegue identificar como diferentes fatores, como educação e experiência, interagem e qual a importância de cada um para explicar as diferenças salariais.

### Capacidade Inerente de Modelar Interações Complexas 🧩
A pergunta foca explicitamente na **interação** entre formação e experiência. Modelos baseados em árvores, como o Random Forest, são excelentes em capturar automaticamente interações não lineares entre features. Cada caminho da raiz até uma folha em uma árvore de decisão representa uma sequência de condições, que é, em essência, uma regra de interação. Por exemplo, o impacto da "experiência profissional" no salário pode ser diferente para quem tem "doutorado" versus quem tem apenas "graduação". O Random Forest, ao agregar centenas de árvores, explora inúmeras dessas interações potenciais. O notebook até inclui uma visualização específica (`interacao_formacao_experiencia.png`) que tenta mostrar a probabilidade de salário alto com base na combinação de níveis de formação e experiência, demonstrando a capacidade do modelo de aprender e representar essas interações.

---
### Identificação dos Fatores Mais Influentes (Importância das Features) 📊
Para entender como diferentes fatores influenciam a disparidade salarial, é crucial saber quais são os mais determinantes. O Random Forest fornece uma métrica de "importância das features", que quantifica a contribuição de cada variável (como 'Nível de ensino alcançado', 'Tempo de experiência na área de dados', 'Nível de senioridade', 'UF onde mora', etc.) para a precisão da previsão. O notebook demonstra a extração e visualização dessas importâncias, permitindo identificar os principais direcionadores da disparidade salarial.

---
### Flexibilidade para Modelar Relações Não Lineares 📈
A relação entre fatores socioeconômicos e salário raramente é linear. Por exemplo, o aumento salarial com a experiência pode não ser constante, ou o benefício de um diploma adicional pode variar dependendo do nível de senioridade atual. O Random Forest não assume relações lineares e pode modelar essas complexidades de forma eficaz.

---
### Robustez e Desempenho Geral 🚀
Random Forests são conhecidos por sua **robustez** a outliers (em certa medida) e por seu **bom desempenho preditivo** em uma ampla gama de problemas de classificação sem a necessidade de um ajuste extensivo de hiperparâmetros (embora o tuning, como feito no notebook via `GridSearchCV`, geralmente melhore ainda mais o desempenho). A capacidade de lidar com diferentes tipos de features (numéricas e categóricas codificadas) e a menor propensão a overfitting em comparação com árvores de decisão únicas também são vantagens significativas.

---
### Adequação à Definição do Problema no Notebook 🎯
No notebook fornecido, a "disparidade salarial" foi transformada em um problema de **classificação binária** (salário alto vs. salário baixo/médio). O `RandomForestClassifier` é projetado especificamente para esse tipo de tarefa. Além disso, o código implementa:
* **Engenharia de features** relevante (mapeamento de níveis de formação, experiência, etc.).
* **Tratamento de classes desbalanceadas** (usando `sample_weights` e `class_weight`), o que é comum em dados salariais.
* **Calibração de probabilidades** e **otimização de limiar**, levando a um modelo mais confiável e ajustado ao problema.

---
## - Capacidade de Capturar Interações Complexas:

### Como as Árvores de Decisão (Base do Random Forest) Capturam Interações

* **Natureza Hierárquica e Condicional**:
    * Uma árvore de decisão funciona dividindo o espaço das features em regiões menores através de uma série de **decisões condicionais (splits)**.
    * O caminho de uma amostra de dados da raiz até uma folha (nó terminal) representa uma **sequência específica de condições** sobre diferentes features.
    * Por exemplo, uma árvore pode aprender que "SE `Nível de senioridade` é 'Sênior' E `Tempo de experiência na área de dados` é 'Mais de 10 anos', ENTÃO a probabilidade de `salario_alto` é X". Esta é uma interação direta entre `Nível de senioridade` e `Tempo de experiência`. O efeito da experiência no salário pode ser diferente para um júnior versus um sênior.

* **Profundidade da Árvore**:
    * Árvores mais profundas (controladas por `max_depth`, `min_samples_split`, `min_samples_leaf`) podem capturar interações de ordem superior (interações entre três ou mais features). No modelo otimizado, `max_depth` foi definido como `None`, permitindo que as árvores cresçam até que os critérios de `min_samples_leaf: 7` e `min_samples_split: 15` sejam atingidos. Isso dá flexibilidade para capturar interações significativas.

---

### Como o Random Forest (Ensemble) Amplifica essa Capacidade

* **Múltiplas Perspectivas**:
    * O Random Forest constrói **muitas árvores de decisão** (100 neste caso), cada uma treinada em uma subamostra diferente dos dados (bootstrap) e considerando um subconjunto aleatório de features em cada divisão.
    * Isso significa que diferentes árvores terão a oportunidade de explorar e modelar **diferentes interações** ou as mesmas interações de maneiras ligeiramente diferentes. Algumas árvores podem priorizar certas interações, enquanto outras focam em combinações distintas.

* **Agregação de Conhecimento**:
    * A previsão final do Random Forest é uma agregação (média de probabilidades para classificação) das previsões de todas as árvores individuais.
    * Ao combinar o "conhecimento" de muitas árvores que aprenderam diversas interações, o ensemble se torna capaz de representar um **panorama de interações muito mais rico e robusto** do que uma única árvore conseguiria.

---

### Evidências e Suporte no Código do Notebook

* **Visualização de Interação Específica**:
    * O notebook inclui uma "Análise de Interação entre Formação e Experiência" que gera um heatmap (`interacao_formacao_experiencia.png`). Este gráfico mostra a probabilidade média de `salario_alto` para diferentes combinações de `formacao_academica_encoded` e `experiencia_profissional_encoded`.
    * O fato de o modelo conseguir gerar previsões que resultam em um padrão claro neste heatmap (por exemplo, mostrando que a combinação de alta formação E alta experiência leva a uma maior probabilidade de salário alto) é uma **demonstração direta** de que o modelo está capturando e utilizando essa interação específica.

* **Engenharia de Features**:
    * A codificação one-hot de features como `'Área de formação acadêmica'`, `'UF onde mora'`, e `'Setor de atuação da empresa'` cria colunas binárias. O modelo pode então aprender, por exemplo, se o impacto do `'Tempo de experiência na área de dados'` no salário é diferente para `'UF onde mora_São Paulo'` versus `'UF onde mora_Bahia'`.

* **Desempenho Geral do Modelo**:
    * Um bom desempenho em um problema complexo como a previsão salarial, que intuitivamente depende de como múltiplos fatores se combinam, sugere que o modelo está efetivamente capturando não apenas os efeitos principais das features, mas também suas interações. Se o modelo não conseguisse capturar essas interações, seu poder preditivo seria provavelmente muito menor.

Em resumo, a estrutura baseada em árvores do Random Forest, combinada com a diversidade introduzida pelo bagging e pela amostragem aleatória de features, permite que o modelo aprenda e utilize automaticamente as interações complexas e não lineares entre as variáveis preditoras, o que é fundamental para sua eficácia em muitos problemas do mundo real.

---
## - Fornecimento de Importância das Features:

### Como o Random Forest Calcula a Importância das Features

* **Redução Média da Impureza (Mean Decrease in Impurity - MDI)**:
    * O método mais comum, e o padrão no Scikit-learn para `RandomForestClassifier`, é baseado na **impureza de Gini** (ou entropia, dependendo da configuração do critério da árvore).
    * Quando uma árvore de decisão é construída, cada divisão de um nó é feita escolhendo a feature que resulta na maior redução da impureza (ou seja, que torna os nós filhos mais "puros" em termos de classes).
    * A importância de uma feature é calculada como a **média da redução da impureza** que ela proporciona em todas as árvores da floresta. Quanto mais uma feature contribui para reduzir a impureza nos nós onde é utilizada para divisão, maior será sua importância.
    * As importâncias são então normalizadas para que a soma de todas as importâncias seja igual a 1.

---

### Implementação no Código do Notebook

O notebook extrai e utiliza a importância das features da seguinte maneira:

1.  **Extração dos Valores de Importância**:
    * Após o treinamento e a otimização do `RandomForestClassifier` (armazenado em `best_rf_model`), os valores de importância são acessados diretamente através do atributo:
        ```python
        importances = best_rf_model.feature_importances_
        ```
    * Os nomes das features correspondentes são obtidos a partir das colunas do DataFrame `X`:
        ```python
        feature_names = X.columns
        ```

2.  **Ordenação e Seleção**:
    * As importâncias são ordenadas em ordem decrescente para identificar as features mais relevantes:
        ```python
        indices = np.argsort(importances)[::-1]
        ```

3.  **Visualização da Importância das Features**:
    * O código gera múltiplos gráficos para visualizar essas importâncias, facilitando a interpretação:
        * **Top 20 Features Mais Relevantes**: Um gráfico de barras horizontais mostrando as 20 features com maior pontuação de importância (`importancia_features_top20.png`).
        * **Importância Agrupada por Prefixo**: Se houver muitas features (especialmente após o one-hot encoding), gráficos de barras separados são criados para grupos de features com o mesmo prefixo (ex: "UF onde mora\_", "Área de formação acadêmica\_") para melhor organização (`importancia_features_grupo_*.png`).
        * **Top 3 Features Mais Importantes**: Um gráfico de barras focado nas três features de maior impacto, com os valores de importância anotados (`top3_features.png`).
        * **Gráfico de Dispersão das Duas Features Mais Importantes**: Visualiza a relação entre as duas features mais importantes e a probabilidade de salário alto (`dispersao_top2_features.png`).

---

### Valor da Análise de Importância das Features

Conhecer a importância das features é extremamente útil por diversos motivos:

* **Interpretabilidade do Modelo**: Ajuda a entender quais fatores o modelo considera mais decisivos para fazer suas previsões. No contexto do problema, revela quais aspectos (como nível de ensino, experiência, senioridade, etc.) são mais determinantes para a faixa salarial.
* **Seleção de Features (Feature Selection)**:
    * Features com importância muito baixa podem, em alguns casos, ser removidas do modelo sem grande perda de performance (ou até mesmo com ganho, ao reduzir ruído e complexidade).
    * Isso pode levar a modelos mais simples, mais rápidos de treinar e, potencialmente, mais generalizáveis.
* **Direcionamento de Negócios e Pesquisas**:
    * As features mais importantes podem indicar áreas onde intervenções ou foco podem ser mais eficazes. Por exemplo, se "Nível de ensino alcançado" é muito importante, isso reforça o valor da educação para progressão salarial.
* **Detecção de Problemas (Sanity Check)**: Se uma feature que intuitivamente não deveria ser importante aparece com alta relevância, isso pode indicar problemas nos dados (vazamento de dados - data leakage) ou na formulação do problema.
* **Comunicação dos Resultados**: É mais fácil explicar o comportamento de um modelo para stakeholders não técnicos destacando as poucas variáveis que têm o maior impacto.

A análise de importância das features fornecida pelo Random Forest é, portanto, uma etapa crucial não apenas para avaliar o modelo, mas também para extrair insights acionáveis a partir dos dados.

---
## - Robustez e Generalização:

### Robustez do Modelo 💪

A robustez refere-se à capacidade do modelo de manter seu desempenho mesmo diante de variações nos dados de entrada, como ruído ou outliers.

* **Natureza de Ensemble (Bagging)**:
    * O Random Forest constrói múltiplas árvores de decisão (100 neste modelo). Cada árvore é treinada em uma subamostra diferente dos dados (bootstrap).
    * Ao agregar as previsões de muitas árvores, o impacto de **outliers** ou **ruído** que possam ter afetado uma ou algumas árvores é diluído. Uma única árvore pode ser sensível a esses pontos, mas é menos provável que a maioria das árvores seja influenciada da mesma maneira.

* **Aleatoriedade na Seleção de Features**:
    * Em cada divisão de nó de cada árvore, apenas um subconjunto aleatório de features é considerado. Isso **descorrelaciona as árvores** e impede que features individualmente muito fortes (mas possivelmente ruidosas ou específicas demais para a amostra de treino) dominem a construção de todas as árvores. Isso torna o modelo menos sensível a pequenas variações nas features individuais.

* **Controle da Complexidade das Árvores**:
    * Os hiperparâmetros otimizados `min_samples_split: 15` e `min_samples_leaf: 7` restringem o crescimento das árvores. Eles evitam que as árvores se tornem excessivamente complexas e se ajustem ao ruído presente nos dados de treinamento. Árvores mais simples e robustas contribuem para uma floresta mais robusta.

* **Tratamento de Desbalanceamento de Classes**:
    * O uso de `class_weight='balanced_subsample'` e `sample_weights` torna o modelo robusto a distribuições de classe desiguais. Sem isso, o modelo poderia simplesmente aprender a prever a classe majoritária, mostrando um desempenho pobre e não robusto quando confrontado com diferentes proporções de classe ou com a importância da classe minoritária.

---

### Generalização do Modelo 🌍

A generalização é a capacidade do modelo de performar bem em dados novos e não vistos, após ter sido treinado em um conjunto de dados específico. É o objetivo principal do aprendizado de máquina.

* **Redução de Variância pelo Bagging**:
    * A principal vantagem do bagging (usado no Random Forest) é a **redução da variância** do modelo sem aumentar significativamente o bias. Modelos com alta variância tendem a se ajustar demais aos dados de treinamento (overfitting) e generalizam mal. Ao agregar múltiplas árvores, o Random Forest suaviza as previsões e melhora a generalização.

* **Validação Cruzada (`GridSearchCV` e `CalibratedClassifierCV`)**:
    * O uso de validação cruzada de **5 folds** tanto no `GridSearchCV` (para otimização de hiperparâmetros) quanto no `CalibratedClassifierCV` (para calibração) é fundamental para a generalização.
    * Nesses processos, o modelo é treinado e avaliado múltiplas vezes em diferentes subconjuntos dos dados de treinamento. Isso ajuda a garantir que os hiperparâmetros selecionados e o processo de calibração sejam eficazes não apenas para uma divisão específica dos dados, mas que **generalizem bem** para porções não vistas do conjunto de treinamento.

* **Divisão em Conjunto de Treino e Teste**:
    * A separação inicial dos dados em conjuntos de treino (70%) e teste (30%) é a prática padrão para avaliar a generalização. O modelo é treinado exclusivamente nos dados de treino, e seu desempenho final no conjunto de teste (dados que o modelo nunca viu durante o treinamento, otimização ou calibração) é uma estimativa de quão bem ele generalizará para dados do mundo real.

* **Otimização de Hiperparâmetros Focada em Generalização**:
    * Parâmetros como `min_samples_split` e `min_samples_leaf` (além de `max_depth`, que aqui foi `None` mas efetivamente limitado pelos outros) são cruciais para controlar a complexidade do modelo.
    * O `GridSearchCV` seleciona a combinação desses parâmetros que maximiza a `balanced_accuracy` na validação cruzada, buscando um equilíbrio que evite o overfitting aos dados de treino e promova uma boa performance em dados não vistos.

* **Número Adequado de Árvores (`n_estimators=100`)**:
    * Construir um número suficiente de árvores (100, no caso) geralmente leva a um modelo mais estável e com melhor generalização, pois a agregação se beneficia da "sabedoria da multidão" das árvores. Embora adicionar mais árvores possa não prejudicar (além do custo computacional) após um certo ponto, um número muito pequeno poderia levar a uma generalização pobre.

Em resumo, o modelo Random Forest do notebook é projetado e treinado de forma a não apenas se ajustar bem aos dados de treinamento, mas também a ser estável e performar de maneira confiável em novos dados, o que é essencial para sua aplicação prática.

---
## - Bom Desempenho em Problemas de Classificação:

### 1. Forças Fundamentais do Algoritmo Random Forest

* **Aprendizado por Ensemble (Bagging)**:
    * O Random Forest constrói múltiplas árvores de decisão (100, neste caso) treinadas em diferentes subamostras dos dados (bootstrap).
    * A decisão final é tomada por agregação (média das probabilidades ou voto majoritário para classificação). Isso **reduz a variância** do modelo em comparação com uma única árvore de decisão, tornando-o menos propenso a memorizar o ruído nos dados de treinamento e melhorando a **generalização** para dados não vistos.

* **Alta Capacidade de Modelagem (Não Linearidade)**:
    * Árvores de decisão, a base do Random Forest, são capazes de capturar relações complexas e **não lineares** entre as features e o alvo. O ensemble herda essa capacidade.

* **Robustez a Outliers e Ruído (Relativa)**:
    * Devido à agregação de múltiplas árvores, o impacto de outliers individuais ou ruído em algumas árvores tende a ser mitigado pelas outras, tornando o modelo geralmente mais robusto.

* **Redução de Overfitting (Comparado a Árvores Individuais)**:
    * Ao combinar muitas árvores, cada uma possivelmente overfit a uma parte dos dados, o Random Forest como um todo tende a ter um **overfitting menor**. A aleatoriedade na seleção de features para cada divisão também contribui para isso.

* **Fornecimento de Importância das Features**:
    * O modelo calcula intrinsecamente a importância de cada feature, o que ajuda a entender os direcionadores da previsão e pode guiar a seleção de features. O código utiliza essa capacidade extensivamente para análise.

---

### 2. Técnicas Específicas Aplicadas no Código que Potencializam o Desempenho

* **Otimização de Hiperparâmetros (`GridSearchCV`)**:
    * O uso do `GridSearchCV` permitiu testar sistematicamente uma grade de hiperparâmetros (`n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`, `class_weight`).
    * A seleção dos **melhores parâmetros** (`{'class_weight': 'balanced_subsample', 'max_depth': None, 'min_samples_leaf': 7, 'min_samples_split': 15, 'n_estimators': 100}`) otimiza o modelo especificamente para este conjunto de dados, maximizando a métrica `balanced_accuracy`.

* **Tratamento Eficaz de Classes Desbalanceadas**:
    * **`class_weight='balanced_subsample'`**: Este hiperparâmetro ajusta automaticamente os pesos das classes em cada árvore com base nas frequências da subamostra de bootstrap, dando mais importância à classe minoritária.
    * **`sample_weights`**: Pesos foram explicitamente calculados e passados aos métodos `.fit()` do `GridSearchCV` e `CalibratedClassifierCV`. Isso força o modelo a prestar mais atenção aos exemplos da classe minoritária durante o treinamento.
    * **Métrica de Avaliação Adequada (`balanced_accuracy`)**: A escolha da `balanced_accuracy` como métrica de scoring no `GridSearchCV` e para a seleção do melhor limiar garante que o desempenho seja avaliado de forma justa, mesmo com classes desbalanceadas.

* **Calibração de Probabilidades (`CalibratedClassifierCV`)**:
    * Modelos como Random Forest podem produzir probabilidades de classe que não são perfeitamente calibradas (ou seja, uma probabilidade prevista de 0.8 não corresponde necessariamente a uma chance real de 80%).
    * A calibração com `method='isotonic'` ajusta essas probabilidades para serem **mais confiáveis e realistas**, o que pode ser crucial para a tomada de decisão baseada nas saídas do modelo.

* **Otimização do Limiar de Classificação**:
    * Em vez de usar o limiar padrão de 0.5 para converter probabilidades em classes, o código **testa múltiplos limiares** (0.3, 0.4, 0.5, 0.6, 0.7).
    * O limiar que maximiza a `balanced_accuracy` (neste caso, 0.6) é selecionado. Isso ajusta o ponto de decisão do modelo para otimizar o desempenho na métrica escolhida, sendo particularmente útil em cenários com classes desbalanceadas ou custos de erro assimétricos.

* **Engenharia de Features Cuidadosa**:
    * O mapeamento de variáveis categóricas ordinais para numéricas (`nivel_ensino_map`, `experiencia_map`, etc.) e a aplicação de one-hot encoding (`pd.get_dummies`) para variáveis nominais são etapas cruciais que preparam os dados adequadamente para o algoritmo Random Forest.

* **Avaliação Abrangente e Visualizações Detalhadas**:
    * O uso de múltiplas métricas (Acurácia, Acurácia Balanceada, F1-Score, Precisão, Recall, Matriz de Confusão, Curva ROC, Curva Precision-Recall) fornece uma visão completa do desempenho do modelo.
    * As visualizações ajudam a diagnosticar o comportamento do modelo e a identificar áreas de força e fraqueza.

A combinação desses fatores – as qualidades inerentes do Random Forest e as técnicas de modelagem e avaliação cuidadosamente implementadas – resulta em um modelo de classificação com bom desempenho e confiabilidade para o problema em questão.

---
## - Manejo de Features Categóricas e Numéricas:

| Atributo                                         | Nome                                      | Tipo         | Subtipo                             | Descrição                                                                                     | Relevância |
|--------------------------------------------------|-------------------------------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| P0                                               | id                 		       | Qualitativo  | Nominal                             | Para identificação da resposta                                    		            | Alta       |
| P1l                                              | Nível de ensino alcançado                 | Qualitativo  | Ordinal                             | Nível de ensino do respondente (graduação, mestrado, etc.)                                    | Alta       |
| P1m                                              | Área de formação acadêmica                | Qualitativo  | Nominal (Multivalorado)             | Área de formação acadêmica do respondente (TI, Economia, etc.)                                | Alta       |
| P2h                                              | Faixa salarial mensal                     | Qualitativo  | Ordinal                             | Faixa salarial mensal do respondente                                                          | Alta       |
| P2i                                              | Tempo de experiência na área de dados     | Quantitativo | Discreto                            | Tempo de experiência do respondente na área de dados (em anos)                                | Alta       |
| P2g                                              | Nível de senioridade                      | Qualitativo  | Ordinal                             | Nível de senioridade do respondente (Júnior, Pleno, Sênior)                                   | Alta       |
| P1b                                              | Gênero do profissional                    | Qualitativo  | Nominal (Multivalorado)             | Identidade de gênero do respondente                                                           | Alta       |
| P1c                                              | Cor/Raça/Etnia                            | Qualitativo  | Nominal (Multivalorado)             | Cor ou raça do respondente                                                                    | Alta       |
| P2b                                              | Setor de atuação da empresa               | Qualitativo  | Nominal (Multivalorado)             | Setor em que a empresa do respondente atua (Tecnologia, Finanças, etc.)                       | Alta       |
| P1i1                                             | UF onde mora                              | Qualitativo  | Nominal (Multivalorado)             | Unidade Federativa onde o respondente reside                                                  | Alta       |
| P2f                                              | Cargo atual                               | Qualitativo  | Nominal (Multivalorado)             | Cargo atual ocupado pelo respondente                                                          | Alta       |
| P2o6                                             | Oportunidade de aprendizado               | Qualitativo  | Nominal (Multivalorado)             | Valorização das oportunidades de aprendizado e crescimento profissional                       | Alta       |
| P2o10                                            | Reputação da empresa                      | Qualitativo  | Nominal (Multivalorado)             | Valorização da reputação que a empresa tem no mercado                                         | Alta       |

---

## *Processo de Amostragem de Dados1-1*
### 1. Divisão Inicial dos Dados em Treino e Teste  partitioning

* **Método**: A função `train_test_split` do Scikit-learn é utilizada para dividir o conjunto de dados completo (`X`, `y`) e os pesos das amostras (`sample_weights`) em conjuntos de treinamento e teste.
    ```python
    X_train, X_test, y_train, y_test, sample_weights_train, _ = train_test_split(
        X, y, sample_weights, test_size=0.3, random_state=42, stratify=y
    )
    ```
* **Proporção**: **70%** dos dados são alocados para o conjunto de **treinamento** (`X_train`, `y_train`, `sample_weights_train`) e **30%** para o conjunto de **teste** (`X_test`, `y_test`).
* **Estratificação**: O parâmetro `stratify=y` garante que a proporção das classes da variável alvo (`y`) seja mantida tanto no conjunto de treino quanto no de teste. Isso é crucial, especialmente porque o dataset possui classes desbalanceadas, assegurando que ambas as classes estejam representadas adequadamente em ambas as divisões.
* **Reprodutibilidade**: `random_state=42` é usado para que a divisão seja sempre a mesma em diferentes execuções do código, garantindo a reprodutibilidade dos resultados.
* **Pesos das Amostras (`sample_weights_train`)**: Os pesos calculados para lidar com o desbalanceamento de classes são divididos juntamente com os dados, e a porção de treino (`sample_weights_train`) é usada nas etapas subsequentes de treinamento e otimização.

---

### 2. Amostragem Interna do `RandomForestClassifier` (Bootstrap) 🌳

* **Bootstrap Aggregating (Bagging)**: O `RandomForestClassifier` é um ensemble de árvores de decisão. Por padrão (**`bootstrap=True`**, que é o default no Scikit-learn e não foi alterado no código), cada árvore na floresta é treinada em uma amostra diferente do conjunto de treinamento, gerada através de **amostragem com reposição** (bootstrap).
    * Isso significa que, para cada uma das `n_estimators` (100 árvores, conforme o melhor parâmetro encontrado), uma nova subamostra do `X_train` é criada, tendo o mesmo tamanho do `X_train` original, mas com algumas instâncias repetidas e outras ausentes.
* **`class_weight='balanced_subsample'`**: Este parâmetro, definido como o melhor pelo `GridSearchCV`, interage com o processo de bootstrap. Os pesos das classes são calculados para cada amostra de bootstrap individualmente, ajustando a importância das classes dentro de cada árvore de forma dinâmica. Isso ajuda a mitigar o desbalanceamento em cada árvore construída.
* **Amostragem de Features**: Além da amostragem de instâncias (linhas), o Random Forest também realiza uma amostragem de features (colunas) ao procurar a melhor divisão em cada nó de cada árvore. O número de features consideradas é tipicamente `sqrt(n_features)`.

---

### 3. Amostragem na Otimização de Hiperparâmetros (`GridSearchCV`) 🔄

* **Validação Cruzada (Cross-Validation)**: O `GridSearchCV` utiliza validação cruzada para avaliar o desempenho de diferentes combinações de hiperparâmetros. No código, `cv=5` foi especificado.
    * O conjunto de **treinamento** (`X_train`, `y_train`) é dividido em **5 folds (subconjuntos)** de tamanho aproximadamente igual.
    * Para cada combinação de hiperparâmetros, o modelo é treinado 5 vezes:
        * Em cada iteração, 4 folds são usados para treinar o modelo.
        * O fold restante (1 fold) é usado como conjunto de validação para avaliar o desempenho.
    * A métrica de desempenho (`balanced_accuracy`) é calculada para cada fold de validação, e a média dessas métricas é usada para classificar a combinação de hiperparâmetros.
* **Uso de `sample_weights_train`**: Os pesos das amostras (`sample_weights_train`) são passados para o método `fit` do `GridSearchCV`. Isso significa que, durante o treinamento de cada modelo dentro da validação cruzada, as amostras são ponderadas conforme definido, influenciando o aprendizado do modelo e o cálculo da métrica de avaliação em cada fold.

---

### 4. Amostragem na Calibração do Modelo (`CalibratedClassifierCV`) ⚖️

* **Validação Cruzada Interna**: O `CalibratedClassifierCV` também utiliza um esquema de validação cruzada para ajustar o calibrador (neste caso, usando o método `'isotonic'`). O parâmetro `cv=5` foi usado aqui também.
    * O conjunto de **treinamento** (`X_train`, `y_train`) é novamente dividido em 5 folds.
    * O `base_estimator` (o `best_rf_model` encontrado pelo GridSearchCV) é treinado em 4 folds, e as previsões de probabilidade são feitas no fold restante.
    * Este processo é repetido para todos os 5 folds, de modo que se obtêm previsões de probabilidade "out-of-fold" para todo o conjunto de treinamento.
    * O calibrador (regressor isotônico) é então treinado usando essas previsões "out-of-fold" como entrada e os verdadeiros rótulos `y_train` como saída.
    * Finalmente, o `base_estimator` é retreinado em todo o conjunto `X_train`, `y_train` (com `sample_weights_train`), e o calibrador treinado é aplicado a ele.
* **Uso de `sample_weights_train`**: Assim como no `GridSearchCV`, os `sample_weights_train` são passados para o método `fit` do `CalibratedClassifierCV`, garantindo que o processo de calibração também leve em consideração o desbalanceamento das classes através da ponderação das amostras.

Este conjunto de técnicas de amostragem e reponderação visa construir um modelo robusto, generalizável e que lide adequadamente com o desbalanceamento inerente aos dados.

---
## *Parâmetros utilizados1-1*
O modelo final é um `RandomForestClassifier` cujos hiperparâmetros foram otimizados usando `GridSearchCV`, e subsequentemente, este modelo otimizado foi calibrado usando `CalibratedClassifierCV`.

### 1. Hiperparâmetros Otimizados do `RandomForestClassifier` (Resultado do `GridSearchCV`)

Estes são os melhores parâmetros encontrados pelo `GridSearchCV` para o `RandomForestClassifier`, que é então usado como `base_estimator` para a calibração:

* **`class_weight`**: `'balanced_subsample'`
    * *Explicação*: Ajusta os pesos das classes de forma inversamente proporcional às suas frequências. A variante `'balanced_subsample'` calcula os pesos com base nas amostras de bootstrap para cada árvore.
* **`max_depth`**: `None`
    * *Explicação*: Indica que não há um limite predefinido para a profundidade máxima das árvores. As árvores são expandidas até que todas as folhas sejam puras ou até que todas as folhas contenham menos amostras do que `min_samples_split`.
* **`min_samples_leaf`**: `7`
    * *Explicação*: O número mínimo de amostras que um nó folha (nó terminal de uma árvore) deve ter. Um valor maior previne a criação de folhas muito específicas, ajudando a evitar overfitting.
* **`min_samples_split`**: `15`
    * *Explicação*: O número mínimo de amostras que um nó interno deve ter para poder ser dividido em novos nós. Similar ao `min_samples_leaf`, ajuda a controlar a complexidade da árvore e a evitar overfitting.
* **`n_estimators`**: `100`
    * *Explicação*: O número de árvores na floresta. Um valor maior geralmente leva a um modelo melhor e mais estável, mas também aumenta o tempo de treinamento.

**Parâmetros Adicionais (Fixos na Instanciação Base do `RandomForestClassifier` antes do `GridSearchCV`):**

* **`random_state`**: `42`
    * *Explicação*: Controla tanto a aleatoriedade do bootstrapping das amostras usadas ao construir as árvores (se `bootstrap=True`) quanto a amostragem das features a serem consideradas ao procurar a melhor divisão em cada nó. Usado para reprodutibilidade.
* **`n_jobs`**: `-1`
    * *Explicação*: Indica ao Scikit-learn para usar todos os processadores disponíveis para paralelizar o treinamento das árvores, acelerando o processo.

### 2. Parâmetros do `CalibratedClassifierCV`

O `best_rf_model` (com os hiperparâmetros acima) é então usado como o estimador base para a calibração:

* **`base_estimator`**: `best_rf_model` (o RandomForestClassifier com os parâmetros otimizados listados acima)
    * *Explicação*: O modelo cujas probabilidades serão calibradas.
* **`method`**: `'isotonic'`
    * *Explicação*: O método usado para a calibração. A regressão isotônica é um método não paramétrico que ajusta as probabilidades de forma a minimizar o erro quadrático médio, sob a restrição de que a função de calibração seja monotonicamente crescente. É geralmente mais flexível que o método 'sigmoid'.
* **`cv`**: `5`
    * *Explicação*: Determina a estratégia de validação cruzada. Aqui, 5 folds são usados. O modelo é treinado em 4 folds e calibrado no fold restante, e este processo é repetido para todos os folds. As previsões para cada fold são então usadas para treinar o calibrador final.

### 3. Parâmetros Utilizados na Chamada `.fit()` do `GridSearchCV` e `CalibratedClassifierCV`

* **`sample_weight`**: `sample_weights_train`
    * *Explicação*: Pesos aplicados a amostras individuais durante o treinamento. No código, esses pesos são calculados para dar maior importância às amostras da classe minoritária, ajudando a lidar com o desbalanceamento dos dados. Este parâmetro é passado tanto para o `.fit()` do `GridSearchCV` quanto do `CalibratedClassifierCV`.

---

# *Explicação do Código1-1*

## Análise Detalhada do Código Python: Modelo Random Forest para Previsão Salarial

### 1. Visão Geral do Código

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

-------------------------------------------

### Modelo 2 Análise de Disparidade Salarial de Profissionais de Dados no Brasil Utilizando o Arvore de decisão por classificação
### *Justificativa1-2*

O modelo escolhido foi o Gradient Boosting Classifier, uma técnica de ensemble baseada em árvores de decisão. A escolha se justifica porque o problema envolve múltiplas variáveis categóricas, relações não-lineares e a necessidade de interpretar a influência de fatores como formação acadêmica e experiência profissional sobre faixas salariais. O Gradient Boosting é reconhecido por sua eficácia em tarefas de classificação com dados tabulares e mistos, como é o caso do dataset analisado

### *Processo de Amostragem de Dados (Particionamento e Cross-Validation)1-2*

## Processo de Amostragem de Dados (Particionamento e Cross-Validation)

### 1. Particionamento dos Dados (Train-Test Split)

- **Divisão Estratificada:**  
  O conjunto de dados foi dividido em 70% para treinamento e 30% para teste, utilizando `train_test_split` com o parâmetro `stratify` baseado na variável alvo (faixa salarial agrupada).  
  Isso garante que a proporção de cada classe salarial seja mantida tanto no treino quanto no teste, evitando viés na avaliação do modelo.

- **Reprodutibilidade:**  
  O parâmetro `random_state=42` foi utilizado para garantir que a divisão dos dados seja sempre a mesma em diferentes execuções, permitindo reprodutibilidade dos resultados.

---

### 2. Cross-Validation Estratificada (Stratified K-Fold)

- **Validação Cruzada Estratificada:**  
  Durante a otimização de hiperparâmetros (`RandomizedSearchCV`), foi empregada a validação cruzada estratificada (`StratifiedKFold`) com 3 folds.  
  Em cada iteração, o conjunto de treino é novamente dividido em 3 subconjuntos, mantendo a proporção das classes em cada fold. O modelo é treinado em dois folds e avaliado no terceiro, repetindo o processo para todos os folds.

- **Vantagens da Estratificação:**  
  - Garante que todas as classes estejam representadas de forma proporcional em cada fold, o que é crucial para problemas com classes desbalanceadas.
  - Reduz o risco de variações indesejadas nos resultados devido à distribuição das classes.


3. **Estratificação:**  
   Mantém a distribuição das faixas salariais em todas as etapas, tanto no split inicial quanto na validação cruzada, assegurando comparabilidade e evitando viés de classe.


### **Capacidade de Capturar Interações Complexas**

Modelos de árvores, especialmente ensembles como o Gradient Boosting, capturam automaticamente interações complexas entre variáveis sem a necessidade de especificá-las manualmente. Isso é fundamental para o contexto, pois a relação entre formação acadêmica, experiência e salário não é linear nem independente: o impacto de um fator depende do outro. O modelo constrói sucessivas árvores que corrigem os erros das anteriores, ajustando-se a padrões e interações sutis presentes nos dados


### **Fornecimento de Importância das Features**

O Gradient Boosting permite extrair a importância relativa de cada variável para a predição, facilitando a interpretação dos fatores que mais influenciam o salário. O código calcula e reporta métricas como o coeficiente de Cramer's V para variáveis categóricas antes do treinamento, e a própria biblioteca do modelo possibilita gerar rankings de importância das features após o ajuste. Isso é essencial para análises orientadas a dados e para justificar decisões baseadas nos resultados do modelo


### **Robustez e Generalização**

O Gradient Boosting é robusto a outliers e a diferentes escalas de variáveis, além de apresentar boa capacidade de generalização quando parametrizado corretamente. O pipeline do código inclui validação cruzada estratificada, balanceamento de classes e busca de hiperparâmetros (RandomizedSearchCV), o que reduz o risco de overfitting e melhora a performance em dados não vistos. Isso garante que as conclusões sobre disparidade salarial sejam confiáveis e replicáveis em outros conjuntos de dados semelhantes

### **Bom Desempenho em Problemas de Classificação**

Modelos baseados em Gradient Boosting frequentemente apresentam desempenho superior em benchmarks de classificação com dados tabulares, especialmente quando há múltiplas classes e desbalanceamento, como no caso das faixas salariais. O modelo atingiu acurácia de 52,7% e acurácia balanceada de 40,1%, valores considerados competitivos para um problema de alta complexidade e múltiplas categorias. Além disso, o modelo lida bem com variáveis categóricas codificadas via OneHotEncoder e com a necessidade de interpretar resultados para diferentes grupos

### 

### *Parâmetros utilizados1-2*

## Parâmetros Utilizados no Modelo GradientBoostingClassifier

Abaixo estão os principais hiperparâmetros definidos após otimização com RandomizedSearchCV:

| Parâmetro           | Valor   | Descrição                                                                                           |
|---------------------|---------|-----------------------------------------------------------------------------------------------------|
| `subsample`         | 0.8     | Proporção de amostras usadas em cada árvore (80%). Ajuda a reduzir overfitting e aumenta robustez. |
| `n_estimators`      | 100     | Número de árvores no ensemble. Equilibra desempenho e custo computacional.                          |
| `min_samples_split` | 2       | Mínimo de amostras para dividir um nó. Permite divisões detalhadas, capturando padrões sutis.      |
| `min_samples_leaf`  | 2       | Mínimo de amostras em cada folha. Evita que folhas pequenas capturem apenas ruído.                 |
| `max_depth`         | 6       | Profundidade máxima das árvores. Limita a complexidade e controla overfitting.                     |
| `learning_rate`     | 0.2     | Taxa de aprendizado. Controla o quanto cada árvore corrige os erros das anteriores.                |

Esses parâmetros foram escolhidos para equilibrar desempenho, capacidade de generalização e evitar overfitting, garantindo que o modelo seja capaz de capturar padrões relevantes dos dados salariais sem se ajustar demais ao conjunto de treino.


### *Explicação do Código:1-2*

### 1. Contexto do Modelo

* **Problema:** O modelo visa classificar profissionais em diferentes **faixas salariais** (variável alvo) com base em um conjunto de características categóricas, como nível de ensino, área de formação, tempo de experiência, etc. Trata-se de um problema de **classificação multiclasse**.
* **Gradient Boosting Classifier:** É um algoritmo de aprendizado de máquina poderoso que pertence à família de modelos de *ensemble boosting*. Ele constrói modelos (geralmente árvores de decisão) de forma sequencial, onde cada novo modelo tenta corrigir os erros cometidos pelo modelo anterior. O resultado final é uma combinação ponderada de todos os modelos, o que geralmente leva a uma melhor performance e robustez em comparação com modelos individuais.

---

### 2. Análise do Código Bloco a Bloco

#### **Importações de Bibliotecas**

O código começa importando diversas bibliotecas essenciais para manipulação de dados, visualização, pré-processamento, modelagem e avaliação:

* `pandas` (pd): Para manipulação e análise de dados tabulares (DataFrames).
* `numpy` (np): Para operações numéricas eficientes, especialmente com arrays.
* `matplotlib.pyplot` (plt) e `seaborn` (sns): Para criação de gráficos e visualizações de dados.
* `sklearn.model_selection`: Contém funções para divisão de dados (`train_test_split`), otimização de hiperparâmetros (`GridSearchCV`, `RandomizedSearchCV`) e validação cruzada (`StratifiedKFold`).
* `sklearn.preprocessing`: Inclui ferramentas para transformação de features, como `LabelEncoder` (para codificar a variável alvo) e `OneHotEncoder` (para codificar variáveis categóricas).
* `sklearn.compose`: Permite a criação de transformadores complexos para diferentes tipos de colunas (`ColumnTransformer`).
* `sklearn.pipeline`: Embora `Pipeline` seja importado, não é explicitamente utilizado para construir o pipeline do modelo neste trecho final, mas o pré-processador (`ColumnTransformer`) age de forma similar para as features.
* `sklearn.metrics`: Fornece métricas para avaliação de modelos de classificação, como `classification_report`, `confusion_matrix`, `roc_curve`, `auc`, `accuracy_score`, `balanced_accuracy_score`.
* `sklearn.ensemble.GradientBoostingClassifier`: A implementação do modelo de Gradient Boosting.
* `collections.Counter`: Para contagem de itens (não utilizado explicitamente no fluxo principal, mas útil para EDA).
* `os`: Para interagir com o sistema operacional (ex: verificar existência de arquivos).
* `warnings`: Para controlar mensagens de aviso.
* `joblib`: Para salvar e carregar modelos treinados.
* `sklearn.inspection.permutation_importance`: Para avaliar a importância das features (importado, mas não usado no trecho final).
* `scipy.stats.chi2_contingency`: Para o teste qui-quadrado, usado no cálculo do V de Cramer.
* `matplotlib.cm`: Para mapas de cores (importado, mas não usado diretamente).
* `scipy.sparse`: Para manipulação de matrizes esparsas, que podem ser resultado do `OneHotEncoder`.
* `time`: Para medir o tempo de execução de trechos do código.

Configurações iniciais também são definidas para visualizações (`warnings.filterwarnings`, `plt.style.use`, `sns.set_palette`, `plt.rcParams`).

#### **Funções Auxiliares Definidas**

* `safe_execution(func, error_message, *args, **kwargs)`: Uma função wrapper para executar outras funções e capturar exceções, imprimindo uma mensagem de erro personalizada.
* `cramers_v(x, y)`: Calcula o coeficiente V de Cramer, uma medida de associação entre duas variáveis categóricas.
* `detect_outliers(df, column)`: Define uma função para detectar outliers usando o método do Intervalo Interquartil (IQR). Esta função é definida mas não explicitamente chamada para remover outliers do dataframe principal no fluxo de pré-processamento do modelo.
* `group_salary_ranges(df, salary_column)`: Agrupa faixas salariais originais em categorias mais amplas para reduzir o número de classes da variável alvo.

#### **Carregamento e Exploração Inicial dos Dados**

* **Carregamento:** Os dados são carregados de um arquivo CSV (`dados_limpos.csv`). O código tenta primeiro um caminho (`/kaggle/input/dataset-clean/dados_limpos.csv`) e, se não encontrado, tenta um caminho local (`dados_limpos.csv`).
    ```python
    file_path = '/kaggle/input/dataset-clean/dados_limpos.csv'
    if not os.path.exists(file_path):
        file_path = 'dados_limpos.csv'
    df = pd.read_csv(file_path)
    ```
* **Informações Básicas:** São impressas informações sobre o dataset:
    * Número de registros e colunas (`df.shape`).
    * Lista das colunas (`df.columns.tolist()`).
* **Exploração da Variável Alvo Original:** A distribuição da coluna original `Faixa salarial mensal` é calculada e impressa usando `value_counts()`.
* **Visualização da Distribuição Salarial Original:** Um gráfico de barras (`sns.countplot`) é gerado para mostrar a distribuição das faixas salariais originais e salvo como `distribuicao_faixas_salariais_originais.png`.

#### **Pré-processamento dos Dados**

* **Agrupamento de Faixas Salariais:** A função `group_salary_ranges` é chamada para criar uma nova coluna `Faixa salarial agrupada`, que será a variável alvo do modelo. Isso é feito para simplificar o problema, reduzindo a granularidade e o desbalanceamento entre as classes.
    ```python
    df = group_salary_ranges(df, 'Faixa salarial mensal')
    ```
* **Visualização da Distribuição Salarial Agrupada:** Um novo gráfico de barras é gerado e salvo (`distribuicao_faixas_salariais_agrupadas.png`) para mostrar a distribuição das novas faixas salariais agrupadas.
* **Análise de Correlação (V de Cramer):** O coeficiente V de Cramer é calculado entre as variáveis categóricas selecionadas (`categorical_cols`) e a nova variável alvo `Faixa salarial agrupada`. Isso ajuda a entender a força da relação entre as features e o target. Os resultados são impressos e visualizados em um gráfico de barras salvo como `correlacao_variaveis_faixa_salarial.png`.
    ```python
    categorical_cols = ['Nível de ensino alcançado', 'Área de formação acadêmica', ...]
    # ...
    corr_with_target[col] = cramers_v(df[col], df['Faixa salarial agrupada'])
    ```
* **Seleção de Features e Target:**
    * **Features (X):** As colunas definidas em `categorical_cols` são selecionadas como variáveis preditoras.
        ```python
        features = df[categorical_cols]
        ```
    * **Target (y):** A coluna `Faixa salarial agrupada` é definida como a variável alvo.
        ```python
        target = df['Faixa salarial agrupada']
        ```
* **Codificação da Variável Alvo:** A variável alvo (`target`) é categórica e é transformada em valores numéricos usando `LabelEncoder`. Um mapeamento dos códigos para os rótulos originais é criado e impresso.
    ```python
    le_target = LabelEncoder()
    y = le_target.fit_transform(target)
    target_mapping = dict(zip(range(len(le_target.classes_)), le_target.classes_))
    ```
* **Tratamento de Variáveis Categóricas (Features):** As features categóricas são transformadas usando `OneHotEncoder` dentro de um `ColumnTransformer`. O `handle_unknown='ignore'` garante que, se novas categorias aparecerem no conjunto de teste, elas não causarão erro e serão codificadas como todas as colunas do OHE zeradas para aquela feature.
    ```python
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])
    ```
* **Normalização/Padronização:** Não há etapas explícitas de normalização (ex: MinMaxScaler) ou padronização (ex: StandardScaler) aplicadas às features numéricas resultantes do One-Hot Encoding. Para árvores de decisão e ensembles baseados em árvores como Gradient Boosting, a normalização de features não é estritamente necessária, pois esses modelos são menos sensíveis à escala das features.

#### **Divisão dos Dados**

* Os dados (features e target codificado) são divididos em conjuntos de **treino** e **teste** na proporção 70/30. A função `train_test_split` é utilizada com `stratify=y` para garantir que a proporção das classes da variável alvo seja mantida em ambos os conjuntos, o que é importante para dados desbalanceados. `random_state=42` garante a reprodutibilidade da divisão.
    ```python
    X_train, X_test, y_train, y_test = train_test_split(
        features, y, test_size=0.3, random_state=42, stratify=y
    )
    ```
* O pré-processador (OneHotEncoder) é ajustado (`fit_transform`) **apenas** nos dados de treino (`X_train`) e depois aplicado (`transform`) nos dados de teste (`X_test`). Isso evita o vazamento de dados (data leakage) do conjunto de teste para o processo de treinamento.
    ```python
    X_train_transformed = preprocessor.fit_transform(X_train)
    # ... mais tarde ...
    X_test_transformed = preprocessor.transform(X_test)
    ```

#### **Balanceamento de Classes (Oversampling)**

* Como as classes da variável alvo podem ser desbalanceadas (algumas faixas salariais podem ter muito menos amostras que outras), uma técnica de **oversampling manual** é aplicada ao conjunto de **treinamento**.
* O código primeiro converte `X_train_transformed` (que pode ser uma matriz esparsa) para uma matriz densa.
* Para cada classe minoritária no conjunto de treinamento, amostras são reamostradas **com reposição** (`replace=True`) usando `sklearn.utils.resample` até que o número de amostras naquela classe atinja o tamanho da classe majoritária.
* Isso resulta em `X_train_resampled` e `y_train_resampled` onde todas as classes têm o mesmo número de instâncias no conjunto de treino.
    ```python
    # ... (código para encontrar majority_size e iterar pelas classes)
    resampled_features, resampled_targets = resample(
        class_features, class_targets,
        replace=True,
        n_samples=n_samples, # n_samples é majority_size
        random_state=42
    )
    # ...
    X_train_resampled = np.vstack(X_resampled_list)
    y_train_resampled = np.concatenate(y_resampled_list)
    ```
* A distribuição das classes após o balanceamento é impressa.

#### **Criação e Treinamento do Modelo (Gradient Boosting)**

* **Instanciação do Modelo:** Um `GradientBoostingClassifier` é instanciado.
    ```python
    gb_clf = GradientBoostingClassifier(random_state=42)
    ```
* **Otimização de Hiperparâmetros:** O código oferece três opções para definir/otimizar os hiperparâmetros do modelo:
    1.  `GridSearchCV` com um grid reduzido de parâmetros.
    2.  `RandomizedSearchCV` com uma distribuição de parâmetros (opção escolhida automaticamente no script).
    3.  Usar um conjunto pré-definido de parâmetros otimizados.

    A **Opção 2 (RandomizedSearchCV)** é executada por padrão:
    * `param_dist`: Um dicionário define o espaço de busca dos hiperparâmetros (`n_estimators`, `learning_rate`, `max_depth`, `min_samples_split`, `min_samples_leaf`, `subsample`).
    * `cv = StratifiedKFold(n_splits=3, ...)`: Validação cruzada estratificada com 3 folds é usada para avaliar cada combinação de hiperparâmetros.
    * `RandomizedSearchCV` explora `n_iter=20` combinações aleatórias de hiperparâmetros do `param_dist`.
    * `scoring='balanced_accuracy'`: A métrica usada para selecionar o melhor modelo é a acurácia balanceada, que é mais apropriada para dados desbalanceados (embora o oversampling já tenha sido feito, é uma boa prática).
    * O modelo é treinado (`.fit()`) nos dados de treino balanceados (`X_train_resampled`, `y_train_resampled`).
        ```python
        random_search = RandomizedSearchCV(
            gb_clf, param_dist, n_iter=20, cv=cv,
            scoring='balanced_accuracy', n_jobs=-1, verbose=1, random_state=42
        )
        random_search.fit(X_train_resampled, y_train_resampled)
        best_gb = random_search.best_estimator_
        ```
    * Os melhores hiperparâmetros encontrados e o tempo de execução são impressos.

* **Hiperparâmetros Selecionados (Exemplo da Saída):**
    Da saída fornecida, os melhores parâmetros encontrados pelo `RandomizedSearchCV` foram:
    `{'subsample': 0.8, 'n_estimators': 100, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_depth': 6, 'learning_rate': 0.2}`
    Estes são:
    * `subsample`: Fração de amostras usadas para ajustar as árvores individuais.
    * `n_estimators`: Número de árvores (estágios de boosting) a serem construídas.
    * `min_samples_split`: Número mínimo de amostras necessárias para dividir um nó interno.
    * `min_samples_leaf`: Número mínimo de amostras necessárias em um nó folha.
    * `max_depth`: Profundidade máxima das árvores de decisão individuais.
    * `learning_rate`: Taxa de aprendizado, encolhe a contribuição de cada árvore.

* **Treinamento do Melhor Modelo:** O `best_gb` (o `GradientBoostingClassifier` com os melhores hiperparâmetros encontrados) já foi treinado pelo `RandomizedSearchCV` nos dados de treino balanceados. Se a opção de parâmetros pré-definidos fosse escolhida, o `.fit()` seria chamado explicitamente.

#### **Realização de Previsões**

* Os dados de teste (`X_test`) são transformados usando o pré-processador já ajustado (`preprocessor.transform(X_test)`). Se a saída for uma matriz esparsa, ela é convertida para densa.
* As previsões são feitas no conjunto de teste transformado (`X_test_transformed`) usando o modelo treinado (`best_gb.predict()`).
    ```python
    X_test_transformed = preprocessor.transform(X_test)
    if scipy.sparse.issparse(X_test_transformed):
        X_test_transformed = X_test_transformed.toarray()
    y_pred = best_gb.predict(X_test_transformed)
    ```

#### **Avaliação do Modelo**

* **Métricas de Desempenho:**
    * **Acurácia:** (`accuracy_score`) A proporção de previsões corretas.
    * **Acurácia Balanceada:** (`balanced_accuracy_score`) A média das taxas de recall obtidas em cada classe. É útil para alvos desbalanceados, pois a acurácia simples pode ser enganosa.
    * **Relatório de Classificação:** (`classification_report`) Fornece as principais métricas de classificação (precision, recall, F1-score, support) para cada classe. `zero_division=0` evita avisos caso alguma métrica resulte em divisão por zero.
    * **Matriz de Confusão:** (`confusion_matrix`) Mostra o número de previsões corretas e incorretas para cada classe. É visualizada usando `sns.heatmap` e salva como `matriz_confusao.png`.
* **Interpretação (baseada na saída fornecida):**
    * Acurácia no teste: `0.5273` (52.73%)
    * Acurácia Balanceada no teste: `0.4015` (40.15%)
    * O relatório de classificação mostra que o modelo tem desempenho variado entre as classes. Por exemplo:
        * A classe "R$ 8.001/mês a R$ 16.000/mês" tem o melhor F1-score (0.66), com recall de 0.72.
        * A classe "Acima de R$ 30.000/mês" tem o pior desempenho (F1-score de 0.11).
    * A Acurácia Balanceada ser consideravelmente menor que a Acurácia simples sugere que o modelo ainda tem dificuldades com as classes minoritárias, mesmo após o oversampling (o desbalanceamento original no conjunto de teste ainda afeta a avaliação).

#### **Visualização da Árvore**

* Para um `GradientBoostingClassifier`, visualizar uma única árvore não é tão informativo quanto para um `DecisionTreeClassifier`, pois o modelo é um ensemble de muitas árvores. O código não tenta visualizar as árvores individuais do ensemble.
* A visualização mais relevante para o desempenho do modelo fornecida é a **matriz de confusão**.

#### **Salvando o Modelo e Componentes**

* O melhor modelo treinado (`best_gb`), o pré-processador (`preprocessor`) e o mapeamento do target (`target_mapping`) são salvos em arquivos `.pkl` usando `joblib.dump`. Isso permite que sejam recarregados e reutilizados posteriormente sem a necessidade de retreinar.
    ```python
    joblib.dump(best_gb, 'modelo_gradient_boosting_disparidade_salarial_otimizado.pkl')
    joblib.dump(preprocessor, 'preprocessador_otimizado.pkl')
    joblib.dump(target_mapping, 'target_mapping.pkl')
    ```

---

### 3. Estrutura da Explicação

Esta análise seguiu a estrutura solicitada, utilizando Markdown, cabeçalhos, listas e blocos de código para clareza.

---

### 4. Tom e Nível de Detalhe

A explicação buscou ser clara, tecnicamente precisa e detalhada, explicando o propósito de cada etapa do código.

---

### 5. Conclusão

* **Resumo:** O notebook desenvolve um modelo `GradientBoostingClassifier` para prever faixas salariais. As etapas incluem carregamento de dados, extenso pré-processamento (agrupamento de faixas salariais, codificação de variáveis categóricas, balanceamento de classes por oversampling), otimização de hiperparâmetros com `RandomizedSearchCV`, treinamento, avaliação e salvamento do modelo.
* **Possíveis Melhorias e Próximos Passos:**
    * **Engenharia de Features:** Explorar a criação de novas features a partir das existentes.
    * **Tratamento de Outliers:** A função `detect_outliers` foi definida, mas não aplicada. Avaliar o impacto da remoção ou tratamento de outliers nas features numéricas (se houvesse, ou se fossem criadas).
    * **Técnicas de Balanceamento Alternativas:** Experimentar outras técnicas como SMOTE (Synthetic Minority Over-sampling Technique) ou undersampling da classe majoritária, e avaliar seu impacto.
    * **Seleção de Features:** Utilizar técnicas como `permutation_importance` (que foi importada) ou RFE (Recursive Feature Elimination) para selecionar as features mais relevantes e potencialmente simplificar o modelo.
    * **Outros Modelos:** Comparar o desempenho do Gradient Boosting com outros algoritmos de classificação (ex: Random Forest, SVM, Redes Neurais).
    * **Análise de Erros:** Investigar mais a fundo por que o modelo tem dificuldade com certas classes (ex: "Acima de R$ 30.000/mês") e se há padrões nos erros.
    * **Validação Cruzada Mais Robusta:** Embora 3 folds tenham sido usados para otimização, uma validação cruzada mais extensa (e.g., 5 ou 10 folds) no processo de avaliação final do modelo escolhido poderia fornecer uma estimativa mais robusta do desempenho.
    * **Interpretabilidade do Modelo:** Usar ferramentas como SHAP (SHapley Additive exPlanations) para entender melhor as previsões do modelo Gradient Boosting e a importância das features de forma mais granular.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Indução de modelos

# Modelos 2º pergunta orietada a dados

## Random Forest Regressor
**Este modelo foi utilizado para prever a faixa salarial média (R$/mês) de profissionais da área de dados no Brasil, a partir da junção de duas bases:**

*State of Data BR 2023 (Kaggle): informações profissionais.*

*MICRODADOS_ED_SUP_IES_2023 (MEC): características regionais da educação.*

## 2º Pergunta orientada a dados:
* Qual é a relação entre o tempo de experiência na área de dados, o nível de senioridade e a faixa salarial dos profissionais no Brasil?
  
## Objetivo

Investigar as relações entre os principais fatores da carreira de profissionais de dados no Brasil e suas faixas salariais, utilizando dados da base survey_cleaned.csv. Esta análise busca entender como variáveis como experiência, senioridade, formação acadêmica, estado (UF) e habilidades técnicas (ex: Python, SQL) influenciam a remuneração.

## Justificativa

A escolha desta pergunta se justifica pela necessidade de entender quais variáveis impactam mais os salários na área de dados. Além disso, identificar o peso de fatores individuais (como experiência e nível) versus regionais (como estrutura educacional) pode orientar políticas educacionais e decisões de carreira.

## Processo de Amostragem de Dados (Particionamento e Cross-Validation)

| **Etapa**            | **Descrição**                                                                                                                 |
| :------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **Particionamento**  | Divisão dos dados em **treinamento** e **teste** utilizando `train_test_split`, com `random_state=42` para reprodutibilidade. |
| **Treinamento**      | O modelo foi treinado com a amostra de treinamento (`X_train`, `y_train`).                                                    |
| **Validação**        | Avaliação realizada na amostra de teste (`X_test`, `y_test`) com métricas como MAE e R².                                      |
| **Cross-Validation** | Não foi implementada neste código, mas poderia ser adicionada para uma avaliação mais robusta da generalização do modelo.     |

## Parâmetros utilizados

```
RandomForestRegressor(
    max_depth=None,
    max_features='sqrt',
    min_samples_leaf=2,
    min_samples_split=5,
    n_estimators=100,
    random_state=42
)
```

| **Parâmetro**         | **Descrição**                                                                               |
| :-------------------- | :------------------------------------------------------------------------------------------ |
| `max_depth=None`      | Sem limitação de profundidade, permitindo que as árvores cresçam até parar automaticamente. |
| `max_features='sqrt'` | Seleção de número de atributos igual à raiz quadrada do total, para cada divisão.           |
| `min_samples_leaf=2`  | Mínimo de 2 amostras por folha, evitando árvores muito complexas.                           |
| `min_samples_split=5` | Mínimo de 5 amostras para dividir um nó, reduzindo overfitting.                             |
| `n_estimators=100`    | Uso de 100 árvores na floresta.                                                             |
| `random_state=42`     | Semente fixa para garantir reprodutibilidade.                                               |


## Explicação do Código:

| **Etapa**                            | **Descrição**                                                                                                             |
| :----------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| **Importação de bibliotecas**        | Importa pandas, numpy, ferramentas de pré-processamento, modelo RandomForest, particionamento e métricas.                 |
| **Leitura dos dados**                | `pd.read_csv` lê os dois datasets: State of Data (profissionais) e MEC (educação).                                        |
| **Pré-processamento State of Data**  | Seleção e renomeação de colunas, mapeamento numérico para experiência e salário, codificação do nível com `LabelEncoder`. |
| **Agregação dos dados educacionais** | Agrupamento por região, somando docentes, técnicos, mestres e contando IES.                                               |
| **Merge das bases**                  | `pd.merge` junta a base profissional com a educacional, cruzando pela região.                                             |
| **Preparação para modelagem**        | Seleção das variáveis explicativas e variável alvo (`salario_num`).                                                       |
| **Particionamento**                  | Separação em treino e teste com `train_test_split`.                                                                       |
| **Treinamento do modelo**            | Criação e ajuste do `RandomForestRegressor` com hiperparâmetros definidos.                                                |
| **Avaliação**                        | Cálculo do **MAE** e do **R²** com `mean_absolute_error` e `r2_score`.                                                    |
| **Importância das variáveis**        | Extração das importâncias com `model.feature_importances_` e exibição percentual.                                         |


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Indução de modelos

# Modelos 3º pergunta orietada a dados 

### Arvore de decisao LightGBM (Optuna)

---
## **1 JUSTIFICATIVA E OBJETIVO (Modelo 3.1)**

O objetivo deste modelo é classificar a faixa salarial de indivíduos em duas categorias: "Salário Baixo" e "Salário Alto". A transição de uma classificação multiclasse (3 faixas) para uma binária visa simplificar o problema e potencialmente melhorar a distinção entre os grupos salariais, buscando um equilíbrio na distribuição das amostras entre as classes definidas por um ponto de corte específico. A última execução utilizou um ponto de corte fixo (presumivelmente R$7.500,00 com base nos resultados) para a variável `salary_numeric_lower_bound` para realizar essa divisão.

**O projeto busca responder à seguinte pergunta orientada a dados:** *Como fatores como formalidade no emprego, características demográficas e regionais interagem entre si e com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?.*

---
## **2 METODOLOGIA (Modelo 3.1)**

### **2.1 Processo de Amostragem de Dados (Particionamento e Cross-Validation)**

O processo de amostragem e validação do modelo é crucial para garantir sua generalização e evitar overfitting. As seguintes etapas são empregadas no código:

#### **2.1.1 Particionamento inicial (Treino e Teste Principal)**

* **Método**: `train_test_split` da biblioteca `sklearn.model_selection`.
* **Divisão**: O conjunto de dados processado (`X_initial`, `y_full`) é dividido em:
    * Conjunto de Treinamento para Optuna e RFECV (`X_train_optuna`, `y_train_optuna`): 75% dos dados.
    * Conjunto de Teste Final (`X_test`, `y_test`): 25% dos dados.
* **Parâmetros Utilizados**:
    * `test_size=0.25`: Reserva 25% dos dados para o conjunto de teste final, que não é utilizado durante o treinamento ou otimização de hiperparâmetros.
    * `random_state=42`: Garante a reprodutibilidade da divisão. O mesmo estado aleatório resultará sempre na mesma divisão dos dados.
    * `stratify=y_full`: Realiza uma divisão estratificada. Isso significa que a proporção das classes da variável alvo (`y_full`, que contém "Salário Baixo" e "Salário Alto" codificados) é mantida tanto no conjunto de treino quanto no de teste. Isso é especialmente importante para dados desbalanceados ou quando se quer garantir que ambas as classes estejam representadas adequadamente em ambas as partições.

#### **2.1.2 Validação cruzada estratificada para RFECV (Recursive Feature Elimination with Cross-Validation)**

* **Método**: `StratifiedKFold` da `sklearn.model_selection`, utilizado dentro do `RFECV`.
* **Objetivo**: Selecionar o subconjunto ótimo de features de forma robusta, avaliando o desempenho do modelo com diferentes combinações de features em múltiplas dobras (folds) do conjunto de treinamento.
* **Parâmetros Utilizados no `StratifiedKFold` para `RFECV`**:
    * `n_splits=rfecv_folds` (padrão `3` no código): O conjunto de treinamento (`X_train_optuna_for_rfecv`, `y_train_optuna`) é dividido em 3 folds.
    * `shuffle=True`: Embaralha os dados antes de dividir em folds.
    * `random_state=42`: Garante a reprodutibilidade do embaralhamento e da divisão em folds.
* **Funcionamento do `RFECV`**: Treina o estimador (`lgb.LGBMClassifier`) recursivamente, removendo features e avaliando o desempenho (definido por `rfecv_scoring`, padrão `'accuracy'`) através da validação cruzada estratificada. Isso ajuda a encontrar o número de features que maximiza a métrica de scoring.

#### **2.1.3 Validação cruzada estratificada para otimização de hiperparâmetros com Optuna**

* **Método**: `StratifiedKFold` utilizado dentro da função `objective_optuna_cv`.
* **Objetivo**: Avaliar o desempenho de diferentes combinações de hiperparâmetros do `lgb.LGBMClassifier` de forma robusta, treinando e validando em múltiplas dobras do conjunto de treinamento selecionado pelo RFECV (`X_train_optuna_selected`, `y_train_optuna`).
* **Parâmetros Utilizados no `StratifiedKFold` para `Optuna`**:
    * `n_splits=n_cv_folds_optuna`: O número de folds é determinado dinamicamente, sendo o mínimo entre 5 e a contagem da classe minoritária no conjunto `y_train_optuna` (desde que essa contagem seja >= 2). Se a contagem da classe minoritária for muito pequena, é usado um fallback para validação simples (holdout). Na sua última execução com classes mais equilibradas, provavelmente usou 5 folds.
    * `shuffle=True`: Embaralha os dados.
    * `random_state=trial.number`: O estado aleatório é vinculado ao número do "trial" do Optuna, promovendo diversidade nas divisões entre diferentes trials.
* **Funcionamento**: Para cada "trial" do Optuna (combinação de hiperparâmetros), o modelo é treinado e avaliado `n_cv_folds_optuna` vezes. A métrica de desempenho (acurácia média dos folds) é retornada ao Optuna, que busca maximizá-la.

#### **2.1.4 Partição interna para Early Stopping no treinamento final**

* **Método**: `train_test_split` para criar um conjunto de validação interna.
* **Divisão**: O conjunto `X_train_optuna_selected` (que é 75% do total) é novamente dividido:
    * Conjunto de Treinamento Final (`X_train_final`, `y_train_final`): 80% de `X_train_optuna_selected`.
    * Conjunto de Validação Interna (`X_val_internal`, `y_val_internal`): 20% de `X_train_optuna_selected`.
* **Objetivo**: Este conjunto de validação interna é usado para o mecanismo de `early_stopping` do LightGBM durante o treinamento do modelo final com os melhores hiperparâmetros encontrados pelo Optuna. O `early_stopping` monitora a métrica (`binary_logloss` para o caso binário) no conjunto de validação interna e para o treinamento quando essa métrica não melhora por um número definido de rodadas (`early_stopping_rounds=25`), ajudando a evitar overfitting no conjunto de treinamento final.
* **Parâmetros Utilizados**:
    * `test_size=0.20`
    * `random_state=42`
    * `stratify=y_train_optuna`

#### **2.1.5 Justificativa das escolhas de amostragem**

* **Divisão Treino/Teste Principal**: Essencial para avaliar o desempenho final do modelo em dados não vistos. A proporção 75/25 é comum.
* **Estratificação**: Crucial para problemas de classificação, especialmente com classes desbalanceadas (embora o objetivo seja reduzir o desbalanceamento), para garantir que as proporções das classes sejam mantidas nas divisões, levando a estimativas de desempenho mais confiáveis.
* **Validação Cruzada (RFECV e Optuna)**: Reduz a variância da estimativa de desempenho e torna a seleção de features e hiperparâmetros mais robusta, diminuindo a chance de escolhas baseadas em uma divisão particular dos dados. `StratifiedKFold` é usado para manter a proporção das classes em cada fold.
* **Conjunto de Validação Interna para Early Stopping**: Permite que o modelo pare de treinar no momento ótimo, evitando o overfitting aos dados de `X_train_final`, usando `X_val_internal` como um proxy para dados não vistos durante essa fase.

### **2.2 Análise de Correlação das Features Iniciais com o Alvo**

Antes da seleção de features pelo RFECV, foi realizada uma análise de correlação das features iniciais (após limpeza e transformações como UF para Região) com a variável alvo (`TARGET_SALARIO_CODIFICADO`). As features consideradas nesta fase foram: `P1_a_1` (Faixa Etária), `P1_b` (Gênero), `P1_l` (Nível de Ensino), `P2_i` (Tempo de Experiência), `P2_g_Nivel` (Nível de Senioridade), `P2_f_Cargo_Atual` (Cargo Atual), e `Regiao_Mapeada`.

**Suposição da Codificação do Alvo para Interpretação da Correlação:** Para a análise abaixo, assume-se que "Salário Baixo" foi codificado com um valor numérico MAIOR e "Salário Alto" com um valor numérico MENOR (ex: Salário Alto -> 0, Salário Baixo -> 1). Se a codificação for inversa, a interpretação dos sinais de correlação de Pearson e Spearman também se inverte. A Correlação de Distância (dcor) mede apenas a força da dependência (0 a 1), não a direção.

**Tabela 1 –** Resumo das correlações com `TARGET_SALARIO_CODIFICADO` (Dados Completos Processados)

| Feature            | Pearson | Spearman | dcor (Força) | Interpretação Consolidada (assumindo Salário Baixo como valor maior) |
| :----------------- | :------ | :------- | :----------- | :----------------------------------------------------------------- |
| `P2_i`               | -0.52   | -0.57    | 0.53         | Forte dependência. Maior experiência tende a salário mais alto.    |
| `P2_g_Nivel`         | -0.44   | -0.44    | 0.45         | Moderada a forte dependência. Maior senioridade tende a salário mais alto. |
| `P2_f_Cargo_Atual` | -0.32   | -0.31    | 0.33         | Moderada dependência. "Melhores" cargos tendem a salário mais alto. |
| `P1_a_1`             | -0.31   | -0.33    | 0.30         | Moderada dependência. Faixas etárias maiores tendem a salário mais alto. |
| `P1_l`               | -0.18   | -0.22    | 0.20         | Baixa a moderada dependência. Maior nível de ensino tende a salário mais alto. |
| `P1_b`               | -0.07   | -0.07    | 0.08         | Dependência muito fraca.                                           |
| `Regiao_Mapeada`     | -0.00   | 0.01     | 0.05         | Dependência muito fraca ou inexistente.                            |

**Observações da Análise de Correlação:**
* **Consistência**: As correlações mostraram-se bastante consistentes entre os dados completos, treino e teste.
* **Pearson vs. Spearman vs. dcor**:
    * Para `P2_i`, Spearman e dcor mostraram valores ligeiramente maiores (em magnitude para Spearman) que Pearson, sugerindo que a relação, embora forte, pode não ser perfeitamente linear, mas é fortemente monotônica e com alta dependência geral.
    * Para `P2_g_Nivel`, todas as três métricas foram muito próximas, indicando que a relação é razoavelmente bem capturada por uma aproximação linear/monotônica.
    * Para as demais features, as magnitudes foram geralmente consistentes entre os métodos, com `dcor` reforçando a força da dependência detectada.
* **Features mais Correlacionadas**: `P2_i` (Tempo de Experiência) e `P2_g_Nivel` (Nível de Senioridade) destacaram-se como as mais fortemente correlacionadas com a faixa salarial.

**(Gráficos Mais Relevantes - Mapas de Calor para Dados Completos Processados)**

Para uma visualização completa das inter-relações entre todas as features iniciais e a variável alvo, os seguintes mapas de calor (gerados a partir dos dados completos processados, antes da divisão treino/teste e RFECV) são os mais relevantes. Recomenda-se visualizá-los em um ambiente gráfico.

1.  **Mapa de Calor da Correlação de Pearson:**
    ![Image](https://github.com/user-attachments/assets/ef5f53bd-a116-4c75-a6c0-e5de9fc3c1af)
    * Descrição: Este gráfico exibe a força e a direção das relações *lineares* entre cada par de variáveis. Cores mais intensas (vermelho para positivo, azul para negativo) indicam correlações lineares mais fortes.

2.  **Mapa de Calor da Correlação de Spearman:**
    ![Image](https://github.com/user-attachments/assets/f2da6d6a-1dbb-4dd1-8089-4ee9b385ec99)
    * Descrição: Este gráfico mostra a força e a direção das relações *monotônicas* (onde as variáveis tendem a se mover juntas, mas não necessariamente a uma taxa constante). É útil para identificar tendências consistentes que podem não ser estritamente lineares.

3.  **Mapa de Calor da Correlação de Distância (dcor):**
    ![Image](https://github.com/user-attachments/assets/1aaf66f2-fbe0-49b1-92a3-f8ac9902724c)
    * Descrição: Este gráfico indica a força da dependência (linear ou não linear) entre os pares de variáveis, com valores variando de 0 (independência) a 1 (dependência perfeita). Cores mais claras (amarelo, no esquema 'viridis') indicam maior dependência. Ele não mostra a direção da relação.

### **2.3 Parâmetros e Ferramentas Utilizados**

#### **2.3.1 Criação da variável alvo (`target_col_agrupada_name`)**

* **`salary_group_labels = ["Salário Baixo", "Salário Alto"]`**: Define os nomes das duas categorias da variável alvo.
* **`point_of_cut_fixed`**: Um valor monetário específico (ex: `7500.0` na última execução que produziu o suporte 622/567) usado para dividir `salary_numeric_lower_bound`. Salários `<= point_of_cut_fixed` são "Salário Baixo/Médios", e `> point_of_cut_fixed` são "Salário Alto". **Este é o parâmetro chave que você tem ajustado para controlar a distribuição das classes.**
* O gráfico abaixo mostra a distribuição da faixa salarial, onde é notável que uma divisão de `<= point_of_cut_fixed` (Salários Baixos/Medios) e `> point_of_cut_fixed` (salários Altos), produziram um suporte 622/567.
    ![Image](https://github.com/user-attachments/assets/cc8fdd29-49bd-4b07-82a3-803c81bcb2a7)
* **`pd.cut(..., include_lowest=True, duplicates='drop')`**: Usado para realizar a divisão com base no `point_of_cut_fixed`.

#### **2.3.2 Utilização das variáveis preditivas**

**Tabela 2 –** Descrição das variáveis preditivas utilizadas

| Atributo | Código de Referência | Tipo | Subtipo | Descrição | Relevância |
|---|---|---|---|---|---|
| Faixa etária | P1a1 | Qualitativo | Ordinal | Faixa etária do respondente | Alta |
| Gênero | P1b | Qualitativo | Nominal (Multivalorado) | Identidade de gênero do respondente | Alta |
| Nivel de ensino alcançado | P1l | Qualitativo | Ordinal | Nível de ensino do respondente (graduação, mestrado, etc.) | Alta |
| Faixa salarial mensal | P2h | Qualitativo | Ordinal | Faixa salarial mensal do respondente | Alta |
| Tempo de experiência na área de dados | P2i | Quantitativo | Discreto | Tempo de experiência do respondente na área de dados (em anos) | Alta |
| UF onde mora | P1i1 | Qualitativo | Nominal (Multivalorado) | Unidade Federativa onde o respondente reside | Alta |
| Cargo atual | P2f | Qualitativo | Nominal (Multivalorado) | Cargo atual ocupado pelo respondente | Alta |
| Nível de senioridade | P2g | Qualitativo | Ordinal | Nível de senioridade do respondente (Júnior, Pleno, Sênior) | Alta |

#### **2.3.3 Parâmetros do `RFECV`**

* `estimator=lgb.LGBMClassifier(random_state=42, n_jobs=-1, verbose=-1)`: Modelo base para a seleção de features.
* `step=rfecv_step` (padrão `1`): Número de features a serem removidas em cada iteração.
* `cv=StratifiedKFold(n_splits=rfecv_folds, ...)` (padrão `rfecv_folds=3`): Estratégia de validação cruzada.
* `scoring=rfecv_scoring` (padrão `'accuracy'`): Métrica para avaliar o subconjunto de features.
* `min_features_to_select=1`: Número mínimo de features a serem selecionadas.

#### **2.3.4 Parâmetros da otimização com `Optuna`**

* `n_trials=n_optuna_trials` (padrão `100`): Número de combinações de hiperparâmetros a serem testadas.
* `timeout=optuna_timeout` (padrão `1800` segundos): Tempo máximo para a otimização.
* `direction='maximize'`: O Optuna tenta maximizar a métrica retornada por `objective_optuna_cv` (que é a acurácia).
* **Espaço de Busca dos Hiperparâmetros (exemplos da sua última execução bem-sucedida):**
    * `n_estimators`: 1100 (valor encontrado)
    * `learning_rate`: 0.06509... (valor encontrado)
    * `num_leaves`: 80 (valor encontrado)
    * `max_depth`: 12 (valor encontrado)
    * `min_child_samples`: 25 (valor encontrado)
    * `subsample`: 0.5 (valor encontrado)
    * `colsample_bytree`: 0.6 (valor encontrado)
    * `reg_alpha`: 1.567... (valor encontrado)
    * `reg_lambda`: 14.655... (valor encontrado)
    * `min_split_gain`: 0.385... (valor encontrado)
    * `min_child_weight`: 0.139... (valor encontrado)
* **Adaptação para Classificação Binária em Optuna e Modelo Final**:
    * `objective`: Definido como `'binary'` (pois `is_binary_classification` é `True`).
    * `metric`: Definido como `'binary_logloss'` para avaliação interna e early stopping.
    * `num_class`: Omitido para classificação binária no LightGBM (ou definido como 1 implicitamente).

#### **2.3.5 Parâmetros do treinamento do modelo final (`best_lgbm`)**

* Usa os `best_params_optuna` encontrados.
* `early_stopping(callbacks=[lgb.early_stopping(25, verbose=False)])`: Para o treinamento se a métrica no conjunto de validação interna (`X_val_internal`) não melhorar por 25 rodadas. O número de árvores final foi 105 na sua última execução.
---
## **3 FLUXO DE EXECUÇÃO DO CÓDIGO (Modelo 3.1)**

### **3.1 Carregamento e preparação inicial dos dados**

* Leitura do arquivo Excel (`Main_database (2).xlsx`).
* Limpeza dos nomes das colunas para remover caracteres especiais e espaços (função `clean_col_name`).
* Mapeamento heurístico de colunas importantes (faixa salarial original, experiência, senioridade, etc.) para nomes padronizados internos (armazenados em `col_mapping`).

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import RFECV
import lightgbm as lgb
import optuna
import warnings
import re
import pickle
import time
import traceback

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=optuna.exceptions.ExperimentalWarning)

# Certifique-se de que a pasta para salvar visualizações existe
os.makedirs('visualizacoes_classificacao_salario_v7_rfecv', exist_ok=True)
```
### **3.2 Engenharia da variável alvo (`target_col_agrupada_name`)**

* A coluna da faixa salarial original (ex: `P2_h`) é processada para extrair um valor numérico (`salary_numeric_lower_bound`) usando `extract_salary_lower_bound`.
* **Divisão em Duas Categorias**: Um **ponto de corte fixo** (`point_of_cut_fixed`), como R$7.500,00, é usado para dividir `salary_numeric_lower_bound` em "Salário Baixo" e "Salário Alto" usando `pd.cut`. Esta etapa inclui lógica para lidar com casos onde o ponto de corte é extremo e um fallback para `pd.qcut` (divisão pela mediana) se o `pd.cut` falhar.
* A distribuição de `salary_numeric_lower_bound` é plotada para auxiliar na escolha/ajuste do `point_of_cut_fixed`.
* Amostras com valor nulo na nova variável alvo são removidas.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
# ... (Código para extração de salário e criação da variável alvo com pd.cut) ...
# Esta seção contém a lógica detalhada para definir as faixas salariais
# com base no 'point_of_cut_fixed' e tratar casos extremos.
```
### **3.3 Preparação das features (`X_initial`) e codificação do alvo (`y_full`)**

* As features relevantes (idade, gênero, UF, ensino, cargo, senioridade, experiência) são selecionadas.
* A coluna 'UF' é transformada na feature 'Regiao_Mapeada'.
* A variável alvo (`target_col_agrupado_name`) é codificada numericamente (0 e 1) usando `LabelEncoder`.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
# ... (Após a engenharia da variável alvo e remoção de NaNs na coluna alvo) ...

# Seleciona as colunas de features iniciais com base no mapeamento
feature_cols_to_use_initial = [
    col_mapping[col_internal] for col_internal in required_cols_internal_for_features 
    if col_internal in col_mapping and col_mapping[col_internal] in df_main_processed.columns
]
X_initial = df_main_processed[feature_cols_to_use_initial].copy()

# Mapeia UF para Região e remove a coluna original de UF
uf_col_original_name_mapped = col_mapping.get("uf_mora_P1i1")
if uf_col_original_name_mapped and uf_col_original_name_mapped in X_initial.columns:
    X_initial['Regiao_Mapeada'] = map_uf_to_region(X_initial[uf_col_original_name_mapped])
    X_initial.drop(columns=[uf_col_original_name_mapped], inplace=True)

# Codifica a variável alvo
global le, is_binary_classification
le = LabelEncoder()
y_full = pd.Series(le.fit_transform(df_main_processed[target_col_agrupada_name]), index=df_main_processed.index)

is_binary_classification = len(le.classes_) == 2
```
### **3.4 Pré-processamento das features**

* **Valores Ausentes**: Features numéricas são imputadas com a mediana; categóricas com uma string constante ("Missing_Val_Cat").
* **Outliers**: Linhas com outliers em features numéricas (critério 1.5*IQR) são removidas.
* **Codificação e Escalonamento**: Features categóricas são convertidas para o tipo `category`; numéricas são padronizadas com `StandardScaler`.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
# ... (Código para tratamento de valores ausentes, remoção de outliers, 
#      e escalonamento de features numéricas com StandardScaler) ...
```
### **3.5 Divisão treino-teste principal**

* Os dados processados (`X_initial`, `y_full`) são divididos em 75% para treino/otimização (`X_train_optuna`, `y_train_optuna`) e 25% para teste final (`X_test`, `y_test`), de forma estratificada.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
X_train_optuna, X_test, y_train_optuna, y_test = train_test_split(
    X_initial, y_full, 
    test_size=0.25, 
    random_state=42, 
    stratify=y_full
)
```
### **3.6 Seleção de features com RFECV**

* `RFECV` é aplicado usando `lgb.LGBMClassifier` e `StratifiedKFold` (3 folds) para encontrar o subconjunto ótimo de features baseado na acurácia.
* `X_train_optuna` e `X_test` são atualizados para conter apenas as features selecionadas.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
# ... (Código de inicialização e ajuste do RFECV) ...
rfecv_selector.fit(X_train_optuna_for_rfecv, y_train_optuna)
selected_features_names = X_train_optuna.columns[rfecv_selector.support_].tolist()
X_train_optuna_selected = X_train_optuna[selected_features_names].copy()
X_test_selected = X_test[selected_features_names].copy()
```
### **3.7 Otimização de hiperparâmetros com Optuna**

* A função `objective_optuna_cv` avalia cada conjunto de hiperparâmetros sugeridos pelo Optuna, usando `StratifiedKFold` (padrão 5 folds).
* O Optuna executa `n_optuna_trials` (padrão 100) para encontrar os hiperparâmetros que maximizam a acurácia média da validação cruzada.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
study = optuna.create_study(direction='maximize')
study.optimize(
    lambda trial: objective_optuna_cv(
        trial,
        X_train_optuna_selected,
        y_train_optuna,
        n_cv_splits_internal=n_cv_folds_optuna
    ),
    n_trials=n_optuna_trials,
    timeout=optuna_timeout
)
best_params_optuna = study.best_trial.params
```
### **3.8 Treinamento do modelo final**

* O conjunto `X_train_optuna_selected` é dividido em treino final (80%) e validação interna (20%).
* O modelo `lgb.LGBMClassifier` é treinado com os melhores hiperparâmetros e `early_stopping` para evitar overfitting.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
X_train_final, X_val_internal, y_train_final, y_val_internal = train_test_split(
    X_train_optuna_selected, y_train_optuna,
    test_size=0.20,
    random_state=42,
    stratify=y_train_optuna
)

best_lgbm = lgb.LGBMClassifier(objective='binary', metric='binary_logloss', **best_params_optuna)

best_lgbm.fit(
    X_train_final, y_train_final,
    eval_set=[(X_val_internal, y_val_internal)],
    callbacks=[lgb.early_stopping(25, verbose=False)]
)
```
### **3.9 Avaliação do modelo final**

* O modelo treinado é usado para fazer previsões no conjunto de teste (`X_test_selected`).
* São calculadas e exibidas métricas: acurácia, relatório de classificação, matriz de confusão e ROC AUC.
* Gráficos de matriz de confusão e importância de features são gerados.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
y_pred_test = best_lgbm.predict(X_test_selected)
y_pred_proba_all_classes_test = best_lgbm.predict_proba(X_test_selected)

accuracy_test = accuracy_score(y_test, y_pred_test)
report_str_test = classification_report(y_test, y_pred_test, target_names=le.classes_)
roc_auc_test = roc_auc_score(y_test, y_pred_proba_all_classes_test[:, 1])

# ... (plotagem de gráficos) ...
```
### **3.10 Retorno de resultados**

* A função principal retorna um dicionário contendo as métricas de performance, parâmetros utilizados e caminhos para os artefatos salvos.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
return {
    'accuracy_test': accuracy_test,
    'roc_auc_test': roc_auc_test,
    'best_params': best_params_optuna,
    'model_object_path': model_filename_pkl,
    # ... (outras métricas) ...
}
```
> Este fluxo demonstra uma abordagem robusta para modelagem, incluindo pré-processamento cuidadoso, seleção de features, otimização de hiperparâmetros e avaliação rigorosa usando múltiplas técnicas de particionamento de dados.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Indução de modelos

## Modelos 3º pergunta orietada a dados

### Rede Neural com Embeddings e Otimização via Ray Tune (RNA v2) 

---
## **1 JUSTIFICATIVA E OBJETIVO (modelo 3.2)** 

O objetivo deste modelo é classificar a faixa salarial de indivíduos em duas categorias: "Salário Baixo" e "Salário Alto", utilizando uma abordagem de rede neural artificial (RNA). A intenção é explorar se uma arquitetura de RNA, com capacidade de aprender interações complexas e representações ricas para features categóricas (via embeddings), pode oferecer um desempenho comparável ou superior aos modelos baseados em árvores (como o LightGBM anteriormente explorado) para a mesma pergunta orientada a dados.

A classificação binária ("Salário Baixo" vs. "Salário Alto") visa simplificar o problema e potencialmente melhorar a distinção entre os grupos salariais. O modelo busca um equilíbrio na distribuição das amostras entre as classes definidas por um ponto de corte específico. Na última execução do modelo de referência (LightGBM), um ponto de corte fixo de R$ 7.500,00 foi utilizado para a variável `salary_numeric_lower_bound` para realizar essa divisão. Este mesmo ponto de corte é mantido para a RNA.

## **2 PROCESSO DE AMOSTRAGEM DE DADOS (modelo 3.2)**

O processo de amostragem e validação do modelo de rede neural é crucial para garantir sua generalização e evitar overfitting.

### **2.1 Particionamento inicial (Treino HPO e Teste Final)**

* **Método**: `train_test_split` da biblioteca `sklearn.model_selection`.
* **Divisão**: O conjunto de dados processado (`X_initial_nn`, `y_full_nn` - que já passou por limpeza, tratamento de outliers e mapeamento de features) é dividido em:
    * Conjunto de Treinamento para HPO e posterior treino final (`X_train_nn_full`, `y_train_nn_full`): 75% dos dados.
    * Conjunto de Teste Final (`X_test_nn_full`, `y_test_nn_full`): 25% dos dados.
* **Parâmetros Utilizados**:
    * `test_size=0.25`: Reserva 25% dos dados para o conjunto de teste final.
    * `random_state=42`: Garante a reprodutibilidade da divisão.
    * `stratify=y_full_nn`: Realiza uma divisão estratificada, mantendo a proporção das classes da variável alvo em ambas as partições.

### **2.2 Particionamento interno para otimização de hiperparâmetros com Ray Tune (Keras)**

* **Método**: `train_test_split` para criar um conjunto de validação interna a partir do `X_train_nn_full`.
* **Divisão**: O `X_train_nn_full` (75% do total) é novamente dividido:
    * Conjunto de Treinamento Interno para HPO (`X_train_hpo_nn_list_for_tune`, `y_train_hpo_nn_arr_for_tune`): 80% de `X_train_nn_full`.
    * Conjunto de Validação Interno para HPO (`X_val_hpo_nn_list_for_tune`, `y_val_hpo_nn_arr_for_tune`): 20% de `X_train_nn_full`.
* **Objetivo**: Este conjunto de validação interno é usado por cada *trial* do Ray Tune para avaliar o desempenho do modelo Keras com uma dada combinação de hiperparâmetros. O callback `EarlyStopping` do Keras monitora a `val_accuracy` neste conjunto, e o `ReportCheckpointCallback` reporta essa métrica ao Ray Tune.

### **2.3 Particionamento interno para Early Stopping no treinamento final da RNA**

* **Método**: `train_test_split` para criar um conjunto de validação interna a partir do `X_train_nn_full` (que corresponde a `X_train_nn_inputs_final_list` e `y_train_nn_final_arr` no código da RNA v2).
* **Divisão**: O conjunto `X_train_nn_full` (75% do total) é dividido novamente para o treinamento do *modelo final* com os melhores hiperparâmetros:
    * Conjunto de Treinamento Final Efetivo (`X_final_train_list`, `y_final_train_arr`): 85% de `X_train_nn_full`.
    * Conjunto de Validação para Early Stopping Final (`X_final_val_list`, `y_final_val_arr`): 15% de `X_train_nn_full`.
* **Objetivo**: Este conjunto de validação é usado para o `EarlyStopping` do Keras durante o treinamento do modelo RNA final com os melhores hiperparâmetros encontrados pelo Ray Tune, ajudando a evitar overfitting no conjunto de treinamento final.

### **2.4 Justificativa das escolhas de amostragem**

* **Divisão Treino/Teste Principal**: Essencial para avaliar o desempenho final do modelo em dados completamente não vistos durante o treinamento ou HPO. A proporção 75/25 é comum.
* **Estratificação**: Crucial para problemas de classificação binária para garantir que as proporções das classes sejam mantidas nas divisões, levando a estimativas de desempenho e HPO mais confiáveis.
* **Conjunto de Validação Interna para HPO**: Permite que o Ray Tune avalie cada combinação de hiperparâmetros de forma justa, usando um subconjunto dos dados de treino para validação, com `EarlyStopping` para otimizar o tempo de cada trial.
* **Conjunto de Validação Interna para Treinamento Final**: Permite que o modelo final pare de treinar no momento ótimo, evitando o overfitting aos dados de treinamento final.

## **3 PARÂMETROS UTILIZADOS (PRINCIPAIS) - (modelo 3.2)**

### **3.1 Criação da variável alvo (`target_col_agrupada_name`)**

* **`salary_group_labels = ["Salário Baixo", "Salário Alto"]`**: Define os nomes das duas categorias da variável alvo.
* **`point_of_cut_fixed = 7500.0`**: Valor monetário usado para dividir `salary_numeric_lower_bound`. Salários `<= 7500.0` são "Salário Baixo", e `> 7500.0` são "Salário Alto". Este ponto de corte produziu um suporte de 2268 para "Salário Baixo" e 2485 para "Salário Alto" no dataset processado.
* A coluna alvo é codificada numericamente usando `LabelEncoder` (ex: "Salário Alto" -> 0, "Salário Baixo" -> 1).

### **3.2 Features preditivas utilizadas e pré-processamento para RNA**

Para o modelo de Rede Neural v2, utilizou-se diretamente o conjunto de 7 features iniciais relevantes, sem a etapa de RFECV baseada em LightGBM, para permitir que a RNA aprendesse as relações e a importância das features diretamente. As features são:

**Tabela 1 – Features preditivas utilizadas no modelo RNA v2**
| Atributo | Código de Referência Original | Tipo | Subtipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| Faixa etária | P1_a_1 | Qualitativo | Ordinal (tratada como cat.) | Faixa etária do respondente |
| Gênero | P1_b | Qualitativo | Nominal (tratada como cat.) | Identidade de gênero do respondente |
| Nível de ensino alcançado | P1_l | Qualitativo | Ordinal (tratada como cat.) | Nível de ensino do respondente (graduação, mestrado, etc.) |
| Tempo de experiência na área de dados | P2_i | Quantitativo | Discreto | Tempo de experiência do respondente na área de dados (em anos) |
| Nível de senioridade | P2_g | Qualitativo | Ordinal (tratada como cat.) | Nível de senioridade do respondente (Júnior, Pleno, Sênior) |
| Cargo atual | P2_f | Qualitativo | Nominal (tratada como cat.) | Cargo atual ocupado pelo respondente |
| Região Mapeada | Derivada de P1_i_1 | Qualitativo | Nominal (tratada como cat.) | Região do Brasil onde o respondente reside |

**Pré-processamento para RNA:**
* **Features Numéricas (`P2_i` - experiência):**
    * Valores ausentes imputados com a mediana.
    * Outliers identificados usando 1.5\*IQR e as linhas contendo outliers são removidas do conjunto de dados antes do split principal.
    * Escalonadas usando `StandardScaler`.
* **Features Categóricas (todas as outras listadas acima):**
    * Valores ausentes preenchidos com a string "Missing_Val_Cat_NN".
    * Codificadas usando `LabelEncoder` individualmente para cada feature.
    * Para o conjunto de teste, categorias não vistas durante o ajuste do `LabelEncoder` (no treino) são mapeadas para um novo índice numérico (índice "UNK" - desconhecido).
    * Utilizadas como entrada para camadas de `Embedding` na rede neural. A `input_dim` de cada camada de Embedding é a cardinalidade da feature + 1 (para o índice UNK).

### **3.3 Arquitetura da Rede Neural (Keras - `create_keras_model_v2`)**

* **Múltiplos Inputs:** Um input para cada feature categórica (para as camadas de Embedding) e um input para todas as features numéricas concatenadas.
* **Camadas de Embedding:** Para cada feature categórica, uma camada `Embedding` transforma o índice numérico em um vetor denso. A dimensão de saída de cada embedding (`output_dim`) é um hiperparâmetro otimizado pelo Ray Tune. Regularização L2 é aplicada às embeddings.
* **Concatenação:** Os outputs achatados (`Flatten`) de todas as camadas de Embedding são concatenados com as features numéricas (já escalonadas).
* **Camadas Densas (MLP):**
    * A primeira camada densa possui um número de unidades e regularização L2 otimizados via Ray Tune, seguida por `BatchNormalization`, ativação `ReLU` e `Dropout`.
    * O modelo pode ter uma segunda camada densa opcional (controlada pelo hiperparâmetro `num_hidden_layers`), também com unidades, L2, `BatchNormalization`, `ReLU` e `Dropout` otimizados.
* **Camada de Saída:** Uma camada `Dense` com 1 neurônio e ativação `sigmoid` para classificação binária.
* **Compilação:**
    * Otimizador: O tipo de otimizador (Adam, Nadam, AdamW) e a taxa de aprendizado são hiperparâmetros.
    * Função de Perda: `binary_crossentropy`.
    * Métricas: `accuracy`.

### **3.4 Otimização de hiperparâmetros com Ray Tune (Keras)**

* **`n_ray_tune_samples_nn`**: Número de combinações de hiperparâmetros a serem testadas (ex: 75 na última execução).
* **`ray_tune_timeout_nn`**: Tempo máximo para a otimização (ex: 5400 segundos).
* **`objective_ray_tune_keras_v2`**: Função que treina e avalia um modelo Keras para uma dada configuração de hiperparâmetros, utilizando um split de validação interno e `EarlyStopping`. Reporta `val_accuracy` (como `val_accuracy_tune`) para o Ray Tune.
* **`TuneReportCallback`**: Utilizado para reportar métricas do Keras para o Ray Tune durante o treinamento de cada trial.
* **`ASHAScheduler`**: Utilizado para interromper trials menos promissores mais cedo. Configurado com `metric='val_accuracy_tune'` e `mode='max'`.
* **`HyperOptSearch`**: Utilizado como algoritmo de busca para encontrar os melhores hiperparâmetros, também configurado com `metric='val_accuracy_tune'` e `mode='max'`.
* **Espaço de Busca dos Hiperparâmetros (otimizados pelo Ray Tune):**
    * `dense_units_1`, `dense_units_2` (unidades nas camadas densas)
    * `dropout_1`, `dropout_2` (taxas de dropout)
    * `learning_rate_nn` (taxa de aprendizado)
    * `batch_size`
    * `epochs` (número máximo de épocas, controlado por EarlyStopping)
    * `num_hidden_layers` (1 ou 2 camadas densas ocultas)
    * `early_stopping_patience`
    * `l2_strength_embedding`, `l2_strength_dense` (força da regularização L2)
    * `optimizer` (tipo de otimizador: adam, nadam, adamw)
    * `weight_decay` (para AdamW)
    * `reduce_lr_patience`, `reduce_lr_factor` (para o callback `ReduceLROnPlateau`)
    * `emb_dim_{feature_name}` (dimensão de saída para cada camada de Embedding)
* **Melhores Hiperparâmetros Encontrados (exemplo da última execução):**
    * `dense_units_1`: 64, `dense_units_2`: 128 (mas `num_hidden_layers`: 1, então `dense_units_2` não foi usada)
    * `learning_rate_nn`: 0.000236...
    * `batch_size`: 32
    * `num_hidden_layers`: 1
    * Outros parâmetros específicos para dropout, L2, e dimensões de embedding também foram definidos.

### **3.5 Treinamento do modelo final (RNA v2)**

* Utiliza os melhores hiperparâmetros encontrados pelo Ray Tune.
* O modelo Keras é treinado no conjunto de treino HPO completo (`X_train_nn_full`, que corresponde a 75% dos dados após tratamento de outliers), com um novo split de validação (15% de `X_train_nn_full`) para `EarlyStopping` (com paciência aumentada e `ReduceLROnPlateau`).
* O número de épocas efetivas é determinado pelo `EarlyStopping`. Na última execução, o modelo final parou na época 40 (restaurando pesos da época 20).

## **4 RESULTADOS DA AVALIAÇÃO (RNA V2) - (modelo 3.2)**

A avaliação foi realizada no conjunto de teste (25% dos dados), com base em um exemplo da última execução.

* **Melhor Acurácia na Validação (HPO da RNA):** 0.8345
* **Acurácia no Teste:** 0.8377
* **F1-Score (Ponderado) no Teste:** 0.8377
* **ROC AUC no Teste:** 0.9263
* **Relatório de Classificação (Teste):**
    * Salário Alto: precision 0.85, recall 0.84, f1-score 0.84
    * Salário Baixo: precision 0.83, recall 0.84, f1-score 0.83

## **5 EXPLICAÇÃO DO CÓDIGO (FLUXO PRINCIPAL PARA RNA V2) -  (modelo 3.2)**

A pergunta orientada a dados é: **Como fatores como formalidade no emprego, características demográficas e regionais se interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?**

O fluxo de execução do código para o modelo de Rede Neural (RNA v2) é:

1.  **Carregamento e Preparação Inicial dos Dados**:
    * Leitura do arquivo Excel.
    * Limpeza dos nomes das colunas.
    * Mapeamento de colunas importantes para nomes padronizados.
2.  **Engenharia da Variável Alvo**:
    * Extração do `salary_numeric_lower_bound`.
    * Divisão em "Salário Baixo" e "Salário Alto" usando o ponto de corte fixo de R$ 7.500,00.
    * Codificação da variável alvo com `LabelEncoder`.
3.  **Preparação das Features Iniciais para RNA**:
    * Seleção das 7 features relevantes (faixa etária, gênero, UF transformado em Região, ensino, cargo, senioridade, experiência).
    * Tratamento de valores ausentes e outliers nas features numéricas (experiência).
4.  **Divisão Treino-Teste Principal**:
    * Os dados processados (`X_initial_nn`, `y_full_nn`) são divididos em 75% para treino/HPO (`X_train_nn_full`) e 25% para teste final (`X_test_nn_full`).
5.  **Pré-processamento Específico para RNA (em `X_train_nn_full` e `X_test_nn_full`):**
    * Features numéricas são escalonadas com `StandardScaler`.
    * Features categóricas são tratadas para NaNs e codificadas com `LabelEncoder` (individualmente). Um índice UNK é reservado para categorias não vistas no teste. São coletadas informações para as camadas de `Embedding` (cardinalidade, dimensão de output).
    * Os inputs são formatados como uma lista de arrays para o modelo Keras.
6.  **Otimização de Hiperparâmetros com Ray Tune**:
    * Um subconjunto de `X_train_nn_full` é usado para criar dados de treino e validação internos para cada trial da HPO.
    * A função `objective_ray_tune_keras_v2` define como cada trial (combinação de hiperparâmetros da RNA) é treinado (com `EarlyStopping` e `ReduceLROnPlateau`) e avaliado (pela `val_accuracy`).
    * `TuneReportCallback` envia métricas para o Ray Tune.
    * `tune.run` executa a busca usando `ASHAScheduler` e `HyperOptSearch`.
7.  **Treinamento do Modelo RNA Final**:
    * O modelo Keras é instanciado com os melhores hiperparâmetros encontrados.
    * É treinado no conjunto `X_train_nn_full` (usando 85% para treino efetivo e 15% para validação do `EarlyStopping` e `ReduceLROnPlateau`).
8.  **Avaliação do Modelo RNA Final**:
    * Previsões são feitas no conjunto de teste (`X_test_nn_full`).
    * Métricas (acurácia, F1, ROC AUC, relatório de classificação, matriz de confusão) são calculadas e exibidas.
9.  **Salvamento de Resultados e Modelo**:
    * Resultados detalhados são salvos em arquivo de texto.
    * O modelo Keras treinado e os objetos de pré-processamento (scalers, encoders, informações de embedding) são salvos em arquivos (`.keras` e `.pkl`).

> Este processo visa construir um modelo de rede neural otimizado e avaliado de forma robusta, fornecendo insights sobre os fatores que determinam as faixas salariais, focando na capacidade da RNA de aprender representações e interações complexas.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Resultados


*   [1. RESULTADOS OBTIDOS COM OS MODELOS 1º PERGUNTA ORIETADA A DADOS](#resultados-obtidos-com-os-modelos-1º-pergunta-orietada-a-dados)
*   [1.1 Resultados obtidos com o modelo 1 da 1º pergunta orietada a dados](#resultados-obtidos-com-o-modelo-1-da-1º-pergunta-orietada-a-dados)
	*   [1.1.1 top3_features](#top3_features)
	*   [1.1.2 precision_recall_curve](#precision_recall_curve)
 	*   [1.1.3 matriz_confusao_otimizada](#matriz_confusao_otimizada) 
	*   [1.1.4 interacao_formacao_experiencia](#interacao_formacao_experiencia)
	*   [1.1.5 importancia_features_top20](#importancia_features_top20)
	*   [1.1.6 importancia_features_grupo_senioridade](#importancia_features_grupo_senioridade)
	*   [1.1.7 importancia_features_grupo_formacao](#importancia_features_grupo_formacao)
	*   [1.1.8 importancia_features_grupo_experiencia](#importancia_features_grupo_experiencia)
	*   [1.1.9 importancia_features_grupo_Área de formação acadêmica](#importancia_features_grupo_área-de-formação-acadêmica)
	*   [1.1.10 distribuicao_probabilidades](#distribuicao_probabilidades)
	*   [1.1.11 dispersao_top2_features](#dispersao_top2_features)
	*   [1.1.12 curva_roc_otimizada](#curva_roc_otimizada)
	*   [1.1.13 arvore_exemplo_simplificada](#arvore_exemplo_simplificada)
	*   [1.1.14 arvore_exemplo_melhorada](#arvore_exemplo_melhorada)

*   [1.2 Resultados obtidos com o modelo 2 da 1º pergunta orietada a dados](#resultados-obtidos-com-o-modelo-2-da-1º-pergunta-orietada-a-dados) 
	*   [1.2.1 matriz_confusao 1-2](#matriz_confusao_1_2)
	*   [1.2.2 distribuicao_faixas_salariais_originais 1-2](#distribuicao_faixas_salariais_originais_1_2)
 	*   [1.2.3 distribuicao_faixas_salariais_agrupadas 1-2](#distribuicao_faixas_salariais_agrupadas_1_2) 
	*   [1.2.4 correlacao_variaveis_faixa_salarial 1-2](#correlacao_variaveis_faixa_salarial_1_2)



*   [2. RESULTADOS OBTIDOS COM OS MODELOS 2º PERGUNTA ORIETADA A DADOS](#resultados-obtidos-com-os-modelos-2º-pergunta-orietada-a-dados)

*   [3. RESULTADOS OBTIDOS COM OS MODELOS 3º PERGUNTA ORIETADA A DADOS](#resultados-obtidos-com-os-modelos-3º-pergunta-orietada-a-dados)
	* [3.1 Árvore de Decisão LightGBM (Modelo 3.1)](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#arv%C3%B3re-de-deci%C3%A7%C3%A3o-ligthgbm-modelo-31)
		* [3.1.1. RESULTADOS E DISCUSSÃO](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#1-resultados-e-discuss%C3%A3o)
		* [3.1.2. CONFIGURAÇÃO DO MODELO](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#2-configura%C3%A7%C3%A3o-do-modelo)
		* [3.1.3. ANÁLISE DOS RESULTADOS E INSIGHTS](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#3-an%C3%A1lise-dos-resultados-e-insights)
		* [3.1.4. CONSIDERAÇÕES FINAIS](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#4-considera%C3%A7%C3%B5es-finais)
	* [3.2 Rede Neural com Embeddings e Otimização via Ray Tune (RNA v2) - (Modelo 3.2)](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#rede-neural-com-embeddings-e-otimiza%C3%A7%C3%A3o-via-ray-tune-rna-v2---modelo-32)
   		* [3.2.1. RESULTADOS E DISCUSSÃO](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#1-resultados-e-discuss%C3%A3o-do-modelo-de-rede-neural-v8)
		* [3.2.2. Gráficos de correlaçao](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#2-an%C3%A1lise-explorat%C3%B3ria-e-correla%C3%A7%C3%A3o-de-atributos)
		* [3.2.3. OTIMIZAÇÃO E TREINAMENTO DO MODELO](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#3-otimiza%C3%A7%C3%A3o-e-treinamento-do-modelo)
		* [3.2.4. Avaliaçao](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#4-avalia%C3%A7%C3%A3o-do-modelo-final)
  		* [3.2.5. CONSIDERAÇÕES FINAIS](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo2-disparidade-salarial-2025-1/blob/main/docs/report.md#5-considera%C3%A7%C3%B5es-finais)

# Resultados obtidos com os Modelos 1º pergunta orietada a dados

## Resultados obtidos com o modelo 1 da 1º pergunta orietada a dados


| Classe          | Precisão | Recall | F1-Score | Suporte |
|-----------------|----------|--------|----------|---------|
| Salário Baixo/Médio    | 0.84     | 0.84   | 0.84     | 568     |
| Salário Alto | 0.79     | 0.78   | 0.78     | 422     |
| accuracy |  |  | **0.82** | **990** |
| macro avg | **0.81** | **0.81** | **0.81** | **990** |
| weighted avg | **0.81** | **0.82** | **0.82** | **990** |

- Acurácia do Modelo: 0.82
- Acurácia do Modelo no Conjunto de Treinamento: 0.8328 (83.28%)
- Acurácia do Modelo no Conjunto de Teste: 0.8152 (81.52%)
- Diferença de Acurácia (Treino - Teste):  0.0177 (1.77%)

## Métricas de Desempenho:

Com o limiar de classificação otimizado em 0.6, o modelo apresentou os seguintes resultados principais no conjunto de teste:

* **Acurácia Geral:** `0.82` (ou 82%)
* **Acurácia Balanceada:** `0.8106` (ou 81.06%)
* **F1-Score (Macro Avg):** `0.81`
* **F1-Score (Weighted Avg):** `0.82`

**Métricas por Classe (com limiar otimizado de 0.6):**

* **Salário Baixo/Médio (Classe 0):**
    * Precisão: `0.84`
    * Recall: `0.84`
    * F1-Score: `0.84`
    * Suporte (Número de amostras reais): 568
* **Salário Alto (Classe 1):**
    * Precisão: `0.79`
    * Recall: `0.78`
    * F1-Score: `0.78`
    * Suporte (Número de amostras reais): 422

**Matriz de Confusão (com limiar otimizado de 0.6):**
* Verdadeiros Negativos (TN - Previu Baixo/Médio, Real Baixo/Médio): 478
* Falsos Positivos (FP - Previu Alto, Real Baixo/Médio): 90
* Falsos Negativos (FN - Previu Baixo/Médio, Real Alto): 93
* Verdadeiros Positivos (TP - Previu Alto, Real Alto): 329

**Explicação das Métricas:**

* **Acurácia Geral:** Percentual de previsões corretas que o modelo fez no total. Neste caso, 82% das vezes o modelo acertou se um profissional teria um salário "Alto" ou "Baixo/Médio".
* **Acurácia Balanceada:** Média da proporção de acertos para cada classe individualmente. É uma métrica importante quando as classes têm tamanhos diferentes (desbalanceadas), como neste caso (57.35% Salário Baixo/Médio vs. 42.65% Salário Alto). Um valor de `0.8106` indica um bom equilíbrio no desempenho entre as classes.
* **Precisão (por classe):**
    * Para "Salário Baixo/Médio" (`0.84`): Das vezes que o modelo previu que um profissional teria um salário "Baixo/Médio", ele acertou em 84% dos casos.
    * Para "Salário Alto" (`0.79`): Das vezes que o modelo previu que um profissional teria um salário "Alto", ele acertou em 79% dos casos.
* **Recall (Sensibilidade, por classe):**
    * Para "Salário Baixo/Médio" (`0.84`): Dos profissionais que realmente têm salário "Baixo/Médio", o modelo conseguiu identificar corretamente 84% deles.
    * Para "Salário Alto" (`0.78`): Dos profissionais que realmente têm salário "Alto", o modelo conseguiu identificar corretamente 78% deles.
* **F1-Score (por classe e médias):** Média harmônica entre precisão e recall. É útil para ter uma única medida que resume a performance em ambas as métricas. Valores mais altos são melhores.
    * Um F1-Score de `0.84` para "Salário Baixo/Médio" e `0.78` para "Salário Alto" indicam um bom equilíbrio entre precisão e recall para ambas as classes, sendo ligeiramente melhor para a classe majoritária.
    * As médias "Macro Avg" (`0.81`) e "Weighted Avg" (`0.82`) fornecem um resumo geral do F1-Score considerando todas as classes.
* **Matriz de Confusão:** Mostra os acertos e erros do modelo em detalhe:
    * **TN (478):** O modelo previu corretamente 478 profissionais como "Salário Baixo/Médio".
    * **FP (90):** O modelo previu erroneamente 90 profissionais como "Salário Alto" quando na verdade eram "Salário Baixo/Médio".
    * **FN (93):** O modelo previu erroneamente 93 profissionais como "Salário Baixo/Médio" quando na verdade eram "Salário Alto".
    * **TP (329):** O modelo previu corretamente 329 profissionais como "Salário Alto".

## Interpretação dos Resultados:

O modelo Random Forest demonstrou um desempenho geral **bom** na tarefa de classificar profissionais de dados entre faixas salariais "Alto" e "Baixo/Médio".

* **Pontos Fortes:**
    * A acurácia geral de 82% e a acurácia balanceada de aproximadamente 81% indicam que o modelo é consistentemente bom em suas previsões, mesmo com um leve desbalanceamento nas classes originais.
    * O modelo apresenta um bom equilíbrio entre precisão e recall para a classe "Salário Baixo/Médio" (ambos `0.84`). Isso significa que ele é confiável ao prever essa classe e também consegue identificar a maioria dos pertencentes a ela.
    * A otimização do limiar para `0.6` (em vez do padrão `0.5`) foi crucial para alcançar a melhor acurácia balanceada, mostrando a importância de ajustar o ponto de corte da probabilidade para as necessidades específicas do problema e a distribuição das classes.

* **Pontos Fracos e Áreas para Melhoria:**
    * O desempenho para a classe "Salário Alto" (Precisão `0.79`, Recall `0.78`) é ligeiramente inferior ao da classe "Salário Baixo/Médio". Isso significa que há um pouco mais de erro ao prever salários altos, tanto em termos de previsões incorretas dessa classe (afetando a precisão) quanto em não conseguir identificar todos os que de fato têm salário alto (afetando o recall). Especificamente, 93 profissionais de salário alto foram classificados erroneamente como de salário baixo/médio (Falsos Negativos).
    * Ainda existem 90 casos onde o modelo previu "Salário Alto" mas era "Salário Baixo/Médio" (Falsos Positivos). Dependendo do objetivo de negócio, esses erros podem ter custos diferentes.

## Principais Insights e Observações:

* **Distribuição das Classes:** O dataset original apresentava um leve desbalanceamento, com 57.35% dos profissionais na categoria "Salário Baixo/Médio" e 42.65% em "Salário Alto". O uso de `class_weight='balanced_subsample'` nos hiperparâmetros do modelo e a otimização do limiar baseada na `balanced_accuracy` foram estratégias importantes para lidar com isso.
* **Busca de Hiperparâmetros:** O `GridSearchCV` testou 162 combinações de parâmetros em 5 validações cruzadas (totalizando 810 ajustes de modelo) para encontrar a configuração ótima: `{'class_weight': 'balanced_subsample', 'max_depth': None, 'min_samples_leaf': 7, 'min_samples_split': 15, 'n_estimators': 100}`. Isso indica um esforço robusto para otimizar o modelo.
* **Otimização do Limiar de Classificação:** A avaliação com diferentes limiares (`0.3` a `0.7`) mostrou que `0.6` forneceu a melhor `Acurácia Balanceada` (`0.8106`). Isso é um passo crucial, pois o limiar padrão de `0.5` nem sempre é o ideal, especialmente em classes desbalanceadas ou quando os custos de diferentes tipos de erros são assimétricos.
* **Impacto das Features:** Embora não detalhado nestes resultados numéricos, o código Python gera gráficos de importância de features. As features com maior impacto no modelo (como nível de ensino, tempo de experiência, área de formação, senioridade) seriam os principais impulsionadores da disparidade salarial identificada.
* **Salvamento de Gráficos:** Todos os gráficos gerados pela análise foram salvos no diretório `/kaggle/working/`, permitindo uma exploração visual mais aprofundada dos resultados.
* **Tempo de Treinamento/Inferência:** O log indica "Fitting 5 folds for each of 162 candidates, totalling 810 fits", o que, dependendo do tamanho do dataset e da complexidade, pode levar um tempo considerável para a busca de hiperparâmetros. O tempo de inferência para o modelo final (depois de treinado) em 990 amostras de teste costuma ser rápido para Random Forests.


### top3_features
![top3_features](https://github.com/user-attachments/assets/02f25d1b-4639-4cd9-a357-7a89297bff03)

O gráfico apresentado é um **diagrama de barras horizontais** que ilustra as **três características (features) mais influentes** que o modelo de machine learning utilizou para fazer suas previsões sobre a faixa salarial dos profissionais de dados. O título "Top 3 Features Mais Importantes" já nos indica seu propósito principal.

**Como Ler o Gráfico:**

* **Eixo Vertical (Features):** No lado esquerdo, temos o nome das três features mais relevantes identificadas pelo modelo:
    * `senioridade_encoded`
    * `experiencia_profissional_encoded`
    * `formacao_academica_encoded`
    *(Estas são as versões codificadas (transformadas em números) das características originais de nível de senioridade, tempo de experiência e formação acadêmica.)*

* **Eixo Horizontal (Importância Relativa):** Na parte inferior, temos a escala de "Importância Relativa". Esta escala vai de 0.00 até um valor um pouco acima de 0.40. Quanto maior a barra, maior a importância relativa daquela característica para as decisões do modelo.

* **Barras e Valores:** Cada barra colorida representa uma feature, e seu comprimento corresponde à sua importância. Os números ao final de cada barra indicam o valor exato dessa importância:
    * **`senioridade_encoded`:** A barra azul, a mais longa, tem uma importância relativa de aproximadamente **0.4053**. Isso significa que o nível de senioridade do profissional foi o fator individual mais forte que o modelo usou para diferenciar as faixas salariais.
    * **`experiencia_profissional_encoded`:** A barra laranja, a segunda mais longa, tem uma importância de **0.3588**. O tempo de experiência profissional é a segunda característica mais decisiva.
    * **`formacao_academica_encoded`:** A barra verde, a menor entre as três, possui uma importância de **0.0952**. Embora ainda esteja entre as três primeiras, a formação acadêmica teve um peso consideravelmente menor na definição da faixa salarial em comparação com a senioridade e a experiência, segundo este modelo.

**O que isso significa?**

Este gráfico nos diz que, para o modelo treinado, o **nível de senioridade** de um profissional de dados é o indicador mais poderoso para prever sua faixa salarial. Em seguida, vem o **tempo de experiência na área**. A **formação acadêmica**, apesar de relevante, aparece com uma influência menor quando comparada diretamente com os outros dois fatores dentro deste top 3.


### precision_recall_curve
![precision_recall_curve (1)](https://github.com/user-attachments/assets/c74124a4-f6b4-4592-9011-bba7013e93f4)

O gráfico apresentado é uma **Curva Precision-Recall**. Este tipo de gráfico é uma ferramenta visual importante para avaliar o desempenho de um modelo de classificação, especialmente quando as classes que o modelo tenta prever são desbalanceadas (ou seja, uma classe tem muito mais exemplos que a outra).

**Como Ler o Gráfico:**

* **Título:** "Curva Precision-Recall" indica o que o gráfico representa.
* **Eixo Vertical (Precision / Precisão):** Este eixo mede a "Precisão" do modelo e varia de aproximadamente 0.4 (40%) a 1.0 (100%).
    * **O que é Precisão?** De todas as vezes que o modelo previu um resultado positivo (por exemplo, "Salário Alto"), qual a porcentagem dessas previsões estava realmente correta? Uma precisão alta significa que quando o modelo diz que algo é positivo, ele geralmente está certo.
* **Eixo Horizontal (Recall / Revocação / Sensibilidade):** Este eixo mede o "Recall" do modelo e varia de 0.0 (0%) a 1.0 (100%).
    * **O que é Recall?** De todos os casos que eram *realmente* positivos (por exemplo, todos os profissionais que *realmente* têm "Salário Alto"), qual a porcentagem que o modelo conseguiu identificar corretamente? Um recall alto significa que o modelo encontra a maioria dos casos positivos existentes.
* **A Linha Azul:** A linha azul no gráfico traça a relação entre a precisão e o recall do modelo em diferentes "limiares de decisão".
    * **Limiar de Decisão:** Pense nisso como o nível de confiança que o modelo precisa ter para classificar algo como positivo. Se o limiar for muito alto, o modelo será muito cauteloso (alta precisão, mas pode perder alguns casos positivos, resultando em baixo recall). Se o limiar for muito baixo, o modelo identificará mais casos positivos (alto recall), mas também cometerá mais erros ao classificar casos negativos como positivos (baixa precisão).

**Interpretando a Curva:**

* **Trade-off entre Precisão e Recall:** A curva geralmente mostra um "trade-off" (uma troca) entre precisão e recall. Idealmente, gostaríamos que ambas as métricas fossem 100% (canto superior direito do gráfico), mas na prática, aumentar uma muitas vezes leva à diminuição da outra. Isso é visível no gráfico: à medida que o Recall aumenta (movendo-se para a direita no eixo horizontal), a Precisão tende a diminuir (a linha azul geralmente desce).
* **Formato da Curva:**
    * No início (lado esquerdo), quando o Recall é baixo (o modelo está identificando poucos dos verdadeiros positivos), a Precisão é alta (próxima de 1.0). Isso sugere que para os poucos casos que ele classifica como positivos, ele está muito certo.
    * À medida que o modelo tenta capturar mais dos verdadeiros positivos (Recall aumenta), a Precisão começa a cair. Vemos isso pela descida da linha azul. Por exemplo, quando o Recall está em torno de 0.8, a Precisão já caiu para perto de 0.7.
    * A queda se torna mais acentuada no final direito da curva, onde para alcançar um Recall muito alto (perto de 1.0), a Precisão cai significativamente para cerca de 0.4.
* **O que é um "bom" resultado?** Uma curva que se mantém o mais próximo possível do canto superior direito (alta precisão e alto recall simultaneamente) indica um modelo com melhor desempenho. Quanto mais a curva "abraça" o canto superior direito, melhor.

**O que este gráfico nos diz sobre o modelo?**

Este gráfico específico mostra que o modelo pode alcançar uma precisão muito alta (perto de 100%) se estivermos dispostos a aceitar um recall baixo (identificar apenas uma pequena fração dos verdadeiros positivos). Por outro lado, se quisermos que o modelo encontre quase todos os verdadeiros positivos (recall perto de 100%), a precisão cairá consideravelmente (para cerca de 40-50%).

A escolha do "melhor" ponto na curva (ou seja, o melhor limiar de decisão) depende do problema específico e de qual erro é mais custoso: classificar um negativo como positivo (erro de precisão) ou não conseguir identificar um positivo (erro de recall).

### matriz_confusao_otimizada
![matriz_confusao_otimizada (1)](https://github.com/user-attachments/assets/44b373ea-b840-4d47-afd7-804967449a49)

O gráfico apresentado é uma **Matriz de Confusão**. Este é um tipo de tabela que ajuda a visualizar o quão bem um modelo de machine learning está performando em uma tarefa de classificação. No caso deste modelo, ele está classificando profissionais entre duas categorias de salário: "Salário Baixo/Médio" e "Salário Alto". O título nos informa que estes resultados são do "Conjunto de Teste" (dados que o modelo não viu durante o treinamento) e que foi utilizado um "Limiar Otimizado" para a classificação.

**Como Ler o Gráfico:**

A matriz é dividida em quatro quadrantes principais, comparando os valores *verdadeiros* (a realidade) com os valores *previstos* pelo modelo:

* **Eixo Vertical (Rótulo "Verdadeiro"):** Mostra a classificação real dos profissionais.
    * Linha de cima: Profissionais que *realmente* têm "Salário Baixo/Médio".
    * Linha de baixo: Profissionais que *realmente* têm "Salário Alto".

* **Eixo Horizontal (Rótulo "Previsto"):** Mostra o que o modelo *previu* para esses profissionais.
    * Coluna da esquerda: O modelo previu "Salário Baixo/Médio".
    * Coluna da direita: O modelo previu "Salário Alto".

**Interpretando os Quadrantes:**

1.  **Quadrante Superior Esquerdo (Valor: 478):**
    * **Verdadeiro:** Salário Baixo/Médio
    * **Previsto:** Salário Baixo/Médio
    * **Significado:** O modelo acertou! Ele classificou corretamente 478 profissionais que realmente têm salário baixo/médio como tendo salário baixo/médio. Estes são os **Verdadeiros Negativos (TN)**, assumindo "Salário Alto" como a classe positiva.

2.  **Quadrante Superior Direito (Valor: 90):**
    * **Verdadeiro:** Salário Baixo/Médio
    * **Previsto:** Salário Alto
    * **Significado:** O modelo errou. Ele classificou 90 profissionais que realmente têm salário baixo/médio como se tivessem salário alto. Estes são os **Falsos Positivos (FP)** – o modelo "positivou" erroneamente para salário alto.

3.  **Quadrante Inferior Esquerdo (Valor: 93):**
    * **Verdadeiro:** Salário Alto
    * **Previsto:** Salário Baixo/Médio
    * **Significado:** O modelo errou. Ele classificou 93 profissionais que realmente têm salário alto como se tivessem salário baixo/médio. Estes são os **Falsos Negativos (FN)** – o modelo "negou" erroneamente a presença de um salário alto.

4.  **Quadrante Inferior Direito (Valor: 329):**
    * **Verdadeiro:** Salário Alto
    * **Previsto:** Salário Alto
    * **Significado:** O modelo acertou! Ele classificou corretamente 329 profissionais que realmente têm salário alto como tendo salário alto. Estes são os **Verdadeiros Positivos (TP)**.

**Cores:**
A intensidade da cor azul nos quadrantes geralmente corresponde ao número de instâncias. Quadrantes com números maiores (como 478 e 329, que são os acertos) são mais escuros, enquanto quadrantes com números menores (como 90 e 93, que são os erros) são mais claros.

**O que este gráfico nos diz sobre o modelo?**

* **Acertos:** O modelo acertou um bom número de previsões, como indicado pelos valores na diagonal principal (478 e 329).
* **Tipos de Erros:**
    * Ele cometeu 90 erros do tipo "Falso Positivo" (achou que era salário alto, mas não era).
    * Ele cometeu 93 erros do tipo "Falso Negativo" (não identificou um salário alto que era real).
* **Desempenho Geral:** A matriz de confusão permite uma análise detalhada de onde o modelo está acertando e onde está errando. Idealmente, os números na diagonal principal (acertos) seriam os maiores possíveis, e os números fora da diagonal (erros) seriam os menores possíveis.

### interacao_formacao_experiencia
![interacao_formacao_experiencia (1)](https://github.com/user-attachments/assets/c6c03e66-554e-42db-a435-e5e909bb9857)

O gráfico apresentado é um **mapa de calor (heatmap)**. Ele mostra visualmente como a combinação do **nível de formação acadêmica** e do **tempo de experiência profissional** influencia a **probabilidade de um profissional ter um salário considerado alto**.

**Como Ler o Gráfico:**

* **Título:** "Probabilidade de Salário Alto por Formação Acadêmica e Experiência Profissional" indica claramente o que o gráfico está medindo.
* **Eixo Vertical (Nível de Formação):** Lista os diferentes níveis de escolaridade, desde "Estudante de Graduação" no topo até "Doutorado ou Phd" na base.
* **Eixo Horizontal (Tempo de Experiência):** Apresenta faixas de tempo de experiência profissional, começando com "Menos de 1 ano" à esquerda e indo até "de 7 a 10 anos" à direita.
* **Células e Números:** Cada "quadradinho" (célula) no gráfico representa a intersecção de um nível de formação específico com uma faixa de tempo de experiência. O número dentro de cada célula (por exemplo, 0.01, 0.61, 0.94) é a **probabilidade estimada** de um profissional com aquela combinação de formação e experiência ter um salário alto. Uma probabilidade de 0.01 significa 1% de chance, enquanto 0.94 significa 94% de chance.
* **Escala de Cores (Barra à Direita):** A barra vertical à direita é a legenda das cores. As cores no mapa de calor correspondem a essas probabilidades:
    * **Cores escuras (roxo/azul escuro):** Indicam uma baixa probabilidade de ter salário alto.
    * **Cores claras (verde, amarelo):** Indicam uma alta probabilidade de ter salário alto.
    Quanto mais clara/amarela a cor, maior a chance.

**Interpretando as Tendências e Insights do Gráfico:**

1.  **Impacto da Experiência (Movendo da Esquerda para a Direita):**
    * Para qualquer nível de formação, de modo geral, **quanto maior o tempo de experiência, maior a probabilidade de ter um salário alto.** Isso é visível porque, ao seguir uma linha horizontal (mesmo nível de formação), as cores tendem a ficar mais claras/amarelas à medida que você se move para a direita.
    * Por exemplo, para um "Graduação/Bacharelado":
        * Com "Menos de 1 ano" de experiência, a probabilidade é baixa (0.06 ou 6%).
        * Com "de 7 a 10 anos" de experiência, a probabilidade sobe consideravelmente (0.74 ou 74%).

2.  **Impacto da Formação Acadêmica (Movendo de Cima para Baixo):**
    * Para qualquer faixa de experiência (especialmente após alguns anos), **quanto maior o nível de formação acadêmica, maior a probabilidade de ter um salário alto.** Isso é notado porque, ao seguir uma coluna vertical (mesmo tempo de experiência), as cores geralmente se tornam mais claras/amarelas à medida que você desce.
    * Por exemplo, com "de 3 a 4 anos" de experiência:
        * Um "Estudante de Graduação" tem 0.23 (23%) de probabilidade.
        * Um "Doutorado ou Phd" tem 0.89 (89%) de probabilidade.

3.  **Interação entre Formação e Experiência (O Ponto Crucial):**
    * O gráfico demonstra que não é apenas um fator isolado, mas a **combinação** de formação e experiência que mais fortemente influencia a probabilidade de um salário alto.
    * Profissionais com **níveis mais altos de formação E mais tempo de experiência** (canto inferior direito do gráfico) são os que apresentam as maiores probabilidades de terem salários altos (cores mais amarelas, com probabilidades como 0.91, 0.92, 0.94).
    * Por outro lado, aqueles com **baixa formação E pouca experiência** (canto superior esquerdo) têm as menores probabilidades (cores mais escuras, com probabilidades como 0.01, 0.06).
    * É interessante notar que, em alguns casos, muita experiência pode compensar um nível de formação um pouco menor. Por exemplo, um "Estudante de Graduação" com "de 7 a 10 anos" de experiência (0.67) tem uma probabilidade maior de salário alto do que um "Mestrado" com "Menos de 1 ano" de experiência (0.04).


### importancia_features_top20
![importancia_features_top20](https://github.com/user-attachments/assets/cbfc487f-4a48-45e1-8a0a-b5ccdf0b2bb5)

O gráfico apresentado é um **diagrama de barras horizontais** que mostra as **20 características (features) consideradas mais importantes** pelo modelo Random Forest para fazer suas previsões sobre a faixa salarial. O título "Importância das 20 Features Mais Relevantes (Random Forest)" resume seu objetivo.

**Como Ler o Gráfico:**

* **Eixo Vertical (Features):** No lado esquerdo, estão listados os nomes das 20 features que mais influenciaram o modelo. Elas estão ordenadas da menos importante (no topo das 20) para a mais importante (na base das 20).
    * Vemos features como `senioridade_encoded`, `experiencia_profissional_encoded`, `formacao_academica_encoded` (que já vimos serem as top 3), e outras como `UF onde mora_SP` (indicando se a pessoa mora em São Paulo), `Setor de atuação da empresa_Finanças ou Bancos`, `Área de formação acadêmica_Computação / Engenharia de Software / Sistemas de Informação / TI`, entre outras.
* **Eixo Horizontal (Importância Relativa):** Na parte inferior, a escala de "Importância Relativa" varia de 0.00 a pouco mais de 0.40. Quanto maior a barra para uma feature, maior sua importância para as decisões tomadas pelo modelo.
* **Barras Azuis:** Cada barra azul representa uma feature, e seu comprimento é proporcional à sua importância relativa.

**Interpretando as Informações do Gráfico:**

1.  **As Campeãs de Importância:**
    * As três barras na parte inferior do gráfico (`senioridade_encoded`, `experiencia_profissional_encoded` e `formacao_academica_encoded`) são significativamente mais longas que todas as outras. Isso confirma que o **nível de senioridade**, o **tempo de experiência profissional** e o **nível de formação acadêmica codificado** são, de longe, os fatores mais decisivos que o modelo utiliza para prever a faixa salarial.
    * `senioridade_encoded` é a mais importante, com um valor de importância relativa em torno de 0.40.
    * `experiencia_profissional_encoded` vem em seguida, com importância em torno de 0.35.
    * `formacao_academica_encoded` tem uma importância próxima a 0.10.

2.  **As Demais Features Relevantes:**
    * Após as três primeiras, há uma queda acentuada na importância. As 17 features restantes têm uma influência consideravelmente menor, com barras muito mais curtas.
    * Entre estas, encontramos:
        * **Localização:** `UF onde mora_SP` (morar em São Paulo) aparece como a quarta feature mais importante, embora com um peso bem menor que as três primeiras. Outras UFs como RJ, PR, RS, DF também figuram na lista, indicando que a localização geográfica tem alguma influência.
        * **Setor de Atuação da Empresa:** Características como `Setor de atuação da empresa_Finanças ou Bancos`, `Setor de atuação da empresa_Tecnologia/Fábrica de Software`, `Setor de atuação da empresa_Area de Consultoria` também são consideradas pelo modelo, sugerindo que o setor onde o profissional trabalha impacta a previsão salarial.
        * **Área de Formação Específica:** Além do nível de formação (já no top 3), a área específica da formação também contribui, como `Área de formação acadêmica_Computação / Engenharia de Software / Sistemas de Informação / TI` e `Área de formação acadêmica_Economia/ Administração / Contabilidade / Finanças/ Negócios`.

3.  **O Conceito de "Importância Relativa":**
    * Os valores no eixo horizontal não são, por exemplo, percentagens diretas do salário, mas sim uma medida de quanto cada feature contribuiu para reduzir a impureza (ou aumentar a precisão) nas árvores de decisão que compõem o modelo Random Forest. A soma de todas as importâncias de todas as features (não apenas as 20 mostradas) seria 1.0 (ou 100%).

**O que este gráfico nos diz sobre o modelo?**

Este gráfico é fundamental para entender "o que o modelo está pensando". Ele revela que, embora muitas características sejam consideradas, um pequeno grupo delas (senioridade, experiência e nível de formação) domina o processo de decisão para prever salários. As outras 17 features mostradas, como localização, setor da empresa e área de formação específica, adicionam nuances e refinamentos à previsão, mas têm um papel secundário em comparação com os três principais fatores.

### importancia_features_grupo_senioridade
![importancia_features_grupo_senioridade](https://github.com/user-attachments/assets/88a8e6a4-5bff-4e58-a613-523fe4915bed)

**Como Ler o Gráfico:**

* **Eixo Vertical (Feature):** No lado esquerdo, vemos apenas uma característica listada: `senioridade_encoded`. Este é o nome da feature que representa o nível de senioridade do profissional, após ter sido codificada (transformada em um formato numérico que o modelo pode entender).
* **Eixo Horizontal (Importância Relativa):** Na parte inferior, a escala de "Importância Relativa" vai de 0.00 até um valor um pouco acima de 0.40.
* **Barra Verde:** Há uma única e longa barra verde que corresponde à feature `senioridade_encoded`. O comprimento desta barra indica o quão importante essa característica é para as previsões de faixa salarial feitas pelo modelo.

**Interpretando as Informações do Gráfico:**

1.  **Foco na Senioridade Codificada:**
    * O gráfico isola a feature `senioridade_encoded`. Isso sugere que a informação original sobre o nível de senioridade (por exemplo, Júnior, Pleno, Sênior) foi transformada em uma única variável numérica (`senioridade_encoded`) para o modelo.

2.  **Alta Importância Confirmada:**
    * A barra se estende até um valor de importância relativa de aproximadamente **0.4053** (este valor exato foi visto em outros gráficos de importância geral, como o "Top 3 Features").
    * Este valor é bastante alto, especialmente quando comparado com a importância de muitas outras características individuais (como os estados ou setores de atuação vistos em gráficos anteriores).

3.  **O que significa "Grupo senioridade" neste contexto?**
    * Diferentemente dos gráficos de "Grupo UF onde mora" ou "Grupo Setor de atuação da empresa", onde várias features dentro do grupo eram comparadas (por exemplo, diferentes UFs ou diferentes setores), aqui o "Grupo senioridade" parece se referir apenas a esta única feature consolidada.
    * Isso reforça que a senioridade, como um todo, foi tratada como um conceito único e poderoso pelo modelo.

**O que este gráfico nos diz sobre o modelo?**

Este gráfico serve para enfatizar de forma isolada e clara o **peso significativo que a senioridade (codificada) tem nas previsões do modelo**. Ele reitera que, de todas as informações fornecidas ao modelo, o nível de senioridade de um profissional é um dos indicadores mais fortes e influentes para determinar sua faixa salarial.


### importancia_features_grupo_formacao
![importancia_features_grupo_formacao](https://github.com/user-attachments/assets/e9180d58-b603-4e09-9f57-a94ecc4d824f)

**Como Ler o Gráfico:**

* **Eixo Vertical (Feature):** No lado esquerdo, é listada apenas uma característica: `formacao_academica_encoded`. Este é o nome da feature que representa o nível de formação acadêmica do profissional, após ter sido codificada (ou seja, transformada em um valor numérico que o modelo pode processar).
* **Eixo Horizontal (Importância Relativa):** Na parte inferior, a escala de "Importância Relativa" varia de 0.00 até 0.10.
* **Barra Verde:** Existe uma única e proeminente barra verde que corresponde à feature `formacao_academica_encoded`. O comprimento desta barra indica o peso ou a influência que esta característica tem nas previsões de faixa salarial feitas pelo modelo.

**Interpretando as Informações do Gráfico:**

1.  **Foco na Formação Acadêmica Codificada:**
    * O gráfico isola a feature `formacao_academica_encoded`. Isso sugere que a informação original sobre o nível de formação acadêmica (por exemplo, Graduação, Pós-graduação, Mestrado, Doutorado, etc.) foi consolidada e transformada em uma única variável numérica (`formacao_academica_encoded`) que foi utilizada pelo modelo.

2.  **Importância Significativa:**
    * A barra se estende até um valor de importância relativa de aproximadamente **0.0952**. Embora este valor seja menor do que os observados para `senioridade_encoded` (próximo a 0.4053) e `experiencia_profissional_encoded` (próximo a 0.3588) em outros gráficos, ele ainda representa a terceira característica mais importante no geral para o modelo.
    * Isso indica que, após a senioridade e a experiência, o nível de formação acadêmica é o próximo fator mais influente nas previsões salariais.

3.  **O que significa "Grupo formacao" neste contexto?**
    * Assim como no gráfico do "Grupo senioridade", o "Grupo formacao" aqui se refere a esta única feature consolidada, `formacao_academica_encoded`.
    * Isso não é uma comparação entre diferentes aspectos da formação, mas sim uma maneira de destacar a importância total atribuída ao conceito de "nível de formação acadêmica" da forma como foi processado e incluído no modelo.

**O que este gráfico nos diz sobre o modelo?**

Este gráfico simples, mas direto, serve para reforçar que o **nível de formação acadêmica (codificado) dos profissionais é uma variável com impacto considerável nas previsões do modelo** sobre suas faixas salariais. Embora não seja tão dominante quanto a senioridade ou a experiência profissional, a formação acadêmica ainda se destaca como um dos principais fatores levados em conta pelo modelo.

### importancia_features_grupo_experiencia
![importancia_features_grupo_experiencia](https://github.com/user-attachments/assets/bffd0e4f-bc56-42d1-802c-ea1b22b872b7)

**Como Ler o Gráfico:**

* **Eixo Vertical (Feature):** À esquerda, é apresentada apenas uma característica: `experiencia_profissional_encoded`. Este é o nome da feature que representa o tempo ou nível de experiência profissional, após ter sido codificada (transformada em um valor numérico que o modelo pode utilizar).
* **Eixo Horizontal (Importância Relativa):** Na parte inferior, a escala de "Importância Relativa" se estende de 0.00 até um valor um pouco acima de 0.35.
* **Barra Verde:** Há uma única e muito longa barra verde. Seu comprimento corresponde diretamente à importância da feature `experiencia_profissional_encoded` para as previsões de faixa salarial feitas pelo modelo.

**Interpretando as Informações do Gráfico:**

1.  **Foco na Experiência Profissional Codificada:**
    * O gráfico isola a feature `experiencia_profissional_encoded`. Isso indica que a informação original sobre o tempo de experiência profissional (por exemplo, "Menos de 1 ano", "de 1 a 2 anos", etc.) foi transformada em uma única variável numérica (`experiencia_profissional_encoded`) para ser usada pelo modelo.

2.  **Importância Muito Elevada:**
    * A barra se estende até um valor de importância relativa de aproximadamente **0.3588**. Este valor é substancial e, conforme visto em gráficos anteriores (como o "Top 3 Features"), posiciona a experiência profissional como a segunda característica mais importante para o modelo, ficando atrás apenas da senioridade.

3.  **Significado de "Grupo experiencia" neste Contexto:**
    * Assim como nos gráficos de "Grupo senioridade" e "Grupo formacao", o "Grupo experiencia" aqui se refere a esta única feature consolidada.
    * Não se trata de uma comparação entre diferentes facetas da experiência, mas sim de uma forma de destacar a importância total atribuída ao conceito de "experiência profissional" da maneira como foi processado e incluído no modelo.

**O que este gráfico nos diz sobre o modelo?**

Este gráfico, embora simples por apresentar uma única barra, serve para enfatizar de forma clara e inequívoca o **peso extremamente significativo que a experiência profissional (codificada) tem nas previsões do modelo**. Ele confirma que, entre todas as informações fornecidas, o nível de experiência profissional de um indivíduo é um dos indicadores mais fortes e decisivos para determinar sua faixa salarial.

### importancia_features_grupo_Área de formação acadêmica
![importancia_features_grupo_Área de formação acadêmica](https://github.com/user-attachments/assets/17e5dd69-f141-4fc0-b0e5-fbb180912aeb)

O gráfico apresentado é um **gráfico de barras horizontais** que ilustra a **importância relativa** de diferentes subcategorias dentro do grupo "Área de formação acadêmica" para um modelo de machine learning. O título "Importância das Features: Grupo Área de formação acadêmica" indica que o gráfico foca em detalhar a relevância de cada área específica de formação.

**Como interpretar o gráfico:**

* **Eixo Y (Vertical):** Lista as diferentes áreas de formação acadêmica que foram consideradas como features (características) pelo modelo. Por exemplo, "Área de formação acadêmica_Ciências Sociais", "Área de formação acadêmica_Marketing / Publicidade / Comunicação / Jornalismo", etc.
* **Eixo X (Horizontal):** Representa a "Importância Relativa" de cada uma dessas áreas. Quanto maior a barra, maior a importância relativa daquela área de formação para as previsões feitas pelo modelo. Os valores no eixo X (ex: 0.000, 0.002, ..., 0.012) indicam a magnitude dessa importância.
* **Barras:** O comprimento de cada barra horizontal é proporcional à importância relativa da área de formação correspondente.

**Análise das Features Apresentadas (da mais importante para a menos importante, visualmente):**

1.  **Área de formação acadêmica_Economia/ Administração / Contabilidade / Finanças/ Negócios:** É a área com a **maior importância relativa** (aproximadamente 0.011).
2.  **Área de formação acadêmica_Computação / Engenharia de Software / Sistemas de Informação/ TI:** Possui a segunda maior importância (aproximadamente 0.009).
3.  **Área de formação acadêmica_Outras Engenharias:** Apresenta uma importância considerável (aproximadamente 0.007).
4.  **Área de formação acadêmica_Outra opção:** Segue com uma importância relativa em torno de 0.005.
5.  **Área de formação acadêmica_Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais:** Mostra uma importância de aproximadamente 0.0035.
6.  **Área de formação acadêmica_Química / Física:** Tem uma importância menor (aproximadamente 0.0015).
7.  **Área de formação acadêmica_Ciências Biológicas/ Farmácia/ Medicina/ Área da Saúde:** Apresenta uma importância similar à anterior (aproximadamente 0.0015).
8.  **Área de formação acadêmica_Marketing / Publicidade / Comunicação / Jornalismo:** Possui uma baixa importância relativa (aproximadamente 0.001).
9.  **Área de formação acadêmica_Ciências Sociais:** É a área com a **menor importância relativa** entre as listadas (muito próxima de 0.0005).

### distribuicao_probabilidades
![distribuicao_probabilidades (1)](https://github.com/user-attachments/assets/f7ed3668-f41f-486f-87bd-dbac9fcd74f1)

O gráfico apresentado é um **histograma** com uma curva de estimativa de densidade do kernel (KDE) sobreposta, intitulado "Distribuição das Probabilidades Preditas". Ele mostra como as probabilidades preditas pelo modelo para a classe "Salário Alto" estão distribuídas.

**Como interpretar o gráfico:**

* **Eixo X (Horizontal):** "Probabilidade de Salário Alto". Este eixo varia de 0.0 a 1.0 e representa a confiança do modelo de que uma determinada instância pertence à classe "Salário Alto".
    * Um valor próximo de 0.0 significa que o modelo prevê uma baixa probabilidade de a instância ter um salário alto.
    * Um valor próximo de 1.0 significa que o modelo prevê uma alta probabilidade de a instância ter um salário alto.
* **Eixo Y (Vertical):** "Contagem". Este eixo indica o número de previsões (instâncias) que caem em cada intervalo de probabilidade (as barras do histograma).
* **Barras do Histograma:** Cada barra representa um intervalo de probabilidades preditas, e a altura da barra mostra quantas previsões do modelo caíram nesse intervalo específico.
* **Curva Azul:** É uma estimativa de densidade do kernel (KDE), que fornece uma representação suavizada da distribuição das probabilidades preditas. Ajuda a visualizar a forma geral da distribuição.
* **Linha Tracejada Vermelha Vertical:** Identificada na legenda como "Limiar Ótimo = 0.6". Este é um limiar (threshold) escolhido para classificar as instâncias.
    * Previsões com probabilidade de salário alto **maior ou igual a 0.6** seriam classificadas como pertencentes à classe "Salário Alto".
    * Previsões com probabilidade **menor que 0.6** seriam classificadas como "Não Salário Alto" (ou a classe oposta).

**Análise da Distribuição:**

* **Concentração nas Extremidades:** Observa-se uma alta concentração de previsões com probabilidades muito baixas (próximas de 0.0). A barra mais alta do histograma está no extremo esquerdo, indicando que muitas instâncias receberam uma probabilidade muito baixa de terem um salário alto.
* **Outro Pico em Altas Probabilidades:** Há também um acúmulo significativo de previsões com probabilidades altas, especialmente entre 0.9 e 1.0, embora menor que o pico em 0.0.
* **Menor Contagem no Meio:** Existem menos previsões com probabilidades na faixa intermediária (por exemplo, entre 0.3 e 0.5, e entre 0.6 e 0.7, excluindo o limiar). Isso sugere que o modelo, em muitos casos, está razoavelmente "decidido" sobre a classe, atribuindo probabilidades mais extremas.
* **Impacto do Limiar (0.6):**
    * A maioria das previsões à esquerda do limiar de 0.6 seriam classificadas como "Não Salário Alto".
    * As previsões à direita do limiar (probabilidade >= 0.6) seriam classificadas como "Salário Alto". O gráfico mostra que um número considerável de instâncias se qualifica para esta classe com base neste limiar, especialmente aquelas com probabilidades entre 0.9 e 1.0.


### dispersao_top2_features
![dispersao_top2_features](https://github.com/user-attachments/assets/99eb2c9f-d3ef-47d7-b337-5431c00d0571)

O gráfico apresentado é um **diagrama de dispersão (scatter plot)** intitulado "Relação entre as Duas Features Mais Importantes: senioridade_encoded vs experiencia_profissional_encoded". Ele visualiza como as duas características consideradas mais importantes pelo modelo – senioridade e experiência profissional (ambas codificadas numericamente) – se relacionam com a probabilidade predita de um indivíduo ter um salário alto.

**Como interpretar o gráfico:**

* **Eixo X (Horizontal):** "senioridade_encoded". Representa os diferentes níveis de senioridade, que foram convertidos para um formato numérico (codificado). Valores maiores neste eixo provavelmente correspondem a níveis de senioridade mais altos.
* **Eixo Y (Vertical):** "experiencia_profissional_encoded". Representa os diferentes níveis de experiência profissional, também codificados numericamente. Valores maiores neste eixo provavelmente indicam mais anos ou níveis de experiência.
* **Pontos no Gráfico:** Cada ponto representa uma combinação específica de `senioridade_encoded` e `experiencia_profissional_encoded` observada nos dados.
* **Escala de Cores (Barra Lateral):** "Probabilidade de Salário Alto". Esta barra de cores, variando do azul (0.0) ao vermelho (1.0), indica a probabilidade predita pelo modelo de um indivíduo ter um salário alto.
    * **Pontos azuis/roxos:** Baixa probabilidade de salário alto.
    * **Pontos vermelhos/laranjas:** Alta probabilidade de salário alto.

**Análise das Relações e Padrões Visíveis:**

* **Impacto da Senioridade:** Observa-se uma tendência clara de que, à medida que `senioridade_encoded` aumenta (movendo da esquerda para a direita no gráfico), a cor dos pontos tende a mudar de azul para vermelho. Isso sugere que níveis mais altos de senioridade estão associados a uma maior probabilidade de ter um salário alto.
    * Por exemplo, os pontos com `senioridade_encoded = 2.00` são predominantemente vermelhos ou laranjas, indicando altas probabilidades de salário alto.
    * Em contraste, os pontos com `senioridade_encoded = 0.00` são todos azuis ou roxos, indicando baixas probabilidades.

* **Impacto da Experiência Profissional:** Similarmente, para um dado nível de senioridade, um aumento em `experiencia_profissional_encoded` (movendo de baixo para cima no gráfico) também tende a aumentar a probabilidade de salário alto.
    * Por exemplo, para `senioridade_encoded = 2.00`:
        * Com `experiencia_profissional_encoded = 0.0`, o ponto é laranja claro (probabilidade moderada-alta).
        * Com `experiencia_profissional_encoded = 4.0`, o ponto é vermelho escuro (probabilidade muito alta).

* **Combinação de Fatores:** O efeito mais forte (maior probabilidade de salário alto) é observado quando ambos, senioridade e experiência profissional, são altos. O ponto no canto superior direito (`senioridade_encoded = 2.00`, `experiencia_profissional_encoded = 4.0`) é o mais vermelho, indicando a maior probabilidade predita de salário alto.

* **Valores Codificados:** Os valores nos eixos parecem ser discretos (ex: 0.00, 1.00, 2.00 para senioridade; 0.0, 1.0, 2.0, 3.0, 4.0 para experiência). Isso é consistente com a ideia de que estas são features categóricas que foram codificadas numericamente para uso no modelo.

### curva_roc_otimizada
![curva_roc_otimizada (1)](https://github.com/user-attachments/assets/2bd509b0-24c8-46ad-9bb0-b18203609795)

O gráfico apresentado é uma **Curva ROC (Receiver Operating Characteristic)**, uma ferramenta fundamental para avaliar o desempenho de modelos de classificação binária. O título "Curva ROC com Limiar Otimizado" indica que, além da curva em si, um limiar específico considerado ótimo é destacado.

**Como interpretar o gráfico:**

* **Eixo X (Horizontal): Taxa de Falsos Positivos (FPR - False Positive Rate)**
    * Também conhecida como (1 - Especificidade).
    * Representa a proporção de instâncias negativas que foram incorretamente classificadas como positivas pelo modelo.
    * Valores mais baixos de FPR são melhores (menos alarmes falsos).

* **Eixo Y (Vertical): Taxa de Verdadeiros Positivos (TPR - True Positive Rate)**
    * Também conhecida como Sensibilidade ou Recall.
    * Representa a proporção de instâncias positivas que foram corretamente classificadas como positivas pelo modelo.
    * Valores mais altos de TPR são melhores (mais acertos corretos dos positivos).

* **Curva ROC (Laranja):**
    * Esta curva ilustra o desempenho do modelo de classificação em todos os limiares de classificação possíveis. Cada ponto na curva ROC representa um par (FPR, TPR) correspondente a um determinado limiar.
    * Um modelo ideal teria uma curva que sobe rapidamente em direção ao canto superior esquerdo do gráfico (TPR = 1, FPR = 0). Quanto mais a curva se aproxima desse canto, melhor o desempenho do modelo.

* **AUC (Area Under the Curve) = 0.88:**
    * A Área Sob a Curva ROC (AUC) é uma medida agregada do desempenho do modelo em todos os limiares.
    * A AUC varia de 0 a 1:
        * AUC = 0.5: O modelo não tem capacidade de discriminação (equivalente a um classificador aleatório).
        * AUC > 0.5: O modelo tem alguma capacidade de discriminação.
        * AUC = 1.0: O modelo é um classificador perfeito.
    * Um valor de **AUC = 0.88** indica um bom desempenho do modelo, significando que há uma probabilidade de 88% de que o modelo classifique corretamente uma instância positiva escolhida aleatoriamente como mais provável de ser positiva do que uma instância negativa escolhida aleatoriamente.

* **Linha Diagonal Tracejada (Azul Escuro):**
    * Representa o desempenho de um classificador aleatório (que não tem poder de discriminação). A Curva ROC de um bom modelo deve estar significativamente acima desta linha.

* **Linha Vertical Tracejada (Verde): Limiar Ótimo = 0.6**
    * Esta linha vertical indica um limiar específico (threshold) de 0.6 que foi escolhido como "ótimo" para este modelo, possivelmente com base em algum critério de otimização (como maximizar o índice de Youden, ou balancear TPR e FPR de acordo com as necessidades do problema).
    * O ponto onde esta linha verde intercepta a Curva ROC laranja mostra o desempenho do modelo (o par TPR e FPR) quando este limiar de 0.6 é usado para classificar as instâncias. Visualmente, para este limiar de 0.6, o FPR é baixo (aproximadamente 0.08) e o TPR é considerável (aproximadamente 0.65).

**Análise do Desempenho:**

* A Curva ROC laranja está bem acima da linha diagonal, e o valor de AUC de 0.88 confirma que o modelo tem um bom poder de discriminação entre as classes positiva e negativa.
* A escolha do "Limiar Ótimo = 0.6" resulta em uma baixa taxa de falsos positivos (poucos negativos classificados erroneamente como positivos) e uma taxa de verdadeiros positivos razoavelmente alta (uma boa proporção dos positivos reais são identificados corretamente). A adequação deste limiar depende do contexto específico do problema e dos custos associados a falsos positivos versus falsos negativos.


### arvore_exemplo_simplificada
![arvore_exemplo_simplificada](https://github.com/user-attachments/assets/a4d395fd-d40a-43e0-a655-1cc5eece761e)

O gráfico apresentado é uma **visualização de uma única árvore de decisão**, extraída de um modelo mais complexo chamado **Random Forest**. Um Random Forest é um conjunto (ou "floresta") de múltiplas árvores de decisão, onde cada árvore contribui para a predição final. Esta visualização simplificada nos ajuda a entender como uma dessas árvores toma decisões para classificar os dados.

---

**Como interpretar os componentes da árvore:**

* **Nós (Retângulos):** Cada retângulo é um nó na árvore.
    * **Nós de Decisão (Nós Internos):** São os retângulos que têm ramificações (setas) saindo deles. Eles contêm uma condição baseada em uma das *features* (características) dos dados.
        * **Condição de Divisão:** A primeira linha no nó de decisão (ex: `experiencia_profissional_encoded <= 1.5`). Esta é a pergunta que a árvore faz sobre uma amostra de dados. Se a condição for verdadeira, a amostra segue para o galho da esquerda; se for falsa, para o galho da direita.
        * `gini`: O **Índice de Gini** é uma medida de impureza do nó. Um valor de Gini igual a 0 significa que o nó é perfeitamente puro (todas as amostras nesse nó pertencem à mesma classe). Quanto maior o Gini, mais misturadas estão as classes no nó.
        * `samples`: O número de amostras de treinamento que alcançaram este nó.
        * `value`: Mostra a distribuição das amostras entre as diferentes classes possíveis dentro daquele nó. Por exemplo, `value = [100, 632, 267, 722]` no segundo nó da esquerda indica como as amostras estão distribuídas entre as classes (o número de classes e sua ordem dependeriam da codificação do problema).
        * `class`: Indica a classe majoritária entre as amostras presentes naquele nó. Se este fosse um nó folha, essa seria a predição da árvore para as amostras que chegam até ele.
    * **Nós Folha (Nós Terminais):** São os nós no final das ramificações, onde não há mais divisões. Eles representam a predição final para qualquer amostra que percorra o caminho até eles.
        * Neste gráfico, os nós cinzas com `(...)` no final indicam que a árvore continua, mas foi **truncada ou simplificada** para esta visualização, não mostrando todos os detalhes das ramificações mais profundas.
        * Os nós coloridos que não possuem mais divisões (como o nó mais à direita `Setor de atuação da empresa_Finanças ou Bancos <= 0.5`) também são nós folha para os caminhos que terminam ali na visualização.

* **Cores dos Nós:** As diferentes cores dos nós (neste caso, laranja e azul) geralmente representam a classe predominante naquele nó, ajudando a visualizar como a árvore está tentando separar as diferentes classes.

---

**Exemplo de Caminho de Decisão:**

Vamos seguir um caminho hipotético:

1.  **Nó Raiz (Topo):** A primeira decisão é baseada em `experiencia_profissional_encoded <= 1.5`.
    * **Se VERDADEIRO** (experiência profissional codificada é menor ou igual a 1.5): A amostra segue para o nó da esquerda, cuja próxima decisão é `senioridade_encoded <= 1.5`.
    * **Se FALSO** (experiência profissional codificada é maior que 1.5): A amostra segue para o nó da direita, cuja próxima decisão é `UF onde mora_MG <= 0.5` (provavelmente perguntando se a UF onde mora é Minas Gerais ou não, baseado na codificação).

2.  Suponha que `experiencia_profissional_encoded <= 1.5` foi **VERDADEIRO**. Chegamos ao nó que pergunta `senioridade_encoded <= 1.5`.
    * Se `senioridade_encoded <= 1.5` for **VERDADEIRO**: A amostra vai para o nó mais à esquerda, `Setor de atuação da empresa_Marketing <= 0.5`. A classe predominante neste nó é "Salário Baixo/Médio".
    * ... e assim por diante, até que a amostra chegue a um nó folha (ou um nó truncado `(...)` nesta visualização).


### arvore_exemplo_melhorada
![arvore_exemplo_melhorada](https://github.com/user-attachments/assets/410ea2af-736a-4cbf-9541-d0edb1ac49d1)

O gráfico apresentado é uma **visualização de uma única árvore de decisão**, extraída de um modelo mais complexo chamado **Random Forest**. Um Random Forest é um conjunto (ou "floresta") de múltiplas árvores de decisão, onde cada árvore contribui para a predição final. Esta visualização nos ajuda a entender como uma dessas árvores toma decisões para classificar os dados.

---

**Como interpretar os componentes da árvore:**

* **Nós (Retângulos):** Cada retângulo é um nó na árvore.
    * **Nós de Decisão (Nós Internos):** São os retângulos que têm ramificações (setas) saindo deles. Eles contêm uma condição baseada em uma das *features* (características) dos dados.
        * **Condição de Divisão:** A primeira linha no nó de decisão (ex: `experiencia_profissional_encoded <= 1.5`). Esta é a pergunta que a árvore faz sobre uma amostra de dados. Se a condição for verdadeira, a amostra segue para o galho da esquerda; se for falsa, para o galho da direita.
        * `gini`: O **Índice de Gini** é uma medida de impureza do nó. Um valor de Gini igual a 0 significa que o nó é perfeitamente puro (todas as amostras nesse nó pertencem à mesma classe). Quanto maior o Gini, mais misturadas estão as classes no nó.
        * `samples`: O número de amostras de treinamento que alcançaram este nó.
        * `value`: Mostra a distribuição das amostras entre as diferentes classes possíveis dentro daquele nó. Por exemplo, `value = [100,632, 267,722]` no segundo nó da esquerda (contando o nó raiz como o primeiro nível) indica como as 1801 amostras (`samples = 1801`) estão distribuídas entre as classes. A classe predominante, "Salário Baixo/Médio", é determinada por essa distribuição.
        * `class`: Indica a classe majoritária entre as amostras presentes naquele nó. Se este fosse um nó folha, essa seria a predição da árvore para as amostras que chegam até ele.
    * **Nós Folha (Nós Terminais):** São os nós no final das ramificações, onde não há mais divisões. Eles representam a predição final para qualquer amostra que percorra o caminho até eles.
        * Neste gráfico, os nós cinzas com `(...)` no final indicam que a árvore continua, mas foi **truncada ou simplificada** para esta visualização, não mostrando todos os detalhes das ramificações mais profundas.
        * Os nós coloridos que não possuem mais divisões (como o nó mais à direita na segunda linha de profundidade: `Setor de atuação da empresa_Finanças ou Bancos <= 0.5`) também são nós folha para os caminhos que terminam ali na visualização, se não tiverem mais ramificações abaixo deles.

* **Cores dos Nós:** As diferentes cores dos nós (neste caso, laranja e azul) geralmente representam a classe predominante naquele nó, ajudando a visualizar como a árvore está tentando separar as diferentes classes. Por exemplo, nós laranjas podem predominantemente representar "Salário Baixo/Médio", enquanto nós azuis podem representar "Salário Alto".

---

**Exemplo de Caminho de Decisão:**

Vamos seguir um caminho hipotético:

1.  **Nó Raiz (Topo):** A primeira decisão é baseada em `experiencia_profissional_encoded <= 1.5`.
    * **Se VERDADEIRO** (experiência profissional codificada é menor ou igual a 1.5): A amostra segue para o nó da esquerda, cuja próxima decisão é `senioridade_encoded <= 1.5`.
    * **Se FALSO** (experiência profissional codificada é maior que 1.5): A amostra segue para o nó da direita, cuja próxima decisão é `UF onde mora_MG <= 0.5`.

2.  Suponha que `experiencia_profissional_encoded <= 1.5` foi **VERDADEIRO**. Chegamos ao nó que pergunta `senioridade_encoded <= 1.5`.
    * Se `senioridade_encoded <= 1.5` for **VERDADEIRO**: A amostra vai para o nó mais à esquerda na linha seguinte, `Setor de atuação da empresa_Marketing <= 0.5`. A classe predominante neste nó é "Salário Baixo/Médio".
    * ... e assim por diante, até que a amostra chegue a um nó folha (ou um nó truncado `(...)` nesta visualização). A classe indicada no nó final alcançado seria a predição dessa árvore específica para a amostra.




## Resultados obtidos com o modelo 2 da 1º pergunta orietada a dados

### Modelo Árvore de Decisão Classificatória

| Classe          | Precisão | Recall | F1-Score | Suporte |
|-----------------|----------|--------|----------|---------|
| Acima de R$ 30.000/mês    | 0.12     | 0.10   | 0.11     | 10     |
| Até R$ 2.000/mês | 0.28     | 0.41   | 0.33     | 56     | 
| R$ 16.001/mês a R$ 30.000/mês  | 0.40     | 0.31   | 0.35     | 59     |
| R$ 2.001/mês a R$ 4.000/mês | 0.42     | 0.42   | 0.42     | 160     |
| R$ 4.001/mês a R$ 8.000/mês | 0.57     | 0.45   | 0.50     | 352     |
| R$ 8.001/mês a R$ 16.000/mês | 0.61     | 0.72   | 0.66     | 353     |
| accuracy |  |  | **0.53** | **990** |
| macro avg | **0.40** | **0.40** | **0.40** | **990** |
| weighted avg | **0.53** | **0.53** | **0.52** | **990** |

- Acurácia do Modelo: 0.53
- Acurácia do Modelo no Conjunto de Treinamento: -
- Acurácia do Modelo no Conjunto de Teste: -
- Diferença de Acurácia (Treino - Teste): -


### matriz_confusao 1_2
![matriz_confusao](https://github.com/user-attachments/assets/ac19812f-ecd2-47b0-a08b-f8b7b0db1732)

**Como interpretar a Matriz de Confusão:**

* **Eixo Vertical (Real):** Indica a classe verdadeira à qual cada instância pertence.
* **Eixo Horizontal (Predito):** Indica a classe que o modelo previu para cada instância.
* **Células da Matriz:**
    * **Diagonal Principal (do canto superior esquerdo ao canto inferior direito):** Os números nestas células representam as **classificações corretas**. Por exemplo, o valor na célula onde "Real" é "R$ 8.001/mês a R$ 16.000/mês" e "Predito" também é "R$ 8.001/mês a R$ 16.000/mês" indica quantas vezes o modelo acertou essa classe. Quanto maiores os valores na diagonal, melhor o desempenho para aquelas classes específicas.
    * **Fora da Diagonal Principal:** Os números nestas células representam **erros de classificação** (confusões).
        * Um valor em uma célula onde a classe "Real" é X e a classe "Predita" é Y (e X ≠ Y) significa que o modelo classificou erroneamente instâncias da classe X como pertencentes à classe Y.
* **Escala de Cores:** A barra de cores à direita (geralmente um gradiente) indica a magnitude dos valores nas células. Cores mais escuras (neste caso, azul mais intenso) correspondem a contagens mais altas, facilitando a identificação visual de onde ocorrem a maioria das classificações e misclassificações.

**Análise da Matriz de Confusão Específica (baseada na imagem):**

1.  **Desempenho por Classe (Diagonal):**
    * **Acima de R$ 30.000/mês:** Apenas **1** instância foi classificada corretamente.
    * **Até R$ 2.000/mês:** **23** instâncias foram classificadas corretamente.
    * **R$ 16.001/mês a R$ 30.000/mês:** **18** instâncias foram classificadas corretamente.
    * **R$ 2.001/mês a R$ 4.000/mês:** **68** instâncias foram classificadas corretamente.
    * **R$ 4.001/mês a R$ 8.000/mês:** **158** instâncias foram classificadas corretamente.
    * **R$ 8.001/mês a R$ 16.000/mês:** **254** instâncias foram classificadas corretamente. Esta é a classe com o maior número de acertos.

2.  **Principais Erros de Classificação (Fora da Diagonal):**
    * **Classe "Acima de R$ 30.000/mês" (Real):**
        * Foi frequentemente confundida com outras classes, especialmente com "R$ 8.001/mês a R$ 16.000/mês" (**7** vezes) e "R$ 16.001/mês a R$ 30.000/mês" (**2** vezes). Isso indica que o modelo tem muita dificuldade em identificar corretamente os salários mais altos.
    * **Classe "Até R$ 2.000/mês" (Real):**
        * Foi confundida principalmente com "R$ 2.001/mês a R$ 4.000/mês" (**20** vezes) e "R$ 4.001/mês a R$ 8.000/mês" (**11** vezes).
    * **Classe "R$ 16.001/mês a R$ 30.000/mês" (Real):**
        * A maior confusão foi com "R$ 8.001/mês a R$ 16.000/mês" (**34** vezes).
    * **Classe "R$ 2.001/mês a R$ 4.000/mês" (Real):**
        * Confundida com "Até R$ 2.000/mês" (**36** vezes) e "R$ 4.001/mês a R$ 8.000/mês" (**42** vezes).
    * **Classe "R$ 4.001/mês a R$ 8.000/mês" (Real):**
        * Confundida com "R$ 2.001/mês a R$ 4.000/mês" (**69** vezes) e "R$ 8.001/mês a R$ 16.000/mês" (**104** vezes).

**Observações Gerais:**

* O modelo parece ter um melhor desempenho para a classe **"R$ 8.001/mês a R$ 16.000/mês"**, que possui o maior número de classificações corretas na diagonal.
* Há uma tendência de confusão entre faixas salariais adjacentes, o que é esperado, pois a distinção entre elas pode ser sutil.
* A classe **"Acima de R$ 30.000/mês"** é a que apresenta o pior desempenho em termos de acertos, sendo frequentemente subestimada pelo modelo. Isso pode ser devido a um menor número de amostras nessa classe nos dados de treinamento (desbalanceamento de classes) ou à dificuldade intrínseca de separar essa faixa das demais com as features disponíveis.


### distribuicao_faixas_salariais_originais 1_2
![distribuicao_faixas_salariais_originais](https://github.com/user-attachments/assets/9f135a05-dc93-4d26-8b6c-45c32f05a136)

O gráfico apresentado é um **gráfico de barras horizontais** intitulado "Distribuição de Faixas Salariais Originais". Ele mostra a frequência (ou contagem) de cada faixa salarial presente nos dados originais, antes de qualquer agrupamento ou processamento dessas faixas.

**Como interpretar o gráfico:**

* **Eixo Vertical (Faixa Salarial):** Lista as diferentes categorias de faixas salariais mensais que foram reportadas ou coletadas. Cada barra horizontal corresponde a uma dessas faixas.
* **Eixo Horizontal (Contagem):** Indica o número de vezes que cada faixa salarial aparece no conjunto de dados. O comprimento da barra é diretamente proporcional a essa contagem.
* **Barras:** Cada barra representa uma faixa salarial específica. Quanto mais longa a barra, maior o número de indivíduos ou registros que se enquadram naquela faixa salarial.

**Análise da Distribuição Apresentada:**

Observando o gráfico, podemos extrair as seguintes informações sobre a distribuição das faixas salariais originais:

* **Faixas Mais Comuns:**
    * A faixa salarial **"de R$8.001/mês a R$ 12.000/mês"** é a mais frequente, com uma contagem significativamente maior que as outras (aproximadamente 790 ocorrências).
    * Seguida por **"de R$4.001/mês a R$ 6.000/mês"** (aproximadamente 630-640 ocorrências).
    * E depois **"de R$6.001/mês a R$ 8.000/mês"** (aproximadamente 540 ocorrências).

* **Faixas Menos Comuns:**
    * Várias faixas salariais têm contagens muito baixas, indicando que são raras no conjunto de dados. Estas incluem, por exemplo:
        * "de R$101/mês a R$ 2.000/mês" (contagem muito próxima de zero, quase imperceptível).
        * "Acima de R$ 40.001/mês".
        * "Menos de R$ 1.000/mês".
        * "de R$30.001/mês a R$ 40.000/mês".
        * "de R$25.001/mês a R$ 30.000/mês".

* **Desbalanceamento:** O gráfico demonstra claramente um desbalanceamento entre as diferentes faixas salariais. Algumas poucas faixas concentram a maioria dos registros, enquanto muitas outras são representadas por um número pequeno de instâncias. Este desbalanceamento é uma característica importante dos dados e frequentemente leva à necessidade de agrupar faixas salariais (como visto no código do notebook) para criar classes mais equilibradas e significativas para modelos de machine learning.


### distribuicao_faixas_salariais_agrupadas 1_2
![distribuicao_faixas_salariais_agrupadas](https://github.com/user-attachments/assets/0844c00b-371f-49c3-82d2-505ec0830728)

O gráfico apresentado é um **gráfico de barras horizontais** intitulado "Distribuição de Faixas Salariais Agrupadas". Ele ilustra a frequência (ou contagem) de cada faixa salarial **após** estas terem sido agrupadas em categorias mais amplas. Este agrupamento é uma etapa comum de pré-processamento de dados, realizada para simplificar o problema de classificação, reduzir o número de classes e, potencialmente, lidar com classes minoritárias no conjunto de dados original.

**Como interpretar o gráfico:**

* **Eixo Vertical (Faixa Salarial):** Lista as novas categorias de faixas salariais agrupadas. Cada barra horizontal corresponde a uma dessas faixas consolidadas.
* **Eixo Horizontal (Contagem):** Indica o número de vezes que cada faixa salarial agrupada aparece no conjunto de dados. O comprimento da barra é diretamente proporcional a essa contagem.
* **Barras:** Cada barra representa uma faixa salarial agrupada específica. Quanto mais longa a barra, maior o número de indivíduos ou registros que se enquadram naquela faixa salarial consolidada.

**Análise da Distribuição Apresentada:**

Observando o gráfico, podemos notar o seguinte sobre a distribuição das faixas salariais após o agrupamento:

* **Faixas Mais Comuns (Agrupadas):**
    * A faixa **"R$8.001/mês a R$ 16.000/mês"** é a mais frequente entre as agrupadas (com uma contagem de aproximadamente 1180).
    * Seguida de perto pela faixa **"R$4.001/mês a R$ 8.000/mês"** (com uma contagem de aproximadamente 1170).
    * A faixa **"R$2.001/mês a R$ 4.000/mês"** aparece em seguida, com uma contagem consideravelmente menor (aproximadamente 530).

* **Faixas Menos Comuns (Agrupadas):**
    * A faixa **"Acima de R$ 30.000/mês"** é a menos frequente, com uma contagem muito baixa em comparação com as outras (menos de 50).
    * As faixas **"Até R$ 2.000/mês"** e **"R$16.001/mês a R$ 30.000/mês"** possuem contagens intermediárias, mas ainda significativamente menores que as duas faixas mais populosas (ambas em torno de 180-200).

* **Impacto do Agrupamento:**
    * Comparando com uma distribuição de faixas salariais originais (que tipicamente teria mais categorias e maior granularidade), este gráfico mostra um número reduzido de classes.
    * Embora o agrupamento possa ter tornado algumas classes mais balanceadas (especialmente as duas primeiras), ainda existe um desbalanceamento notável, com a categoria de salário mais alto ("Acima de R$ 30.000/mês") sendo uma classe minoritária clara. Este desbalanceamento é uma consideração importante para o treinamento do modelo de machine learning.


### correlacao_variaveis_faixa_salarial 1_2
![correlacao_variaveis_faixa_salarial](https://github.com/user-attachments/assets/18aea812-9bdf-42a8-ae94-46dd2d18a141)

O gráfico apresentado é um **gráfico de barras verticais** intitulado "Correlação (Cramer's V) com Faixa Salarial Agrupada". Ele exibe a força da associação entre diversas variáveis categóricas (features) e a variável alvo, que é a "Faixa Salarial Agrupada". A medida de associação utilizada é o **Coeficiente V de Cramer**.

**Como interpretar o gráfico:**

* **Eixo Vertical (Coeficiente de Cramer's V):** Este eixo mostra o valor do Coeficiente V de Cramer, que varia de 0 a 1.
    * Um valor próximo de **0** indica uma associação fraca ou inexistente entre a feature e a faixa salarial agrupada.
    * Um valor próximo de **1** indica uma associação forte entre a feature e a faixa salarial agrupada.
* **Eixo Horizontal (Features):** Este eixo lista as diferentes variáveis categóricas que foram analisadas em relação à faixa salarial agrupada. As legendas estão rotacionadas para facilitar a leitura.
* **Barras:** Cada barra representa uma feature. A altura da barra é proporcional ao valor do Coeficiente V de Cramer para aquela feature, indicando visualmente a força de sua associação com a faixa salarial agrupada. As barras estão ordenadas da maior para a menor associação.

**Análise das Associações Apresentadas (da mais forte para a mais fraca):**

1.  **Nível de senioridade:** Apresenta a associação **mais forte** com a faixa salarial agrupada, com um Coeficiente V de Cramer de aproximadamente **0.55**. Isso sugere que o nível de senioridade do profissional é o indicador mais forte da sua faixa salarial entre as features analisadas.
2.  **Tempo de experiência na área de dados:** Possui a segunda associação mais forte, com um coeficiente em torno de **0.30**.
3.  **Nível de ensino alcançado:** Mostra uma associação moderada, com um coeficiente de aproximadamente **0.23**.
4.  **Cargo atual:** Apresenta uma associação de cerca de **0.19**.
5.  **Setor de atuação da empresa:** A associação é mais fraca, com um coeficiente em torno de **0.09**.
6.  **UF onde mora:** Mostra uma associação semelhante à anterior, com um coeficiente de aproximadamente **0.08**.
7.  **Área de formação acadêmica:** Apresenta uma associação de cerca de **0.07**.
8.  **Gênero do profissional:** A associação é bastante fraca, com um coeficiente em torno de **0.04**.
9.  **Cor/Raça/Etnia:** Apresenta a associação **mais fraca** entre as features listadas, com um coeficiente também em torno de **0.04**.

**Importância da Análise:**

Este tipo de análise é útil por várias razões:

* **Entendimento dos Dados:** Ajuda a entender quais características dos profissionais estão mais relacionadas com suas faixas salariais.
* **Seleção de Features:** Features com associações muito baixas com a variável alvo podem, em alguns casos, ser consideradas menos importantes para um modelo preditivo e, potencialmente, descartadas para simplificar o modelo ou reduzir o ruído. No entanto, mesmo features com baixa correlação individual podem ser úteis em combinação com outras.
* **Direcionamento de Análises Futuras:** Pode indicar quais aspectos merecem uma investigação mais aprofundada.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Resultados obtidos com os Modelos 2º pergunta orietada a dados

# Resultados do Modelo Random Forest Regressor

Este modelo foi desenvolvido para prever a **faixa salarial média (R$/mês)** de profissionais da área de dados no Brasil. Ele utiliza como base a junção de duas fontes de dados:

- **[State of Data BR 2023 - Kaggle](https://www.kaggle.com/datasets)**: informações de profissionais atuando na área de dados.
- **[MICRODADOS_ED_SUP_IES_2023 - MEC](http://inep.gov.br/microdados)**: características da infraestrutura educacional por região do país.

## Modelo

Utilizamos o algoritmo **Random Forest Regressor**, com os seguintes hiperparâmetros:

```python
RandomForestRegressor(
    max_depth=None,
    max_features='sqrt',
    min_samples_leaf=2,
    min_samples_split=5,
    n_estimators=100,
    random_state=42
)
```
## Métricas de Avaliação

| **Métrica**                          | **Valor**    |
| :----------------------------------- | :----------- |
| **MAE (Erro Médio Absoluto)**        | R\$ 2.882,21 |
| **R² (Coeficiente de Determinação)** | 0.38         |

## Importância das Variáveis

| **Variável**                            | **Importância (%)** |
| :-------------------------------------- | :-----------------: |
| **nivel\_cod (Nível de cargo)**         |        73.29%       |
| experiencia\_num (Tempo de experiência) |        23.72%       |
| docentes\_mestrado\_regiao              |        0.82%        |
| tecnicos\_regiao                        |        0.78%        |
| docentes\_regiao                        |        0.70%        |
| num\_ies\_regiao                        |        0.70%        |

##  Interpretação

| **Insight**         | **Descrição**                                                    |
| :------------------ | :--------------------------------------------------------------- |
| Fator Principal     | O nível do cargo é o fator mais relevante para a faixa salarial. |
| Experiência         | O tempo de experiência também tem peso significativo.            |
| Variáveis Regionais | Impacto reduzido na predição salarial.                           |

## 🧾 Conclusão
**Embora o modelo apresente desempenho moderado (R² = 0.38), ele oferece bons insights sobre os fatores que mais influenciam o salário na área de dados no Brasil. A predominância das variáveis individuais em relação às regionais sugere que decisões salariais estão mais associadas a fatores pessoais do que à estrutura educacional da região.**

# Relatório de Resultados e Insights (Modelo Random Forest Classifier)

**1. Resumo do Experimento**
Foi treinado um modelo de classificação RandomForest para prever faixas salariais a partir de variáveis relacionadas à experiência, nível profissional e dados regionais de educação. O modelo foi avaliado em um conjunto de teste com 3 exemplos, cada um representando uma faixa salarial distinta.

**2. Resultados**

| Métrica                | Valor   |
| :--------------------- | :------ |
| **Acurácia**           | 33.33%  |

**Matriz de Confusão**

|                        | Predito: R$ 1k-2k | Predito: R$ 2k-3k | Predito: R$ 3k-4k |
|------------------------|:-----------------:|:-----------------:|:-----------------:|
| **Real: R$ 1k-2k**     |        0          |        1          |        0          |
| **Real: R$ 2k-3k**     |        0          |        1          |        0          |
| **Real: R$ 3k-4k**     |        0          |        1          |        0          |

**Matriz de Confusão**

| Classe             | Predito: R$ 1k-2k | Predito: R$ 2k-3k | Predito: R$ 3k-4k |
|--------------------|:-----------------:|:-----------------:|:-----------------:|
| Real: R$ 1k-2k     |        0          |        1          |        0          |
| Real: R$ 2k-3k     |        0          |        1          |        0          |
| Real: R$ 3k-4k     |        0          |        1          |        0          |

**Relatório de Classificação**

| Classe                          | Precision | Recall | F1-score | Suporte |
|----------------------------------|:---------:|:------:|:--------:|:-------:|
| de R$ 1.001/mês a R$ 2.000/mês   |   0.00    |  0.00  |   0.00   |    1    |
| de R$ 2.001/mês a R$ 3.000/mês   |   0.33    |  1.00  |   0.50   |    1    |
| de R$ 3.001/mês a R$ 4.000/mês   |   0.00    |  0.00  |   0.00   |    1    |
| **Acurácia**                     |           |        |  0.33    |    3    |
| **Macro avg**                    |   0.11    |  0.33  |   0.17   |    3    |
| **Weighted avg**                 |   0.11    |  0.33  |   0.17   |    3    |

**Importância das Variáveis**

| Feature                    | Importância |
|----------------------------|:----------:|
| experiencia_num            |   0.00%    |
| nivel_cod                  |   0.00%    |
| docentes_regiao            |   0.00%    |
| tecnicos_regiao            |   0.00%    |
| docentes_mestrado_regiao   |   0.00%    |
| num_ies_regiao             |   0.00%    |


**3. Insights**
Baixa performance: O modelo apresentou acurácia de 33%, equivalente ao acaso para três classes. O modelo só conseguiu prever corretamente a classe "de R$ 2.001/mês a R$ 3.000/mês".

Matriz de confusão: Todas as amostras foram classificadas na mesma faixa salarial, indicando que o modelo não conseguiu distinguir entre as classes.

Importância das variáveis: Todas as features tiveram importância zero, sugerindo que o modelo não encontrou padrões relevantes nos dados para realizar as previsões.

Tamanho da amostra: O principal motivo para o baixo desempenho é o número extremamente reduzido de exemplos (apenas 6 no total, 3 no teste). Modelos de machine learning geralmente precisam de dezenas ou centenas de exemplos por classe para aprender padrões úteis.

Avisos de métricas: O relatório de classificação apresenta avisos sobre métricas indefinidas, pois algumas classes não foram previstas pelo modelo.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Resultados obtidos com os Modelos 3º pergunta orietada a dados

### Arvóre de decição LigthGBM (Modelo 3.1) 
---
## 1 RESULTADOS E DISCUSSÃO 

Esta seção detalha os resultados obtidos com o modelo LightGBM para a classificação binária da faixa salarial ("Salário Alto" vs. "Salário Baixo"). A análise abrange métricas de desempenho, a importância dos atributos (features) e a interpretação dos gráficos gerados para extrair insights.

### 1.1 DESEMPENHO DO MODELO

O modelo final demonstrou um desempenho robusto na tarefa de classificação. A seguir, são apresentadas as principais características e métricas de desempenho.

* Tipo de Classificação: Binária
* Classes da Variável Alvo (codificadas): ['Salário Alto', 'Salário Baixo'] (onde "Salário Alto" corresponde à classe 0 e "Salário Baixo" à classe 1 após LabelEncoding)
* Acurácia Média na Validação Cruzada (Optuna): 0.8505
* Acurácia do Modelo Final no Conjunto de Treinamento: 0.8583
* Número de Árvores no Modelo Final (após early stopping): 105

### 1.2 Avaliação no conjunto de teste

Os resultados da avaliação do modelo final, aplicados sobre o conjunto de teste, são apresentados na Tabela 1.

Tabela 1 – Métricas de avaliação do modelo no conjunto de teste
------------------------------------------------------------------
| Métrica                       | Valor          |
|-------------------------------|----------------|
| Acurácia no Teste             | 0.8335         |
| Precisão Média (Macro Avg)    | 0.8331         |
| Precisão Média (Weighted Avg) | 0.8335         |
| F1-Score (Ponderado)          | 0.8335         |
| ROC AUC (Binário)             | 0.9234         |
------------------------------------------------------------------

A acurácia de 0.8335 indica que o modelo classificou corretamente aproximadamente 83,35% das instâncias no conjunto de teste. O valor de ROC AUC, 0.9234, é um excelente indicador da capacidade do modelo em distinguir entre as classes, sugerindo alta performance na separação. As precisões médias e o F1-Score ponderado, todos em torno de 0.83, mostram um bom equilíbrio geral entre precisão e recall.

### 1.3 Relatório de classificação detalhado

A Tabela 2 apresenta o relatório de classificação detalhado, que expande as métricas para cada uma das classes individualmente.

Tabela 2 – Relatório de classificação detalhado no conjunto de teste
------------------------------------------------------------------------------------
| Classe        | Precision      | Recall         | F1-score       | Support        |
|:--------------|:---------------|:---------------|:---------------|:---------------|
| Salário Alto  | 0.84           | 0.84           | 0.84           | 622            |
| Salário Baixo | 0.83           | 0.83           | 0.83           | 567            |
|               |                |                |                |                |
| accuracy      |                |                | 0.83           | 1189           |
| macro avg     | 0.83           | 0.83           | 0.83           | 1189           |
| weighted avg  | 0.83           | 0.83           | 0.83           | 1189           |
------------------------------------------------------------------------------------


O suporte (Support) indica uma distribuição bem equilibrada entre as classes no conjunto de teste (622 instâncias para "Salário Alto" e 567 para "Salário Baixo"). A precisão (Precision) para a classe "Salário Alto" foi de 0.84, indicando que 84% das predições para esta classe estavam corretas. De forma similar, o recall de 0.84 demonstra que o modelo identificou corretamente 84% de todos os casos reais de "Salário Alto". Resultados análogos foram observados para a classe "Salário Baixo". Os valores do F1-score e a proximidade entre as métricas "macro avg" e "weighted avg" reforçam o bom equilíbrio do modelo.

---
## 2 CONFIGURAÇÃO DO MODELO

### 2.1 Atributos selecionados

O processo de seleção de atributos com o método RFECV (Recursive Feature Elimination with Cross-Validation) indicou um conjunto final de 6 atributos, a saber: ['P1_a_1', 'P1_l', 'P2_i', 'P2_g_Nivel', 'P2_f_Cargo_Atual', 'Regiao_Mapeada'].

### 2.2 Hiperparâmetros do modelo

Os hiperparâmetros do modelo LightGBM foram otimizados com a ferramenta Optuna. Os valores selecionados foram:
* n_estimators: 1100 (valor inicial, com o modelo final utilizando 105 árvores devido ao early stopping)
* learning_rate: 0.06509228494862056
* num_leaves: 80
* max_depth: 12
* min_child_samples: 25
* subsample: 0.5
* colsample_bytree: 0.6
* reg_alpha: 1.5671157141467156
* reg_lambda: 14.655960291115573
* min_split_gain: 0.3854595582770911
* min_child_weight: 0.1393188921160219

----
## 3 ANÁLISE DOS RESULTADOS E INSIGHTS

A seguir, são apresentadas as análises dos resultados visuais obtidos.

### 3.1 Matriz de confusão

A matriz de confusão, apresentada na Figura 1, visualiza o desempenho do modelo em termos de classificações corretas e incorretas para cada classe.

Figura 1 – Matriz de confusão normalizada para o conjunto de teste
![Image](https://github.com/user-attachments/assets/2e9d9ea5-2a0b-42ae-bd7e-5d4cc188a293)

As porcentagens na diagonal principal representam as taxas de acerto (recall). O modelo classificou corretamente 84,08% dos casos que eram "Salário Alto" e 82,54% dos casos que eram "Salário Baixo". Os erros, representados fora da diagonal principal, mostram que aproximadamente 15,92% dos "Salário Alto" foram classificados incorretamente como "Salário Baixo", e 17,46% dos "Salário Baixo" foram classificados como "Salário Alto". O desempenho é similar e bom para ambas as classes, com uma taxa de erro relativamente equilibrada.

### 3.2 Importância dos atributos

A Figura 2 ilustra quais atributos tiveram o maior impacto nas decisões do modelo.

Figura 2 – Importância dos atributos (features) do modelo LightGBM
![Image](https://github.com/user-attachments/assets/48fd3daf-dc28-4a8f-bc89-9459b1945aee)

Observa-se que a experiência (`P2_i`), o cargo atual (`P2_f_Cargo_Atual`) e o nível de senioridade (`P2_g_Nivel`) são os preditores mais fortes da faixa salarial. O nível de ensino (`P1_l`), a faixa etária (`P1_a_1`) e a região (`Regiao_Mapeada`) também apresentam contribuições significativas, sugerindo a influência de fatores demográficos e geográficos na remuneração.

### 3.3 Distribuição salarial por cargo

A Figura 3 exibe a distribuição das faixas salariais para os 15 cargos mais frequentes na amostra.

Figura 3 – Distribuição de faixa salarial por Top 15 cargos
![Image](https://github.com/user-attachments/assets/ba7c4d30-870f-48f7-951f-cc2263f9c65a)

A análise indica que cargos como "Cientista de Dados" e "Engenheiro/Arquiteto de Dados" possuem predominância de "Salário Alto". Em contrapartida, cargos como "Analista de Dados/Data Analyst" e "Analista de BI" concentram a maior parte dos profissionais na faixa de "Salário Baixo". Este resultado pode guiar investigações sobre a valorização de diferentes especialidades no mercado de dados.

### 3.4 Distribuição salarial por nível de senioridade

A relação entre o nível de senioridade e a faixa salarial é detalhada na Figura 4.

Figura 4 – Distribuição de faixa salarial por nível de senioridade
![Image](https://github.com/user-attachments/assets/3ee422da-3ebc-4ab5-92d0-208953caf231)

Como esperado, o nível "Júnior" está quase exclusivamente associado a "Salário Baixo", enquanto o nível "Sênior" apresenta predominância de "Salário Alto". O nível "Pleno", que concentra o maior número de respondentes, tem uma maioria na categoria "Salário Baixo". O gráfico demonstra a progressão salarial esperada com o avanço na carreira.

### 3.5 Distribuição da experiência por faixa salarial

As Figuras 5 e 6 apresentam a distribuição do tempo de experiência para cada faixa salarial por meio de um boxplot e um violin plot, respectivamente.

Figura 5 – Boxplot do tempo de experiência por faixa salarial
![Image](https://github.com/user-attachments/assets/390ae2c5-36e8-4af9-9eda-ba46a1abaf7b)

Figura 6 – Violin plot do tempo de experiência por faixa salarial
![Image](https://github.com/user-attachments/assets/c8674650-d96c-4932-972b-c8d1a0ac64f9)

A análise dos gráficos revela que a mediana de experiência para a faixa de "Salário Baixo" é significantemente inferior à da faixa de "Salário Alto" (aproximadamente 1-2 anos contra cerca de 5 anos). O violin plot (Figura 6) sugere que a distribuição para "Salário Alto" é mais ampla e possui múltiplas concentrações, indicando que diferentes níveis de experiência podem alcançar remunerações mais altas, possivelmente a depender de outros fatores como cargo ou empresa.

---
## 4 CONSIDERAÇÕES FINAIS

Os resultados indicam que o modelo LightGBM possui bom potencial preditivo para a classificação de faixas salariais. A análise dos atributos e das distribuições fornece insights valiosos sobre os fatores que influenciam a remuneração no setor de dados. A definição do ponto de corte que separa as classes ("Salário Alto" e "Salário Baixo") é um elemento crucial que afeta diretamente a interpretação dos resultados e o balanceamento do modelo, sendo um parâmetro que pode ser ajustado em iterações futuras para refinar a análise.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Resultados obtidos com os Modelos 3º pergunta orietada a dados

###  Rede Neural com Embeddings e Otimização via Ray Tune (RNA v2) - (Modelo 3.2)
---
## 1 RESULTADOS E DISCUSSÃO DO MODELO DE REDE NEURAL (V8)

Esta seção detalha os resultados da avaliação e treinamento de um modelo de Rede Neural Artificial (RNA) para a classificação de faixas salariais. A análise inclui a performance do modelo final, os hiperparâmetros otimizados por meio do Ray Tune, e a interpretação dos gráficos de correlação e importância de atributos.

## 2 ANÁLISE EXPLORATÓRIA E CORRELAÇÃO DE ATRIBUTOS

Antes do treinamento do modelo, foi realizada uma análise de correlação entre os atributos para entender as relações lineares (Pearson) e não lineares (Correlação de Distância) existentes nos dados.

Figura 1 – Heatmap de Correlação de Pearson entre os atributos
![Image](https://github.com/user-attachments/assets/f29ed58e-2175-4b2f-b5c9-e963f07fb542)

A análise de Correlação de Pearson (Figura 1) indica correlações lineares moderadas entre o tempo de experiência (`P2_i`), o nível de senioridade (`P2_g_Nivel`) e o nível de ensino (`P1_l`), o que é um comportamento esperado. A correlação de distância, que poderia capturar relações não lineares, não pôde ser gerada devido a um erro na biblioteca `dcor` (`module 'dcor' has no attribute 'pairwise'`).

## 3 OTIMIZAÇÃO E TREINAMENTO DO MODELO

O modelo de rede neural foi otimizado utilizando a biblioteca Ray Tune, que explorou 75 combinações de hiperparâmetros em um tempo limite de 2 horas. O objetivo foi maximizar a acurácia no conjunto de validação.

### 3.1 Melhores hiperparâmetros

O processo de otimização identificou o seguinte conjunto de hiperparâmetros como o de melhor desempenho:

* **num_hidden_layers**: 2
* **dense_units_1**: 64
* **dropout_1**: 0.35
* **dense_units_2**: 32
* **dropout_2**: 0.15
* **learning_rate_nn**: 0.000487
* **batch_size**: 64
* **optimizer**: 'nadam'
* **l2_strength_embedding**: 0.000478
* **l2_strength_dense**: 0.000139
* **early_stopping_patience**: 10
* **Demais hiperparâmetros**: Conforme log do Ray Tune.

## 4 AVALIAÇÃO DO MODELO FINAL

Após a otimização, o modelo final foi treinado com todos os dados de treino e avaliado no conjunto de teste. A Tabela 1 resume as principais métricas de performance.

Tabela 1 – Métricas de avaliação do modelo final no conjunto de teste
------------------------------------------------------------------
| Métrica                       | Valor          |
|-------------------------------|----------------|
| Acurácia no Teste             | 0.8452         |
| F1-Score (Ponderado) no Teste | 0.8451         |
| ROC AUC no Teste              | 0.9272         |
------------------------------------------------------------------

A acurácia final de **0.8452** e a ROC AUC de **0.9272** indicam um modelo com forte capacidade preditiva e boa distinção entre as classes "Salário Alto" e "Salário Baixo". O F1-Score ponderado, próximo à acurácia, sugere um bom equilíbrio entre precisão e recall.

### 4.1 Matriz de confusão

A matriz de confusão (Figura 2) visualiza o desempenho da classificação para cada classe no conjunto de teste.

Figura 2 – Matriz de Confusão para o conjunto de teste (RNA Final)
![Image](https://github.com/user-attachments/assets/f91e740a-ee5d-4e1d-881e-c7785dad2b9a)

A matriz demonstra que o modelo possui um desempenho equilibrado. Para a classe "Salário Alto", o modelo classificou corretamente 519 das 622 instâncias (recall de 83.4%). Para a classe "Salário Baixo", foram 489 acertos em 567 instâncias (recall de 86.2%). Os erros de classificação entre as classes são relativamente simétricos.

## 4.2 ANÁLISE DE IMPORTÂNCIA DOS ATRIBUTOS

A importância dos atributos foi calculada utilizando a técnica de "Permutation Importance", que mede a queda na acurácia do modelo ao embaralhar aleatoriamente os valores de cada atributo, um por vez.

Figura 3 – Importância de Atributos por Permutação (no Conjunto de Teste)
![Image](https://github.com/user-attachments/assets/4d0ece44-1cab-4fd5-852e-b64a9f6dfc92)

A análise (Figura 3) revela que o **Nível de Senioridade (`P2_g_Nivel`)** é, de longe, o atributo mais influente para a predição da faixa salarial, causando a maior queda de acurácia quando seus valores são permutados. Em seguida, o **Cargo Atual (`P2_f_Cargo_Atual`)** e o **Tempo de Experiência (`P2_i`)** aparecem como os próximos preditores mais relevantes. Atributos como Faixa Etária, Região e Nível de Ensino possuem uma importância secundária, enquanto Gênero (`P1_b`) apresentou um impacto nulo na performance do modelo.

## 5 CONSIDERAÇÕES FINAIS

O modelo de Rede Neural Artificial V8, após otimização de hiperparâmetros, demonstrou ser robusto e preciso, com uma acurácia de 84,52% no conjunto de teste. A análise de importância dos atributos confirmou que fatores diretamente ligados à progressão de carreira (nível, cargo e experiência) são os principais determinantes da faixa salarial, conforme aprendido pelo modelo. Os resultados indicam que o modelo é confiável para a tarefa de classificação proposta.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# _Interpretação dos modelos_

*   [Interpretação dos modelo 1º pergunta orientada a dados](#interpretação-dos-modelo-1º-pergunta-orientada-a-dados)
	*   [Interpretação do modelo 1_1](#interpretação-do-modelo-1_1)
	*   [Interpretação do modelo 2_1](#interpretação-do-modelo-2_1)
 
*   [Interpretação dos modelo 2º pergunta orientada a dados](#interpretação-dos-modelo-2º-pergunta-orientada-a-dados)
	*    [Interpretação do modelo 1_2](#interpretação-do-modelo-1_2)
	*    [Interpretação do modelo 2_2](#interpretação-do-modelo-2_2)
	 
*   [Interpretação dos modelo 3º pergunta orientada a dados](#interpretação-dos-modelo-3º-pergunta-orientada-a-dados)
	*    [Interpretação do modelo 1_3](#interpretação-do-modelo-1_3)
	*    [Interpretação do modelo 2_3](#interpretação-do-modelo-2_3)


## Interpretação dos modelo 1º pergunta orientada a dados

## Interpretação do modelo 1_1

### I. Especificação do Modelo e Parâmetros Chave

#### a. Tipo de Modelo de Machine Learning
O modelo de machine learning implementado no código Python é um **`RandomForestClassifier`**. Este é um modelo de ensemble que utiliza múltiplas árvores de decisão para realizar classificações, combinando as previsões de cada árvore para obter um resultado final mais robusto e preciso.

#### b. Principais Hiperparâmetros do Modelo Final Treinado
O modelo final (`best_rf_model` no código) foi obtido após um processo de otimização de hiperparâmetros utilizando `GridSearchCV`. Os principais hiperparâmetros do `best_rf_model` são:

1.  **`n_estimators`: 100**
    * **Relevância**: Define o número de árvores de decisão que compõem a floresta. Um número maior de árvores geralmente leva a um desempenho melhor e mais estável, mas também aumenta o custo computacional. 100 é um valor comum e razoável.

2.  **`max_depth`: `None`**
    * **Relevância**: Controla a profundidade máxima de cada árvore individual. Se `None`, os nós são expandidos até que todas as folhas sejam puras ou até que todas as folhas contenham menos amostras do que `min_samples_split`. Neste modelo, a profundidade é efetivamente limitada por `min_samples_leaf` e `min_samples_split`.

3.  **`min_samples_split`: 15**
    * **Relevância**: Especifica o número mínimo de amostras que um nó deve ter para poder ser dividido. Ajuda a controlar a complexidade da árvore e previne o overfitting, evitando que a árvore crie divisões baseadas em poucas amostras.

4.  **`min_samples_leaf`: 7**
    * **Relevância**: Define o número mínimo de amostras que devem estar presentes em um nó folha (um nó terminal). Assim como `min_samples_split`, este parâmetro ajuda a suavizar o modelo e a evitar o overfitting, garantindo que cada decisão final seja baseada em um número suficiente de exemplos.

5.  **`class_weight`: `'balanced_subsample'`**
    * **Relevância**: Este parâmetro é crucial para lidar com classes desbalanceadas. `'balanced_subsample'` ajusta os pesos das classes de forma inversamente proporcional às suas frequências, mas os pesos são calculados para cada subamostra de bootstrap usada para treinar cada árvore. Isso ajuda o modelo a dar mais importância à classe minoritária durante o treinamento.

6.  **`random_state`: 42**
    * **Relevância**: Garante a reprodutibilidade dos resultados. Ao fixar o `random_state`, a aleatoriedade envolvida na construção do Random Forest (como a seleção de amostras para bootstrap e a seleção de features em cada divisão) será a mesma em diferentes execuções.

7.  **`n_jobs`: -1**
    * **Relevância**: Utiliza todos os processadores disponíveis para paralelizar o treinamento das árvores, o que pode acelerar significativamente o processo de treinamento.

Estes parâmetros foram selecionados pelo `GridSearchCV` como a melhor combinação para maximizar a métrica `balanced_accuracy`, indicando um foco em obter um bom desempenho em ambas as classes da variável alvo (salário alto vs. salário baixo/médio).

---

### II. Fatores Preditivos Dominantes: Uma Análise de 'Feature Importances'

#### a. Importância Global das Features
O modelo `RandomForestClassifier` calcula a importância de cada feature com base em quão bem ela contribui para a pureza dos nós nas árvores de decisão (geralmente usando a redução média da impureza de Gini). As features mais importantes identificadas pelo modelo (`best_rf_model.feature_importances_`), ordenadas da mais para a menos importante, são:

1.  **`senioridade_encoded`**: Importância relativa de aproximadamente **0.4053**
2.  **`experiencia_profissional_encoded`**: Importância relativa de aproximadamente **0.3588**
3.  **`formacao_academica_encoded`**: Importância relativa de aproximadamente **0.0952**
4.  **`UF onde mora_SP`**: Importância relativa de aproximadamente **0.0125**
5.  **`Área de formação acadêmica_Economia/ Administração / Contabilidade / Finanças/ Negócios`**: Importância relativa de aproximadamente **0.0110**
6.  **`Área de formação acadêmica_Computação / Engenharia de Software / Sistemas de Informação/ TI`**: Importância relativa de aproximadamente **0.0087**
7.  **`Setor de atuação da empresa_Tecnologia/Fábrica de Software`**: Importância relativa de aproximadamente **0.0083**
8.  **`UF onde mora_RJ`**: Importância relativa de aproximadamente **0.0077**
9.  **`Setor de atuação da empresa_Finanças ou Bancos`**: Importância relativa de aproximadamente **0.0076**
10. **`Área de formação acadêmica_Outras Engenharias`**: Importância relativa de aproximadamente **0.0068**

*(As demais features apresentam importâncias progressivamente menores.)*

#### b. Classificação de 'Formação Acadêmica' e 'Experiência Profissional'
Conforme a lista acima:
* **`experiencia_profissional_encoded`** é a **segunda feature mais importante** (0.3588).
* **`formacao_academica_encoded`** (que representa o nível de ensino alcançado) é a **terceira feature mais importante** (0.0952).
* Além do nível de formação, as **áreas específicas de formação acadêmica** (como `Área de formação acadêmica_Economia/ Administração...` e `Área de formação acadêmica_Computação...`) também aparecem entre as 10 mais importantes, embora com pesos individuais menores que o nível de formação geral.

#### c. Interpretação das Importâncias no Contexto da Disparidade Salarial
As importâncias das features revelam que, para este modelo, os fatores mais determinantes para prever se um profissional de dados terá um salário "alto" ou "baixo/médio" são, nesta ordem:

1.  **Nível de Senioridade (`senioridade_encoded`)**: Este é o fator de maior impacto. O modelo aprendeu que o nível hierárquico do profissional (Júnior, Pleno, Sênior) é o principal diferenciador salarial. Isso está alinhado com a expectativa de mercado, onde a senioridade reflete uma combinação de experiência, responsabilidade e impacto.
2.  **Tempo de Experiência na Área de Dados (`experiencia_profissional_encoded`)**: O segundo fator mais crucial. O número de anos de experiência prática na área de dados influencia fortemente a faixa salarial. O `report.md` já indicava, na seção "Descrição de dados", que a correlação entre Experiência Total e Salário era de 0.54, sugerindo uma relação positiva.
3.  **Nível de Ensino Alcançado (`formacao_academica_encoded`)**: Embora menos influente que senioridade e experiência, a formação acadêmica ainda é o terceiro fator mais importante. Isso sugere que possuir níveis mais altos de educação formal (como Mestrado ou Doutorado) contribui para alcançar salários mais elevados, conforme também indicado na análise exploratória do `report.md` (onde Doutorado tinha a maior mediana salarial).

As demais features, como a localização (especialmente morar em SP ou RJ) e o setor/área de formação específicos, adicionam nuances à previsão, mas têm um peso significativamente menor. Isso indica que, embora esses fatores possam influenciar, o modelo considera senioridade, experiência e nível de formação como os pilares principais da disparidade salarial.

---

### III. Desvendando a Lógica do Modelo: 'Regras de Raciocínio' e Caminhos de Decisão

Sendo um `RandomForestClassifier`, a lógica do modelo é uma agregação das decisões de 100 árvores de decisão. Para elucidar as 'regras de raciocínio', podemos visualizar uma árvore individual do ensemble. O código fornecido gera visualizações de uma árvore (`arvore_exemplo_melhorada.png` e `arvore_exemplo_simplificada.png`). Analisando a `arvore_exemplo_simplificada.png` (com `max_depth=3`):

#### a. Exemplo de Caminhos de Decisão (Decision Paths)
(Baseado na estrutura típica de `plot_tree` e nas features mais importantes)

* **Nó Raiz (Decisão Inicial):** Geralmente a feature mais importante globalmente, ou uma muito importante, como `experiencia_profissional_encoded`.
    * Exemplo: `experiencia_profissional_encoded <= 1.5` (corresponde a menos de 1 a 2 anos de experiência).

* **Caminho 1 (Baixa Experiência):** Se `experiencia_profissional_encoded <= 1.5` é **Verdadeiro**:
    * Próxima Decisão: `senioridade_encoded <= 1.5` (corresponde a Júnior ou Pleno).
        * Se **Verdadeiro** (Júnior/Pleno com pouca experiência):
            * Última Decisão (neste nível de profundidade): `formacao_academica_encoded <= 0.5` (Estudante de Graduação ou Graduação).
                * Se **Verdadeiro**: Leva a um nó folha com alta probabilidade de "Salário Baixo/Médio".
                * Se **Falso** (Pós-graduação ou superior, mas Júnior/Pleno com pouca experiência): Ainda pode levar a "Salário Baixo/Médio", mas talvez com uma probabilidade ligeiramente menor ou com mais amostras da classe "Salário Alto" em comparação ao nó anterior.
        * Se **Falso** (Sênior, mas com pouca experiência - caso menos comum): A árvore faria outra divisão, talvez por `UF onde mora_SP`. Se não for SP, pode ainda levar a "Salário Baixo/Médio", mas se for SP, poderia pender para "Salário Alto" dependendo das amostras.

* **Caminho 2 (Alta Experiência):** Se `experiencia_profissional_encoded <= 1.5` é **Falso** (mais de 1-2 anos de experiência):
    * Próxima Decisão: `senioridade_encoded <= 1.5` (Júnior ou Pleno).
        * Se **Verdadeiro** (Júnior/Pleno com mais experiência):
            * Última Decisão: `formacao_academica_encoded <= 2.5` (Até Pós-graduação).
                * Se **Verdadeiro**: Pode levar a "Salário Alto", mas com menor probabilidade do que um Sênior.
                * Se **Falso** (Mestrado/Doutorado, Pleno com mais experiência): Maior probabilidade de "Salário Alto".
        * Se **Falso** (Sênior com mais experiência):
            * Última Decisão: `UF onde mora_SP <= 0.5`.
                * Se **Falso** (Mora em SP, Sênior com mais experiência): Alta probabilidade de "Salário Alto".
                * Se **Verdadeiro** (Não mora em SP, Sênior com mais experiência): Provavelmente "Salário Alto", mas com menor proporção de amostras dessa classe do que se morasse em SP.

#### b. Como as 'Regras' Ajudam a Entender as Decisões
Esses caminhos ilustram que o modelo não avalia as features isoladamente. Ele aprende combinações de condições. Por exemplo:
* **Pouca experiência + Baixa senioridade + Baixa formação** => Quase certamente Salário Baixo/Médio.
* **Muita experiência + Alta senioridade + Localização em SP** => Alta chance de Salário Alto.
* Casos intermediários são resolvidos por divisões subsequentes que consideram outras features (como setor de atuação, área de formação específica, etc., visíveis na árvore mais profunda).

A árvore mostra que o impacto da `formacao_academica_encoded` é frequentemente avaliado *após* a experiência e a senioridade já terem sido consideradas, o que está alinhado com suas importâncias relativas.

---

### IV. A Interação entre Formação Acadêmica e Experiência Profissional na Disparidade Salarial: Insights Orientados pelo Modelo

#### a. Evidências de Efeitos de Interação
A pergunta central é sobre a **interação** entre formação e experiência. O modelo Random Forest é inerentemente bom em capturar interações, pois os caminhos de decisão são sequências de condições.

1.  **Importância das Features:** O fato de `experiencia_profissional_encoded` (0.3588) e `formacao_academica_encoded` (0.0952) serem ambas importantes sugere que ambas contribuem, mas a experiência tem um peso maior. No entanto, a importância individual não revela totalmente a interação.

2.  **Caminhos de Decisão (Seção III):** As árvores consistentemente usam tanto experiência quanto formação para segmentar os dados. A ordem em que aparecem e as condições subsequentes indicam uma interação. Por exemplo, o "valor" de uma alta formação pode ser diferente dependendo se o profissional já tem muita ou pouca experiência.

3.  **Gráfico de Interação Específico (`interacao_formacao_experiencia.png`):** O código Python gera um heatmap da "Probabilidade de Salário Alto por Formação Acadêmica e Experiência Profissional". Este gráfico é a evidência mais direta da interação:
    * **Pouca Experiência ("Menos de 1 ano"):** A probabilidade de salário alto é baixa para todos os níveis de formação (0.01 para Estudante, 0.02 para Graduação, até 0.04 para Mestrado). Aqui, a formação não consegue compensar a falta de experiência.
    * **Muita Experiência ("de 7 a 10 anos"):** A probabilidade de salário alto é significativamente maior e varia mais acentuadamente com a formação. Um Estudante de Graduação com 7-10 anos de experiência tem 0.67 de probabilidade, enquanto um Doutorado com a mesma experiência tem 0.94.
    * **Impacto Diferencial da Formação:**
        * Com "de 1 a 2 anos" de experiência, passar de "Graduação" (0.20) para "Doutorado" (0.53) aumenta a probabilidade em 0.33.
        * Com "de 7 a 10 anos" de experiência, passar de "Graduação" (0.74) para "Doutorado" (0.94) aumenta a probabilidade em 0.20. Embora o aumento absoluto seja menor, o ponto de partida já é mais alto. O gráfico mostra que para atingir as probabilidades mais altas (>0.90), é necessária uma combinação de alta formação (Mestrado/Doutorado) E alta experiência (7-10 anos).
    * **Limiares de Experiência:**
        * Com **Mestrado ou Doutorado**, a probabilidade de salário alto ultrapassa 0.50 (torna-se mais provável ter salário alto) já com "de 1 a 2 anos" de experiência.
        * Com **Graduação/Bacharelado**, isso só ocorre com "de 3 a 4 anos" de experiência.
        * Com **Pós-graduação (lato sensu)**, também a partir de "de 3 a 4 anos", mas com probabilidades ligeiramente maiores que apenas Graduação.

#### b. Como o Modelo Sugere a Interação
O modelo não apenas considera os efeitos principais da formação e da experiência, mas o `heatmap de interação` (derivado das previsões do modelo em combinações dessas features) e os caminhos de decisão das árvores internas mostram que o efeito de uma variável no salário depende do nível da outra.
* **Formação se torna mais crítica com mais experiência para atingir os salários mais altos:** Ter muitos anos de experiência com apenas graduação leva a uma boa chance de salário alto (ex: 0.74), mas para se aproximar de 100% de chance, um Mestrado ou Doutorado parece ser necessário.
* **Experiência pode compensar (até certo ponto) menor formação:** Um "Estudante de Graduação" com 7-10 anos de experiência (0.67 de probabilidade) tem uma chance maior de salário alto do que um "Doutorado" com menos de 1 ano de experiência (0.03).

---

### V. Síntese: Conectando a Interpretação do Modelo à Pergunta Central da Pesquisa

#### a. Resumo das Principais Descobertas
O modelo `RandomForestClassifier` identificou que o **nível de senioridade**, o **tempo de experiência profissional** e o **nível de formação acadêmica** são os três fatores mais importantes para prever se um profissional de dados no Brasil terá um salário acima ou abaixo de R$ 8.000/mês. A lógica do modelo, visualizada através de árvores de decisão e um heatmap de interação, demonstra que esses fatores não atuam isoladamente.

#### b. Relação com a Pergunta Orientadora
A pergunta central é: "Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial entre profissionais de dados no Brasil?"

A interpretação do modelo fornece as seguintes respostas:

1.  **Ambos são Cruciais, mas a Experiência (e a Senioridade que dela deriva) Pesa Mais Inicialmente:** A experiência profissional (e a senioridade, que está altamente correlacionada com ela) tem um impacto mais forte e imediato na diferenciação salarial do que o nível de formação isoladamente.
2.  **A Formação Acadêmica Potencializa o Retorno da Experiência:** O modelo sugere que, embora a experiência seja vital, níveis mais altos de formação acadêmica (especialmente Mestrado e Doutorado) permitem que os profissionais capitalizem melhor sobre sua experiência acumulada para alcançar os patamares salariais mais elevados. A diferença salarial entre níveis de formação se torna mais evidente para profissionais mais experientes.
3.  **Interação Não Linear e Contextual:** Não há uma regra simples como "X anos de experiência + Y nível de formação = Z salário". O `heatmap de interação` mostra que o impacto de um ano adicional de experiência é diferente para um graduado versus um doutor, e o "valor" de um diploma avançado se manifesta de forma mais acentuada quando combinado com experiência substancial. Profissionais com alta formação mas pouca experiência não necessariamente comandam salários altos imediatamente, enquanto experiência considerável pode, até certo ponto, compensar uma formação menos avançada.

#### c. Limitações da Interpretação e do Modelo
1.  **Variáveis Codificadas:** A interpretação de `_encoded` features requer sempre a referência aos mapeamentos originais. A "distância" entre os valores codificados (ex: 0, 1, 2) pode não refletir linearmente o impacto real.
2.  **Causalidade vs. Correlação:** O modelo identifica correlações e padrões preditivos, mas não estabelece causalidade. Por exemplo, ter um Doutorado e alta experiência leva a um salário alto, ou profissionais que já estão em posições de alto salário são mais propensos a buscar Doutorado?
3.  **Outras Variáveis Não Incluídas ou Menos Importantes no Modelo:** Habilidades técnicas específicas (linguagens de programação, ferramentas), tipo de contrato (CLT, PJ), tamanho da empresa, e outros fatores mencionados no `report.md` como influenciadores da disparidade salarial, tiveram menos peso neste modelo específico ou não foram detalhadamente explorados nas features. A granularidade dessas features pode ser importante.
4.  **Simplificação da Variável Alvo:** A binarização do salário ("Alto" vs. "Baixo/Médio") simplifica o problema, mas perde nuances das faixas salariais intermediárias e extremas.
5.  **Interpretabilidade do Ensemble:** Embora uma árvore possa ser visualizada, a lógica completa do Random Forest (100 árvores) é mais complexa. A importância das features e o heatmap de interação fornecem boas aproximações, mas não capturam todas as sutilezas. Técnicas como SHAP poderiam oferecer insights mais granulares por instância.
6.  **Representatividade dos Dados:** A qualidade e representatividade do dataset original (`dados_limpos.csv`) são cruciais. Se houver vieses nos dados, o modelo os aprenderá.

-------------------------------------------------------------------------------------------------------------------------


## Interpretação do modelo 2_1

### I. Especificação do Modelo e Parâmetros Chave

a.  **Tipo de Modelo de Machine Learning:**
    O modelo implementado no código é um **`GradientBoostingClassifier`** da biblioteca `sklearn.ensemble`. Este é um modelo de ensemble que constrói árvores de decisão de forma sequencial, onde cada nova árvore tenta corrigir os erros cometidos pelas árvores anteriores.

b.  **Principais Hiperparâmetros do Modelo Final Treinado e Relevância:**
    O modelo final foi otimizado usando `RandomizedSearchCV`. Com base na saída do notebook, os melhores hiperparâmetros encontrados foram:
    * **`subsample`: 0.8**
        * *Relevância*: Esta é a fração de amostras a ser usada para ajustar cada árvore individual. Um valor menor que 1.0 introduz estocasticidade, o que pode ajudar a reduzir a variância e prevenir o overfitting. 80% das amostras são usadas para cada árvore.
    * **`n_estimators`: 100**
        * *Relevância*: O número de árvores (estágios de boosting) a serem construídas. Um número maior de árvores geralmente leva a um melhor desempenho, até um certo ponto, mas também aumenta o tempo de treinamento.
    * **`min_samples_split`: 2**
        * *Relevância*: O número mínimo de amostras necessárias para dividir um nó interno de uma árvore. Um valor pequeno como 2 permite que as árvores cresçam bastante, capturando detalhes finos, mas pode levar a overfitting se não controlado por outros parâmetros como `max_depth` ou `min_samples_leaf`.
    * **`min_samples_leaf`: 2**
        * *Relevância*: O número mínimo de amostras que um nó folha (terminal) deve ter. Este parâmetro ajuda a suavizar o modelo e reduzir o overfitting, garantindo que cada decisão final seja baseada em pelo menos 2 amostras.
    * **`max_depth`: 6**
        * *Relevância*: A profundidade máxima de cada árvore de decisão individual. Limitar a profundidade ajuda a controlar a complexidade do modelo e a prevenir o overfitting, pois árvores muito profundas podem memorizar o ruído nos dados de treinamento.
    * **`learning_rate`: 0.2**
        * *Relevância*: Também conhecido como "encolhimento" (shrinkage), este parâmetro reduz a contribuição de cada árvore. Taxas de aprendizado menores geralmente requerem um `n_estimators` maior, mas podem levar a uma melhor generalização. Um valor de 0.2 é relativamente alto, sugerindo uma convergência mais rápida.
    * **`random_state`: 42** (usado na instanciação inicial e no `RandomizedSearchCV`)
        * *Relevância*: Garante a reprodutibilidade dos resultados. O modelo se comportará da mesma maneira em execuções subsequentes.

### II. Fatores Preditivos Dominantes: Uma Análise de 'Feature Importances'

a.  **Feature Importances Globais do Modelo:**
    O notebook `modelo-1-2-arvore-classificatoria-v5.ipynb` **não calcula explicitamente nem exibe as `feature_importances_` do modelo `GradientBoostingClassifier` treinado (`best_gb`)**. A análise de importância de features no notebook é realizada *antes* da modelagem, utilizando o **Coeficiente V de Cramer** para medir a associação entre as variáveis categóricas e a faixa salarial agrupada.
    Embora o V de Cramer meça a força da associação bivariada e não a importância que o modelo GBT aprendeu, ele pode nos dar uma indicação dos atributos que provavelmente serão influentes.

    Com base na análise de V de Cramer realizada no notebook, as features mais associadas à "Faixa salarial agrupada" (em ordem decrescente de importância) foram:
    1.  **Nível de senioridade**: 0.5506
    2.  **Tempo de experiência na área de dados**: 0.2984
    3.  **Nível de ensino alcançado**: 0.2277
    4.  **Cargo atual**: 0.1862
    5.  **Setor de atuação da empresa**: 0.0938
    6.  **UF onde mora**: 0.0787
    7.  **Área de formação acadêmica**: 0.0698
    8.  **Gênero do profissional**: 0.0437
    9.  **Cor/Raça/Etnia**: 0.0428

b.  **Classificação de 'Formação Acadêmica' e 'Experiência Profissional':**
    * **Experiência Profissional**: Representada diretamente por "Tempo de experiência na área de dados" (importância V de Cramer: 0.2984, 2º lugar) e fortemente correlacionada com "Nível de senioridade" (importância V de Cramer: 0.5506, 1º lugar). Claramente, a experiência profissional é um dos fatores mais dominantes.
    * **Formação Acadêmica**: Representada por "Nível de ensino alcançado" (importância V de Cramer: 0.2277, 3º lugar) e "Área de formação acadêmica" (importância V de Cramer: 0.0698, 7º lugar). O nível de ensino alcançado tem uma associação moderada, enquanto a área específica de formação tem uma associação mais fraca com a faixa salarial agrupada, segundo o V de Cramer.

c.  **Interpretação no Contexto da Disparidade Salarial:**
    A análise de V de Cramer sugere que a **experiência** (manifestada como tempo na área e senioridade) é o principal fator associado à variação salarial. Isso está alinhado com a expectativa de que profissionais mais experientes e em níveis hierárquicos mais altos tendem a receber salários maiores. O **nível de escolaridade** também é um fator relevante, indicando que maior qualificação formal está associada a melhores salários. A área de formação específica parece ter um papel menos preponderante. O `report.md` corrobora isso ao mencionar que "profissionais que possuem certificações específicas em grandes empresas costumam receber remunerações mais altas" e que a "experiência, formação acadêmica, setor de atuação e habilidades técnicas" influenciam as diferenças salariais. O modelo GBT, se treinado com essas features, provavelmente aprenderia a dar pesos significativos a elas.

### III. Desvendando a Lógica do Modelo: 'Regras de Raciocínio' e Caminhos de Decisão

a.  **Elucidando a Lógica do `GradientBoostingClassifier`:**
    Um `GradientBoostingClassifier` constrói um ensemble de árvores de decisão. Cada árvore é treinada para corrigir os erros residuais das árvores anteriores. A previsão final é uma combinação ponderada das previsões de todas as árvores.
    * **Extração de Regras Explícitas:** Extrair regras if-then simples de um modelo GBT com muitas árvores (100 neste caso, com `max_depth=6`) é complexo. Não há uma única "árvore" que represente o modelo.
    * **Caminhos de Decisão:** Cada árvore individual possui caminhos de decisão. Por exemplo, uma árvore poderia ter um caminho como:
        * `IF Nível de senioridade_encoded <= 1.5 (Júnior ou Pleno) AND Tempo de experiência_encoded <= 2.5 (até ~4 anos) THEN predict_class_A`
        * `ELSE IF Nível de senioridade_encoded > 1.5 (Sênior) AND Nível de ensino_encoded >= 3 (Mestrado ou Doutorado) THEN predict_class_B`
        O GBT agrega muitos desses caminhos de forma ponderada.
    * **Interpretabilidade via SHAP/LIME:** O notebook fornecido não implementa técnicas como SHAP ou LIME. Essas ferramentas seriam ideais para entender as contribuições de cada feature para previsões específicas (LIME) ou para o comportamento geral do modelo (SHAP). Sem elas, a interpretação da lógica detalhada do GBT é limitada.
    * **Compreensão Baseada na Importância (V de Cramer como Proxy):** Podemos inferir que o modelo provavelmente usa "Nível de senioridade" e "Tempo de experiência" para fazer as primeiras e mais impactantes divisões nos dados, pois estas foram as features com maior associação com o alvo. Subsequentemente, "Nível de ensino" e "Cargo atual" seriam usados para refinar essas divisões.

b.  **Como as 'Regras' Ajudam a Entender as Decisões:**
    Se tivéssemos as regras ou os valores SHAP, poderíamos ver explicitamente como o modelo pondera a formação acadêmica versus a experiência. Por exemplo:
    * Um profissional com "Doutorado" (alta formação) mas "Menos de 1 ano" de experiência (baixa experiência) poderia ser classificado em uma faixa salarial mais baixa do que um profissional com "Graduação" mas "7-10 anos" de experiência.
    * O modelo aprenderia limiares para cada feature (e suas interações) que melhor separam as faixas salariais. Por exemplo, a partir de `X` anos de experiência, o impacto de ter um mestrado no salário pode aumentar significativamente.

### IV. A Interação entre Formação Acadêmica e Experiência Profissional na Disparidade Salarial: Insights Orientados pelo Modelo

a.  **Evidências de Efeitos de Interação:**
    * **Implícito no GBT:** Modelos baseados em árvores como o Gradient Boosting são inerentemente capazes de capturar efeitos de interação entre features. Uma divisão em uma feature (ex: experiência) cria subgrupos, e dentro desses subgrupos, o efeito de outra feature (ex: formação) pode ser diferente. O modelo GBT, ao construir árvores sequencialmente, pode aprender interações complexas.
    * **Ausência de Termos Explícitos:** O código não cria explicitamente features de interação (ex: `experiencia * formacao`). No entanto, o `OneHotEncoder` transforma features categóricas em múltiplas colunas binárias, e o GBT pode então aprender interações entre essas colunas binárias e outras features.
    * **Análise do `report.md`:** O `report.md` na seção "Analises exploratorias de dados" -> "1º Pergunta orientada a dados" -> "Analise exploratoria de dados bases integradas" menciona gráficos como "Salário Médio Estimado vs. Anos de Experiência por Nível de Ensino" e "Relação 3D entre Salário, Experiência e Nível de Ensino". Essas visualizações exploratórias já sugerem uma interação:
        * "As linhas [de salário médio] tendem a se divergir mais à medida que os anos de experiência aumentam. Isso significa que a diferença salarial entre os níveis de ensino se torna mais pronunciada para profissionais mais experientes." (Interpretação do gráfico de linhas no `report.md`).
        * "Para alcançar os salários mais altos, geralmente é necessária uma combinação de alto nível de ensino *e* experiência substancial." (Interpretação do gráfico 3D no `report.md`).
    * **O Modelo GBT provavelmente aprendeu essas interações observadas na EDA.** Por exemplo, o modelo pode ter aprendido que o "retorno" de um doutorado é maior para alguém com 5 anos de experiência do que para alguém com 1 ano.

b.  **Limiares e Criticidade:**
    * O modelo GBT aprende os limiares ótimos para cada divisão nas árvores. Ele poderia, por exemplo, identificar que abaixo de 2 anos de experiência, o nível de formação tem um impacto menor no salário, mas acima de 5 anos de experiência, ter um mestrado ou doutorado se torna um diferenciador mais crítico para alcançar faixas salariais mais altas.
    * Da mesma forma, para cargos de alta senioridade, um nível de formação avançado pode ser um requisito ou um fator que impulsiona significativamente o salário, enquanto para cargos juniores, a experiência prática inicial pode ser mais valorizada que a diferença entre uma graduação e uma pós-graduação.

### V. Síntese: Conectando a Interpretação do Modelo à Pergunta Central da Pesquisa

a.  **Principais Descobertas da Interpretação do Modelo (com base no GBT e proxy de V de Cramer):**
    1.  O modelo `GradientBoostingClassifier` foi treinado para prever faixas salariais agrupadas.
    2.  A experiência profissional (especialmente "Nível de senioridade" e "Tempo de experiência") e o "Nível de ensino alcançado" são os fatores mais fortemente associados (e provavelmente os mais importantes para o modelo GBT) com a disparidade salarial.
    3.  O GBT é capaz de capturar interações complexas entre formação e experiência implicitamente através de sua estrutura baseada em árvores.

b.  **Relação com a Pergunta Orientadora:**
    A pergunta é: "Como fatores como formação acadêmica e experiência profissional interagem para influenciar a disparidade salarial?"
    * **Influência Direta:** Tanto a formação acadêmica quanto a experiência profissional influenciam diretamente a faixa salarial. Maior experiência e maior nível de formação tendem a levar a salários mais altos.
    * **Interação:** O modelo GBT, ao aprender com os dados, implicitamente modela essa interação. A EDA no `report.md` sugere que o valor da formação acadêmica no salário pode ser potencializado pela experiência. Ou seja, um diploma avançado pode render mais (em termos salariais) para alguém que já acumulou alguns anos de experiência, em comparação com um recém-formado com o mesmo diploma. Da mesma forma, a progressão na carreira através da experiência pode ser mais rápida ou levar a tetos salariais mais altos para aqueles com formação mais robusta. O modelo GBT aprenderia a "premiar" essas combinações favoráveis.

c.  **Limitações da Interpretação/Modelo:**
    1.  **Ausência de `feature_importances_` Diretas:** A falta do cálculo explícito da importância das features do modelo GBT treinado no notebook limita a confirmação direta de quais features o *modelo* considerou mais importantes, dependendo-se do V de Cramer como proxy.
    2.  **Interpretabilidade do GBT:** Modelos GBT são caixas-pretas em maior grau que árvores de decisão únicas. Sem ferramentas como SHAP ou LIME, entender *exatamente* como as interações são modeladas é desafiador.
    3.  **Agrupamento da Variável Alvo:** A variável "Faixa salarial agrupada" simplifica o problema, mas pode mascarar nuances dentro das faixas agrupadas. As interações podem ser diferentes para distinguir salários muito altos versus moderadamente altos, por exemplo.
    4.  **Causalidade vs. Correlação:** O modelo identifica associações e padrões preditivos, mas não estabelece causalidade. Por exemplo, maior experiência leva a maior salário, ou pessoas que recebem maiores salários permanecem mais tempo na área? Provavelmente um ciclo virtuoso, mas o modelo não distingue isso.
    5.  **Features Não Utilizadas ou Latentes:** Outros fatores mencionados no `report.md`, como "habilidades técnicas específicas" ou "qualidade da instituição de ensino", não foram explicitamente modelados como features de entrada e podem interagir com formação e experiência.



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Interpretação dos modelo 2º pergunta orientada a dados

### Interpretação do modelo 1_2

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.

-------------------------------------------------------------------------------------------------------------------------

### Interpretação do modelo 2_2

**Parâmetros do Modelo RandomForestClassifier:**

**Matriz de Confusão**

| Classe         | Predito: R$ 1k-2k | Predito: R$ 2k-3k | Predito: R$ 3k-4k |
|---------------|:-----------------:|:-----------------:|:-----------------:|
| Real: R$ 1k-2k |        0          |        1          |        0          |
| Real: R$ 2k-3k |        0          |        1          |        0          |
| Real: R$ 3k-4k |        0          |        1          |        0          |

**Relatório de Classificação**

| Classe                          | Precision | Recall | F1-score | Suporte |
|----------------------------------|:---------:|:------:|:--------:|:-------:|
| de R$ 1.001/mês a R$ 2.000/mês   |   0.00    |  0.00  |   0.00   |    1    |
| de R$ 2.001/mês a R$ 3.000/mês   |   0.33    |  1.00  |   0.50   |    1    |
| de R$ 3.001/mês a R$ 4.000/mês   |   0.00    |  0.00  |   0.00   |    1    |
| **Acurácia**                     |           |        |  0.33    |    3    |
| **Macro avg**                    |   0.11    |  0.33  |   0.17   |    3    |
| **Weighted avg**                 |   0.11    |  0.33  |   0.17   |    3    |

**Importância das Variáveis**

| Feature                    | Importância |
|----------------------------|:----------:|
| experiencia_num            |   0.00%    |
| nivel_cod                  |   0.00%    |
| docentes_regiao            |   0.00%    |
| tecnicos_regiao            |   0.00%    |
| docentes_mestrado_regiao   |   0.00%    |
| num_ies_regiao             |   0.00%    |

**Interpretação:**

Uma importância de 0% significa que a feature raramente (ou nunca) foi usada para dividir os nós das árvores, ou que sua contribuição para a redução da impureza foi insignificante.
Em modelos reais, espera-se que algumas features tenham importâncias significativamente maiores, indicando que são mais relevantes para a classificação.

**Resumo**

O RandomForestClassifier toma decisões combinando várias árvores de decisão, cada uma baseada em regras de splits em features diferentes.

A análise da importância das features mostra quais atributos mais influenciaram as decisões do modelo — sendo essencial para interpretar o “raciocínio” do sistema inteligente.

No caso apresentado, todas as importâncias ficaram em 0%, indicando que o modelo não encontrou padrões relevantes nos dados, provavelmente devido ao baixo volume de dados ou falta de variabilidade nas features.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## Interpretação dos modelo 3º pergunta orientada a dados

### Interpretação do modelo 1_3

## Interpretação Completa do Modelo v7 (LightGBM com RFECV e Optuna) - Incluindo Análise de Correlação e Relatório de Resultados

### I. Especificação do Modelo e Parâmetros Chave

a.  **Tipo de Modelo de Machine Learning:**
    O modelo implementado é um **`LGBMClassifier`** da biblioteca `lightgbm`. Este é um framework de gradient boosting que utiliza árvores de decisão, reconhecido por sua eficiência e performance. O objetivo do modelo é realizar uma classificação binária, distinguindo entre 'Salário Alto' e 'Salário Baixo'.
    * **Codificação da Variável Alvo**: 'Salário Alto' é a classe 0 e 'Salário Baixo' é a classe 1 (após LabelEncoding), conforme indicado no Relatório de Resultados.

b.  **Principais Hiperparâmetros do Modelo Final Treinado e Relevância (conforme Relatório de Resultados, Seção 2.2):**
    O modelo final foi otimizado usando `Optuna` para hiperparâmetros e `RFECV` para seleção de features.
    * **`n_estimators` (configurado em Optuna): 1100**
        * *Relevância*: Número máximo de árvores a serem construídas.
        * *Nota*: O modelo final utilizou **105 árvores** devido ao mecanismo de **early stopping**.
    * **`learning_rate`: 0.06509228494862056**
        * *Relevância*: Controla a contribuição de cada árvore.
    * **`num_leaves`: 80**
        * *Relevância*: Número máximo de folhas por árvore.
    * **`max_depth`: 12**
        * *Relevância*: Profundidade máxima das árvores.
    * **`min_child_samples`: 25**
        * *Relevância*: Número mínimo de amostras necessárias em um nó folha.
    * **`subsample`: 0.5**
        * *Relevância*: Fração de amostras usadas para treinar cada árvore (50%).
    * **`colsample_bytree`: 0.6000000000000001**
        * *Relevância*: Fração de features usadas para treinar cada árvore (60%).
    * **`reg_alpha` (L1 regularização): 1.5671157141467156**
        * *Relevância*: Penaliza pesos grandes, podendo levar à esparsidade.
    * **`reg_lambda` (L2 regularização): 14.655960291115573**
        * *Relevância*: Penaliza pesos grandes quadraticamente.
    * **`min_split_gain`: 0.3854595582770911**
        * *Relevância*: Ganho mínimo necessário para uma divisão.
    * **`min_child_weight`: 0.1393188921160219**
        * *Relevância*: Peso mínimo (soma dos pesos de hessiana) em um nó filho.

### II. Análise de Correlação Inicial das Features com o Alvo

Antes da seleção de features pelo RFECV e do treinamento do modelo LightGBM final, foi realizada uma análise de correlação das features iniciais (após limpeza e transformações) com a variável alvo `TARGET_SALARIO_CODIFICADO`. As features consideradas nesta fase foram: `P1_a_1` (Faixa Etária), `P1_b` (Gênero), `P1_l` (Nível de Ensino), `P2_i` (Tempo de Experiência), `P2_g_Nivel` (Nível de Senioridade), `P2_f_Cargo_Atual` (Cargo Atual), e `Regiao_Mapeada`.

a.  **Metodologia e Codificação do Alvo para Correlação:**
    Para a interpretação da correlação, assume-se a codificação onde "Salário Baixo" recebeu um valor numérico MAIOR e "Salário Alto" um valor numérico MENOR (ex: Salário Alto -> 0, Salário Baixo -> 1). Com esta codificação, um coeficiente de correlação negativo entre uma feature e o alvo indica que um aumento no valor da feature tende a estar associado a "Salário Alto". A Correlação de Distância (dcor) mede a força da dependência (0 a 1), independentemente da direção.

b.  **Resumo das Correlações das Features Iniciais com `TARGET_SALARIO_CODIFICADO`:**

| Feature            | Pearson | Spearman | dcor (Força) | Interpretação Consolidada (assumindo Salário Baixo como valor maior no alvo) |
| :----------------- | :------ | :------- | :----------- | :--------------------------------------------------------------------------- |
| `P2_i`             | -0.52   | -0.57    | 0.53         | Forte dependência. Maior experiência tende a salário mais alto.               |
| `P2_g_Nivel`       | -0.44   | -0.44    | 0.45         | Moderada a forte dependência. Maior senioridade tende a salário mais alto.     |
| `P2_f_Cargo_Atual` | -0.32   | -0.31    | 0.33         | Moderada dependência. "Melhores" cargos (assumindo codificação ordinal favorável) tendem a salário mais alto. |
| `P1_a_1`           | -0.31   | -0.33    | 0.30         | Moderada dependência. Faixas etárias maiores tendem a salário mais alto.       |
| `P1_l`             | -0.18   | -0.22    | 0.20         | Baixa a moderada dependência. Maior nível de ensino tende a salário mais alto. |
| `P1_b`             | -0.07   | -0.07    | 0.08         | Dependência muito fraca.                                                     |
| `Regiao_Mapeada`   | -0.00   | 0.01     | 0.05         | Dependência muito fraca ou inexistente (linear/monotônica).                  |

c.  **Observações da Análise de Correlação Inicial:**
    * **Consistência e Força:** `P2_i` (Tempo de Experiência) e `P2_g_Nivel` (Nível de Senioridade) exibiram as correlações (negativas, indicando associação com "Salário Alto") e dependências (dcor) mais fortes com a faixa salarial. `P2_f_Cargo_Atual` (Cargo Atual) e `P1_a_1` (Faixa Etária) seguiram com dependência moderada.
    * **Relações Não Estritamente Lineares:** Para `P2_i`, os valores de Spearman e dcor ligeiramente maiores que Pearson sugerem que a relação, embora forte, pode ter componentes não perfeitamente lineares, mas é claramente monotônica.
    * **Impacto Menor (Linear/Monotônico):** `P1_l` (Nível de Ensino) mostrou uma associação mais modesta. `P1_b` (Gênero) e `Regiao_Mapeada` (Região) apresentaram correlações lineares/monotônicas muito fracas com o alvo nesta análise inicial. Isso sugere que, individualmente e de forma linear/monotônica, Gênero e Região têm pouca influência na distinção das faixas salariais.

d.  **Insights dos Mapas de Calor de Correlação (Inter-feature):**
    Os mapas de calor de correlação (Pearson, Spearman, dcor) são ferramentas visuais importantes para entender as inter-relações entre todas as features *antes* da modelagem.
    * **Pearson e Spearman Heatmaps:** Estes gráficos revelam a força e direção das relações lineares (Pearson) e monotônicas (Spearman) entre pares de features. É esperado, por exemplo, observar correlações positivas entre `P2_i` (Experiência), `P1_a_1` (Faixa Etária) e `P2_g_Nivel` (Senioridade). Entender essas inter-correlações ajuda a contextualizar a importância que o modelo LightGBM atribui a cada uma, pois features correlacionadas podem ter suas importâncias "compartilhadas" ou uma pode "representar" a outra parcialmente.
    * **Distance Correlation (dcor) Heatmap:** Este mapa destaca a força da dependência geral (linear ou não linear) entre as features, complementando as outras duas métricas ao identificar relações que podem não ser capturadas por medidas lineares ou monotônicas.

### III. Fatores Preditivos Dominantes no Modelo LightGBM: Análise das Features Selecionadas e Sua Importância

a.  **Features Selecionadas (RFECV) e Seus Significados (conforme Relatório de Resultados, Seção 3.2):**
    O processo de `RFECV` selecionou 6 features para o modelo final:
    1.  `P2_i`: Tempo de experiência
    2.  `P2_f_Cargo_Atual`: Cargo atual
    3.  `P2_g_Nivel`: Nível de senioridade
    4.  `P1_l`: Nível de ensino
    5.  `P1_a_1`: Faixa etária
    6.  `Regiao_Mapeada`: Região onde mora

>Nota: `P1_b` (Gênero), que apresentou correlação inicial muito fraca com o alvo, foi eliminada pelo RFECV, o que é consistente com sua baixa associação linear/monotônica individual.

b.  **Análise de Importância de Features no Modelo LightGBM (conforme Relatório de Resultados, Seção 3.2):**
    O LightGBM atribuiu a seguinte ordem de importância (provavelmente baseada em "ganho") para as features selecionadas:
    1.  **`P2_i` (Tempo de experiência)**
    2.  **`P2_f_Cargo_Atual` (Cargo atual)**
    3.  **`P2_g_Nivel` (Nível de senioridade)**
    4.  **`P1_l` (Nível de ensino)**
    5.  **`P1_a_1` (Faixa etária)**
    6.  **`Regiao_Mapeada` (Região onde mora)**

c.  **Interpretação no Contexto da Predição Salarial (Considerando Correlações e Importância no Modelo):**
    * **Consistência entre Correlação e Importância:** As features com maior correlação inicial com o alvo (`P2_i`, `P2_g_Nivel`, `P2_f_Cargo_Atual`, `P1_a_1`) também figuram entre as mais importantes para o modelo LightGBM. Isso reforça a ideia de que são direcionadores chave da faixa salarial.
    * **Papel da Experiência e Hierarquia:** `P2_i`, `P2_f_Cargo_Atual`, e `P2_g_Nivel` dominam tanto na correlação inicial quanto na importância para o modelo, sublinhando que a progressão na carreira e o acúmulo de experiência são cruciais para atingir salários mais altos.
    * **Nível de Ensino e Faixa Etária (`P1_l`, `P1_a_1`):** Apresentaram correlações moderadas e são importantes para o modelo, embora com menor peso que o trio anterior. O modelo provavelmente as utiliza para refinar predições dentro de grupos definidos por experiência/cargo/nível.
    * **Região Mapeada (`Regiao_Mapeada`):** Esta feature teve uma correlação linear/monotônica inicial quase nula com o alvo. No entanto, foi selecionada pelo RFECV e possui alguma importância (a menor entre as 6) no modelo LightGBM. Isso sugere que sua contribuição é provavelmente não-linear ou se manifesta através de interações com outras features que o modelo de árvore consegue capturar, mas que a análise de correlação bivariada simples não evidencia. Por exemplo, o impacto de um cargo pode variar significativamente apenas em certas regiões.

### IV. Desvendando a Lógica do Modelo: 'Regras de Raciocínio' e Caminhos de Decisão

a.  **Elucidando a Lógica do `LGBMClassifier`:**
    O modelo final consiste em 105 árvores de decisão. Extrair regras globais simples é inviável. Cada árvore contém múltiplos caminhos de decisão baseados em limiares para as 6 features selecionadas.
    * **Exemplo de Caminho (Ilustrativo):** `IF P2_i (Experiência) > 6 anos AND P2_g_Nivel == 'Sênior' AND Regiao_Mapeada == 'Sudeste' THEN probabilidade_Salario_Alto aumenta.`
    * **Interpretabilidade Adicional:** Ferramentas como SHAP ou LIME, não mencionadas no relatório, poderiam oferecer maior detalhamento sobre as contribuições de features para previsões individuais ou para o comportamento geral do modelo.

b.  **Como as 'Regras' (Implícitas) Ajudam a Entender as Decisões:**
    A lógica do modelo, inferida a partir da importância das features e dos gráficos do relatório (Seções 3.3, 3.4, 3.5), sugere que:
    * Divisões primárias ocorrem com base em `P2_i` (Experiência).
    * `P2_f_Cargo_Atual` e `P2_g_Nivel` segmentam ainda mais os dados.
    * As demais features (`P1_l`, `P1_a_1`, `Regiao_Mapeada`) refinam as probabilidades dentro desses subgrupos, capturando nuances específicas.

### V. A Interação entre Fatores Chave na Predição Salarial

a.  **Capacidade de Modelar Interações:**
    O LightGBM é inerentemente capaz de modelar interações complexas e não lineares entre features.

b.  **Discussão sobre Interações Prováveis (Considerando Correlações e o Modelo):**
    * **Experiência (`P2_i`), Senioridade (`P2_g_Nivel`) e Cargo (`P2_f_Cargo_Atual`):** Estas três features, fortemente correlacionadas entre si e com o alvo, provavelmente interagem de forma sinérgica. O efeito da experiência no salário pode ser potencializado por um nível de senioridade ou cargo mais alto.
    * **Nível de Ensino (`P1_l`) com Experiência/Cargo:** O "retorno" de um maior nível de ensino pode ser mais pronunciado para profissionais com mais experiência ou em cargos que valorizam essa qualificação.
    * **Região (`Regiao_Mapeada`) com Cargo/Nível:** A importância da `Regiao_Mapeada`, apesar da baixa correlação inicial, sugere que ela interage significativamente. Um cargo de "Gerente" (`P2_f_Cargo_Atual`, `P2_g_Nivel`) pode ter um diferencial salarial muito maior em uma capital (`Regiao_Mapeada`) do que em uma cidade do interior.
    * **Faixa Etária (`P1_a_1`) e Experiência (`P2_i`):** Embora correlacionadas, o modelo pode identificar que, para uma mesma experiência, faixas etárias diferentes podem ter salários distintos, ou vice-versa, capturando maturidade ou outros fatores não diretamente medidos pela experiência.

### VI. Síntese: Conectando a Interpretação do Modelo à Pergunta Central da Pesquisa

a.  **Principais Descobertas da Interpretação do Modelo:**
    1.  O modelo `LGBMClassifier` (Acurácia Teste: 0.8335, ROC AUC Teste: 0.9234) é eficaz na predição de faixas salariais.
    2.  **Tempo de Experiência, Cargo Atual e Nível de Senioridade** são os determinantes mais fortes, com altas correlações iniciais com o alvo e maior importância no modelo.
    3.  Nível de Ensino e Faixa Etária também são preditores relevantes.
    4.  A Região onde mora, embora com baixa correlação linear inicial, contribui para o modelo, provavelmente através de interações ou efeitos não-lineares.
    5.  O modelo captura interações complexas entre esses fatores para distinguir as classes salariais.
    6.  A definição do ponto de corte (`point_of_cut_fixed`) para as classes 'Salário Alto'/'Baixo' é crucial para a análise.

b.  **Relação com a Pergunta Orientadora:**
    A pergunta ("Quais fatores e suas interações influenciam a classificação em 'Salário Alto' vs. 'Salário Baixo'?") é respondida:
    * **Fatores Primários:** Experiência, cargo e senioridade são os principais.
    * **Fatores Secundários/Moduladores:** Nível de ensino, faixa etária e região.
    * **Interações Fundamentais:** O valor de cada fator é frequentemente dependente dos outros (ex: o impacto da experiência é modulado pelo cargo e pela região).

c.  **Limitações da Interpretação/Modelo:**
    1.  **Interpretabilidade Detalhada:** Sem SHAP/LIME, a compreensão exata das contribuições para previsões individuais é limitada.
    2.  **Causalidade:** O modelo identifica associações preditivas, não causa e efeito.
    3.  **Simplificação Binária:** A divisão em duas faixas salariais oculta nuances da distribuição completa de salários.
    4.  **Features Eliminadas:** A eliminação de features como Gênero (`P1_b`) pelo RFECV significa que elas não melhoraram o poder preditivo *deste modelo específico*, mas não invalida sua importância em outras análises, especialmente de equidade ou com diferentes configurações de modelo/feature. A baixa correlação inicial de Gênero com o alvo é consistente com sua eliminação.

Esta versão integrada fornece uma visão mais completa, começando com as relações lineares/monotônicas e depois explorando como o modelo LightGBM utiliza essas e outras informações de forma mais complexa.

-------------------------------------------------------------------------------------------------------------------------

### Interpretação do modelo 2_3

## Interpretação Detalhada do Modelo de Rede Neural (RNA v2) para Classificação de Faixa Salarial

### I. Justificativa, Objetivo e Configuração do Modelo RNA v2

a.  **Justificativa e Objetivo do Modelo:**
    O principal objetivo deste modelo de Rede Neural Artificial (RNA v2) é classificar a faixa salarial de indivíduos em duas categorias distintas: "Salário Baixo" e "Salário Alto". A intenção é investigar se uma arquitetura de RNA, com sua capacidade intrínseca de aprender interações complexas e representações ricas para features categóricas (através de camadas de embedding), pode oferecer um desempenho comparável ou superior aos modelos baseados em árvores (como o LightGBM previamente analisado) para a mesma pergunta orientada a dados. A abordagem de classificação binária visa simplificar o problema e potencialmente aprimorar a distinção entre os grupos salariais.

b.  **Ponto de Corte e Balanceamento das Classes:**
    Para a divisão das faixas salariais, foi utilizado um ponto de corte fixo de R$ 7.500,00 aplicado à variável `salary_numeric_lower_bound`. Conforme os logs do projeto, essa definição resultou em um dataset processado (antes da divisão treino/teste) com aproximadamente 2268 amostras para "Salário Baixo" e 2485 para "Salário Alto", indicando um bom equilíbrio entre as classes, o que é favorável para o treinamento do modelo.

c.  **Features de Entrada para a RNA v2:**
    O modelo RNA v2 utilizou o seguinte conjunto de 7 features (após mapeamento e tratamento inicial):
    1.  `P1_a_1`: Faixa etária
    2.  `P1_b`: Gênero
    3.  `P1_l`: Nível de ensino
    4.  `P2_i`: Tempo de experiência na área de dados
    5.  `P2_g_Nivel`: Nível de senioridade
    6.  `P2_f_Cargo_Atual`: Cargo atual
    7.  `Regiao_Mapeada`: Região Mapeada (derivada da UF)
    *Nota: É importante observar que esta RNA v2 inclui a feature `P1_b` (Gênero), que havia sido eliminada pelo processo de RFECV no modelo LightGBM anterior. A inclusão aqui permite à RNA explorar diretamente a influência desta feature.*

d.  **Arquitetura e Principais Hiperparâmetros (Otimizados com Ray Tune):**
    A arquitetura da RNA v2 e seus hiperparâmetros foram otimizados usando Ray Tune. A última execução bem-sucedida resultou na seguinte configuração:
    * **Arquitetura Geral:** Rede neural com camadas de embedding para features categóricas e camadas densas para processamento.
    * `num_hidden_layers`: 1 (uma camada densa oculta)
    * `dense_units_1`: 64 (número de neurônios na primeira camada densa oculta)
    * (`dense_units_2`: 128, mas não utilizada devido a `num_hidden_layers: 1`)
    * `dropout_1`: 0.45 (taxa de dropout na primeira camada densa para regularização)
    * (`dropout_2`: 0.30, não utilizada)
    * `optimizer`: 'adam'
    * `learning_rate_nn`: 0.0002366... (taxa de aprendizado para o otimizador Adam)
    * `batch_size`: 32
    * `epochs`: 50 (número máximo de épocas, controlado por `early_stopping_patience`)
    * `early_stopping_patience`: 10 (critério para interromper o treinamento se não houver melhora na métrica de validação)
    * **Regularização L2:**
        * `l2_strength_embedding`: 0.0046... (força da regularização L2 nas camadas de embedding)
        * `l2_strength_dense`: 4.19e-05 (força da regularização L2 nas camadas densas)
    * **Dimensões das Camadas de Embedding (para features categóricas):**
        * `emb_dim_P1_a_1` (Faixa etária): 8
        * `emb_dim_P1_b` (Gênero): 4
        * `emb_dim_P1_l` (Nível de ensino): 4
        * `emb_dim_P2_g_Nivel` (Nível de senioridade): 4
        * `emb_dim_P2_f_Cargo_Atual` (Cargo atual): 9
        * `emb_dim_Regiao_Mapeada` (Região Mapeada): 4
    Estas dimensões de embedding permitem que a rede aprenda representações vetoriais densas para cada categoria das features, capturando semelhanças e relações entre elas.

### II. Resultados da Avaliação do Modelo RNA v2

a.  **Métricas de Desempenho Agregadas (Conjunto de Teste):**
    Com base nos logs da última execução bem-sucedida:
    * Melhor Acurácia na Validação (durante HPO com Ray Tune): 0.8345
    * **Acurácia no Teste:** 0.8377
    * Precisão Média (Macro Avg) no Teste: 0.8377 (calculado a partir do relatório de classificação)
    * F1-Score (Ponderado) no Teste: 0.8377
    * **ROC AUC (Binário) no Teste:** 0.9263
    A acurácia de aproximadamente 83.77% no teste e um ROC AUC de 0.9263 indicam que o modelo RNA v2 possui um bom poder preditivo e capacidade de discriminação entre as classes "Salário Alto" e "Salário Baixo".


b.  **Relatório de Classificação Detalhado (Teste - RNA v2) e Análise da Matriz de Confusão:**

    O relatório de classificação detalhado fornece insights sobre o desempenho por classe:

| Feature            | Pearson | Spearman | dcor (Força) | Interpretação Consolidada (assumindo Salário Baixo como valor maior no alvo) |
| :----------------- | :------ | :------- | :----------- | :--------------------------------------------------------------------------- |
| `P2_i`             | -0.52   | -0.57    | 0.53         | Forte dependência. Maior experiência tende a salário mais alto.               |
| `P2_g_Nivel`       | -0.44   | -0.44    | 0.45         | Moderada a forte dependência. Maior senioridade tende a salário mais alto.     |
| `P2_f_Cargo_Atual` | -0.32   | -0.31    | 0.33         | Moderada dependência. "Melhores" cargos (assumindo codificação ordinal favorável) tendem a salário mais alto. |
| `P1_a_1`           | -0.31   | -0.33    | 0.30         | Moderada dependência. Faixas etárias maiores tendem a salário mais alto.       |
| `P1_l`             | -0.18   | -0.22    | 0.20         | Baixa a moderada dependência. Maior nível de ensino tende a salário mais alto. |
| `P1_b`             | -0.07   | -0.07    | 0.08         | Dependência muito fraca.                                                     |
| `Regiao_Mapeada`   | -0.00   | 0.01     | 0.05         | Dependência muito fraca ou inexistente (linear/monotônica).                  |

    * **Interpretação:**

        * O modelo demonstra um desempenho equilibrado para ambas as classes, com Precision, Recall e F1-score em torno de 0.83-0.85.

        * Para "Salário Alto": 85% das previsões de "Salário Alto" estavam corretas (Precision), e o modelo identificou 84% de todos os verdadeiros "Salário Alto" (Recall).

        * Para "Salário Baixo": 83% das previsões de "Salário Baixo" estavam corretas (Precision), e o modelo identificou 84% de todos os verdadeiros "Salário Baixo" (Recall).

    * **Matriz de Confusão Normalizada (Teste - RNA v2 - `matriz_confusao_norm_RNA.png`):**

        * A matriz de confusão visualiza esses resultados. Conforme o relatório fornecido, ela mostra que aproximadamente 83.60% dos verdadeiros "Salário Alto" foram corretamente previstos como "Salário Alto", e cerca de 83.95% dos verdadeiros "Salário Baixo" foram corretamente previstos como "Salário Baixo" (valores baseados na interpretação da imagem `download.png`, que devem ser consistentes com os Recalls de 0.84 acima).

        * As taxas de erro (classificações incorretas) são relativamente simétricas: ~16.40% dos "Salário Alto" classificados incorretamente como "Baixo", e ~16.05% dos "Salário Baixo" classificados incorretamente como "Alto". Isso indica que o modelo não tem um viés significativamente maior para errar em uma direção específica.

### III. Análise de Preditores e Lógica do Modelo RNA v2

a.  **Importância das Features na RNA v2 (Métodos e Expectativas):**
    Diferentemente de modelos baseados em árvores (como LightGBM), a obtenção da "importância das features" em redes neurais não é direta através de um atributo do modelo. Técnicas mais avançadas são necessárias, como:
    * **Permutation Importance:** Avalia a queda no desempenho do modelo quando os valores de uma feature são permutados aleatoriamente.
    * **SHAP (SHapley Additive exPlanations) values:** Fornece uma medida da contribuição de cada feature para cada predição individual.
    O relatório fornecido não indica a aplicação dessas técnicas, mas aponta expectativas:
    * **Expectativa de Impacto:** Espera-se que features ligadas à experiência e progressão na carreira, como `P2_i` (Tempo de experiência), `P2_f_Cargo_Atual` (Cargo atual), e `P2_g_Nivel` (Nível de senioridade), tenham um impacto significativo nas decisões do modelo.
    * **Outras Features Consideradas:** Características como `P1_l` (Nível de ensino), `P1_a_1` (Faixa etária), `P1_b` (Gênero) e `Regiao_Mapeada` também são processadas pela rede, e sua influência específica precisaria ser quantificada pelas técnicas mencionadas. A inclusão de `P1_b` (Gênero) diretamente na RNA permite que o modelo aprenda sua relevância (ou falta dela) e suas interações.

b.  **Elucidando a Lógica da Rede Neural (Embeddings, Camadas Densas):**
    A RNA v2 processa as informações da seguinte maneira:
    1.  **Camadas de Embedding:** As features categóricas (`P1_a_1`, `P1_b`, `P1_l`, `P2_g_Nivel`, `P2_f_Cargo_Atual`, `Regiao_Mapeada`) são primeiro transformadas em vetores densos de dimensão fixa (conforme `emb_dim_*`). Essas camadas de embedding aprendem representações significativas para cada categoria, capturando relações semânticas entre elas (ex: categorias de cargos similares podem ter vetores de embedding próximos no espaço vetorial).
    2.  **Concatenação:** Os vetores de embedding resultantes e as features numéricas (se houvesse, mas aqui `P2_i` - Tempo de Experiência, embora numérico, pode ter sido tratado via embedding ou normalizado e concatenado) são combinados.
    3.  **Camada Densa Oculta:** A informação combinada passa por uma camada densa (`dense_units_1: 64`) com função de ativação (provavelmente ReLU), onde o modelo aprende combinações não lineares das features representadas. O dropout (`dropout_1: 0.45`) é aplicado para regularização, prevenindo overfitting.
    4.  **Camada de Saída:** Uma camada de saída com uma função de ativação sigmoide produz a probabilidade de a instância pertencer à classe "Salário Alto" (ou "Salário Baixo", dependendo da codificação da classe positiva).

### IV. Insights dos Dados de Contexto Utilizados pela RNA v2 (Baseado nos Gráficos)

Os gráficos mencionados no relatório ilustram as distribuições da variável alvo *real* em relação a algumas features chave. Eles fornecem o contexto dos padrões nos dados que a RNA v2 tenta aprender.

a.  **Distribuição de Faixa Salarial (Real) por Top 15 Cargos (`dist_salario_top15_cargos_RNA_contexto.png`):**
    * Este gráfico mostra, para os 15 cargos mais frequentes, a contagem de profissionais em "Salário Baixo" vs. "Salário Alto".
    * **Insights:** Permite identificar cargos com predominância natural de salários mais altos (ex: Cientista de Dados, Engenheiro de Dados) ou mais baixos (ex: Analista de Dados). A RNA tenta aprender e generalizar esses padrões observados.

b.  **Distribuição de Faixa Salarial (Real) por Nível de Senioridade (`dist_salario_senioridade_RNA_contexto.png`):**
    * Apresenta a distribuição das faixas salariais reais para cada nível de senioridade.
    * **Insights:** Demonstra a clara progressão salarial com o aumento da senioridade, um padrão forte que a RNA deve capturar. Júniores tendem a "Salário Baixo", Plenos são mistos, e Sêniores têm maior proporção em "Salário Alto".

c.  **Boxplot e Violin Plot de Tempo de Experiência (Real) por Faixa Salarial (`dist_experiencia_salario_RNA_contexto.png`):**
    * Mostram a distribuição do tempo de experiência para as faixas salariais reais.
    * **Insights:** Indivíduos na faixa "Salário Alto" claramente tendem a ter mais tempo de experiência (mediana mais alta, distribuições deslocadas para a direita). A forma do violin plot pode indicar diferentes concentrações de experiência que levam a salários mais altos, sugerindo relações não lineares que a RNA pode modelar.

### V. A Interação entre Fatores Chave na Predição Salarial (Perspectiva da RNA)

a.  **Capacidade da RNA de Modelar Interações Complexas:**
    As redes neurais, especialmente com camadas de embedding e camadas densas não lineares, são inerentemente capazes de aprender interações complexas e de alta ordem entre as features de entrada.
    * **Embeddings:** As camadas de embedding não apenas reduzem a dimensionalidade de features categóricas, mas também aprendem um espaço onde as interações entre categorias (e entre diferentes features categóricas após a concatenação) podem ser mais facilmente modeladas pelas camadas densas subsequentes.

b.  **Discussão sobre Interações Prováveis (Considerando as features de entrada e a natureza da RNA):**
    A RNA v2 tem o potencial de aprender interações como:
    * O impacto do **Nível de Ensino (`P1_l`)** pode variar dependendo do **Cargo Atual (`P2_f_Cargo_Atual`)** e do **Tempo de Experiência (`P2_i`)**.
    * A combinação de **Nível de Senioridade (`P2_g_Nivel`)** e **Região Mapeada (`Regiao_Mapeada`)** pode influenciar o salário de forma diferente da soma de seus efeitos individuais.
    * O **Gênero (`P1_b`)**, se relevante, pode interagir com o **Cargo** ou **Nível de Senioridade**, e a RNA pode modelar essas interações sutis caso existam nos dados e sejam preditivas.
    * A rede aprende essas interações implicitamente através dos pesos ajustados durante o treinamento nas camadas densas.

### VI. Síntese: Conectando a Interpretação do Modelo à Pergunta Central da Pesquisa

a.  **Principais Descobertas da Interpretação do Modelo RNA v2:**
    1.  A RNA v2 alcançou um bom desempenho (Acurácia Teste: ~0.838, ROC AUC Teste: ~0.926), comparável em métricas globais ao modelo LightGBM v7.
    2.  O modelo utiliza 7 features, incluindo Gênero, e emprega camadas de embedding para aprender representações ricas de features categóricas.
    3.  A determinação exata da importância das features requer técnicas específicas (Permutation Importance, SHAP), mas espera-se que experiência, cargo e senioridade sejam influentes.
    4.  A RNA é capaz de modelar interações complexas e não lineares, o que é uma de suas principais vantagens teóricas.

b.  **Comparativo Potencial com Modelos Anteriores (ex: LightGBM v7):**
    * **Desempenho:** As métricas globais (Acurácia, ROC AUC) entre a RNA v2 e o LightGBM v7 parecem ser muito próximas. Uma análise mais detalhada (ex: custos de erro diferentes, desempenho em subgrupos específicos) poderia revelar vantagens de um sobre o outro.
    * **Interpretabilidade:** Modelos baseados em árvores como o LightGBM geralmente oferecem interpretabilidade mais direta (feature importance nativa). Redes Neurais são mais "caixa-preta", exigindo esforço adicional para interpretação.
    * **Tratamento de Features:** A RNA com embeddings oferece uma forma sofisticada de lidar com features categóricas. O LightGBM também lida bem com categóricas nativamente.
    * **Recursos Computacionais:** O treinamento de RNAs e a otimização de hiperparâmetros (especialmente com Ray Tune) podem ser mais intensivos computacionalmente do que para modelos LightGBM.

c.  **Relação com a Pergunta Orientadora:**
    A pergunta ("Quais fatores e suas interações influenciam a classificação em 'Salário Alto' vs. 'Salário Baixo'?") é abordada pela RNA v2 através da sua capacidade de aprender complexas funções de mapeamento a partir das features de entrada. Embora a explicitação dessas relações seja menos direta, o desempenho do modelo sugere que ele está capturando padrões válidos nos dados relacionados a experiência, cargo, senioridade, educação, demografia e localização.

d.  **Limitações da Interpretação/Modelo RNA v2:**
    1.  **Interpretabilidade da "Caixa-Preta":** Sem a aplicação de SHAP/Permutation Importance, a contribuição exata de cada feature e a natureza das interações aprendidas permanecem obscuras.
    2.  **Sensibilidade a Hiperparâmetros:** Redes Neurais são notoriamente sensíveis à escolha da arquitetura e dos hiperparâmetros. A otimização com Ray Tune mitiga isso, mas o espaço de busca é vasto.
    3.  **Custo Computacional:** Treinamento e HPO podem ser demorados e exigir mais recursos.
    4.  **Simplificação Binária:** A classificação em duas faixas salariais, definida pelo ponto de corte de R$ 7.500,00, é uma simplificação.
    5.  **Causalidade:** O modelo identifica associações preditivas, não relações causais.

Esta interpretação visa cobrir os aspectos mais relevantes do seu modelo RNA v2 com base no relatório fornecido.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Análise comparativa dos modelos

*   [Análise comparativa dos modelos da 1º pergunta orientada a dados](#análise-comparativa-dos-modelos-da-1º-pergunta-orientada-a-dados)
*   [Análise comparativa dos modelos da 2º pergunta orientada a dados](#análise-comparativa-dos-modelos-da-2º-pergunta-orientada-a-dados)
*   [Análise comparativa dos modelos da 3º pergunta orientada a dados](#análise-comparativa-dos-modelos-da-3º-pergunta-orientada-a-dados)



# Análise comparativa dos modelos da 1º pergunta orientada a dados

## Discussão de Forças e Fragilidades de Cada Modelo

### Modelo A: `RandomForestClassifier` (Classificação Binária)

* **Fonte do Código:** `new-model1-versao12 (1).ipynb`

#### Forças do Modelo A:

* **Capacidade de Modelar Interações Complexas:**
    * O Random Forest é inerentemente bom em capturar interações não lineares entre features sem a necessidade de especificá-las manualmente. Isso é crucial para a 1ª pergunta orientada a dados do `report.md`, que foca na interação entre formação e experiência. O heatmap de interação gerado no código (`interacao_formacao_experiencia.png`) demonstra essa capacidade.
    * *Conexão com Objetivos:* Contribui diretamente para "compreender os fatores que influenciam a variação salarial" e "identificar padrões e tendências".

* **Fornecimento de Importância das Features:**
    * O modelo fornece uma métrica clara de importância das features, ajudando a identificar quais fatores (formação, experiência, senioridade, etc.) são mais determinantes para a classificação da faixa salarial. No `report.md` (e confirmado pelo código do Modelo A), as top 3 features foram senioridade (`senioridade_encoded`), experiência (`experiencia_profissional_encoded`) e formação (`formacao_academica_encoded`), o que está alinhado com as hipóteses do estudo.
    * *Conexão com Objetivos:* Auxilia na "Identificação de Fatores Relevantes" e na "interpretação dos resultados".

* **Robustez e Generalização:**
    * Sendo um ensemble (bagging), é geralmente robusto a outliers (até certo ponto) e menos propenso a overfitting do que uma única árvore de decisão. A otimização de hiperparâmetros (`min_samples_leaf`, `min_samples_split`) e a validação cruzada no `GridSearchCV` (cv=5) visam melhorar a generalização.
    * *Conexão com Objetivos:* A construção de um "sistema inteligente" confiável requer boa generalização para "auxiliar na equiparação salarial" de forma consistente.

* **Bom Desempenho em Problemas de Classificação Binária:**
    * O Random Forest é um algoritmo forte para tarefas de classificação. A transformação do problema em binário ("Salário Alto" vs. "Salário Baixo/Médio") simplifica a tarefa e foca na distinção de um limiar salarial chave (R$ 8.000/mês, conforme engenharia de features no código).
    * O uso de `sample_weights` e `class_weight='balanced_subsample'`, junto com a otimização do limiar de decisão e a calibração das probabilidades, são boas práticas que melhoram a confiabilidade em cenários com leve desbalanceamento.
    * A acurácia balanceada de 0.8106 no teste, conforme o `report.md`, é um bom resultado para este problema binário.
    * *Conexão com Objetivos:* Permite "aplicar por meio de algoritmos de aprendizado de máquina, a previsão da variação salarial com base nos fatores identificados" de forma eficaz para o problema binário definido.

* **Interpretabilidade Parcial e Visualizações:**
    * Embora ensembles sejam caixas-pretas, a importância das features e a capacidade de visualizar árvores individuais (como feito no código, ex: `arvore_exemplo_simplificada.png`) oferecem alguma interpretabilidade. O heatmap de interação (`interacao_formacao_experiencia.png`) é uma excelente forma de visualizar o efeito combinado de formação e experiência.
    * *Conexão com Objetivos:* Ajuda na "interpretação dos resultados" e na "geração de insights para o mercado".

##### Fragilidades do Modelo A:

* **Variável Alvo Binária Simplificada:**
    * A conversão da "Faixa salarial mensal" em apenas duas classes ("Salário Alto" vs. "Salário Baixo/Médio" com corte em R$ 8.000) perde a granularidade das disparidades salariais. Profissionais ganhando R$ 8.500 e R$ 30.000 estão ambos na mesma classe "Salário Alto", o que limita a profundidade da análise de "variação salarial".
    * *Impacto na Investigação:* Dificulta a compreensão das nuances da disparidade dentro das categorias "Alto" e "Baixo/Médio", que é um dos focos do `report.md`.

* **Interpretabilidade Limitada do Ensemble:**
    * Embora a importância das features seja útil, entender *como* o modelo combina centenas de árvores para chegar a uma decisão específica para um indivíduo é complexo. Explicar as "regras" exatas do modelo para um stakeholder não técnico é desafiador.
    * *Impacto na Investigação:* Pode ser difícil "desenvolver um sistema inteligente para *compreender* os fatores que influenciam a variação salarial" em profundidade apenas com as saídas do Random Forest.

* **Tratamento Ordinal de Features Chave:**
    * `formacao_academica_encoded` e `experiencia_profissional_encoded` são tratadas como numéricas ordinais. Embora haja uma ordem, o modelo de árvore pode tratar os intervalos entre os valores codificados como equidistantes, o que pode não ser verdade (o "salto" de Graduação para Pós pode não ser o mesmo que de Pós para Mestrado em termos de impacto salarial). Isso pode levar a splits subótimos se a relação não for estritamente linear dentro da ordem.
    * *Impacto na Investigação:* A representação da influência dessas variáveis chave pode não ser totalmente precisa, afetando a análise da interação.

* **Sensibilidade a Hiperparâmetros:**
    * Embora o `GridSearchCV` tenha sido usado, Random Forests ainda podem ser sensíveis à escolha da grade de parâmetros. O `max_depth=None` (melhor parâmetro encontrado) pode levar a árvores muito profundas se não bem controlado por `min_samples_leaf` (7) e `min_samples_split` (15).
    * *Impacto na Investigação:* Uma otimização subótima poderia levar a conclusões menos robustas sobre a importância dos fatores.

---

#### Modelo B: `GradientBoostingClassifier` (Classificação Multiclasse)

* **Fonte do Código:** `modelo-1-2-arvore-classificatoria-v5.ipynb`

##### Forças do Modelo B:

* **Análise Granular da Disparidade Salarial:**
    * Ao usar uma variável alvo multiclasse com 6 faixas salariais agrupadas (ex: 'Até R$ 2.000/mês', 'R$ 2.001/mês a R$ 4.000/mês', etc.), o modelo permite uma análise mais detalhada da disparidade salarial do que uma simples classificação binária. É possível ver como os fatores influenciam a probabilidade de pertencer a diferentes níveis de renda.
    * *Conexão com Objetivos:* Alinha-se melhor com "compreender os fatores que influenciam a *variação* salarial" de forma mais ampla, como detalhado no problema do `report.md`.

* **Tratamento Flexível de Features Categóricas com One-Hot Encoding:**
    * Aplicar One-Hot Encoding a todas as features de entrada, incluindo 'Nível de ensino alcançado' e 'Tempo de experiência na área de dados' (que foram tratadas como categóricas antes do OHE no código), evita impor uma relação ordinal que pode não ser linear ou equidistante em seu efeito no salário. Cada categoria (ex: cada nível de ensino, cada faixa de experiência) torna-se uma feature binária independente, permitindo ao modelo aprender seu impacto específico.
    * *Conexão com Objetivos:* Pode levar a uma modelagem mais flexível do impacto das variáveis chave 'formação acadêmica' e 'experiência profissional'.

* **Poder Preditivo do Gradient Boosting:**
    * Gradient Boosting Machines (GBMs) são frequentemente algoritmos de ponta para dados tabulares, capazes de alcançar alta performance através da construção sequencial de árvores que corrigem os erros das anteriores.
    * *Conexão com Objetivos:* Pode levar a uma "previsão da variação salarial com base nos fatores identificados" mais precisa, dentro do contexto multiclasse.

* **Importância das Features e Análise de Associação Inicial:**
    * Assim como o Random Forest, GBMs podem fornecer a importância das features (geralmente baseada no ganho). O código também calcula o V de Cramer para uma análise de correlação inicial entre features e o alvo multiclasse, informando sobre a força da associação antes da modelagem. 'Nível de senioridade' e 'Tempo de experiência' foram identificados como os mais correlacionados com a faixa salarial agrupada.
    * *Conexão com Objetivos:* Ajuda na "Identificação de Fatores Relevantes".

##### Fragilidades do Modelo B:

* **Maior Dificuldade de Interpretação (Multiclasse e Boosting):**
    * Modelos de Boosting são sequenciais e mais complexos de interpretar do que Random Forests. Explicar como as previsões são feitas para 6 classes diferentes é intrinsecamente mais difícil.
    * O `report.md` (baseado na saída do notebook do Modelo B) mostra uma acurácia balanceada de 0.4015 e acurácia geral de 0.5273. Estes valores são mais baixos que os do Modelo A (binário), o que é esperado dada a maior complexidade da tarefa multiclasse. O desempenho foi particularmente baixo para a classe 'Acima de R$ 30.000/mês' (F1-score de 0.11).
    * *Impacto na Investigação:* Torna a "interpretação dos resultados" e a "geração de insights para o mercado" mais desafiadoras, especialmente para classes com baixo desempenho.

* **Sensibilidade a Hiperparâmetros e Risco de Overfitting:**
    * GBMs são conhecidos por serem sensíveis a hiperparâmetros (especialmente `learning_rate` e `n_estimators`). Embora `RandomizedSearchCV` tenha sido usado, a otimização pode ser mais crítica. Há um risco maior de overfitting se não cuidadosamente ajustado, especialmente com o oversampling.
    * *Impacto na Investigação:* Pode levar a um modelo que não generaliza bem para novos dados ou que superestima a importância de certas interações aprendidas no conjunto de treino.

* **Impacto do Oversampling Manual:**
    * O oversampling manual no conjunto de treino para balancear as 6 classes pode introduzir redundância e potencialmente levar a um modelo que se ajusta demais às características das amostras replicadas, especialmente para as classes originalmente minoritárias. A distribuição das classes após o balanceamento mostrou todas as classes com 825 amostras cada.
    * *Impacto na Investigação:* As estimativas de desempenho no conjunto de treino podem ser otimistas, e a importância das features pode ser distorcida se o oversampling não for bem gerenciado.

* **Perda de Informação Ordinal com One-Hot Encoding para 'Nível de Ensino' e 'Experiência':**
    * Ao tratar 'Nível de ensino alcançado' e 'Tempo de experiência na área de dados' como puramente categóricas para o One-Hot Encoding, a informação inerente de ordem (ex: Mestrado > Graduação, 5 anos > 2 anos) é perdida para o modelo, a menos que ele consiga reaprendê-la através das interações e da estrutura das árvores. Isso pode tornar mais difícil para o modelo capturar tendências monotônicas simples.
    * *Impacto na Investigação:* Pode subestimar o impacto progressivo e ordenado dessas variáveis chave, que são centrais para a 1ª pergunta orientada a dados do `report.md`.

---

### Exemplificação de Casos de Superioridade (Imaginação e Extrapolação Fundamentada)

#### Cenários de Superioridade para o Modelo A (RandomForestClassifier - Binário):

1.  **Cenário: Necessidade de uma Ferramenta Rápida para Segmentação de Talentos para Programas de Desenvolvimento.**
    * **Situação:** Uma empresa de RH ou uma grande corporação deseja implementar rapidamente um sistema para identificar, de forma preliminar, quais profissionais de dados em seu banco de talentos ou entre novas contratações têm maior probabilidade de já estar em uma faixa salarial "elevada" (acima de R$8.000) versus aqueles que provavelmente estão abaixo desse patamar. O objetivo é direcionar os de "salário baixo/médio" para programas de desenvolvimento de carreira e os de "salário alto" para posições mais seniores ou de mentoria. A interpretabilidade dos fatores gerais (quais são os 3-5 principais impulsionadores) é importante, mas a distinção binária é o foco.
    * **Por que Modelo A seria superior:**
        * **Simplicidade e Clareza do Alvo:** A classificação binária é mais direta de entender e comunicar. O Modelo A mostrou bom desempenho (acurácia balanceada ~0.81) para esta tarefa simplificada. Para uma triagem inicial, essa distinção pode ser suficiente e mais acionável.
        * **Interpretação dos Fatores Principais:** O Random Forest do Modelo A fornece importâncias de features claras (senioridade, experiência, formação como top 3), que são fáceis de comunicar para justificar a segmentação. O heatmap de interação formação vs. experiência também é um visual poderoso e diretamente relevante para os objetivos do `report.md`.
        * **Robustez e Implementação:** Random Forests são relativamente robustos e fáceis de treinar. A calibração de probabilidades (realizada no Modelo A) também aumenta a confiança nas pontuações usadas para essa segmentação.
    * **Relação com o Problema:** Este cenário se relaciona com a "geração de insights para o mercado" e "auxiliar na equiparação salarial" (ao identificar grupos para desenvolvimento), fornecendo uma ferramenta prática para tomada de decisão em RH. A investigação da interação entre formação e experiência é bem suportada pela visualização gerada.

2.  **Cenário: Análise de Impacto para Políticas de Incentivo à Formação Contínua e Progressão para Senioridade.**
    * **Situação:** Uma associação de profissionais de dados ou um órgão governamental quer entender o impacto marginal de se alcançar um "nível sênior" ou de se obter "formação adicional" (como uma pós-graduação ou mestrado) na probabilidade de um profissional cruzar um limiar salarial específico considerado como um marco de "bem remunerado" (neste caso, R$8.000). O foco não é prever a faixa exata dentro de um espectro, mas sim o "salto" para uma categoria de maior remuneração.
    * **Por que Modelo A seria superior:**
        * **Foco no Limiar Específico:** O Modelo A é treinado especificamente para distinguir acima/abaixo do limiar de R$8.000. A análise das probabilidades calibradas pode mostrar o quão perto um profissional está desse limiar e como mudanças nas features importantes (senioridade, experiência, formação) alteram essa probabilidade.
        * **Visualização de Interação Direta:** O heatmap de "Probabilidade de Salário Alto por Formação Acadêmica e Experiência Profissional" gerado pelo Modelo A é ideal para mostrar como essas duas variáveis, combinadas, afetam a probabilidade de atingir "Salário Alto", informando diretamente políticas de incentivo à qualificação.
        * **Resultados Mais Claros para Decisão Binária:** Para a pergunta "este investimento em formação ou esta promoção para sênior tende a me levar para a faixa acima de R$8k?", o modelo binário oferece uma resposta mais direta e facilmente comunicável.
    * **Relação com o Problema:** Ajuda a "compreender os fatores que influenciam a variação salarial" de forma direcionada a um ponto de corte relevante e a "gerar insights" para o desenvolvimento profissional, alinhado com o objetivo de entender a interação entre formação e experiência.

---

#### Cenários de Superioridade para o Modelo B (GradientBoostingClassifier - Multiclasse):

1.  **Cenário: Desenvolvimento de um Guia Salarial Detalhado para Profissionais de Dados por Nível e Especialização.**
    * **Situação:** Uma plataforma de empregos ou uma consultoria de carreira deseja criar um guia salarial abrangente que não apenas indique se um salário é "alto" ou "baixo", mas que forneça uma estimativa mais granular das faixas salariais prováveis (ex: 'R$4k-R$8k', 'R$8k-R$16k', 'R$16k-R$30k') para diferentes combinações de experiência, formação acadêmica, área de formação, cargo, setor e localização. O objetivo é oferecer um benchmark mais completo.
    * **Por que Modelo B seria superior:**
        * **Granularidade da Previsão:** A capacidade de prever entre 6 faixas salariais agrupadas oferece um detalhamento muito maior da estrutura de remuneração do que uma simples classificação binária. Isso permite identificar não só se alguém ganha bem, mas *quão* bem, dentro de um espectro.
        * **Identificação de Padrões Multiclasse:** O Gradient Boosting, treinado para um alvo multiclasse, pode capturar nuances sobre quais combinações de features levam a faixas salariais intermediárias, não apenas aos extremos. Por exemplo, pode revelar que certos cargos com experiência moderada tendem a se concentrar na faixa de 'R$8k-R$16k', enquanto outros podem saltar mais rapidamente para faixas superiores.
        * **Análise de Transições:** Embora o modelo não seja temporal, as probabilidades para cada classe podem ser usadas para inferir a "próxima faixa salarial mais provável" se um profissional melhorar uma de suas qualificações (ex: ganhar mais experiência ou mudar de área de formação).
    * **Relação com o Problema:** Aborda mais profundamente a "variação salarial" em todo o espectro e pode gerar "insights para profissionais e empresas" sobre expectativas realistas de remuneração em diferentes estágios e especializações, incluindo o impacto da formação e experiência em diferentes níveis de renda.

2.  **Cenário: Investigação de "Gargalos" ou "Saltos" na Progressão Salarial ao Longo da Carreira.**
    * **Situação:** Um estudo socioeconômico quer identificar se existem pontos específicos na carreira de um profissional de dados (em termos de anos de experiência ou transição entre níveis de formação/senioridade) onde ocorrem os maiores "saltos" salariais, ou, inversamente, onde há "gargalos" ou estagnação, dificultando a passagem para faixas salariais mais elevadas.
    * **Por que Modelo B seria superior:**
        * **Múltiplas Faixas como Indicador de Progressão:** As 6 faixas salariais do Modelo B funcionam como degraus. Analisando as features mais importantes para distinguir entre faixas adjacentes (ex: o que diferencia quem está em 'R$4k-R$8k' de quem está em 'R$8k-R$16k'?), pode-se entender melhor os motores da progressão.
        * **Detecção de Limites entre Classes:** O modelo multiclasse pode revelar se, por exemplo, passar de "Graduação" para "Pós-graduação" tem um impacto maior na transição da faixa 'R$X-R$Y' para 'R$Y-R$Z' do que da faixa 'R$Y-R$Z' para 'R$Z-R$W'. Similarmente para anos de experiência.
        * **Flexibilidade do One-Hot Encoding:** Tratar 'Tempo de experiência' e 'Nível de ensino' como one-hot encoded (como no Modelo B) permite que o modelo atribua importâncias e coeficientes diferentes para cada faixa de experiência ou nível de ensino específico, sem assumir uma progressão linear, o que é útil para identificar saltos ou platôs não lineares.
    * **Relação com o Problema:** Este cenário foca em "identificar padrões e tendências" na variação salarial. A análise da interação entre formação e experiência ganha profundidade ao se observar como essa interação se manifesta em diferentes transições de faixas salariais, em vez de apenas um limiar binário.

#### Cenários de Superioridade para o Modelo B (GradientBoostingClassifier - Multiclasse):

1.  **Cenário: Desenvolvimento de um Guia Salarial Detalhado para Profissionais de Dados por Nível e Especialização.**
    * **Situação:** Uma plataforma de empregos ou uma consultoria de carreira deseja criar um guia salarial abrangente que não apenas indique se um salário é "alto" ou "baixo", mas que forneça uma estimativa mais granular das faixas salariais prováveis (ex: 'R\$4k-R\$8k', 'R\$8k-R\$16k', 'R\$16k-R\$30k') para diferentes combinações de experiência, formação acadêmica, área de formação, cargo, setor e localização. O objetivo é oferecer um benchmark mais completo para os profissionais avaliarem sua remuneração e para as empresas definirem faixas salariais competitivas.
    * **Por que Modelo B seria superior:**
        * **Granularidade da Previsão:** A capacidade de prever entre 6 faixas salariais agrupadas (conforme implementado no código do Modelo B) oferece um detalhamento muito maior da estrutura de remuneração do que uma simples classificação binária. Isso permite identificar não só se alguém ganha bem, mas *quão* bem, dentro de um espectro mais amplo.
        * **Identificação de Padrões Multiclasse:** O Gradient Boosting, treinado para um alvo multiclasse, pode capturar nuances sobre quais combinações de features levam a faixas salariais intermediárias, não apenas aos extremos. Por exemplo, pode revelar que certos cargos com experiência moderada tendem a se concentrar na faixa de 'R\$8k-R\$16k', enquanto outros podem saltar mais rapidamente para faixas superiores. Esta granularidade é essencial para um guia salarial detalhado.
        * **Potencial Preditivo do GBM para Dados Tabulares:** Se bem otimizado (como tentado com `RandomizedSearchCV`), Gradient Boosting pode modelar relações complexas e fornecer probabilidades mais refinadas para cada uma das 6 classes, oferecendo um panorama mais completo da distribuição salarial esperada para um perfil específico. O `report.md` indica que o Modelo B teve uma acurácia balanceada de 0.4015 para 6 classes, o que, embora modesto, é um ponto de partida para uma tarefa mais complexa que a binária.
    * **Relação com o Problema:** Aborda mais profundamente a "variação salarial" em todo o espectro e pode gerar "insights para profissionais e empresas" sobre expectativas realistas de remuneração em diferentes estágios e especializações. A análise da interação entre formação e experiência ganha profundidade ao se observar como ela se distribui por múltiplas faixas de renda, não apenas um corte binário.

2.  **Cenário: Investigação de "Gargalos" ou "Saltos" na Progressão Salarial ao Longo da Carreira para Fins de Política Educacional e de Mercado.**
    * **Situação:** Um estudo socioeconômico, ou uma instituição de ensino superior planejando seus cursos, quer identificar se existem pontos específicos na carreira de um profissional de dados (em termos de anos de experiência, tipo de formação, ou transição entre níveis de senioridade) onde ocorrem os maiores "saltos" salariais, ou, inversamente, onde há "gargalos" ou estagnação, dificultando a passagem para faixas salariais mais elevadas. O objetivo é entender onde intervenções (ex: cursos de especialização, programas de aceleração de carreira) seriam mais impactantes.
    * **Por que Modelo B seria superior:**
        * **Múltiplas Faixas como Indicador de Progressão:** As 6 faixas salariais do Modelo B funcionam como degraus em uma escada de progressão. Analisando as features mais importantes para distinguir entre faixas adjacentes (ex: o que diferencia quem está em 'R\$4k-R\$8k' de quem está em 'R\$8k-R\$16k'?), pode-se entender melhor os motores da progressão salarial.
        * **Detecção de Limites e Transições entre Classes:** O modelo multiclasse pode revelar se, por exemplo, passar de "Graduação" para "Pós-graduação" tem um impacto mais significativo na transição da faixa salarial 'A' para 'B' do que da faixa 'B' para 'C'. Similarmente para o acúmulo de anos de experiência – o modelo pode ajudar a identificar se os primeiros anos de experiência promovem saltos entre faixas mais baixas, enquanto a experiência mais avançada é necessária para as faixas superiores.
        * **Flexibilidade do One-Hot Encoding para Variáveis Ordinais:** No Modelo B, 'Tempo de experiência na área de dados' e 'Nível de ensino alcançado' são tratadas como categóricas e passam por One-Hot Encoding. Isso permite que o modelo atribua importâncias e aprenda pesos diferentes para cada faixa de experiência ou nível de ensino específico, sem assumir uma progressão linear ou ordinal estrita em seu impacto. Isso é útil para identificar saltos ou platôs não lineares na remuneração conforme essas variáveis mudam.
    * **Relação com o Problema:** Este cenário foca em "identificar padrões e tendências" na variação salarial de forma dinâmica. A análise da interação entre formação e experiência ganha profundidade ao se observar como essa interação se manifesta em diferentes transições de faixas salariais, em vez de apenas um limiar binário. Os resultados podem informar "políticas públicas, regulamentações e padrões da indústria" mencionados no `report.md` como parte do público-alvo.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Análise comparativa dos modelos da 2º pergunta orientada a dados

Discuta sobre as forças e fragilidades de cada modelo. Exemplifique casos em que um
modelo se sairia melhor que o outro. Nesta seção é possível utilizar a sua imaginação
e extrapolar um pouco o que os dados sugerem.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Análise comparativa dos modelos da 3º pergunta orientada a dados

## 3.1 Discussão de Forças e Fragilidades de Cada Modelo

---

### Modelo 1: LightGBM  
**Versão**: v7 – Classificação Binária com RFECV e Optuna  
**Fonte do Código**: `Conheça_o_Colab_(2).ipynb` 

#### 🔹 Forças do Modelo 1

**1. Alta Performance Preditiva em Dados Tabulares**
- LightGBM é altamente eficaz para dados tabulares.
- Acurácia de teste: ~0.833  
- ROC AUC: ~0.921–0.923  
- **Conexão com Objetivos**: Eficaz para prever variação salarial com base em fatores identificados.

**2. Fornecimento Direto de Importância das Features**
- Métricas claras de importância com base em ganho/divisões.
- Principais variáveis: `P2_i` (Experiência), `P2_f_Cargo_Atual` (Cargo), `P2_g_Nivel` (Senioridade).
- **Conexão com Objetivos**: Facilita a interpretação dos fatores que influenciam a variação salarial.

**3. Seleção Robusta de Features com RFECV**
- Subconjunto otimizado de 6 features.
- Redução de ruído e foco nos preditores mais impactantes.
- **Conexão com Objetivos**: Alinhado à identificação clara de padrões e tendências.

**4. Eficiência Computacional**
- Treinamento e inferência rápidos.
- Ideal para prototipagem e ajustes frequentes.
- **Conexão com Objetivos**: Agilidade no desenvolvimento do sistema inteligente.

**5. Robustez a Escalas e Tratamento de Categóricas**
- Não exige escalonamento.
- Lida bem com variáveis categóricas.
- **Conexão com Objetivos**: Facilita o pré-processamento e preserva a interpretabilidade.

#### 🔻 Fragilidades do Modelo 1

**1. Interpretabilidade do Ensemble**
- Explicações individuais pouco transparentes.
- Requer SHAP ou ferramentas similares para entender interações.
- **Impacto**: Dificulta interpretação granular, especialmente sobre interação entre formação e experiência.

**2. Sensibilidade a Hiperparâmetros**
- Boosting é sensível a parâmetros.
- Depende da qualidade da busca do Optuna.
- **Impacto**: Pode afetar robustez e conclusões da análise.

**3. Variável Alvo Binária Simplificada**
- Corte fixo em R$ 7.500 reduz granularidade.
- Agrupa salários de R$ 8.000 e R$ 30.000 como equivalentes.
- **Impacto**: Limita a profundidade dos insights sobre progressão salarial.

**4. Exclusão de `P1_b` (Gênero) pelo RFECV**
- Gênero removido por não melhorar performance.
- **Impacto**: Pode omitir um fator relevante para análise de equidade salarial.

---

### Modelo 2: Rede Neural  
**Versão**: RNA v2 – Classificação Binária com RayTune  
**Fonte do Código**: `Conheça_o_Colab (3).ipynb` 

#### 🔹 Forças do Modelo 2

**1. Modelagem de Interações Complexas e Não Lineares**
- Capacidade de capturar relações complexas entre variáveis.
- **Conexão com Objetivos**: Ideal para investigar interações entre formação e experiência.

**2. Embeddings para Features Categóricas**
- Representações densas e contextuais para variáveis como `P1_b`, `P2_g_Nivel`, `Regiao_Mapeada`, etc.
- **Conexão com Objetivos**: Pode revelar padrões mais sutis.

**3. Inclusão de Todas as Features Relevantes**
- Inclui `P1_b` (Gênero) e demais variáveis.
- **Conexão com Objetivos**: Permite uma análise mais ampla das disparidades de gênero e outros fatores.

**4. Alto Desempenho Preditivo Potencial**
- Acurácia de teste: ~0.838  
- ROC AUC: ~0.926 (ligeiramente superior ao LightGBM)
- **Conexão com Objetivos**: Suporta previsões robustas da variação salarial.

### Fragilidades do Modelo 2 (Rede Neural)

**Natureza "Caixa-Preta" e Baixa Interpretabilidade Direta:**
Redes neurais são notoriamente difíceis de interpretar. Entender *por que* o modelo tomou uma decisão específica para um indivíduo requer técnicas especializadas como LIME, SHAP ou Integrated Gradients. Isso dificulta a explicação dos resultados para públicos não técnicos ou para fins de auditoria.

- **Impacto na Investigação:** Limita a transparência e a capacidade de "interpretar os resultados" de maneira clara, dificultando a compreensão granular dos "fatores que influenciam a variação salarial", especialmente em contextos que demandam justificativas explicativas.

**Maior Complexidade de Treinamento e Ajuste:**
O treinamento de redes neurais requer maior cuidado com regularização, taxas de aprendizado, arquitetura, função de ativação, número de épocas e outros hiperparâmetros. O uso de RayTune foi uma escolha adequada, mas ainda assim exige tempo de computação significativo e expertise.

- **Impacto na Investigação:** A complexidade técnica pode se tornar uma barreira para reprodutibilidade, refinamento iterativo ou adoção prática do modelo por stakeholders não especializados.

**Demanda Computacional Elevada:**
Comparado ao LightGBM, o modelo de RNA requer mais tempo de treinamento, maior uso de memória e, potencialmente, GPU para desempenho ideal.

- **Impacto na Investigação:** Aumenta o custo de experimentação e de deploy do "sistema inteligente", podendo ser um entrave para ambientes com recursos computacionais limitados.

**Risco de Overfitting:**
Modelos de rede neural, especialmente com conjuntos de dados pequenos ou com número relativamente baixo de observações por classe, podem superajustar aos dados de treino sem as devidas técnicas de regularização e validação.

- **Impacto na Investigação:** Pode prejudicar a generalização do modelo, afetando sua aplicabilidade em novos contextos ou bases de dados futuras, o que compromete a robustez da "geração de insights para o mercado".

---

## 3.2. Conclusões Comparativas

- **Desempenho Preditivo:** Ambos os modelos apresentaram alto desempenho. A RNA teve leve vantagem no ROC AUC (~0.926 vs. ~0.921), indicando maior capacidade de discriminar entre classes. Contudo, essa diferença é pequena.

- **Interpretabilidade:** O LightGBM se destaca nesse aspecto, fornecendo métricas diretas de importância das features e permitindo interpretação mais acessível, ainda que limitada. A RNA, por outro lado, exige ferramentas especializadas para justificar suas decisões.

- **Tratamento de Interações:** A RNA possui vantagem estrutural por capturar interações complexas automaticamente, especialmente úteis para analisar a relação entre formação e experiência. O LightGBM pode captar algumas interações, mas não da mesma profundidade.

- **Uso de Features Demográficas:** A RNA retém `P1_b` (Gênero), permitindo avaliar seu papel preditivo. O LightGBM, ao eliminá-la, pode ser mais conservador, mas também pode negligenciar nuances relevantes para a equidade salarial.

- **Eficiência e Praticidade:** O LightGBM é mais leve, rápido e simples de implementar. Ideal para pipelines produtivos ou situações com recursos limitados.

---

## 3.3. Recomendação Estratégica

- Para **explicabilidade e aplicabilidade rápida** em ambientes com restrições de tempo e recursos: **LightGBM (Modelo 1)** é preferível.
- Para **exploração mais profunda de interações** e **investigação de disparidades complexas**, especialmente envolvendo demografia: **Rede Neural (Modelo 2)** é mais indicada.
- **Integração futura entre ambos os modelos (ensemble ou comparação sistemática)** pode reunir o melhor dos dois mundos: robustez, explicabilidade e capacidade preditiva.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Conclusão

Apresente aqui a conclusão do seu trabalho. Discussão dos resultados obtidos no trabalho, 
onde se verifica as observações pessoais de cada aluno.

Uma conclusão deve ter 3 partes:

   * Breve resumo do que foi desenvolvido
	 * Apresenação geral dos resultados obtidos com discussão das vantagens e desvantagens do sistema inteligente
	 * Limitações e possibilidades de melhoria


# REFERÊNCIAS 

DATA HACKERS. **State of Data Brazil 2023**. Disponível em: https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023. Acesso em: 5 mar. 2025.

BAIN & COMPANY; DATA HACKERS. **State of Data 2024**. [S.l.]: Bain & Company, 2024. Disponível em: <https://www.stateofdata.com.br/>. Acesso em: 6 mar. 2025.

H2R PESQUISAS; TOTVS. **Estudo Panorama das Carreiras 2030: o que esperar das profissões até o fim da década**. Setembro/2023. Acesso em: 6 mar. 2025

INSTITUTO NACIONAL DE ESTUDOS E PESQUISAS EDUCACIONAIS ANÍSIO TEIXEIRA (INEP). **Censo da Educação Superior. Brasília**, DF: INEP,[2022]. Disponível em: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior. Acesso em: 15 mar. 2025.


# APÊNDICES

---

# Codigos do Projeto

## Códigos relacionados a 1º pergunta orientada a dados

### Limpeza de Dados
- [Limpeza de Dados Base Principal State of Data](/src/code_data_cleanest/base_principal_state_of_data/1_pergunta_orientada_a_dados/versão_3)  
- [Limpeza de Dados Base Auxiliar](/src/code_data_cleanest/base_auxiliares/1_pergunta_orientada_a_dados) 

### Analise Exploratória de Dados
- [Análise Exploratória de Dados](/src/analise_exploratorias_perguntas_orientadas_a_dados/1_pergunta_orientada_a_dados/)

### Indução a Modelos
- [Indução a Modelos](/src/modelos/modelo_1/modelo_state_of_data/)

---

## Códigos relacionados a 2º pergunta orientada a dados

### Limpeza de Dados
[Limpeza de Dados]() ⚠️(2ºPerguntOrientadaaDados) 

### Analise Exploratória de Dados
[Análise Exploratória de Dados]() ⚠️(2ºPerguntOrientadaaDados) 

### Indução a Modelos
[Indução a Modelos]() ⚠️(2ºPerguntOrientadaaDados) 

---

## Códigos relacionados a 3º pergunta orientada a dados

### Limpeza de Dados
[Limpeza de Dados](/src/code_data_cleanest/base_principal_state_of_data/3_pergunta_orientada_a_dados/)   

### Analise Exploratória de Dados
[Análise Exploratória de Dados](/src/analise_exploratorias_perguntas_orientadas_a_dados/3_pergunta_orientada_a_dados/)  

### Indução a Modelos
[Indução a Modelos](/src/modelos/modelo_3)  

---

# Artefatos do Projeto 

## Artefatos relacionados a 1º pergunta orientada a dados
### Base de Dados Originais
- [Base de Dados Original State of Data](/assets/data/bases_principais/base_principal_state_of_data)
- [Base de Dados Original Auxiliar](/assets/data/bases_principais/bases_auxiliar/1_pergunta_orientada_a_dados)

### Limpeza de Dados
- [Base de Dados Original State of Data](/assets/data/cleaned_data/1_pergunta_orientada_a_dados/versão_3/base_principal_state_of_data)
- [Base de Dados Original Auxiliar](/assets/data/cleaned_data/1_pergunta_orientada_a_dados/versão_3/base_auxiliar)

### Analise Exploratória de Dados
[Análise Exploratória de Dados](/assets/results/análise_exploratória_de_dados/1_pergunta_orientada_a_dados)

### Indução a Modelos
[Indução a Modelos](/assets/results/modelos/1º_pergunta_orientada_a_dados/imagens)

---

## Artefatos relacionados a 2º pergunta orientada a dados
### Base de Dados Originais
[Base de Dados Originais]()  ⚠️(2ºPerguntOrientadaaDados)

### Limpeza de Dados
[Limpeza de Dados]()  ⚠️(2ºPerguntOrientadaaDados) 

### Analise Exploratória de Dados
[Análise Exploratória de Dados]() ⚠️(2ºPerguntOrientadaaDados) 

### Indução a Modelos
[Indução a Modelos]() ⚠️(2ºPerguntOrientadaaDados) 

---

## Artefatos relacionados a 3º pergunta orientada a dados
### Base de Dados Originais
[Base de Dados Originais](/assets/data/bases_principais/base_principal_state_of_data)   

### Limpeza de Dados
[Limpeza de Dados](/assets/data/cleaned_data/3_pergunta_orientada_a_dados)  

### Analise Exploratória de Dados
[Análise Exploratória de Dados](/assets/results/análise_exploratória_de_dados/3_pergunta_orientada_a_dados)  

### Indução a Modelos
[Indução a Modelos](/assets/results/modelos/3_pergunta_orientada_a_dados) 

---

**Da apresentação final (armazenado no repositório);** ⚠️

**Do vídeo de apresentação (armazenado no repositório).** ⚠️



