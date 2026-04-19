from groq import Groq

def summarize_commits(summary: str) -> str:
    client = Groq()
    prompt = f"Summarize the following git commit messages into a standup update suitable for sending to a manager: \n\n{summary}"
    response = client.chat.completions.create(
        model = "llama3-8b-8192",
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content or "No summary available."