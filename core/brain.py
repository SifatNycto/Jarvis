import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_llm(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        reply = data.get("response", "").strip()

        print(f"🤖 JARVIS: {reply}")

        return reply

    except Exception as e:
        print(f"❌ LLM error: {e}")
        return None