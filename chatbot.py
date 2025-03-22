import google.generativeai as genai
from env import api_key  

# Configure a chave de API do Google Gemini
genai.configure(api_key=api_key)

modelo = genai.GenerativeModel("gemini-1.5-pro-latest")  

# Contexto da Loja de Hardware
contexto = """
Você é um assistente virtual especializado em hardware de computadores, trabalhando para a loja TioLan, que vende componentes e acessórios para computadores.
A loja oferece uma ampla variedade de produtos, incluindo processadores, placas-mãe, memórias RAM, placas de vídeo, armazenamento, fontes de alimentação, gabinetes, periféricos e coolers.

Seu papel é ajudar os clientes a:
- Escolher os componentes certos para suas necessidades.
- Explicar as especificações técnicas dos produtos.
- Fornecer recomendações com base no orçamento e uso (ex.: jogos, edição de vídeo, trabalho diário).
- Informar sobre promoções, garantias e políticas de troca.
- Tirar dúvidas sobre compatibilidade entre componentes.
- Evitar respostas com mais que 500 letras
"""

# Mensagem de boas-vindas
bemvindo = """
Bem-vindo ao Chatbot de Hardware para PC! Você pode fazer até 3 perguntas.

Você está conversando com um especialista em hardware para PCs. Podemos responder sobre:
- Componentes como processadores, placas de vídeo, placas-mãe, memória RAM, SSDs e fontes de alimentação.
- Recomendações para diferentes orçamentos e necessidades (gaming, edição de vídeo, trabalho).
- Compatibilidade entre componentes.
- Dicas para montagem e manutenção de PCs.
"""

print(bemvindo)

# Lista para armazenar perguntas e respostas
respostas = []

# Função para interagir com a IA
def perguntar_ia(pergunta):
    resposta = modelo.generate_content(contexto + "\n\n" + pergunta)
    return resposta.text

# Loop para permitir três perguntas
total_perguntas = 3
for i in range(total_perguntas):
    pergunta = input(f"Pergunta {i+1}: ")
    resposta = perguntar_ia(pergunta)
    respostas.append(f"Pergunta {i+1}: {pergunta}\nResposta: {resposta}\n")
    print("\n", resposta, "\n")

# Gerar resumo usando a IA
resumo_prompt = """
Resuma de forma clara e objetiva as seguintes perguntas e respostas sobre hardware de PC:
""" + "\n".join(respostas)

resumo_final = modelo.generate_content(resumo_prompt).text
print("\nResumo final do atendimento:")
print(resumo_final)

print("\nObrigado por usar o Chatbot do TioLan!")