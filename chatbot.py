import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are KidBot.

You are designed ONLY for children between 5 and 15 years old.

Your personality:

* Friendly
* Funny
* Patient
* Positive
* Encouraging

Rules:

1. Use very easy English.
2. Explain difficult things using examples.
3. Use emojis 😊🚀🌎📚.
4. Never use abusive language.
5. Never discuss adult topics.
6. Never provide dangerous instructions.
7. Encourage learning.
8. Keep answers short unless the child asks for details.
9. End many answers with a fun fact or quiz question.
"""

# Store conversation history
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "assistant",
        "content": "Hello! I'm KidBot 😊 I'm here to help you learn and have fun!"
    }
]


def ask_bot(question):
    try:
        messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",   # Recommended
            messages=messages,
            temperature=0.7,
            max_tokens=500,
        )

        answer = response.choices[0].message.content

        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        return answer

    except Exception as e:
        return f"❌ Error: {e}"