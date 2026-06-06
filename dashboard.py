import streamlit as st
import pandas as pd
import plotly.express as px
print("Plotly funcionando!")

st.set_page_config(
    page_title="Dashboard de Gestão de Chamados",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.block-container{
    max-width: 1100px;
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
}
</style>
""", unsafe_allow_html=True)


# Background da página
st.markdown("""
<style>
            
/* Barra superior */
[data-testid="stHeader"] {
    background-color: #d1f5de;
}
            
/* Fundo geral */
.stApp {
    background-color: #d1f5de;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #d1f5de;
}

            /* Containers */
[data-testid="stVerticalBlock"] > div {
    border-radius: 12px;
}

/* Dataframes */
[data-testid="stDataFrame"] {
    background-color: #f8fffa;
    border-radius: 12px;
    border: 1px solid #b8eac8;
    padding: 10px;
}         

            /* Containers com border=True */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 15px !important;
    border: 1px solid #b8eac8 !important;
}
              
</style>
""", unsafe_allow_html=True)


def card(titulo, valor, cor):
    st.markdown(
        f"""
        <style>
        .card-hover {{
            background-color: {cor};
            padding: 06px;
            border-radius: 13px;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
            border-left: 5px solid rgba(0,0,0,0.15);
        }}

        .card-hover:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }}

        .card-title {{
            font-size: 12px;
            margin-bottom: 5px;
        }}

        .card-value {{
            font-size: 20px;
            font-weight: bold;
            margin: 0;
        }}
    
        </style>

        <div class="card-hover">
            <div class="card-title">{titulo}</div>
            <div class="card-value">{valor}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
# -----------------------------------------------------#


dados = pd.read_csv("dados.csv")
col1, col2, col3 = st.columns([2, 0.8, 0.8])

with col1:
    st.markdown(
        """
   <h1 style='font-size:35px; margin-top:40px;'>
        📊 Dashboard de Chamados
    </h1>
    """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("##### 🔍 Filtros")

    filtro_col, _ = st.columns([0.7, 0.3])

    with filtro_col:
        status_escolhido = st.selectbox(
            "",
            ["Todos"] + list(dados["status"].unique()),
            label_visibility="collapsed"
        )


# Lógica (aplicação dos filtros)
if status_escolhido != "Todos":
    dados_filtrados = dados[dados["status"] == status_escolhido]
else:
    dados_filtrados = dados

sem_ticket = len(dados[dados["ticket"].isna()])
abertos = len(dados[dados["status"] == "aberto"])
concluidos = len(dados[dados["status"] == "concluido"])
pendentes = dados[dados["status"] == "Pendente"]
em_andamento = dados[dados["status"] == "Em andamento"]

# Sub-Título
st.caption(
    "Monitoramento de tickets, acompanhamento de empresas e indicadores operacionais."
)


# indicadores
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    card("🏢 Empresas", len(dados_filtrados), "#BDE0FE")

with col2:
    card(
        "⚠️ Sem Ticket",
        len(dados_filtrados[dados_filtrados["ticket"].isna()]),
        "#FFADAD"
    )

with col3:
    card(
        "📂 Abertos",
        len(dados_filtrados[dados_filtrados["status"] == "Aberto"]),
        "#FFF3B0"
    )

with col4:
    card(
        "🔄 Andamento",
        len(dados_filtrados[dados_filtrados["status"] == "Em andamento"]),
        "#A2D2FF"
    )

with col5:
    card(
        "⏳ Pendentes",
        len(dados_filtrados[dados_filtrados["status"] == "Pendente"]),
        "#FFD6A5"
    )

with col6:
    card(
        "✅ Concluídos",
        len(dados_filtrados[dados_filtrados["status"] == "Concluído"]),
        "#CAFFBF"
    )

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(" 📊 Chamados por Status")

status_contagem = (
    dados["status"]
    .value_counts()
    .reset_index()
)
status_contagem.columns = [
    "Status",
    "Quantidade"
]

fig = px.bar(
    status_contagem,
    x="Status",
    y="Quantidade",
    text="Quantidade",
    color="Status",
    color_discrete_map={
        "Aberto": "#FFF3B0",
        "Em andamento": "#A2D2FF",
        "Pendente": "#FFD6A5",
        "Concluído": "#CAFFBF"
    }
)

fig.update_layout(
    height=350,
    plot_bgcolor="#F8FFFA",
    paper_bgcolor="#F8FFFA",
    showlegend=False,
    bargap=0.5,
    margin=dict(
        l=20,
        r=20,
        t=20,
        b=20
    )
)

fig.update_traces(width=0.35)

with st.container():
    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.success(
    f"Existem {len(dados[dados['ticket'].isna()])} empresas sem ticket."
)

st.subheader("Empresas sem Ticket")

st.dataframe(
    dados[dados["ticket"].isna()]
)


# Tabela
st.subheader("Empresas")

st.dataframe(dados_filtrados)

st.caption(
    "Dashboard desenvolvido em Python + Streamlit para monitoramento e acompanhamento de chamados."
)
