# Imports
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
import google.generativeai as genai
import os
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain.prompts import PromptTemplate
import sys
from langchain.schema import HumanMessage, SystemMessage

# Validação de parâmetros
if len(sys.argv) != 2:
    print("Usage: python MrPoopybuttholeAI.py <user_question>")
    sys.exit(1)



# Configuração básica do Gemini
load_dotenv() # Obtendo a chave do gemini
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

chat = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key=api_key
)


# Configuração do prompt
system_prompt_text = '''
#Contexto
Você é um agente especializado na série animada "Rick and Morty"

#Missao
Sua missão é compreender e analisar as perguntas dos usuários para que possa responde-las de acordo com a base de dados que será fornecida a você sobre a série por nós. 
O único arquivo que você deve acessar é o arquivo rick_and_morty_characters.txt
É importante ressaltar que todas as informações utilizadas por você devem ter fonte como as informações do arquivo rick_and_morty_characters.txt

#Instruções
- Leia atentamente a pergunta do usuário e compreenda em detalhes
- Ligue essa pergunta com algum dado do documento
- Caso não encontre nenhuma informação relevante, indique que você não sabe e utilize somente sua própria base
- Responda como um adolescente médio de 16 anos bem nerd
- No final de cada pergunta você deve se disponibilizar para responder qualquer outra duvida do usuário
- Você apenas irá responder perguntas sobre "Rick and Morty"

Pergunta do usuário: {input}
'''
system_prompt = PromptTemplate.from_template(system_prompt_text)


# Configuração da memória
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# Criação da ferramenta de acesso ao arquivo de informações
def ler_arquivo(nome_arquivo: str) -> str:
 """Lê o conteúdo de um arquivo de texto."""
 try:
    with open("rick_and_morty_characters.txt", 'r', encoding='utf-8') as f:
        return f.read()
 except FileNotFoundError:
    return f"Erro: Arquivo '{nome_arquivo}' não encontrado."
 except Exception as e:
    return f"Erro ao ler o arquivo '{nome_arquivo}': {e}" 
 
tools = [ Tool( name="ler_arquivo", 
                func=ler_arquivo, 
                description="Útil para ler o conteúdo de um arquivo de texto dado o seu nome.",
)]


# Criação do agente
agent = initialize_agent(
    llm=chat,
    tools=tools,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    prompt=system_prompt.partial(system_message=system_prompt),
    memory=memory,
    verbose=False,
)


# Pergunta do usário e resposta do agente
pergunta = sys.argv[1]
resposta = agent.invoke(pergunta)["output"]
print("\n\nResposta do agente enviesado 🤖👨‍🦲:\n" + resposta)


# Criação do juiz
juiz = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3,
    google_api_key=api_key
)

prompt_juiz = '''
Você é um avaliador imparcial. Sua tarefa é revisar a resposta de um entusiasta de Rick and Morty para uma pergunta de aluno.

Critérios:
- A resposta está tecnicamente correta?
- Está clara para o nível médio técnico?
- O próximo passo sugerido está bem formulado?

Se a resposta for boa, diga “✅ Aprovado” e explique por quê.
Se tiver problemas, diga “⚠️ Reprovado” e proponha uma versão melhorada.
'''


def avaliar_resposta(pergunta, resposta_tutor):
    mensagens = [
        SystemMessage(content=prompt_juiz),
        HumanMessage(content=f"Pergunta do aluno: {pergunta}\n\nResposta do tutor: {resposta_tutor}")
    ]
    return juiz.invoke(mensagens).content


avaliacao = avaliar_resposta(pergunta, resposta)
print("\nAvaliação do juiz:\n", avaliacao)
