import os, sys
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
MODEL = "claude-sonnet-4-20250514"

def claude(prompt, system="", max_tokens=2000):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("Set ANTHROPIC_API_KEY (copy .env.example to .env).")
    c = Anthropic(api_key=key)
    kw = dict(model=MODEL, max_tokens=max_tokens,
              messages=[{"role": "user", "content": prompt}])
    if system:
        kw["system"] = system
    r = c.messages.create(**kw)
    return "".join(b.text for b in r.content if b.type == "text")



def translate(text: str, src: str, dst: str) -> str:
    return claude(
        f"Translate from {src} to {dst}. Keep tone and nuance natural; "
        f"output only the translation.\n\n{text}",
        system="You are a professional literary translator.")

if __name__ == "__main__":
    print(translate("How are you doing today?", "English", "Spanish"))
