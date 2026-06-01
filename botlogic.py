from openai import OpenAI

def messegeForAi(messege):
  client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
  completion = client.chat.completions.create(
    model="google/gemma-4-e4b",
    messages=[
      {"role": "system", "content": "Ответь на вопрос про глобальное потепление так чтобы пользователь понял что ему можно делать а что нельзя чтобы помочь в решении глобального потепления, если вопрос не про глобальное потеление то отвечай пожалуйста задай вопрос про глобальное потеление."},
      {"role": "user", "content": f"{messege}"}
    ],
    temperature=0.7,
  )
  return completion.choices[0].message.content
