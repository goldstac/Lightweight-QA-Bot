# Lightweight QA Bot

A CPU-friendly question-answering bot that learns from your Q&A pairs on the fly.
Uses **TF-IDF vectorization** (instead of heavy neural models) + a **C++ extension** for
blazing-fast cosine similarity search.

## Features

- **Self-learning** — teaches itself new Q&A at runtime, persisted to `~/.minibot/qa.csv`
- **TF-IDF based** — no large model downloads, minimal RAM, instant startup
- **C++ accelerated** — similarity search runs in native code via a Python C extension
- **Potato-friendly** — runs on any machine with Python 3.8+; no GPU, no heavy deps
- **Modular** — clean separation into `src/storage.py`, `src/engine.py`, and `csrc/`

## Prerequisites

- Python 3.8+
- C++ compiler (g++ or clang) with Python dev headers
- `pip install pandas scikit-learn`

## Build & Run

```bash
python setup.py build_ext --inplace
python main.py
```

## Usage

```bash
python main.py
```

- Type a question; the bot replies from what it knows.
- If unsure (similarity < 0.4), it asks you to teach it.
- Type `.exit` to quit.

## Structure

```
├── main.py              # CLI entry point
├── src/
│   ├── engine.py        # QA engine (TF-IDF + C++ search)
│   ├── storage.py       # CSV persistence layer
│   └── csearch.*.so     # compiled C++ extension
├── csrc/
│   ├── csearch.cpp      # Python C extension
│   └── csearch.h        # cosine similarity kernel
└── setup.py             # build script for C extension
```

## License

MIT
