#ifndef CSEARCH_H
#define CSEARCH_H

#include <vector>
#include <cmath>

struct SearchResult {
    int index;
    double score;
};

inline SearchResult cosine_search(const std::vector<double>& query,
                                  const std::vector<std::vector<double>>& vectors) {
    SearchResult best = {-1, -1.0};

    double q_norm = 0.0;
    for (double v : query) q_norm += v * v;
    q_norm = std::sqrt(q_norm);
    if (q_norm == 0.0) return best;

    for (std::size_t i = 0; i < vectors.size(); ++i) {
        double dot = 0.0, v_norm = 0.0;
        const auto& vec = vectors[i];
        std::size_t dim = vec.size() < query.size() ? vec.size() : query.size();
        for (std::size_t j = 0; j < dim; ++j) {
            dot += query[j] * vec[j];
            v_norm += vec[j] * vec[j];
        }
        v_norm = std::sqrt(v_norm);
        double sim = (v_norm == 0.0) ? 0.0 : dot / (q_norm * v_norm);
        if (sim > best.score) {
            best.index = static_cast<int>(i);
            best.score = sim;
        }
    }
    return best;
}

#endif
