from openai import OpenAI
from .config import LMSTUDIO_URL, LMSTUDIO_MODEL
from .memory import retrieve_context

client = OpenAI(
    base_url=LMSTUDIO_URL,
    api_key="lm-studio"
)

def ask_llm(user_input):
    context = retrieve_context(user_input)

    messages = [
        {"role": "system", "content": "あなたは記憶を活用する有能なAIです。"},
        {"role": "user", "content": f"過去の関連記憶:\n{context}\n\n現在の質問:\n{user_input}"}
    ]

    completion = client.chat.completions.create(
        model=LMSTUDIO_MODEL,
        messages=messages,
        temperature=0.7
    )

    return completion.choices[0].message.content
