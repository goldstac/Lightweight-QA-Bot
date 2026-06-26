import sys
from src.storage import load_data
from src.engine import QAEngine

def main():
    data = load_data()
    engine = QAEngine(data)

    print("QA Bot ready. Type '.exit' to quit.\n")

    colors = {
        'user': '\033[34;1m',
        'bot': '\033[33;1m',
        'teach': '\033[32;1m',
        'reset': '\033[37;1m',
    }

    while True:
        user = input(f"{colors['user']}You \u00bb {colors['reset']}").strip()
        if user.lower() in ("exit", "quit", ".exit", ".quit"):
            print(f"{colors['bot']}Goodbye!{colors['reset']}")
            sys.exit(0)

        answer, score = engine.get_reply(user)

        if score < 0.4 or answer is None:
            print(f"{colors['bot']}I don't know, can you teach me? {colors['reset']}")
            new_answer = input(f"{colors['user']}You (teach)\n\u2218 {colors['reset']}").strip()
            if new_answer:
                engine.learn(user, new_answer)
                print(f"{colors['bot']}Got it! I'll remember that.{colors['reset']}")
            continue

        print(f"{colors['bot']}{answer}{colors['reset']}")

if __name__ == "__main__":
    main()
