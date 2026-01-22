import json
import os
import time
from groq import Groq
import sys

MODEL = "llama-3.1-8b-instant"
MAX_RETRIES = 2

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open("prompts/validator_prompt.txt", "r") as f:
    system_prompt = f.read()

def call_llm(user_data):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(user_data)}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()

def parse_and_validate(text):
    data = json.loads(text)

    # Strict schema enforcement
    if set(data.keys()) != {"is_valid", "errors", "warnings"}:
        raise ValueError("Invalid schema keys")

    if not isinstance(data["is_valid"], bool):
        raise ValueError("is_valid must be boolean")

    if not isinstance(data["errors"], list) or not all(isinstance(e, str) for e in data["errors"]):
        raise ValueError("errors must be list of strings")

    if not isinstance(data["warnings"], list) or not all(isinstance(w, str) for w in data["warnings"]):
        raise ValueError("warnings must be list of strings")

    return data

def validate_user(user_data):
    last_error = None

    for attempt in range(MAX_RETRIES + 1):
        try:
            raw = call_llm(user_data)
            return parse_and_validate(raw)
        except Exception as e:
            last_error = e
            time.sleep(0.5)

    raise RuntimeError(f"LLM failed to return valid structured output: {last_error}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_user.py <input_json_file>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        user_data = json.load(f)

    result = validate_user(user_data)
    print(json.dumps(result))
