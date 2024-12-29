import streamlit as st
from groq import Groq

# Busca a chave da API do Streamlit Secrets
key = st.secrets["GROQ_API_KEY"]

# Inicializa o cliente da API com a chave
client = Groq(api_key=key)

def get_chat_response(messages):
    """Envia a conversa para a API Groq e retorna a resposta do bot."""
    response = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
    )

    # Retorna o conteúdo da resposta gerada
    return response.choices[0].message.content
