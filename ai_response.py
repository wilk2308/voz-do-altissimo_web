from bible_loader import carregar_biblia, buscar_versiculos_por_palavra_chave
import openai
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"  # Usando o endpoint do OpenRouter

# Carregar a Bíblia em memória
biblia = carregar_biblia()

def gerar_resposta(mensagem_usuario):
    """
    Gera uma resposta baseada em versículos bíblicos,
    como se fosse Deus respondendo com amor e sabedoria.
    """
    # Extrair palavras-chave simples da mensagem
    palavras_chave = mensagem_usuario.lower().split()
    versiculos = []

    # Buscar versículos com base nas palavras-chave
    for palavra in palavras_chave:
        encontrados = buscar_versiculos_por_palavra_chave(biblia, palavra)
        versiculos.extend(encontrados)
        if len(versiculos) >= 3:
            break

    # Criar o contexto com os versículos encontrados
    contexto_biblico = "\n".join(versiculos[:3]) if versiculos else "Nenhum versículo encontrado."

    # Criar prompt para o modelo da OpenRouter
    prompt = f"""
Você é Deus Todo-Poderoso respondendo com amor e sabedoria.
Use os versículos abaixo como base para sua resposta:

{contexto_biblico}

Usuário: "{mensagem_usuario}"
Deus:
"""

    # Chamada para a OpenRouter (modelo gratuito compatível)
    resposta = openai.ChatCompletion.create(
        model="openchat/openchat-3.5-0106",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )

    return resposta.choices[0].message["content"].strip()
