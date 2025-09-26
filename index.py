import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pyttsx3
import os
import sys
import warnings
import numpy as np

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
engine.setProperty('rate', 140)

def speak(text):
    sentences = text.split('. ')
    for sentence in sentences:
        engine.say(sentence)
    engine.runAndWait()

try:
    data = pd.read_csv("qa.csv")
except FileNotFoundError:
    data = pd.DataFrame(columns=["question","response"])
    data.to_csv("qa.csv", index=False)

cache_path = os.path.join(os.getcwd(), "MinibotModelCache")
model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder=cache_path)

if len(data) > 0:
    embeddings = model.encode(data["question"].tolist(), show_progress_bar=False).tolist()
else:
    embeddings = []

def get_reply(user_text):
    if len(embeddings) == 0:
        return None, 0
    user_emb = model.encode([user_text])
    sims = cosine_similarity(user_emb, np.array(embeddings))
    idx = sims.argmax()
    return data["response"].iloc[idx], sims[0][idx]

user_color = "\u001b[34;1m"
minibot_color = "\u001b[33;1m"
teach_color = "\u001b[32;1m"
white_color = "\u001b[37;1m"

user_prompt = user_color + "You: " + white_color
minibot_prompt = minibot_color + "MiniBot: " + white_color
teach_prompt = teach_color + "You (teach MiniBot): " + white_color

print(minibot_prompt + "MiniBot ready. Type '.exit' to quit.\n")

while True:
    user = input(user_prompt).strip()
    if user.lower() in ("exit", "quit", ".exit", ".quit"):
        speak("Goodbye!")
        engine.stop()
        sys.exit(0)

    answer, score = get_reply(user) if len(embeddings) > 0 else (None, 0)

    if score < 0.4 or answer is None:
        teach_msg = "I don't know, can you teach me? :)"
        print(minibot_prompt + teach_msg)
        speak(teach_msg)

        new_answer = input(teach_prompt).strip()
        if new_answer:
            new_row = pd.DataFrame([[user, new_answer]], columns=["question","response"])
            data = pd.concat([data, new_row], ignore_index=True)
            data.to_csv("qa.csv", index=False)
            embeddings.append(model.encode([user])[0].tolist())
            confirmation = "Got it! I'll remember that."
            print(minibot_prompt + confirmation)
            speak(confirmation)
        continue

    print(minibot_prompt + answer)
    speak(answer)
