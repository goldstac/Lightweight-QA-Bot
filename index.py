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

home_dir = os.path.expanduser('~')
minibot_dir = os.path.join(home_dir, '.minibot')
os.makedirs(minibot_dir, exist_ok=True)

cache_path = os.path.join(minibot_dir, 'MinibotModelCache')
model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder=cache_path)

qa_path = os.path.join(minibot_dir, 'qa.csv')
try:
    data = pd.read_csv(qa_path)
except FileNotFoundError:
    data = pd.DataFrame(columns=["question","response"])
    data.to_csv(qa_path, index=False)

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

print("MiniBot ready. Type '.exit' to quit.\n")

user_color = "\u001b[34;1m"
minibot_color = "\u001b[33;1m"
teach_color = "\u001b[32;1m"
white_color = "\u001b[37;1m"

user_prompt = user_color + "You » "
minibot_prompt = minibot_color + "MiniBot » "
teach_prompt = user_color + "You (teach MiniBot)\n∘ "

while True:
    user = input(user_prompt + white_color).strip()
    if user.lower() in ("exit","quit",".exit",".quit"):
        speak("Goodbye!")
        engine.stop()
        del engine
        sys.exit(0)

    answer, score = get_reply(user) if len(embeddings) > 0 else (None, 0)

    if score < 0.4 or answer is None:
        teach_msg = "I don't know, can you teach me? "
        print(teach_color + "MiniBot » " + white_color + teach_msg)
        speak(teach_msg)

        new_answer = input(teach_prompt + white_color).strip()
        if new_answer:
            new_row = pd.DataFrame([[user, new_answer]], columns=["question","response"])
            data = pd.concat([data, new_row], ignore_index=True)
            data.to_csv(qa_path, index=False)
            embeddings.append(model.encode([user])[0].tolist())
            print(minibot_prompt + white_color + "Got it! I'll remember that.")
            speak("Got it! I'll remember that.")
        continue

    print(minibot_prompt + white_color + answer)
    speak(answer)
