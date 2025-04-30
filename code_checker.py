import os
#from collections import Counter
#from itertools import combinations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import matplotlib.pyplot as plt

from code_clearner import CodeCleaner,Tokenizer
#from code_similarity import SimilarityCalculator
class CodeSimilarityChecker:
    def __init__(self, folder_path):
        print(folder_path)
        self.path_list = folder_path
        self.codes = {}
        self.vectors = {}
        self.submission_count       =   1     # Number of Submission he/she made
        self.run()


    def load_and_preprocess(self):
        print("Inside Code Checker",self.path_list)
        for root, dirs, files in os.walk(self.path_list):
            # Check if the folder is named 'submission'
            if 'submission' in dirs:
                submission_folder = os.path.join(root, 'submission')
                print(f"Processing folder: {submission_folder}")

                # Get all files in the 'submission' folder
                submission_files = [f for f in os.listdir(submission_folder) ]
                
                
                if submission_files:
                    last_file = submission_files[-1]
                    last_file_path = os.path.join(submission_folder, last_file)
                    
                    print(f"Processing {last_file_path}")
                    with open(last_file_path, "r") as f:
                        raw_code = f.read()
                        cleaned_code = CodeCleaner.clean(raw_code)  # Remove comments and White Spaces
                        self.codes[last_file] = cleaned_code

    # def compute_vectors(self, n=3):
    #     for filename, code in self.codes.items():
    #         tokens = Tokenizer.tokenize(code)
    #         ngrams = Tokenizer.generate_ngrams(tokens, n)
    #         self.vectors[filename] = Counter(ngrams)

    # def compare_all(self, threshold=0.8):
    #     for (file1, vec1), (file2, vec2) in combinations(self.vectors.items(), 2):
    #         score = SimilarityCalculator.cosine_similarity(vec1, vec2)
    #         if score > threshold:
    #             print(f"High similarity: {file1} <--> {file2} | Score: {score:.2f}")
    
    def compute_vectors(self, n=3):
        # Prepare the corpus from cleaned code strings
        self.filenames = list(self.codes.keys())
        corpus = list(self.codes.values())
        #self.filenames, corpus = map(list, zip(*self.codes.items()))   # Try to check and verify whether they exactly mapped
        # Check for empty documents and remove them from both corpus and filenames
        # cleaned_filenames = []
        # cleaned_corpus = []

        # print("Removing empty documents:")
        # for idx, (filename, doc) in enumerate(zip(self.filenames, corpus)):
        #     if  doc.strip():  # Only keep documents that are not empty or whitespace
        #         cleaned_filenames.append(filename)
        #         cleaned_corpus.append(doc)
        #     else:
        #         print(f"Empty document found - Index: {idx}, Filename: {filename}, Document: {repr(doc)}")

        # Update self.filenames and corpus to exclude empty documents
        # self.filenames = cleaned_filenames
        # corpus = cleaned_corpus
        #print(corpus)    

        # Vectorize with TF-IDF using custom n-gram tokenizer
        #vectorizer = TfidfVectorizer(tokenizer=ngram_tokenizer, lowercase=False)
        vectorizer = TfidfVectorizer(ngram_range=(1, 1), lowercase=True,stop_words=[])
        self.tfidf_matrix = vectorizer.fit_transform(corpus)

    def compare_all(self, threshold=0.8):
        sim_matrix = cosine_similarity(self.tfidf_matrix)
        sim_matrix[sim_matrix < threshold] = 0

        # Step 3: Convert to NumPy array (already is, but to ensure)
        #sim_matrix = np.array(sim_matrix)

        # Step 4: Plotting
        plt.figure(figsize=(10, 8))
        plt.imshow(sim_matrix, interpolation='nearest', cmap='viridis')
        plt.colorbar(label='Cosine Similarity')

        # Step 5: Annotate axes with filenames
        tick_marks = np.arange(len(self.filenames))
        plt.xticks(tick_marks, [os.path.basename(f) for f in self.filenames], rotation=90)
        plt.yticks(tick_marks, [os.path.basename(f) for f in self.filenames])
        plt.title('Code Similarity Matrix')
        plt.tight_layout()
        plt.show()
        # Iterate over upper triangle of the similarity matrix
        # num_files = len(self.filenames)
        # for i in range(num_files):
        #     for j in range(i + 1, num_files):
        #         score = sim_matrix[i, j]
        #         if score > threshold:
        #             print(f"High similarity: {self.filenames[i]} <--> {self.filenames[j]} | Score: {score:.2f}")


    def run(self):
        self.load_and_preprocess()
        self.compute_vectors()
        self.compare_all()
        #print(self.codes)


