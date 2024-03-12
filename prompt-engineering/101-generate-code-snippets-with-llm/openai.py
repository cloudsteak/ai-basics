from openai import OpenAI
client = OpenAI()
 
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "user",
        "content": "/*\nAsk the user for their name and say \"Hello\"\n*/"
        }
    ],
    temperature=1,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)