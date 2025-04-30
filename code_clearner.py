
import re

class CodeCleaner:
    @staticmethod
    def clean(code):
        code = re.sub(r'#.*', '', code)  # Remove comments
        code = re.sub(r'\s+', ' ', code)  # Normalize whitespace
        return code.strip()


class Tokenizer:
    @staticmethod
    def tokenize(code):
        return re.findall(r'\b\w+\b', code)

    @staticmethod
    def generate_ngrams(tokens, n=3):
        return [' '.join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]

