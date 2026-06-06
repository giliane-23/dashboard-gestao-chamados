# 📊 Dashboard de Gestão de Chamados

Este é um projeto focado em **Análise de Dados, UX e Visão de Negócio**, desenvolvido para centralizar, monitorar e otimizar o acompanhamento de tickets e demandas de suporte.

A ideia do projeto surgiu a partir da observação de rotinas diárias em Customer Success, identificando a oportunidade de transformar planilhas estáticas em um painel visual dinâmico e interativo para apoio à tomada de decisão.

---

## ⚠️ Nota Importante sobre os Dados
Para a construção e validação deste painel, foi utilizada uma **base de dados fictícia gerada por Inteligência Artificial** (`dados.csv`). Este repositório tem fins estritamente didáticos e de portfólio pessoal, **não contendo** quaisquer dados reais, confidenciais ou sensíveis de clientes ou da empresa onde atuo.

---

## 🚀 Funcionalidades Principais

- **Visualização de KPIs operacionais:** Total de empresas mapeadas, chamados em aberto, pendentes, em andamento, concluídos e alertas de empresas sem ticket.
- **Gráficos Interativos:** Distribuição de chamados por status utilizando Plotly.
- **Filtros Dinâmicos:** Filtragem rápida de dados por status diretamente na interface.
- **Automação de Relatórios:** Script em Python integrado para tratamento de dados e geração automática de relatórios formatados em Excel (`relatorio.xlsx`) utilizando `openpyxl`.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **Python** (Linguagem principal)
- **Streamlit** (Construção da interface web e design clean/pastel)
- **Pandas** (Manipulação, limpeza e tratamento dos dados brutos)
- **Plotly Express** (Criação de gráficos interativos e dinâmicos)
- **OpenPyXL** (Formatação estética e automação de planilhas Excel)

---

## 📁 Estrutura do Projeto

- `dados.csv`: Base de dados simulada para o projeto.
- `app.py`: Código-fonte do dashboard interativo em Streamlit.
- `gerar_relatorio.py`: Script responsável por processar o CSV e gerar o relatório formatado.
- `/IMG`: Screenshots e elementos visuais do painel.
