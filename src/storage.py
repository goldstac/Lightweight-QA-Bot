import os
import pandas as pd

DATA_DIR = os.path.join(os.path.expanduser('~'), '.minibot')
QA_PATH = os.path.join(DATA_DIR, 'qa.csv')

def load_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    try:
        return pd.read_csv(QA_PATH)
    except FileNotFoundError:
        data = pd.DataFrame(columns=["question", "response"])
        data.to_csv(QA_PATH, index=False)
        return data

def append_data(data, question, answer):
    new_row = pd.DataFrame([[question, answer]], columns=["question", "response"])
    data = pd.concat([data, new_row], ignore_index=True)
    data.to_csv(QA_PATH, index=False)
    return data
