# Lightweight-QA-Bot

A lightweight, CPU-friendly chatbot that learns from your Q&A and responds in real-time. Built with Python, MiniBot uses **Sentence Transformers** for embeddings and **cosine similarity** to find the best answer.

---

## Features

- **CPU-friendly**: Runs smoothly on laptops without GPU.
- **Self-learning**: Teaches itself new Q&A dynamically and stores them in `qa.csv`.
- **Text-to-Speech**: Speaks responses using `pyttsx3`.
- **Cached model**: Downloads once from Hugging Face and loads instantly afterward.
- **Expandable**: Add more Q&A to the CSV to increase its knowledge base.

---

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/goldstac/Lightweight-QA-Bot.git
    cd Lightweight-QA-Bot
    ```

2. Install required Python modules:

    ```bash
    pip install pandas scikit-learn pyttsx3 sentence-transformers numpy
    ```

     **Note:** This version is CPU-friendly. No TensorFlow or GPU is needed.

---

## Usage

- Make sure `qa.csv` exists in the project folder. If not, MiniBot will create it automatically.
- Run the chatbot:

    ```bash
    python index.py
    ```

- Chat with MiniBot!

    - Type a question and wait for a response.
    - If MiniBot doesn’t know the answer, it will ask you to teach it:

        ```
        MiniBot: I don't know, can you teach me? :)
        You (teach MiniBot): [Type your answer here]
        ```

    - MiniBot will remember it for next time.
    - Type `exit` or `quit` to close the chatbot.

---

## How It Works

1. MiniBot loads all Q&A pairs from `qa.csv`.
2. Each question is converted into an embedding vector using SentenceTransformer.
3. When a user asks something, MiniBot encodes the input and finds the most similar question using cosine similarity.
4. If the similarity score is low (<0.4), MiniBot asks you to teach it.
5. New Q&A are saved to CSV and embeddings are updated dynamically.

---

## Example

You: Hello  
MiniBot: Hi there!

You: Who is Trump?  
MiniBot: I don't know, can you teach me? :)  
You (teach MiniBot): Donald Trump is the 47th president of the USA  
MiniBot: Got it! I'll remember that.

You: Who is Trump?  
MiniBot: Donald Trump is the 47th president of the USA

---

## Dependencies

- pandas
- scikit-learn
- pyttsx3
- sentence-transformers
- numpy

---

## License

This project is licensed under the MIT License – see the LICENSE file for details.

Feel free to update, modify, and contribute!

---

## Notes

- Model is cached locally in `MinibotModelCache` folder to avoid repeated downloads.
- Works fully on CPU; no GPU or TensorFlow needed.
- The more you teach MiniBot, the smarter it gets!
