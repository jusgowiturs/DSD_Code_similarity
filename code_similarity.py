from math import sqrt
class SimilarityCalculator:
    """Based on keys to identify the similarities"""
    @staticmethod
    def cosine_similarity(counter1, counter2):
        intersection = set(counter1.keys()) & set(counter2.keys())
        numerator = sum(counter1[x] * counter2[x] for x in intersection)

        sum1 = sum(v ** 2 for v in counter1.values())
        sum2 = sum(v ** 2 for v in counter2.values())
        denominator = sqrt(sum1) * sqrt(sum2)

        if not denominator:
            return 0.0
        return numerator / denominator