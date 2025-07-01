import streamlit as st
import pandas as pd

# 🌈 Cores da identidade visual
AZUL_ROYAL = "#2643E8"
AZUL_MARINHO = "#0A1033"
LILAS = "#CAC0F4"
DOURADO = "#D4AF37"
BRANCO = "#F9FAFB"
CINZA = "#E5EAF2"

# 🎯 Configurações da página
st.set_page_config(page_title="Innódia - Sistema Empresarial", layout="wide", initial_sidebar_state="expanded")

# 🌐 Estilo visual refinado
st.markdown(f"""
<style>
    body {{
        background-color: {CINZA};
    }}
    .stApp {{
        background-color: {CINZA};
        font-family: 'Segoe UI', sans-serif;
    }}
    h1, h2, h3 {{
        color: {AZUL_MARINHO};
        font-weight: 700;
    }}
    .stButton > button {{
        background-color: {AZUL_ROYAL};
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-size: 16px;
        transition: 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: {DOURADO};
        color: {AZUL_MARINHO};
    }}
    .card {{
        background-color: {BRANCO};
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 1rem;
        text-align: center;
    }}
</style>
""", unsafe_allow_html=True)

# 📋 Menu lateral elegante
menu = st.sidebar.radio("📌 Menu", ["🏠 Início", "👥 Clientes", "📈 Relatórios"])
st.sidebar.markdown("---")
st.sidebar.markdown("**🌐 Innódia © 2025**")

# 🏠 Início
if menu == "🏠 Início":
    st.title("📊 Painel Administrativo - Innódia")
    st.markdown("Sistema inteligente de automação e gestão empresarial com visual moderno e profissional.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='card'><h3>👥 Clientes</h3><h2 style='color:{AZUL_ROYAL};'>12</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card'><h3>📦 Estoque</h3><h2 style='color:{AZUL_ROYAL};'>37</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='card'><h3>💰 Vendas</h3><h2 style='color:{AZUL_ROYAL};'>R$ 4.820</h2></div>", unsafe_allow_html=True)

# 👥 Clientes
elif menu == "👥 Clientes":
    st.title("👤 Gerenciar Clientes")

    if "clientes" not in st.session_state:
        st.session_state.clientes = []

    with st.form("form_cliente"):
        st.subheader("📝 Adicionar Novo Cliente")
        col1, col2, col3 = st.columns(3)
        with col1:
            nome = st.text_input("Nome completo")
        with col2:
            email = st.text_input("E-mail")
        with col3:
            telefone = st.text_input("Telefone")
        enviar = st.form_submit_button("Cadastrar")

        if enviar:
            if nome and email and telefone:
                st.session_state.clientes.append({
                    "Nome": nome,
                    "E-mail": email,
                    "Telefone": telefone
                })
                st.success(f"✅ Cliente {nome} cadastrado com sucesso!")
            else:
                st.warning("⚠️ Por favor, preencha todos os campos.")

    st.markdown("---")
    st.subheader("📋 Lista de Clientes")

    if st.session_state.clientes:
        df = pd.DataFrame(st.session_state.clientes)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Nenhum cliente cadastrado ainda.")

# 📈 Relatórios
elif menu == "📈 Relatórios":
    st.title("📈 Relatórios de Gestão")
    st.markdown("📌 Aqui você poderá ver gráficos de clientes, estoque e vendas em tempo real (em breve).")
    st.info("Este módulo será ativado com integração de dados reais.")