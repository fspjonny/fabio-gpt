
# 🤖 **Fábio GPT**

## **📚 Descrição do Projeto**

É uma aplicação de Chatbot com IA que utiliza a tecnologia da Groq para gerar as respostas.

---

## **🛠️Pré-requisitos**  

- **Python** 3.12 ou superior  
- **Conta na Groq** (para usar a sua API da Groq 😉)

---
## **🛠️Requisitos do projeto**
- **streamlit ^0.6.0"**
- **groq ^0.13.0"**
- **python-decouple ^3.8"**
---

## **🖥️Instalação**  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/fspjonny/fabio-gpt.git
   ```  

2. Crie um arquivo `.env` na raiz do projeto com base no `.env.example` e configure as variáveis de ambiente.  

**Exemplo**:
```
GROQ_API_KEY='sua-chave-de-api-aqui'

PASSWORD_HASH='crie-seu-hash-coloque-aqui'
```

3. Se estiver usando como gerenciador de pacotes o **Poetry**:
- crie um virtual environment
   ```bash
   poetry shell
   ```
- logo depois instale as dependências:   
   ```bash
   poetry install
   ```
4. Se você usa o PIP ou qualquer outro gerenciador de pacotes, instale as dependências, citadas acima em  
**🛠️Requisitos do projeto**.

---

## **🚀 Execução do Chatbot**
- execute o comando na raiz do projeto com seu ambiente virtual ativado:

```bash
streamlit run .\app\main.py
```

- Abra o seu navegador e acesse o link: http://localhost:8501/

### ⚠️ Atenção:
- É necessário criar um hash md5 para validar a senha de acesso ao chatbot. 🔒  
É uma segurança simples para limitar o acesso do chatbot só para pessoas que você autorizar.🤫  

- Para gerar o hash md5, utilize um gerador de hash md5 online, como o [https://www.md5hashgenerator.com/](https://www.md5hashgenerator.com/)  

- Digite uma senha no link para gerar um **hash md5** que você deve salvar no arquivo **.env**, pois ele será carregado para validar a sua senha de acesso ao chatbot e você poderá liberar o uso do chatbot para outras pessoas testarem. 👍
---

## **✉️Contato**

Em caso de dúvidas ou problemas, entre em contato:  
- **E-mail**: [fabio.silvapedro@gmail.com](mailto:fabio.silvapedro@gmail.com)

---

## **👋😃 Obrigado por visitar**