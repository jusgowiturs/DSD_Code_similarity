#from get_path_submission import GetSubmission
from code_checker import CodeSimilarityChecker
#from code_similarity import SimilarityCalculator
import sys,os
from pathlib import Path
class Student_submission:
    def __init__(self):
        self.submission_ID          =   None
        #self.submission_count       =   1     # Number of Submission he/she made
        self.unique_submission      =   False  #Unique Code

    def path(self,collections):
        pass


if __name__ == "__main__":
    # Ensure the user provides a path as an argument
    # if len(sys.argv) != 2:
    #     print("Usage: python script_name.py <path_to_directory>")
    #     sys.exit(1)
    




    # # Get the path from the command line arguments
    # path = sys.argv[1]
    # #print(f"Path {path}")
    # # Call the static method to get the submissions by student
    # submissions = GetSubmission.get_path_submission(path)
    folders = [os.path.join(os.getcwd(),f) for f in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), f)) and f != '__pycache__']
    print(folders)
    # Loop through each folder in the 'folders' list
    # for folder in folders:
    #     for root, dirs, files in os.walk(folder):
    #         print(f"Root: {root}")
    #         print(f"Dirs: {dirs}")
    #         print(f"Files: {files}")
    
    path = Path(folders[0])
    parent_path = path.parent
    checker = CodeSimilarityChecker(parent_path)
    #
    # checker.run()
    