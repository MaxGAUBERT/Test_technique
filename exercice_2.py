from openai import OpenAI

client = OpenAI(api_key="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")


for i in range(3):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': "Génère moi 3 noms marrants d'animaux differents."},
        ],


        temperature=1.5,
        max_tokens=40,

    )
    
chat_response = response.choices[0].message.content.replace("\n", " ")


print(chat_response)









