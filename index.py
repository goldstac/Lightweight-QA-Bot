import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pyttsx3
import os
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

def clear():
    os.system("cls" if os.name=="nt" else "clear")

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

print("MiniBot ready. Type 'exit' to quit.\n")
while True:
    user = input("You: ").strip()
    if user.lower() in ("exit","quit"):
        speak("Goodbye!")
        break

    answer, score = get_reply(user) if len(embeddings) > 0 else (None, 0)

    if score < 0.4 or answer is None:
        teach_msg = "I don't know, can you teach me? :)"
        print(f"MiniBot: {teach_msg}")
        speak(teach_msg)

        new_answer = input("You (teach MiniBot): ").strip()
        if new_answer:
            new_row = pd.DataFrame([[user, new_answer]], columns=["question","response"])
            data = pd.concat([data, new_row], ignore_index=True)
            data.to_csv("qa.csv", index=False)
            embeddings.append(model.encode([user])[0].tolist())
            print("MiniBot: Got it! I'll remember that.")
            speak("Got it! I'll remember that.")
        continue

    print(f"MiniBot: {answer}")
    speak(answer)
