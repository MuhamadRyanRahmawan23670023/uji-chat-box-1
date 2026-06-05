import streamlit as st
from engine import ChatEngine

st.set_page_config(page_title="SIGAB — Chatbot Bencana", page_icon="🚨")
st.title("🚨 SIGAB")
st.caption("Sistem Informasi Cepat Tanggap Bencana — Berbasis Finite State Machine")

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "engine" not in st.session_state:
    st.session_state.engine = ChatEngine()

# --- Sidebar ---
with st.sidebar:
    st.header("📋 Topik yang Tersedia")
    st.markdown("""
    Ketik kata kunci berikut:

    🌍 `gempa` — Gempa Bumi  
    🌊 `banjir` — Banjir  
    🌊 `tsunami` — Tsunami  
    🔥 `kebakaran` — Kebakaran  
    🌋 `erupsi` / `gunung` — Gunung Api  
    🚶 `evakuasi` — Prosedur Evakuasi  
    🩹 `pertolongan pertama` — P3K  
    📦 `logistik` — Bantuan & Logistik  
    🧠 `trauma` / `psikososial` — Dukungan Mental  
    🏗️ `pemulihan` — Pasca Bencana  
    """)
    st.divider()
    st.markdown("📞 **Kontak Darurat:**")
    st.markdown("BNPB: **117** | Basarnas: **115**\nDamkar: **113** | Ambulans: **119**")
    st.divider()
    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []
        st.session_state.engine.reset()
        st.rerun()

# --- Tampilkan Riwayat Chat ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Pesan Awal ---
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown(
            "Halo! Saya **SIGAB** — Sistem Informasi Cepat Tanggap Bencana. 🚨\n\n"
            "Saya dapat membantu kamu dengan informasi seputar:\n"
            "**gempa bumi, banjir, tsunami, kebakaran, erupsi gunung api,**\n"
            "**evakuasi, pertolongan pertama, logistik, psikososial, dan pemulihan pasca bencana.**\n\n"
            "Silakan ketik topik yang ingin kamu tanyakan!"
        )

# --- Input Chat ---
if prompt := st.chat_input("Tanyakan seputar bencana dan penanganannya..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.engine.get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
