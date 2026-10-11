# Pipeline de Dados com IoT e Docker

## 1. Descrição do projeto

Este projeto tem como objetivo desenvolver um pipeline de dados utilizando um conjunto de dados de dispositivos IoT (Internet das Coisas), realizando o tratamento, o armazenamento e a análise de registros de temperatura.

Os dados são processados com Python e Pandas, armazenados em um banco de dados PostgreSQL executado em um contêiner Docker e apresentados em um dashboard interativo desenvolvido com Streamlit.

## 2. Objetivos

* Processar e tratar os dados de temperatura.
* Identificar e remover registros duplicados.
* Armazenar os dados tratados no PostgreSQL.
* Criar consultas e views SQL para análise.
* Apresentar indicadores e gráficos em um dashboard.

## 3. Tecnologias utilizadas

* **Python:** processamento dos dados.
* **Pandas:** limpeza e transformação do conjunto de dados.
* **SQLAlchemy:** conexão entre Python e PostgreSQL.
* **PostgreSQL 16:** armazenamento dos dados.
* **Docker Desktop:** execução do banco de dados em contêiner.
* **Streamlit:** criação do dashboard.
* **SQL:** consultas e criação de views analíticas.

## 4. Estrutura do projeto

```text
pipeline-iot/
├── data/
│   └── IOT-temp.csv
├── docs/
├── sql/
│   ├── 01_create_table.sql
│   └── 02_views.sql
├── src/
│   ├── load_data.py
│   ├── verificar_csv.py
│   └── dashboard.py
├── docker-compose.yml
└── README.md
```

## 5. Etapas do pipeline

1. Leitura do conjunto de dados CSV.
2. Tratamento dos dados com Python e Pandas.
3. Conversão dos tipos de dados e remoção de registros inválidos.
4. Identificação e remoção de duplicidades.
5. Armazenamento dos dados tratados no PostgreSQL.
6. Criação de views SQL para análise.
7. Consulta aos dados e visualização dos resultados no dashboard.

## 6. Resultados obtidos

Após o processamento e a carga dos dados, foram obtidos os seguintes resultados:

* Total de registros: 97.605.
* Temperatura mínima: 21,00.
* Temperatura máxima: 51,00.
* Temperatura média: 35,05.

Os indicadores são apresentados no dashboard desenvolvido com Streamlit, juntamente com gráficos de registros por categoria e de temperatura média ao longo dos dias.

## 7. Como executar o projeto

### Pré-requisitos

* Windows com Docker Desktop instalado.
* Python instalado.
* Dependências do projeto instaladas no ambiente virtual.

### Executar o banco de dados

Na pasta do projeto, execute:

```bash
docker compose up -d
```

### Executar o processamento dos dados

Com o ambiente virtual configurado, execute:

```bash
.venv\Scripts\python.exe src\load_data.py
```

### Executar o dashboard

Execute:

```bash
.venv\Scripts\python.exe -m streamlit run src\dashboard.py
```

Depois, abra o endereço:

http://localhost:8501

## 8. Conclusão

O projeto demonstra a integração entre processamento de dados, banco de dados relacional e visualização de informações. O pipeline permite tratar e armazenar registros de temperatura, enquanto as views SQL e o dashboard facilitam a análise dos dados.

O desenvolvimento proporcionou a aplicação prática de conceitos de Python, SQL, PostgreSQL, Docker e visualização de dados.
