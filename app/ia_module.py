from groq import Groq
from decouple import config

# Busca a chave da API da conta.
key = config('GROQ_API_KEY') 

client = Groq(api_key=key)

def get_chat_response(messages):
    """Envio a conversa para a API Groq e ela retorna a resposta do bot."""
    response = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
    )

    # O Groq já retorna o conteúdo da resposta gerada em formato Markdown.
    return response.choices[0].message.content
