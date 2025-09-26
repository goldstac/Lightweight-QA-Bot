# 🤖 Lightweight-QA-Bot

A snappy, CPU-friendly chatbot that learns from your Q&A and responds in real-time! Built with Python, MiniBot uses **Sentence Transformers** for embeddings and **cosine similarity** to find the best match.

## 🌟 Features

- 🧠 **Self-learning**: Learns new Q&A on the fly and stores them in `qa.csv`.
- 🗣️ **Text-to-Speech**: Speaks answers using `pyttsx3`.
- 💾 **Cached model**: Downloads once from Hugging Face, loads instantly after.
- 🧩 **Expandable**: Add more Q&A to boost its brainpower.
- 🧘 **CPU-friendly**: Runs smoothly on laptops—no GPU needed!

## ⚙️ Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/goldstac/Lightweight-QA-Bot.git
   cd Lightweight-QA-Bot
   ```

2. Install dependencies:

   ```bash
   pip install pandas scikit-learn pyttsx3 sentence-transformers numpy
   ```

   💡 _No TensorFlow, no GPU—just pure Python hustle._

## 💬 Usage

- Ensure `qa.csv` exists (MiniBot will create it if missing).
- Fire it up:

  ```bash
  python index.py
  ```

- Start chatting!

  ```
  You: What's the capital of Mars?
  MiniBot: I don't know, can you teach me? 🙂
  You: Mars doesn't have a capital—yet!
  MiniBot: Got it! I'll remember that.
  ```

- Type `.exit` or `.quit` to close the bot.

## 🧪 How It Works

1. Loads Q&A from `qa.csv`.
2. Converts questions into embedding vectors.
3. Finds the closest match using cosine similarity.
4. If similarity < 0.4, it asks you to teach it.
5. Saves new Q&A and updates embeddings dynamically.

## 🧾 Example

**You**: Who is Trump?  
**MiniBot**: I don't know, can you teach me? 🙂  
**You**: Donald Trump is the 47th president of the USA  
**MiniBot**: Got it! I'll remember that.  
**You**: Who is Trump?  
**MiniBot**: Donald Trump is the 47th president of the USA

## 📦 Dependencies

- pandas
- scikit-learn
- pyttsx3
- sentence-transformers
- numpy

## 📜 License

MIT License — see `LICENSE` for details.  
Feel free to fork, remix, and contribute! 🛠️

## 📝 Notes

- Cached model lives in `MinibotModelCache` to avoid re-downloading.
- Fully CPU-powered—no GPU or TensorFlow required.
- The more you teach MiniBot, the smarter it gets! 🧠💡
