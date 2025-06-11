# 📚 Documentação do Projeto - Flask Rick and Morty Chatbot

## 💡 Visão Geral

Este projeto é um **chatbot temático de "Rick and Morty"** desenvolvido com Flask, que utiliza uma **IA generativa** para responder perguntas como se fosse um personagem da série.  
Além disso, o sistema também avalia automaticamente a qualidade das respostas fornecidas pela IA.

---

## 🗂️ Estrutura do Projeto

### 🔹 `MrPoopybuttholeAI.py`
Responsável pela **configuração da IA** e do **avaliador de respostas**:
- Integração com a API do Gemini.
- Definição de prompts personalizados (agente e juiz).
- Ferramentas para leitura de informações dos personagens.
- Funções principais:
  - `responde_com_ia()`
  - `avalia_resposta()`

### 🔹 `app/routes.py`
Define as **rotas Flask** usadas na aplicação:
- `/health`: Verifica o status da API.
- `/`: Tela inicial para entrada do nome.
- `/usuario`: Interface do chat, histórico e opção de limpar mensagens.

### 🔹 `app/service.py`
Gerencia as **mensagens** trocadas com o chatbot:
- `manda_mensagem()`: Armazena mensagens do usuário.
- `pegar_mensagens()`: Recupera o histórico.
- `manda_mensagem_ia()`: Envia e registra respostas da IA.
- `apagar_mensagens()`: Limpa o histórico.

---

## 🚀 Como Rodar o Projeto

### ✅ Pré-requisitos

- Python **3.8+**
- `pip` instalado
- Bibliotecas listadas no `requirements.txt`

### 📦 Passo a passo

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <PASTA_DO_PROJETO>
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure a chave da API**:
   - Crie um arquivo `.env` na raiz do projeto.
   - Adicione a seguinte linha:
     ```
     user=
     password=
     host=
     port=
     database=
     GEMINI_API_KEY=
     ```

4. **Execute o servidor Flask**:
   ```bash
   python main.py
   ```

5. **Acesse no navegador**:
   - URL padrão: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Estrutura de Diretórios

```
├── MrPoopybuttholeAI.py
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── service.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── usuario.html
│   ├── static/
│   │   ├── images/
│   │   ├── index.css
│   │   ├── base.css
├── requirements.txt
├── .env
```

---

## 📝 Observações Finais

- Certifique-se de ter o arquivo **`rick_and_morty_characters.txt`** na raiz do projeto — ele é essencial para que o agente acesse as informações dos personagens.
- A interface web utiliza estilos personalizados e imagens para garantir a **experiência visual no universo de Rick and Morty**.

---

> 👨‍💻 Projeto desenvolvido com muito caos científico. Wubba Lubba Dub Dub!