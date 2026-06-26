from sklearn.feature_extraction.text import TfidfVectorizer
from .csearch import search

THRESHOLD = 0.4

class QAEngine:
    def __init__(self, data):
        self.data = data
        self.vectorizer = TfidfVectorizer()
        self.vectors = []
        self._build_index()

    def _build_index(self):
        if len(self.data) > 0:
            matrix = self.vectorizer.fit_transform(self.data["question"].tolist())
            self.vectors = matrix.toarray().tolist()
        else:
            self.vectors = []

    def get_reply(self, question):
        if not self.vectors:
            return None, 0.0
        q_vec = self.vectorizer.transform([question]).toarray()[0].tolist()
        idx, score = search(q_vec, self.vectors)
        if idx < 0:
            return None, 0.0
        return self.data["response"].iloc[idx], score

    def learn(self, question, answer):
        from .storage import append_data
        self.data = append_data(self.data, question, answer)
        self._build_index()
