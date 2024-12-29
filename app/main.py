import streamlit as st
from utils import hash_password
from ia_module import get_chat_response
from decouple import config

# Configurações da página
st.set_page_config(
    page_title="Fábio GPT",
    page_icon="🤖",
    layout="wide",
)

# Estilos personalizados usando CSS
with open("app/style.css") as file:
    st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

# Recuperando o Hash da senha de autenticação
password_hash = config('PASSWORD_HASH')


# Cria uma sessão para armazenar a conversa enquanto o app está aberto.
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Você é um super ajudante que pode responder amigavelmente qualquer pessoa."}
    ]

st.title("🤖 Fábio-GPT")
st.write("Baseado no Groq, um DSL que permite a construção de chatbots.")

# Contêiner rolável para exibir as mensagens do chat.
with st.container():
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-message">🧑 <strong>Usuário:</strong> {msg["content"]}</div>', unsafe_allow_html=True)
        elif msg["role"] == "assistant":
            st.markdown(f'<div class="bot-message">🤖 <strong>Bot:</strong> {msg["content"]}</div>', unsafe_allow_html=True)

# Caixa de perguntas do usuário.
prompt = st.chat_input("Digite algo para conversar com o bot:")
if prompt:
    # Adiciona a mensagem do usuário ao contexto
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Exibe a mensagem do usuário na interface
    st.markdown(f'<div class="user-message">🧑 <strong>Usuário:</strong> {prompt}</div>', unsafe_allow_html=True)

    # Obtém a resposta do bot
    bot_response = get_chat_response(st.session_state.messages)

    # Adiciona a resposta do bot ao contexto
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Exibe a resposta do bot na interface
    st.markdown(f'<div class="bot-message">🤖 <strong>Bot:</strong> {bot_response}</div>', unsafe_allow_html=True)

