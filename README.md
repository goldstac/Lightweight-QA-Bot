# Lightweight-QA-Bot 🤖

A snappy, CPU-friendly chatbot that learns from your Q&A and responds in real-time! Built with Python, MiniBot uses Sentence Transformers for embeddings and cosine similarity to find the best match.

---

## 🌟 Features

- **🧠 Self-learning:** Learns new Q&A on the fly and stores them in `qa.csv`.
- **🗣️ Text-to-Speech:** Speaks answers using pyttsx3.
- **💾 Cached model:** Downloads once from Hugging Face, loads instantly after.
- **🧩 Expandable:** Add more Q&A to boost its brainpower.
- **🧘 CPU-friendly:** Runs smoothly on laptops—no GPU needed!

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/goldstac/Lightweight-QA-Bot.git
cd Lightweight-QA-Bot
```

Install required Python modules:

```bash
pip install pandas scikit-learn pyttsx3 sentence-transformers numpy
```

> 💡 **Note:** CPU-friendly version. No TensorFlow or GPU required.

---

## 💬 Usage

- Make sure `qa.csv` exists (MiniBot will create it if missing).
- Run the chatbot:

  ```bash
  python index.py
  ```

- Chat with MiniBot!
  - Type a question and wait for a response.
  - If MiniBot doesn’t know the answer, it will ask you to teach it:
    - **MiniBot:** I don't know, can you teach me? 
    - **You (teach MiniBot):** [Type your answer here]
    - MiniBot will remember it for next time.

- Type `.exit` or `.quit` to close the chatbot.

---

## 🧪 How It Works

1. Loads all Q&A pairs from `qa.csv`.
2. Converts questions into embedding vectors.
3. Finds the closest match using cosine similarity.
4. If similarity < 0.4, it asks you to teach it.
5. Saves new Q&A and updates embeddings dynamically.

---

## 🧾 Example

```
You: Hello
MiniBot: Hi there!

You: Who is Trump?
MiniBot: I don't know, can you teach me? 
You (teach MiniBot): Donald Trump is the 47th president of the USA
MiniBot: Got it! I'll remember that.

You: Who is Trump?
MiniBot: Donald Trump is the 47th president of the USA
```

---

## 📦 Dependencies

- pandas
- scikit-learn
- pyttsx3
- sentence-transformers
- numpy

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.  
Feel free to fork, remix, and contribute! 🛠️

---

## 📝 Notes

- Model is cached locally in `MinibotModelCache` folder to avoid repeated downloads.
- Works fully on CPU; no GPU or TensorFlow needed.
- The more you teach MiniBot, the smarter it gets! 🧠💡
