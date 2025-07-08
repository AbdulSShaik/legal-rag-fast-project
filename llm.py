from openai import OpenAI

client = OpenAI(base_url="https://api.together.xyz/v1", api_key="your_api_key_here")

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=512
    )
    return response.choices[0].message.content