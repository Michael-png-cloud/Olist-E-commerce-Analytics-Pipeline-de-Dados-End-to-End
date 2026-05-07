Olist E-commerce: Pipeline de Dados & Business Intelligence

Este projeto analisa o ecossistema de e-commerce brasileiro utilizando o dataset da Olist. O objetivo foi construir um fluxo de dados completo (End-to-End), desde a extração de dados brutos até a criação de um dashboard analítico para tomada de decisão.

O projeto demonstra competências em Engenharia de Dados, SQL e Business Intelligence, focando na portabilidade do código e na resolução de conflitos de tipos de dados.

Fonte de Dados
Os dados utilizados neste projeto são provenientes do dataset público da Olist hospedado no Kaggle:
[Brazilian E-Commerce Public Dataset by Olist] https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce


Para reproduzir este projeto localmente, siga estes passos:
1 - Faça o o dowload repositório em zip e seguida extraia
2 - Prepare os dados: Abra a pasta chamada `brazilian-ecommerce/versions/2/` na raiz do projeto e coloque os arquivos CSV baixados do Kaggle lá dentro.
3 - Execute o ETL: Rode o script `processo_etl.py` para gerar o banco de dados `olist.db`.

Pré-requisitos e Configuração ODBC
Para que o Power BI consiga ler os dados do banco SQLite (`olist.db`), é necessário configurar um DSN (Data Source Name) no seu Windows:
1. Instalação do Driver: Baixe e instale o [SQLite ODBC Driver](http://www.ch-werner.de/sqliteodbc/) (versão compatível com o seu sistema, geralmente 64-bit).
2. Configuração do DSN:
   - Abra o "Administrador de Fontes de Dados ODBC (64 bits)" no Windows.
   - Vá em "DSN de Usuário" e clique em Adicionar.
   - Escolha SQLite3 ODBC Driver.
   - No campo Data Source Name, use o nome: `ProjetoOlist`.
   - No campo Database Name, clique em `Browse` e selecione o arquivo `olist.db` que você gerou com o Python.
   - Abra o arquivo `dashboard_olist_pedidos.pbit` e, se necessário, atualize o caminho da fonte de dados ODBC para o seu banco local.
3. Ajuste no Power BI:
   - Ao abrir o arquivo `.pbit`, se o Power BI solicitar o caminho, vá em `Transformar Dados` -> `Configurações da Fonte de Dados`.
   - Clique em `Alterar Fonte` e certifique-se que o nome do DSN corresponde ao que você criou.

---

 Stack Tecnológica
* Linguagem: Python (Pandas, SQLAlchemy)
* Banco de Dados: SQL (SQLite)
* Visualização: Power BI (DAX, M-Query)
* Ferramentas: VS Code, Driver ODBC SQLite

---

 Arquitetura do Pipeline
1.  Extração e ETL (Python): Limpeza de dados brutos, tratamento de nulos e normalização de datas. Utilização de caminhos relativos para garantir a portabilidade do script.
2.  Armazenamento (SQL): Persistência dos dados em um banco relacional SQLite.
3.  Modelagem (Power BI): Estruturação em Star Schema, criação de tabela `dCalendario` e desenvolvimento de medidas DAX para KPIs de vendas e logística.

---

Desafios e Aprendizados (Troubleshooting)

Um dos grandes focos deste projeto foi a resolução de problemas reais encontrados durante o desenvolvimento:
* Conflitos de Tipos (Binary/BLOB): Identifiquei que colunas numéricas eram lidas como binários via ODBC. Resolvi aplicando `CAST(coluna AS TEXT)` diretamente no SQL de extração.
* Portabilidade: Refatorei o script Python para usar o módulo `os`, permitindo que o pipeline seja executado em qualquer diretório sem alterações manuais de caminho.
* Contexto de Filtro (DAX): Implementação de rankings dinâmicos utilizando `RANKX` e `ALLSELECTED` para garantir a precisão dos dados em visuais filtrados.

---

 📂 Estrutura de Pastas
```text
├── brazilian-ecommerce/versions/2     # Caminho para guardar CSVs
├── processar_etl.py                   # Script de limpeza e carga
├── dashboard_olist_pedidos.pbit       # Arquivo do Power BI
├── README.md                          # Documentação do projeto
└── .gitignore                         # Arquivos ignorados pelo Git (.db, cache)
